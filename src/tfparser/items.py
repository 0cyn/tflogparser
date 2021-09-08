import json

schema = """[
  [
    "Scout",
    [
      {
        "id": 13,
        "logname": "scattergun",
        "name": "Scattergun",
        "slot_type": "Primary"
      },
      {
        "id": 45,
        "logname": "force_a_nature",
        "name": "Force-A-Nature",
        "slot_type": "Primary"
      },
      {
        "id": 220,
        "logname": "shortstop",
        "name": "The Shortstop",
        "slot_type": "Primary"
      },
      {
        "id": 448,
        "logname": "soda_popper",
        "name": "The Soda Popper",
        "slot_type": "Primary"
      },
      {
        "id": 772,
        "logname": "pep_brawlerblaster",
        "name": "Baby Face's Blaster",
        "slot_type": "Primary"
      },
      {
        "id": 1103,
        "logname": "back_scatter",
        "name": "The Back Scatter",
        "slot_type": "Primary"
      },
      {
        "id": 23,
        "logname": "pistol",
        "name": "Scout's Pistol",
        "slot_type": "Secondary"
      },
      {
        "id": 46,
        "name": "Bonk! Atomic Punch",
        "slot_type": "Secondary"
      },
      {
        "id": 163,
        "name": "Crit-a-Cola",
        "slot_type": "Secondary"
      },
      {
        "id": 222,
        "name": "Mad Milk",
        "slot_type": "Secondary"
      },
      {
        "id": 294,
        "logname": "pep_pistol",
        "reskin": 23,
        "name": "Lugermorph",
        "slot_type": "Secondary"
      },
      {
        "id": 449,
        "logname": "pep_pistol",
        "name": "The Winger",
        "slot_type": "Secondary"
      },
      {
        "id": 773,
        "logname": "pep_pistol",
        "name": "Pretty Boy's Pocket Pistol",
        "slot_type": "Secondary"
      },
      {
        "id": 812,
        "logname": "guillotine",
        "name": "The Flying Guillotine",
        "slot_type": "Secondary"
      },
      {
        "id": 0,
        "logname": "bat",
        "name": "Bat",
        "slot_type": "Melee"
      },
      {
        "id": 44,
        "logname": "sandman",
        "name": "The Sandman",
        "slot_type": "Melee"
      },
      {
        "id": 221,
        "logname": "bat",
        "reskin": 0,
        "name": "The Holy Mackerel",
        "slot_type": "Melee"
      },
      {
        "id": 264,
        "logname": "fryingpan",
        "reskin": 0,
        "name": "Frying Pan",
        "slot_type": "Melee"
      },
      {
        "id": 317,
        "logname": "candy_cane",
        "name": "The Candy Cane",
        "slot_type": "Melee"
      },
      {
        "id": 325,
        "logname": "boston_basher",
        "name": "The Boston Basher",
        "slot_type": "Melee"
      },
      {
        "id": 349,
        "logname": "lava_bat",
        "name": "Sun-on-a-stick",
        "slot_type": "Melee"
      },
      {
        "id": 355,
        "logname": "warfan",
        "name": "The Fan O'War",
        "slot_type": "Melee"
      },
      {
        "id": 450,
        "logname": "atomizer",
        "name": "The Atomizer",
        "slot_type": "Melee"
      },
      {
        "id": 352,
        "logname": "scout_sword",
        "reskin": 325,
        "name": "Three-Rune Blade",
        "slot_type": "Melee"
      },
      {
        "id": 572,
        "logname": "unarmed_combat",
        "reskin": 0,
        "name": "Unarmed Combat",
        "slot_type": "Melee"
      },
      {
        "id": 648,
        "logname": "wrap_assassin",
        "name": "The Wrap Assassin",
        "slot_type": "Melee"
      }
    ]
  ],
  [
    "Soldier",
    [
      {
        "id": 18,
        "logname": "tf_projectile_rocket",
        "name": "Rocket Launcher",
        "slot_type": "Primary"
      },
      {
        "id": 127,
        "logname": "rocketlauncher_directhit",
        "name": "The Direct Hit",
        "slot_type": "Primary"
      },
      {
        "id": 228,
        "logname": "tf_projectile_rocket",
        "name": "The Black Box",
        "slot_type": "Primary"
      },
      {
        "id": 237,
        "name": "Rocket Jumper",
        "slot_type": "Primary"
      },
      {
        "id": 414,
        "logname": "liberty_launcher",
        "name": "The Liberty Launcher",
        "slot_type": "Primary"
      },
      {
        "id": 441,
        "logname": "cow_mangler",
        "name": "The Cow Mangler 5000",
        "slot_type": "Primary"
      },
      {
        "id": 513,
        "logname": "quake_rl",
        "reskin": 18,
        "name": "The Original",
        "slot_type": "Primary"
      },
      {
        "id": 1104,
        "logname": "airstrike",
        "name": "The Air Strike",
        "slot_type": "Primary"
      },
      {
        "id": 10,
        "logname": "shotgun_soldier",
        "name": "Soldier's Shotgun",
        "slot_type": "Secondary"
      },
      {
        "id": 129,
        "name": "The Buff Banner",
        "slot_type": "Secondary"
      },
      {
        "id": 133,
        "name": "Gunboats",
        "slot_type": "Secondary"
      },
      {
        "id": 226,
        "name": "The Battalion's Backup",
        "slot_type": "Secondary"
      },
      {
        "id": 354,
        "name": "The Concheror",
        "slot_type": "Secondary"
      },
      {
        "id": 415,
        "logname": "reserve_shooter",
        "name": "The Reserve Shooter",
        "slot_type": "Secondary"
      },
      {
        "id": 442,
        "logname": "righteous_bison",
        "name": "The Righteous Bison",
        "slot_type": "Secondary"
      },
      {
        "id": 444,
        "logname": "mantreads",
        "name": "The Mantreads",
        "slot_type": "Secondary"
      },
      {
        "id": 1101,
        "name": "The B.A.S.E. Jumper",
        "slot_type": "Secondary"
      },
      {
        "id": 1153,
        "name": "Panic Attack",
        "slot_type": "Secondary"
      },
      {
        "id": 6,
        "name": "Shovel",
        "slot_type": "Melee"
      },
      {
        "id": 128,
        "name": "The Equalizer",
        "logname": "unique_pickaxe",
        "slot_type": "Melee"
      },
      {
        "id": 154,
        "logname": "paintrain",
        "name": "The Pain Train",
        "slot_type": "Melee"
      },
      {
        "id": 357,
        "logname": "demokatana",
        "name": "The Half-Zatoichi",
        "slot_type": "Melee"
      },
      {
        "id": 416,
        "logname": "market_gardener",
        "name": "The Market Gardener",
        "slot_type": "Melee"
      },
      {
        "id": 447,
        "logname": "disciplinary_action",
        "name": "The Disciplinary Action",
        "slot_type": "Melee"
      },
      {
        "id": 775,
        "logname": "unique_pickaxe_escape",
        "name": "The Escape Plan",
        "slot_type": "Melee"
      }
    ]
  ],
  [
    "Pyro",
    [
      {
        "id": 21,
        "logname": "flamethrower",
        "name": "Flame Thrower",
        "slot_type": "Primary"
      },
      {
        "id": 40,
        "logname": "backburner",
        "name": "The Backburner",
        "slot_type": "Primary"
      },
      {
        "id": 215,
        "logname": "degreaser",
        "name": "The Degreaser",
        "slot_type": "Primary"
      },
      {
        "id": 594,
        "logname": "phlogistinator",
        "name": "The Phlogistinator",
        "slot_type": "Primary"
      },
      {
        "id": 741,
        "logname": "flamethrower",
        "reskin": 21,
        "name": "The Rainblower",
        "slot_type": "Primary"
      },
      {
        "id": 1178,
        "logname": "dragonsfury",
        "name": "Dragon's Fury",
        "slot_type": "Primary"
      },
      {
        "id": 30474,
        "logname": "flamethrower",
        "reskin": 21,
        "name": "Nostromo Napalmer",
        "slot_type": "Primary"
      },
      {
        "id": 12,
        "logname": "shotgun_pyro",
        "reskin": 10,
        "name": "Pyro's Shotgun",
        "slot_type": "Secondary"
      },
      {
        "id": 39,
        "logname": "flaregun",
        "name": "The Flare Gun",
        "slot_type": "Secondary"
      },
      {
        "id": 351,
        "logname": "detonator",
        "name": "The Detonator",
        "slot_type": "Secondary"
      },
      {
        "id": 415,
        "logname": "reserve_shooter",
        "name": "The Reserve Shooter",
        "slot_type": "Secondary"
      },
      {
        "id": 595,
        "logname": "manmelter",
        "name": "The Manmelter",
        "slot_type": "Secondary"
      },
      {
        "id": 740,
        "logname": "scorch_shot",
        "name": "The Scorch Shot",
        "slot_type": "Secondary"
      },
      {
        "id": 1179,
        "logname": "rocketpack",
        "name": "Thermal Thruster",
        "slot_type": "Secondary"
      },
      {
        "id": 1180,
        "name": "Gas Passer",
        "slot_type": "Secondary"
      },
      {
        "id": 2,
        "logname": "fireaxe",
        "name": "Fire Axe",
        "slot_type": "Melee"
      },
      {
        "id": 38,
        "logname": "axtinguisher",
        "name": "The Axtinguisher",
        "slot_type": "Melee"
      },
      {
        "id": 153,
        "logname": "sledgehammer",
        "name": "Homewrecker",
        "slot_type": "Melee"
      },
      {
        "id": 214,
        "logname": "powerjack",
        "name": "The Powerjack",
        "slot_type": "Melee"
      },
      {
        "id": 326,
        "logname": "back_scratcher",
        "name": "The Back Scratcher",
        "slot_type": "Melee"
      },
      {
        "id": 348,
        "logname": "lava_axe",
        "name": "Sharpened Volcano Fragment",
        "slot_type": "Melee"
      },
      {
        "id": 457,
        "logname": "mailbox",
        "reskin": 38,
        "name": "The Postal Pummeler",
        "slot_type": "Melee"
      },
      {
        "id": 466,
        "logname": "the_maul",
        "reskin": 153,
        "name": "The Maul",
        "slot_type": "Melee"
      },
      {
        "id": 593,
        "logname": "thirddegree",
        "name": "The Third Degree",
        "slot_type": "Melee"
      },
      {
        "id": 739,
        "logname": "lollichop",
        "reskin": 2,
        "name": "The Lollichop",
        "slot_type": "Melee"
      },
      {
        "id": 813,
        "logname": "annihilator",
        "name": "Neon Annihilator",
        "slot_type": "Melee"
      },
      {
        "id": 1181,
        "logname": "hot_hand",
        "name": "Hot Hand",
        "slot_type": "Melee"
      }
    ]
  ],
  [
    "Demoman",
    [
      {
        "id": 19,
        "logname": "tf_projectile_pipe",
        "name": "Grenade Launcher",
        "slot_type": "Primary"
      },
      {
        "id": 308,
        "logname": "loch_n_load",
        "name": "The Loch-n-Load",
        "slot_type": "Primary"
      },
      {
        "id": 405,
        "name": "Ali Baba's Wee Booties",
        "slot_type": "Primary"
      },
      {
        "id": 608,
        "reskin": 405,
        "name": "The Bootlegger",
        "slot_type": "Primary"
      },
      {
        "id": 996,
        "logname": "loose_cannon",
        "name": "The Loose Cannon",
        "slot_type": "Primary"
      },
      {
        "id": 1101,
        "name": "The B.A.S.E. Jumper",
        "slot_type": "Primary"
      },
      {
        "id": 1151,
        "logname": "iron_bomber",
        "name": "The Iron Bomber",
        "slot_type": "Primary"
      },
      {
        "id": 20,
        "logname": "tf_projectile_pipe_remote",
        "name": "Stickybomb Launcher",
        "slot_type": "Secondary"
      },
      {
        "id": 130,
        "logname": "tf_projectile_pipe_remote",
        "name": "The Scottish Resistance",
        "slot_type": "Secondary"
      },
      {
        "id": 131,
        "logname": "targe",
        "name": "The Chargin' Targe",
        "slot_type": "Secondary"
      },
      {
        "id": 265,
        "name": "Sticky Jumper",
        "slot_type": "Secondary"
      },
      {
        "id": 406,
        "logname": "splendid_screen",
        "name": "The Splendid Screen",
        "slot_type": "Secondary"
      },
      {
        "id": 1099,
        "name": "The Tide Turner",
        "slot_type": "Secondary"
      },
      {
        "id": 1150,
        "logname": "quickiebomb_launcher",
        "name": "The Quickiebomb Launcher",
        "slot_type": "Secondary"
      },
      {
        "id": 1,
        "logname": "bottle",
        "name": "Bottle",
        "slot_type": "Melee"
      },
      {
        "id": 132,
        "logname": "sword",
        "name": "The Eyelander",
        "slot_type": "Melee"
      },
      {
        "id": 154,
        "logname": "paintrain",
        "name": "The Pain Train",
        "slot_type": "Melee"
      },
      {
        "id": 172,
        "logname": "battleaxe",
        "name": "The Scotsman's Skullcutter",
        "slot_type": "Melee"
      },
      {
        "id": 266,
        "logname": "headtaker",
        "reskin": 132,
        "name": "Horseless Headless Horseman's Headtaker",
        "slot_type": "Melee"
      },
      {
        "id": 307,
        "logname": "ullapool_caber",
        "name": "Ullapool Caber",
        "slot_type": "Melee"
      },
      {
        "id": 327,
        "logname": "claidheamohmor",
        "name": "The Claidheamohmor",
        "slot_type": "Melee"
      },
      {
        "id": 357,
        "logname": "demokatana",
        "name": "The Half-Zatoichi",
        "slot_type": "Melee"
      },
      {
        "id": 404,
        "logname": "persian_persuader",
        "name": "The Persian Persuader",
        "slot_type": "Melee"
      },
      {
        "id": 482,
        "logname": "nessieclub",
        "name": "Nessie's Nine Iron",
        "slot_type": "Melee"
      },
      {
        "id": 609,
        "logname": "scotland_shard",
        "reskin": 1,
        "name": "The Scottish Handshake",
        "slot_type": "Melee"
      },
      {
        "id": 0,
        "name": "",
        "slot_type": "Melee"
      }
    ]
  ],
  [
    "Heavy",
    [
      {
        "id": 15,
        "logname": "minigun",
        "name": "Minigun",
        "slot_type": "Primary"
      },
      {
        "id": 41,
        "logname": "natascha",
        "name": "Natascha",
        "slot_type": "Primary"
      },
      {
        "id": 298,
        "logname": "iron_curtain",
        "reskin": 15,
        "name": "Iron Curtain",
        "slot_type": "Primary"
      },
      {
        "id": 312,
        "logname": "brass_beast",
        "name": "The Brass Beast",
        "slot_type": "Primary"
      },
      {
        "id": 424,
        "logname": "tomislav",
        "name": "Tomislav",
        "slot_type": "Primary"
      },
      {
        "id": 811,
        "logname": "long_heatmaker",
        "name": "The Huo-Long Heater",
        "slot_type": "Primary"
      },
      {
        "id": 11,
        "logname": "shotgun_hwg",
        "reskin": 10,
        "name": "Heavy's Shotgun",
        "slot_type": "Secondary"
      },
      {
        "id": 42,
        "logname": "sandvich",
        "name": "Sandvich",
        "slot_type": "Secondary"
      },
      {
        "id": 159,
        "name": "The Dalokohs Bar",
        "slot_type": "Secondary"
      },
      {
        "id": 311,
        "name": "The Buffalo Steak Sandvich",
        "slot_type": "Secondary"
      },
      {
        "id": 425,
        "logname": "family_business",
        "name": "The Family Business",
        "slot_type": "Secondary"
      },
      {
        "id": 433,
        "name": "Fishcake",
        "reskin": 159,
        "slot_type": "Secondary"
      },
      {
        "id": 1190,
        "name": "Second Banana",
        "slot_type": "Secondary"
      },
      {
        "id": 5,
        "logname": "fists",
        "name": "Fists",
        "slot_type": "Melee"
      },
      {
        "id": 43,
        "logname": "gloves",
        "name": "The Killing Gloves of Boxing",
        "slot_type": "Melee"
      },
      {
        "id": 239,
        "logname": "gloves",
        "name": "Gloves of Running Urgently",
        "slot_type": "Melee"
      },
      {
        "id": 310,
        "logname": "warrior_spirit",
        "name": "Warrior's Spirit",
        "slot_type": "Melee"
      },
      {
        "id": 331,
        "logname": "steel_fists",
        "name": "Fists of Steel",
        "slot_type": "Melee"
      },
      {
        "id": 426,
        "logname": "eviction_notice",
        "name": "The Eviction Notice",
        "slot_type": "Melee"
      },
      {
        "id": 587,
        "logname": "apocofists",
        "reskin": 5,
        "name": "Apoco-Fists",
        "slot_type": "Melee"
      },
      {
        "id": 1100,
        "logname": "bread_bite",
        "reskin": 239,
        "name": "The Bread Bite",
        "slot_type": "Melee"
      }
    ]
  ],
  [
    "Engineer",
    [
      {
        "id": 9,
        "logname": "shotgun_primary",
        "reskin": 10,
        "name": "Engineer's Shotgun",
        "slot_type": "Primary"
      },
      {
        "id": 141,
        "logname": "frontier_justice",
        "name": "The Frontier Justice",
        "slot_type": "Primary"
      },
      {
        "id": 527,
        "logname": "widowmaker",
        "name": "The Widowmaker",
        "slot_type": "Primary"
      },
      {
        "id": 588,
        "logname": "pomson",
        "name": "The Pomson 6000",
        "slot_type": "Primary"
      },
      {
        "id": 977,
        "name": "The Rescue Ranger",
        "slot_type": "Primary"
      },
      {
        "id": 22,
        "name": "Engineer's Pistol",
        "slot_type": "Secondary"
      },
      {
        "id": 140,
        "logname": "wrangler",
        "name": "The Wrangler",
        "slot_type": "Secondary"
      },
      {
        "id": 528,
        "logname": "short_circuit",
        "name": "The Short Circuit",
        "slot_type": "Secondary"
      },
      {
        "id": 7,
        "logname": "wrench",
        "name": "Wrench",
        "slot_type": "Melee"
      },
      {
        "id": 142,
        "logname": "robot_arm",
        "name": "The Gunslinger",
        "slot_type": "Melee"
      },
      {
        "id": 155,
        "logname": "southern_hospitality",
        "name": "The Southern Hospitality",
        "slot_type": "Melee"
      },
      {
        "id": 169,
        "logname": "wrench_golden",
        "reskin": 7,
        "name": "Golden Wrench",
        "slot_type": "Melee"
      },
      {
        "id": 329,
        "logname": "wrench_jag",
        "name": "The Jag",
        "slot_type": "Melee"
      },
      {
        "id": 589,
        "logname": "eureka_effect",
        "name": "The Eureka Effect",
        "slot_type": "Melee"
      },
      {
        "id": 25,
        "name": "Construction PDA",
        "slot_type": "PDA"
      }
    ]
  ],
  [
    "Medic",
    [
      {
        "id": 17,
        "logname": "syringegun",
        "name": "Syringe Gun",
        "slot_type": "Primary"
      },
      {
        "id": 36,
        "logname": "blutsauger",
        "name": "The Blutsauger",
        "slot_type": "Primary"
      },
      {
        "id": 305,
        "logname": "crusaders_crossbow",
        "name": "Crusader's Crossbow",
        "slot_type": "Primary"
      },
      {
        "id": 412,
        "logname": "proto_syringe",
        "name": "The Overdose",
        "slot_type": "Primary"
      },
      {
        "id": 29,
        "logname": "medigun",
        "name": "Medi Gun",
        "slot_type": "Secondary"
      },
      {
        "id": 35,
        "logname": "kritzkrieg",
        "name": "The Kritzkrieg",
        "slot_type": "Secondary"
      },
      {
        "id": 411,
        "name": "The Quick-Fix",
        "slot_type": "Secondary"
      },
      {
        "id": 998,
        "name": "The Vaccinator",
        "slot_type": "Secondary"
      },
      {
        "id": 8,
        "logname": "bonesaw",
        "name": "Bonesaw",
        "slot_type": "Melee"
      },
      {
        "id": 37,
        "logname": "ubersaw",
        "name": "The Ubersaw",
        "slot_type": "Melee"
      },
      {
        "id": 173,
        "name": "The Vita-Saw",
        "slot_type": "Melee"
      },
      {
        "id": 304,
        "logname": "battleneedle",
        "name": "Amputator",
        "slot_type": "Melee"
      },
      {
        "id": 413,
        "logname": "solemn_vow",
        "name": "The Solemn Vow",
        "slot_type": "Melee"
      }
    ]
  ],
  [
    "Sniper",
    [
      {
        "id": 14,
        "logname": "sniperrifle",
        "name": "Sniper Rifle",
        "slot_type": "Primary"
      },
      {
        "id": 56,
        "logname": "tf_projectile_arrow",
        "name": "The Huntsman",
        "slot_type": "Primary"
      },
      {
        "id": 230,
        "logname": "sydney_sleeper",
        "name": "The Sydney Sleeper",
        "slot_type": "Primary"
      },
      {
        "id": 402,
        "logname": "bazaar_bargain",
        "name": "The Bazaar Bargain",
        "slot_type": "Primary"
      },
      {
        "id": 526,
        "logname": "machina",
        "name": "The Machina",
        "slot_type": "Primary"
      },
      {
        "id": 752,
        "logname": "pro_rifle",
        "name": "The Hitman's Heatmaker",
        "slot_type": "Primary"
      },
      {
        "id": 851,
        "logname": "awper_hand",
        "reskin": 14,
        "name": "The AWPer Hand",
        "slot_type": "Primary"
      },
      {
        "id": 56,
        "logname": "tf_projectile_arrow",
        "reskin": 56,
        "name": "The Fortified Compound",
        "slot_type": "Primary"
      },
      {
        "id": 1098,
        "logname": "the_classic",
        "name": "The Classic",
        "slot_type": "Primary"
      },
      {
        "id": 16,
        "logname": "smg",
        "name": "SMG",
        "slot_type": "Secondary"
      },
      {
        "id": 57,
        "name": "The Razorback",
        "slot_type": "Secondary"
      },
      {
        "id": 58,
        "name": "Jarate",
        "slot_type": "Secondary"
      },
      {
        "id": 231,
        "name": "Darwin's Danger Shield",
        "slot_type": "Secondary"
      },
      {
        "id": 642,
        "name": "Cozy Camper",
        "slot_type": "Secondary"
      },
      {
        "id": 751,
        "logname": "pro_smg",
        "name": "The Cleaner's Carbine",
        "slot_type": "Secondary"
      },
      {
        "id": 1105,
        "name": "The Self-Aware Beauty Mark",
        "reskin": 58,
        "slot_type": "Secondary"
      },
      {
        "id": 3,
        "logname": "kukri",
        "name": "Kukri",
        "slot_type": "Melee"
      },
      {
        "id": 171,
        "logname": "tribalkukri",
        "name": "The Tribalman's Shiv",
        "slot_type": "Melee"
      },
      {
        "id": 232,
        "logname": "bushwacka",
        "name": "The Bushwacka",
        "slot_type": "Melee"
      },
      {
        "id": 401,
        "logname": "scimitar",
        "name": "The Shahanshah",
        "slot_type": "Melee"
      }
    ]
  ],
  [
    "Spy",
    [
      {
        "id": 24,
        "logname": "revolver",
        "name": "Revolver",
        "slot_type": "Secondary"
      },
      {
        "id": 61,
        "logname": "ambassador",
        "name": "The Ambassador",
        "slot_type": "Secondary"
      },
      {
        "id": 161,
        "logname": "revolver",
        "reskin": 24,
        "name": "Big Kill",
        "slot_type": "Secondary"
      },
      {
        "id": 224,
        "logname": "letranger",
        "name": "L'Etranger",
        "slot_type": "Secondary"
      },
      {
        "id": 460,
        "logname": "enforcer",
        "name": "The Enforcer",
        "slot_type": "Secondary"
      },
      {
        "id": 525,
        "logname": "diamondback",
        "name": "The Diamondback",
        "slot_type": "Secondary"
      },
      {
        "id": 735,
        "logname": "sapper",
        "name": "Sapper",
        "slot_type": "Building"
      },
      {
        "id": 810,
        "logname": "red_tape_recorder",
        "name": "The Red-Tape Recorder",
        "slot_type": "Building"
      },
      {
        "id": 1102,
        "reskin": 735,
        "name": "The Snack Attack",
        "slot_type": "Building"
      },
      {
        "id": 4,
        "logname": "knife",
        "name": "Knife",
        "slot_type": "Melee"
      },
      {
        "id": 225,
        "logname": "eternal_reward",
        "name": "Your Eternal Reward",
        "slot_type": "Melee"
      },
      {
        "id": 356,
        "logname": "kunai",
        "name": "Conniver's Kunai",
        "slot_type": "Melee"
      },
      {
        "id": 461,
        "logname": "big_earner",
        "name": "The Big Earner",
        "slot_type": "Melee"
      },
      {
        "id": 649,
        "logname": "spy_cicle",
        "name": "Spy-cicle",
        "slot_type": "Melee"
      },
      {
        "id": 574,
        "logname": "eternal_reward",
        "reskin": 225,
        "name": "The Wanga Prick",
        "slot_type": "Melee"
      },
      {
        "id": 638,
        "logname": "knife",
        "reskin": 4,
        "name": "The Sharp Dresser",
        "slot_type": "Melee"
      },
      {
        "id": 727,
        "logname": "black_rose",
        "reskin": 4,
        "name": "The Black Rose",
        "slot_type": "Melee"
      },
      {
        "id": 27,
        "name": "Disguise Kit PDA",
        "slot_type": "PDA"
      },
      {
        "id": 30,
        "name": "Invis Watch",
        "slot_type": "PDA2"
      },
      {
        "id": 59,
        "name": "The Dead Ringer",
        "slot_type": "Melee"
      },
      {
        "id": 60,
        "name": "The Cloak and Dagger",
        "slot_type": "Melee"
      },
      {
        "id": 298,
        "name": "Enthusiast's Timepiece",
        "reskin": 30,
        "slot_type": "Melee"
      },
      {
        "id": 947,
        "name": "The Quackenbirdt",
        "reskin": 30,
        "slot_type": "Melee"
      }
    ]
  ]
]"""


reskin_map = {
    727: 638,
    294: 22,
    352: 325,
    405: 608,
    457: 38,
    466: 153,
    266: 132,
    482: 132,
    433: 159,
    587: 5,
    1100: 239,
    169: 7,
    851: 14,
    1092: 56,
    161: 24,
    30474: 21,
}


class Item:
    def __init__(self, weapon_dict):
        self.index = weapon_dict["id"]
        self.name = weapon_dict["name"]
        self.slot_type = weapon_dict["slot_type"]

        self.has_log_name = False
        self.is_reskin = False

        if "logname" in weapon_dict:
            self.logname = weapon_dict["logname"]
            self.has_log_name = True

        if "reskin" in weapon_dict:
            self.reskin = weapon_dict["reskin"]
            self.is_reskin = True


class ItemSchema:
    def __init__(self):

        self.items = {}
        self.lognames = {}

        item_json = json.loads(schema)

        for class_index in range(0, 9):
            for weapon_dict in item_json[class_index][1]:
                item = Item(weapon_dict)
                self.items[weapon_dict["id"]] = item
                if "logname" in weapon_dict:
                    self.lognames[weapon_dict["logname"]] = item.index
