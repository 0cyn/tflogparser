from json import load
import xlwt

import re

from collections import namedtuple

from tfparser.items import ItemSchema
from tfparser.loader import LogLoader

schema = ItemSchema()

regex_loadout_command = r'.*? - .*?: "([^<]*).*?" say "!loadout\s(\S*?)\s([0-9]*?)\s([0-9]*?)\s([0-9]*?)"'
regex_kill_action = r'.*? - .*?: "([^<]*).*?" killed "([^<]*).*?" with "([^"]*)"'

Kill = namedtuple("Kill", ["username", "tfclass", "target", "item", "primary", "secondary", "melee"])
Death = namedtuple("Death", ["username", "tfclass", "primary", "secondary", "melee"])

class User:
    def __init__(self, parser, username):
        self.name = username
        self.tfclass = ""
        self.parser = parser

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

        killed_user = self.parser.get_user_by_name(killed)
        killed_user.death()

        item = None
        if self.primary.has_log_name and self.primary.logname == weaponname:
            item = self.primary
        elif self.secondary.has_log_name and self.secondary.logname == weaponname:
            item = self.secondary
        elif self.melee.has_log_name and self.melee.logname == weaponname:
            item = self.melee

        self.kills.append(Kill(self.name, self.tfclass, killed, item, self.primary, self.secondary, self.melee))


class Parser:

    @staticmethod
    def print(text):
        print(f'[*] {text}')

    def __init__(self):
        Parser.print(f'loading item schema')
        self.schema = ItemSchema()

        self.user_map = {}
        self.loadout_tracker = {}



        self.log = LogLoader().content



        self.only_item_kills = {}
        for itemindex in schema.items:
            self.only_item_kills[itemindex] = 0

        print()
        Parser.print(f'Parsing log')
        print()
        self.parse_log()


        self.relative_kds_melee = {}
        self.relative_kds_secondary = {}
        self.relative_kds_primary = {}
        self.relative_kds_for_items = {}

        Parser.print(f'Processing Data')
        self.process_data()


    def get_user_by_name(self, name):
        if name in self.user_map:
            return self.user_map[name]
        else:
            self.user_map[name] = User(self, name)
        return self.user_map[name]

    def log_loadout(self, tfclass, primary, secondary, melee):
        tfclass = tfclass.lower()
        if tfclass == 'demoman':
            tfclass = 'demo'
        if tfclass not in ['scout', 'soldier', 'pyro', 'demo', 'heavy', 'engineer', 'medic', 'sniper', 'spy']:
            return 
        if primary not in schema.items or secondary not in schema.items or melee not in schema.items:
            return
        loadout_str = f'{tfclass}-{primary}-{secondary}-{melee}'
        if loadout_str in self.loadout_tracker:
            self.loadout_tracker[loadout_str] += 1
        else:
            self.loadout_tracker[loadout_str] = 1


    def log_kill(self, killer, killed, weapon_logname):

        if weapon_logname in schema.lognames:
            weapon_index = schema.lognames[weapon_logname]
            if weapon_logname in ['tf_projectile_rocket', 'tf_projectile_arrow']:
                weapon_index = self.get_user_by_name(killer).primary.index
            if weapon_logname in ['tf_projectile_pipe_remote']:
                weapon_index = self.get_user_by_name(killer).secondary.index
            if self.schema.items[weapon_index].is_reskin:
                weapon_index = self.schema.items[weapon_index].reskin
            self.only_item_kills[weapon_index] += 1
        self.get_user_by_name(killer).kill(killed, weapon_logname)
        

    def parse_log(self):
        for line in self.log.split('\n'):
            try:
                if 'killed' not in line and '!loadout' not in line:
                    continue
                match_loadout_command = re.search(regex_loadout_command, line)
                if match_loadout_command and len(match_loadout_command.groups()) == 5:
                    user = self.get_user_by_name(match_loadout_command.group(1))
                    user.change_loadout(match_loadout_command.group(2),
                                        int(match_loadout_command.group(3)), int(match_loadout_command.group(4)),
                                        int(match_loadout_command.group(5)))
                    self.log_loadout(match_loadout_command.group(2),
                                        int(match_loadout_command.group(3)), int(match_loadout_command.group(4)),
                                        int(match_loadout_command.group(5)))
                    continue
                match_kill_action = re.search(regex_kill_action, line)
                if match_kill_action and len(match_kill_action.groups()) == 3:
                    self.log_kill(match_kill_action.group(1), match_kill_action.group(2), match_kill_action.group(3))
            except ValueError as ex:
                pass

    def process_data(self):

        self.server_kill_count = 1
        self.server_death_count = 1
        self.kills_with_item_equipped = {}
        self.deaths_with_item_equipped = {}

        for index, item in self.schema.items.items():
            self.kills_with_item_equipped[item.index] = 1
            self.deaths_with_item_equipped[item.index] = 1

        for uname, user in self.user_map.items():
            self.server_kill_count += user.size_kills()
            self.server_death_count += user.size_deaths()
            for index in self.kills_with_item_equipped:
                self.kills_with_item_equipped[index] += user.kills_with_item_index(index)
                self.deaths_with_item_equipped[index] += user.deaths_with_item_index(index)

        aggregated_average_kd = self.server_kill_count / self.server_death_count
        kds_for_items = {}

        for index in self.kills_with_item_equipped:
            kds_for_items[index] = self.kills_with_item_equipped[index] / self.deaths_with_item_equipped[index]
            self.relative_kds_for_items[index] = 1 + (self.kills_with_item_equipped[index] / self.deaths_with_item_equipped[index]) - aggregated_average_kd
            slottype = self.schema.items[index].slot_type
            if slottype == "Primary":
                self.relative_kds_primary[index] = 1 + (self.kills_with_item_equipped[index] / self.deaths_with_item_equipped[index]) - aggregated_average_kd
            elif slottype == "Secondary":
                self.relative_kds_secondary[index] = 1 + (self.kills_with_item_equipped[index] / self.deaths_with_item_equipped[index]) - aggregated_average_kd
            elif slottype == "Melee":
                self.relative_kds_melee[index] = 1 + (self.kills_with_item_equipped[index] / self.deaths_with_item_equipped[index]) - aggregated_average_kd

        self.relative_kds_primary = {k: v for k, v in
                             sorted(self.relative_kds_primary.items(), reverse=True, key=lambda item: item[1])}
        self.relative_kds_primary = {k:v for k, v in self.relative_kds_primary.items() if not self.schema.items[k].is_reskin}
        self.relative_kds_secondary = {k: v for k, v in
                             sorted(self.relative_kds_secondary.items(), reverse=True, key=lambda item: item[1])}
        self.relative_kds_secondary = {k:v for k, v in self.relative_kds_secondary.items() if not self.schema.items[k].is_reskin}
        self.relative_kds_melee = {k: v for k, v in
                             sorted(self.relative_kds_melee.items(), reverse=True, key=lambda item: item[1])}
        self.relative_kds_melee = {k:v for k, v in self.relative_kds_melee.items() if not self.schema.items[k].is_reskin}

        self.loadout_tracker = {k: v for k, v in
                             sorted(self.loadout_tracker.items(), reverse=True, key=lambda item: item[1])}


class XMLOutputter:
    def __init__(self, parser):
        self.parser = parser
        self.do_weapon_stats()
        self.do_loadouts()

    def do_loadouts(self):
        book = xlwt.Workbook()
        sh = book.add_sheet("Loadouts")

        col1_name = 'Loadout'
        col2_name = 'Times chosen'

        sh.write(0, 0, col1_name)
        sh.write(0, 1, col2_name)

        for i, loadout_string in enumerate(self.parser.loadout_tracker):
            tfclass, prim_index, sec_index, melee_index = loadout_string.split('-')
            render_string = f'{tfclass} - {schema.items[int(prim_index)].name}, {schema.items[int(sec_index)].name}, {schema.items[int(melee_index)].name}'
            sh.write(i + 1, 0, render_string)
            sh.write(i + 1, 1, self.parser.loadout_tracker[loadout_string])
            
        book.save("loadouts.xls")
        print('Saved spreadsheet with loadouts as loadouts.xls')

    def do_weapon_stats(self):


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
        sh.write(0, 5, col1_name)
        sh.write(0, 6, col2_name)
        sh.write(0, 7, col3_name)
        sh.write(0, 8, col4_name)
        sh.write(0, 10, col1_name)
        sh.write(0, 11, col2_name)
        sh.write(0, 12, col3_name)
        sh.write(0, 13, col4_name)

        for i, item_index in enumerate(self.parser.relative_kds_primary):
            if item_index in self.parser.only_item_kills:
                sh.write(i + 1, 0, self.parser.schema.items[item_index].name)
                sh.write(i + 1, 1, self.parser.relative_kds_primary[item_index])
                sh.write(i + 1, 2, self.parser.only_item_kills[item_index])
                sh.write(i + 1, 3, self.parser.kills_with_item_equipped[item_index])
        for i, item_index in enumerate(self.parser.relative_kds_secondary):
            if item_index in self.parser.only_item_kills:
                sh.write(i + 1, 5, self.parser.schema.items[item_index].name)
                sh.write(i + 1, 6, self.parser.relative_kds_secondary[item_index])
                sh.write(i + 1, 7, self.parser.only_item_kills[item_index])
                sh.write(i + 1, 8,  self.parser.kills_with_item_equipped[item_index])
        for i, item_index in enumerate(self.parser.relative_kds_melee):
            if item_index in self.parser.only_item_kills:
                sh.write(i + 1, 10, self.parser.schema.items[item_index].name)
                sh.write(i + 1, 11, self.parser.relative_kds_melee[item_index])
                sh.write(i + 1, 12, self.parser.only_item_kills[item_index])
                sh.write(i + 1, 13,  self.parser.kills_with_item_equipped[item_index])

        book.save("weapon_stats.xls")
        print('Saved spreadsheet with stats as weapon_stats.xls')

if __name__ == "__main__":
    parser = Parser()
    XMLOutput = XMLOutputter(parser)