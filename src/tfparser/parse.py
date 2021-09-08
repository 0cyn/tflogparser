

if __name__=="__main__":

    """
    So, I think the best way to calculate the effectiveness of a certain item is by
        calculating the user's average KD, and then calculating their KD with that weapon equipped



    """

    import re

    from collections import namedtuple

    from tfparser.items import ItemSchema
    from tfparser.loader import LogLoader

    print('Loading Schema')
    schema = ItemSchema()

    regex_loadout_command = r'.*? - .*?: "([^<]*).*?" say "!loadout\s(\S*?)\s([0-9]*?)\s([0-9]*?)\s([0-9]*?)"'
    regex_kill_action = r'.*? - .*?: "([^<]*).*?" killed "([^<]*).*?" with "([^"]*)"'

    Kill = namedtuple("Kill", ["username", "tfclass", "target", "item", "primary", "secondary", "melee"])
    Death = namedtuple("Death", ["username", "tfclass", "primary", "secondary", "melee"])

    user_map = {}


    def get_user_by_name(name):
        if name in user_map:
            return user_map[name]
        else:
            user_map[name] = User(name)
        return user_map[name]


    class User:
        def __init__(self, username):
            self.name = username
            self.tfclass = ""

            self.primary = schema.items[0]
            self.secondary = schema.items[0]
            self.melee = schema.items[0]

            self.kills = []
            self.deaths = []

        def size_kills(self):
            return len(self.kills)

        def size_deaths(self):
            return len(self.deaths)

        def kills_with_item_index(self, index):
            rel_kills = []
            for kill in self.kills:
                if kill.primary.index == index or kill.secondary.index == index or kill.melee.index == index:
                    rel_kills.append(kill)
            return len(rel_kills)

        def deaths_with_item_index(self, index):
            rel_deaths = []
            for death in self.deaths:
                if death.primary.index == index or death.secondary.index == index or death.melee.index == index:
                    rel_deaths.append(death)
            return len(rel_deaths)

        def relative_kds(self):
            kds = {}
            avg = self.average_kd()
            for index, item in schema.items:
                kds[item.name] = self.kd_with_item_index(index) - avg
            return kds

        def average_kd(self):
            return len(self.kills) / len(self.deaths)

        def kd_with_item_index(self, index):
            rel_kills = []
            rel_deaths = []
            for kill in self.kills:
                if kill.primary.index == index or kill.secondary.index == index or kill.melee.index == index:
                    rel_kills.append(kill)
            for kill in self.deaths:
                if kill.primary.index == index or kill.secondary.index == index or kill.melee.index == index:
                    rel_deaths.append(kill)
            return len(rel_kills) / len(rel_deaths)

        def change_loadout(self, tfclass, primary, secondary, melee):
            if primary not in schema.items.keys() or secondary not in schema.items.keys() or melee not in schema.items.keys():
                return
            self.primary = schema.items[primary]
            self.secondary = schema.items[secondary]
            self.melee = schema.items[melee]
            self.tfclass = tfclass.lower()

        def death(self):
            self.deaths.append(Death(self.name, self.tfclass, self.primary, self.secondary, self.melee))

        def kill(self, killed, weaponname):

            killed_user = get_user_by_name(killed)
            killed_user.death()

            item = None
            if self.primary.has_log_name and self.primary.logname == weaponname:
                item = self.primary
            elif self.secondary.has_log_name and self.secondary.logname == weaponname:
                item = self.secondary
            elif self.melee.has_log_name and self.melee.logname == weaponname:
                item = self.melee

            self.kills.append(Kill(self.name, self.tfclass, killed, item, self.primary, self.secondary, self.melee))


    item_equips = {}


    def log_item_equipped(item_id):
        if item_id not in item_equips:
            item_equips[item_id] = 1
        else:
            item_equips[item_id] += 1


    item_kills = {}
    only_item_kills = {}
    for i in schema.items:
        only_item_kills[i.id] = 0


    def log_kill(killer, killed, weapon_logname):
        only_item_kills[schema.lognames[weapon_logname]] += 1
        get_user_by_name(killer).kill(killed, weapon_logname)


    log = LogLoader().content

    for line in log.split('\n'):
        if 'killed' not in line and '!loadout' not in line:
            continue
        match_loadout_command = re.search(regex_loadout_command, line)
        if match_loadout_command and len(match_loadout_command.groups()) == 5:
            user = get_user_by_name(match_loadout_command.group(1))
            user.change_loadout(match_loadout_command.group(2),
                                int(match_loadout_command.group(3)), int(match_loadout_command.group(4)),
                                int(match_loadout_command.group(5)))
            continue
        match_kill_action = re.search(regex_kill_action, line)
        if match_kill_action and len(match_kill_action.groups()) == 3:
            log_kill(match_kill_action.group(1), match_kill_action.group(2), match_kill_action.group(3))

    # We start all at ONE to avoid divide-by zero
    # Is this actually bad?
    all_kills = 1
    all_deaths = 1
    item_kills = {}
    item_deaths = {}

    for index, item in schema.items.items():
        item_kills[item.index] = 1
        item_deaths[item.index] = 1

    for uname, user in user_map.items():
        all_kills += user.size_kills()
        all_deaths += user.size_deaths()
        for index in item_kills:
            item_kills[index] += user.kills_with_item_index(index)
            item_deaths[index] += user.deaths_with_item_index(index)

    print(all_kills)
    print(all_deaths)

    aggregated_average_kd = all_kills / all_deaths
    kds_for_items = {}
    relative_kds_for_items = {}

    relative_kds_primary = {}
    relative_kds_secondary = {}
    relative_kds_melee = {}

    for index in item_kills:
        kds_for_items[index] = item_kills[index] / item_deaths[index]
        relative_kds_for_items[index] = 1 + (item_kills[index] / item_deaths[index]) - aggregated_average_kd
        slottype = schema.items[index].slot_type
        if slottype == "Primary":
            relative_kds_primary[index] = 1 + (item_kills[index] / item_deaths[index]) - aggregated_average_kd
        elif slottype == "Secondary":
            relative_kds_secondary[index] = 1 + (item_kills[index] / item_deaths[index]) - aggregated_average_kd
        elif slottype == "Melee":
            relative_kds_melee[index] = 1 + (item_kills[index] / item_deaths[index]) - aggregated_average_kd

    srelative_kds_primary = {k: v for k, v in
                             sorted(relative_kds_primary.items(), reverse=True, key=lambda item: item[1])}
    srelative_kds_secondary = {k: v for k, v in
                               sorted(relative_kds_secondary.items(), reverse=True, key=lambda item: item[1])}
    srelative_kds_melee = {k: v for k, v in sorted(relative_kds_melee.items(), reverse=True, key=lambda item: item[1])}

    # print('Primary Weapons --------------------------------')
    # for key in srelative_kds_primary:
    #    print(f'{schema.items[key].name}: {srelative_kds_primary[key]}')
    # print('Secondary Weapons --------------------------------')
    # for key in srelative_kds_secondary:
    #    print(f'{schema.items[key].name}: {srelative_kds_secondary[key]}')
    # print('Melee Weapons --------------------------------')
    # for key in srelative_kds_melee:
    #    print(f'{schema.items[key].name}: {srelative_kds_melee[key]}')

    import xlwt

    book = xlwt.Workbook()
    sh = book.add_sheet("Stats")

    col1_name = 'Weapon Name'
    col2_name = 'Difference from average KD'
    col3_name = 'Kills'
    col4_name = 'Kills with weapon equipped'

    sh.write(0, 0, col1_name)
    sh.write(0, 1, col2_name)
    sh.write(0, 2, col3_name)
    sh.write(0, 3, col4_name)

    for i, item_index in enumerate(srelative_kds_primary):
        sh.write(i + 1, 0, schema.items[item_index].name)
        sh.write(i + 1, 1, srelative_kds_primary[item_index])
        sh.write(i + 1, 2, only_item_kills[item_index])
        sh.write(i + 1, 3, item_kills[item_index])
    for i, item_index in enumerate(srelative_kds_secondary):
        sh.write(i + 1, 4, schema.items[item_index].name)
        sh.write(i + 1, 5, srelative_kds_secondary[item_index])
        sh.write(i + 1, 6, only_item_kills[item_index])
        sh.write(i + 1, 7, item_kills[item_index])
    for i, item_index in enumerate(srelative_kds_melee):
        sh.write(i + 1, 8, schema.items[item_index].name)
        sh.write(i + 1, 9, srelative_kds_melee[item_index])
        sh.write(i + 1, 10, only_item_kills[item_index])
        sh.write(i + 1, 11, item_kills[item_index])

    book.save("stats.xls")
    print('Saved spreadsheet with stats as stats.xls')