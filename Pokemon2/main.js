//Denne siden er laget av Kristoffer Kirkerød

//---------------------Variabler----------------------------

//Liste med Pokemon   Id, Name, Got it?, Got it in shiny?
let pokedex_array = [  
  [1, 'Bulbasaur',0 ,0], [2, 'Ivysaur',0 ,0], [3, 'Venusaur',0 ,0], [4, 'Charmander',0 ,0], [5, 'Charmeleon',0 ,0], [6, 'Charizard',0 ,0],
  [7, 'Squirtle',0 ,0], [8, 'Wartortle',0 ,0], [9, 'Blastoise',0 ,0], [10, 'Caterpie',0 ,0], [11, 'Metapod',0 ,0], [12, 'Butterfree',0 ,0],
  [13, 'Weedle',0 ,0], [14, 'Kakuna',0 ,0], [15, 'Beedrill',0 ,0], [16, 'Pidgey',0 ,0], [17, 'Pidgeotto',0 ,0], [18, 'Pidgeot',0 ,0],
  [19, 'Rattata',0 ,0], [20, 'Raticate',0 ,0], [21, 'Spearow',0 ,0], [22, 'Fearow',0 ,0], [23, 'Ekans',0 ,0], [24, 'Arbok',0 ,0],
  [25, 'Pikachu',0 ,0], [26, 'Raichu',0 ,0], [27, 'Sandshrew',0 ,0], [28, 'Sandslash',0 ,0], [29, 'Nidoran♀',0 ,0], [30, 'Nidorina',0 ,0],
  [31, 'Nidoqueen',0 ,0], [32, 'Nidoran♂',0 ,0], [33, 'Nidorino',0 ,0], [34, 'Nidoking',0 ,0], [35, 'Clefairy',0 ,0], [36, 'Clefable',0 ,0],
  [37, 'Vulpix',0 ,0], [38, 'Ninetales',0 ,0], [39, 'Jigglypuff',0 ,0], [40, 'Wigglytuff',0 ,0], [41, 'Zubat',0 ,0], [42, 'Golbat',0 ,0],
  [43, 'Oddish',0 ,0], [44, 'Gloom',0 ,0], [45, 'Vileplume',0 ,0], [46, 'Paras',0 ,0], [47, 'Parasect',0 ,0], [48, 'Venonat',0 ,0],
  [49, 'Venomoth',0 ,0], [50, 'Diglett',0 ,0], [51, 'Dugtrio',0 ,0], [52, 'Meowth',0 ,0], [53, 'Persian',0 ,0], [54, 'Psyduck',0 ,0],
  [55, 'Golduck',0 ,0], [56, 'Mankey',0 ,0], [57, 'Primeape',0 ,0], [58, 'Growlithe',0 ,0], [59, 'Arcanine',0 ,0], [60, 'Poliwag',0 ,0],
  [61, 'Poliwhirl',0 ,0], [62, 'Poliwrath',0 ,0], [63, 'Abra',0 ,0], [64, 'Kadabra',0 ,0], [65, 'Alakazam',0 ,0], [66, 'Machop',0 ,0],
  [67, 'Machoke',0 ,0], [68, 'Machamp',0 ,0], [69, 'Bellsprout',0 ,0], [70, 'Weepinbell',0 ,0], [71, 'Victreebel',0 ,0], [72, 'Tentacool',0 ,0],
  [73, 'Tentacruel',0 ,0], [74, 'Geodude',0 ,0], [75, 'Graveler',0 ,0], [76, 'Golem',0 ,0], [77, 'Ponyta',0 ,0], [78, 'Rapidash',0 ,0],
  [79, 'Slowpoke',0 ,0], [80, 'Slowbro',0 ,0], [81, 'Magnemite',0 ,0], [82, 'Magneton',0 ,0], [83, 'Farfetchd',0 ,0], [84, 'Doduo',0 ,0],
  [85, 'Dodrio',0 ,0], [86, 'Seel',0 ,0], [87, 'Dewgong',0 ,0], [88, 'Grimer',0 ,0], [89, 'Muk',0 ,0], [90, 'Shellder',0 ,0],
  [91, 'Cloyster',0 ,0], [92, 'Gastly',0 ,0], [93, 'Haunter',0 ,0], [94, 'Gengar',0 ,0], [95, 'Onix',0 ,0], [96, 'Drowzee',0 ,0],
  [97, 'Hypno',0 ,0], [98, 'Krabby',0 ,0], [99, 'Kingler',0 ,0], [100, 'Voltorb',0 ,0], [101, 'Electrode',0 ,0], [102, 'Exeggcute',0 ,0],
  [103, 'Exeggutor',0 ,0], [104, 'Cubone',0 ,0], [105, 'Marowak',0 ,0], [106, 'Hitmonlee',0 ,0], [107, 'Hitmonchan',0 ,0], [108, 'Lickitung',0 ,0],
  [109, 'Koffing',0 ,0], [110, 'Weezing',0 ,0], [111, 'Rhyhorn',0 ,0], [112, 'Rhydon',0 ,0], [113, 'Chansey',0 ,0], [114, 'Tangela',0 ,0],
  [115, 'Kangaskhan',0 ,0], [116, 'Horsea',0 ,0], [117, 'Seadra',0 ,0], [118, 'Goldeen',0 ,0], [119, 'Seaking',0 ,0], [120, 'Staryu',0 ,0],
  [121, 'Starmie',0 ,0], [122, 'Mr.Mime',0 ,0], [123, 'Scyther',0 ,0], [124, 'Jynx',0 ,0], [125, 'Electabuzz',0 ,0], [126, 'Magmar',0 ,0],
  [127, 'Pinsir',0 ,0], [128, 'Tauros',0 ,0], [129, 'Magikarp',0 ,0], [130, 'Gyarados',0 ,0], [131, 'Lapras',0 ,0], [132, 'Ditto',0 ,0],
  [133, 'Eevee',0 ,0], [134, 'Vaporeon',0 ,0], [135, 'Jolteon',0 ,0], [136, 'Flareon',0 ,0], [137, 'Porygon',0 ,0], [138, 'Omanyte',0 ,0],
  [139, 'Omastar',0 ,0], [140, 'Kabuto',0 ,0], [141, 'Kabutops',0 ,0], [142, 'Aerodactyl',0 ,0], [143, 'Snorlax',0 ,0], [144, 'Articuno',0 ,0],
  [145, 'Zapdos',0 ,0], [146, 'Moltres',0 ,0], [147, 'Dratini',0 ,0], [148, 'Dragonair',0 ,0], [149, 'Dragonite',0 ,0], [150, 'Mewtwo',0 ,0],
  [151, 'Mew',0 ,0], 
  
  [152,'Chikorita',0 ,0], [153,'Bayleef',0 ,0], [154,'Meganium',0 ,0], [155,'Cyndaquil',0 ,0], [156,'Quilava',0 ,0], [157,'Typhlosion',0 ,0], 
  [158,'Totodile',0 ,0], [159,'Croconaw',0 ,0], [160,'Feraligatr',0 ,0], [161,'Sentret',0 ,0], [162,'Furret',0 ,0], [163,'Hoothoot',0 ,0], 
  [164,'Noctowl',0 ,0], [165,'Ledyba',0 ,0], [166,'Ledian',0 ,0], [167,'Spinarak',0 ,0], [168,'Ariados',0 ,0], [169,'Crobat',0 ,0], 
  [170,'Chinchou',0 ,0], [171,'Lanturn',0 ,0], [172,'Pichu',0 ,0], [173,'Cleffa',0 ,0], [174,'Igglybuff',0 ,0], [175,'Togepi',0 ,0], 
  [176,'Togetic',0 ,0], [177,'Natu',0 ,0], [178,'Xatu',0 ,0], [179,'Mareep',0 ,0], [180,'Flaaffy',0 ,0], [181,'Ampharos',0 ,0], 
  [182,'Bellossom',0 ,0], [183,'Marill',0 ,0], [184,'Azumarill',0 ,0], [185,'Sudowoodo',0 ,0], [186,'Politoed',0 ,0], [187,'Hoppip',0 ,0], 
  [188,'Skiploom',0 ,0], [189,'Jumpluff',0 ,0], [190,'Aipom',0 ,0], [191,'Sunkern',0 ,0], [192,'Sunflora',0 ,0], [193,'	Yanma',0 ,0], 
  [194,'Wooper',0 ,0], [195,'Quagsire',0 ,0], [196,'Espeon',0 ,0], [197,'Umbreon',0 ,0], [198,'Murkrow',0 ,0], [199,'Slowking',0 ,0], 
  [200,'Misdreavus',0 ,0], [201,'Unown',0 ,0], [202,'Wobbuffet',0 ,0], [203,'Girafarig',0 ,0], [204,'Pineco',0 ,0], [205,'Forretress',0 ,0], 
  [206,'Dunsparce',0 ,0], [207,'Gligar',0 ,0], [208,'Steelix',0 ,0], [209,'Snubbull',0 ,0], [210,'Granbull',0 ,0], [211,'Qwilfish',0 ,0], 
  [212,'Scizor',0 ,0], [213,'Shuckle',0 ,0], [214,'Heracross',0 ,0], [215,'Sneasel',0 ,0], [216,'Teddiursa',0 ,0], [217,'Ursaring',0 ,0], 
  [218,'Slugma',0 ,0], [219,'Magcargo',0 ,0], [220,'Swinub',0 ,0], [221,'Piloswine',0 ,0], [222,'Corsola',0 ,0], [223,'Remoraid',0 ,0], 
  [224,'Octillery',0 ,0], [225,'Delibird',0 ,0], [226,'Mantine',0 ,0], [227,'Skarmory',0 ,0], [228,'Houndour',0 ,0], [229,'Houndoom',0 ,0], 
  [230,'Kingdra',0 ,0], [231,'Phanpy',0 ,0], [232,'Donphan',0 ,0], [233,'Porygon2',0 ,0], [234,'Stantler',0 ,0], [235,'Smeargle',0 ,0],
  [236,'Tyrogue',0 ,0], [237,'Hitmontop',0 ,0], [238,'Smoochum',0 ,0], [239,'Elekid',0 ,0], [240,'Magby',0 ,0], [241,'Miltank',0 ,0],
  [242,'Blissey',0 ,0], [243,'Raikou',0 ,0], [244,'Entei',0 ,0], [245,'Suicune',0 ,0], [246,'Larvitar',0 ,0], [247,'Pupitar',0 ,0],
  [248,'Tyranitar',0 ,0], [249,'Lugia',0 ,0], [250,'Ho-oh',0 ,0], [251,'Celebi',0 ,0], 
  
  [252,'Treecko',0 ,0], [253,'Grovyle',0 ,0], [254,'Sceptile',0 ,0], [255,'Torchic',0 ,0], [256,'Combusken',0 ,0], [257,'Blaziken',0 ,0], 
  [258,'Mudkip',0 ,0], [259,'Marshtomp',0 ,0], [260,'Swampert',0 ,0], [261,'Poochyena',0 ,0], [262,'Mightyena',0 ,0], [263,'Zigzagoon',0 ,0], 
  [264,'Linoone',0 ,0], [265,'Wurmple',0 ,0], [266,'Silcoon',0 ,0], [267,'Beautifly',0 ,0], [268,'Cascoon',0 ,0], [269,'Dustox',0 ,0], 
  [270,'Lotad',0 ,0], [271,'Lombre',0 ,0], [272,'Ludicolo',0 ,0], [273,'Seedot',0 ,0], [274,'Nuzleaf',0 ,0], [275,'Shiftry',0 ,0], 
  [276,'Taillow',0 ,0], [277,'Swellow',0 ,0], [278,'Wingull',0 ,0], [279,'Pelipper',0 ,0], [280,'Ralts',0 ,0], [281,'Kirlia',0 ,0], 
  [282,'Gardevoir',0 ,0], [283,'Surskit',0 ,0], [284,'Masquerain',0 ,0], [285,'Shroomish',0 ,0], [286,'Breloom',0 ,0], [287,'Slakoth',0 ,0], 
  [288,'Vigoroth',0 ,0], [289,'Slaking',0 ,0], [290,'Nincada',0 ,0], [291,'Ninjask',0 ,0], [292,'Shedinja',0 ,0], [293,'Whismur',0 ,0], 
  [294,'Loudred',0 ,0], [295,'Exploud',0 ,0], [296,'Makuhita',0 ,0], [297,'Hariyama',0 ,0], [298,'Azurill',0 ,0], [299,'Nosepass',0 ,0], 
  [300,'Skitty',0 ,0], [301,'Delcatty',0 ,0], [302,'Sableye',0 ,0], [303,'Mawile',0 ,0], [304,'Aron',0 ,0], [305,'Lairon',0 ,0], 
  [306,'Aggron',0 ,0], [307,'Meditite',0 ,0], [308,'Medicham',0 ,0], [309,'Electrike',0 ,0], [310,'Manectric',0 ,0], [311,'Plusle',0 ,0], 
  [312,'Minun',0 ,0], [313,'Volbeat',0 ,0], [314,'Illumise',0 ,0], [315,'Roselia',0 ,0], [316,'Gulpin',0 ,0], [317,'Swalot',0 ,0], 
  [318,'Carvanha',0 ,0], [319,'Sharpedo',0 ,0], [320,'Wailmer',0 ,0], [321,'Wailord',0 ,0], [322,'Numel',0 ,0], [323,'Camerupt',0 ,0], 
  [324,'Torkoal',0 ,0], [325,'Spoink',0 ,0], [326,'Grumpig',0 ,0], [327,'Spinda',0 ,0], [328,'Trapinch',0 ,0], [329,'Vibrava',0 ,0], 
  [330,'Flygon',0 ,0], [331,'Cacnea',0 ,0], [332,'Cacturne',0 ,0], [333,'Swablu',0 ,0], [334,'Altaria',0 ,0], [335,'Zangoose',0 ,0], 
  [336,'Seviper',0 ,0], [337,'Lunatone',0 ,0], [338,'Solrock',0 ,0], [339,'Barboach',0 ,0], [340,'Whiscash',0 ,0], [341,'Corphish',0 ,0], 
  [342,'Crawdaunt',0 ,0], [343,'Baltoy',0 ,0], [344,'Claydol',0 ,0], [345,'Lileep',0 ,0], [346,'Cradily',0 ,0], [347,'Anorith',0 ,0], 
  [348,'Armaldo',0 ,0], [349,'Feebas',0 ,0], [350,'Milotic',0 ,0], [351,'Castform',0 ,0], [352,'Kecleon',0 ,0], [353,'Shuppet',0 ,0], 
  [354,'Banette',0 ,0], [355,'Duskull',0 ,0], [356,'Dusclops',0 ,0], [357,'Tropius',0 ,0], [358,'Chimecho',0 ,0], [359,'Absol',0 ,0], 
  [360,'Wynaut',0 ,0], [361,'Snorunt',0 ,0], [362,'Glalie',0 ,0], [363,'Spheal',0 ,0], [364,'Sealeo',0 ,0], [365,'Walrein',0 ,0], 
  [366,'Clamperl',0 ,0], [367,'Huntail',0 ,0], [368,'Gorebyss',0 ,0], [369,'Relicanth',0 ,0], [370,'Luvdisc',0 ,0], [371,'Bagon',0 ,0], 
  [372,'Shelgon',0 ,0], [373,'Salamence',0 ,0], [374,'Beldum',0 ,0], [375,'Metang',0 ,0], [376,'Metagross',0 ,0], [377,'Regirock',0 ,0], 
  [378,'Regice',0 ,0], [379,'Registeel',0 ,0], [380,'Latias',0 ,0], [381,'Latios',0 ,0], [382,'Kyogre',0 ,0], [383,'Groudon',0 ,0],
  [384,'Rayquaza',0 ,0], [385,'Jirachi',0 ,0], [386,'Deoxys',0 ,0], 
  
  [387,'Turtwig',0 ,0], [388,'Grotle',0 ,0], [389,'Torterra',0 ,0], 
  [390,'Chimchar',0 ,0], [391,'Monferno',0 ,0], [392,'Infernape',0 ,0], [393,'Piplup',0 ,0], [394,'Prinplup',0 ,0], [395,'Empoleon',0 ,0], 
  [396,'Starly',0 ,0], [397,'Staravia',0 ,0], [398,'Staraptor',0 ,0], [399,'Bidoof',0 ,0], [400,'Bibarel',0 ,0], [401,'Kricketot',0 ,0], 
  [402,'Kricketune',0 ,0], [403,'Shinx',0 ,0], [404,'Luxio',0 ,0], [405,'Luxray',0 ,0], [406,'Budew',0 ,0], [407,'Roserade',0 ,0], 
  [408,'Cranidos',0 ,0], [409,'Rampardos',0 ,0], [410,'Shieldon',0 ,0], [411,'Bastiodon',0 ,0], [412,'Burmy',0 ,0], [413,'Wormadam',0 ,0], 
  [414,'Mothim',0 ,0], [415,'Combee',0 ,0], [416,'Vespiquen',0 ,0], [417,'Pachirisu',0 ,0], [418,'Buizel',0 ,0], [419,'Floatzel',0 ,0], 
  [420,'Cherubi',0 ,0], [421,'Cherrim',0 ,0], [422,'Shellos',0 ,0], [423,'Gastrodon',0 ,0], [424,'Ambipom',0 ,0], [425,'Drifloon',0 ,0], 
  [426,'Drifblim',0 ,0], [427,'Buneary',0 ,0], [428,'Lopunny',0 ,0], [429,'Mismagius',0 ,0], [430,'Honchkrow',0 ,0], [431,'Glameow',0 ,0], 
  [432,'Purugly',0 ,0], [433,'Chingling',0 ,0], [434,'Stunky',0 ,0], [435,'Skuntank',0 ,0], [436,'Bronzor',0 ,0], [437,'Bronzong',0 ,0], 
  [438,'Bonsly',0 ,0], [439,'Mime Jr.',0 ,0], [440,'Happiny',0 ,0], [441,'Chatot',0 ,0], [442,'Spiritomb',0 ,0], [443,'Gible',0 ,0], 
  [444,'Gabite',0 ,0], [445,'Garchomp',0 ,0], [446,'Munchlax',0 ,0], [447,'Riolu',0 ,0], [448,'Lucario',0 ,0], [449,'Hippopotas',0 ,0], 
  [450,'Hippowdon',0 ,0], [451,'Skorupi',0 ,0], [452,'Drapion',0 ,0], [453,'Croagunk',0 ,0], [454,'Toxicroak',0 ,0], [455,'Carnivine',0 ,0], 
  [456,'Finneon',0 ,0], [457,'Lumineon',0 ,0], [458,'Mantyke',0 ,0], [459,'Snover',0 ,0], [460,'Abomasnow',0 ,0], [461,'Weavile',0 ,0], 
  [462,'Magnezone',0 ,0], [463,'Lickilicky',0 ,0], [464,'Rhyperior',0 ,0], [465,'Tangrowth',0 ,0], [466,'Electivire',0 ,0], [467,'Magmortar',0 ,0], 
  [468,'Togekiss',0 ,0], [469,'Yanmega',0 ,0], [470,'Leafeon',0 ,0], [471,'Glaceon',0 ,0], [472,'Gliscor',0 ,0], [473,'Mamoswine',0 ,0], 
  [474,'Porygon-Z',0 ,0], [475,'Gallade',0 ,0], [476,'Probopass',0 ,0], [477,'Dusknoir',0 ,0], [478,'Froslass',0 ,0], [479,'Rotom',0 ,0], 
  [480,'Uxie',0 ,0], [481,'Mesprit',0 ,0], [482,'Azelf',0 ,0], [483,'Dialga',0 ,0], [484,'Palkia',0 ,0], [485,'Heatran',0 ,0], 
  [486,'Regigigas',0 ,0], [487,'Giratina',0 ,0], [488,'Cresselia',0 ,0], [489,'Phione',0 ,0], [490,'Manaphy',0 ,0], [491,'Darkrai',0 ,0], 
  [492,'Shaymin',0 ,0], [493,'Arceus',0 ,0], 
  
  
  [494,'Victini',0 ,0], [495,'Snivy',0 ,0], [496,'Servine',0 ,0], [497,'Serperior',0 ,0], [498,'Tepig',0 ,0],
  [499,'Pignite',0 ,0], [500,'Emboar',0 ,0], [501,'Oshawott',0 ,0], [502,'Dewott',0 ,0], [503,'Samurott',0 ,0],
  [504,'Patrat',0 ,0], [505,'Watchog',0 ,0], [506,'Lillipup',0 ,0], [507,'Herdier',0 ,0], [508,'Stoutland',0 ,0],
  [509,'Purrloin',0 ,0], [510,'Liepard',0 ,0], [511,'Pansage',0 ,0], [512,'Simisage',0 ,0], [513,'Pansear',0 ,0],
  [514,'Simisear',0 ,0], [515,'Panpour',0 ,0], [516,'Simipour',0 ,0], [517,'Munna',0 ,0], [518,'Musharna',0 ,0],
  [519,'Pidove',0 ,0], [520,'Tranquill',0 ,0], [521,'Unfezant',0 ,0], [522,'Blitzle',0 ,0], [523,'Zebstrika',0 ,0],
  [524,'Roggenrola',0 ,0], [525,'Boldore',0 ,0], [526,'Gigalith',0 ,0], [527,'Woobat',0 ,0], [528,'Swoobat',0 ,0],
  [529,'Drilbur',0 ,0], [530,'Excadrill',0 ,0], [531,'Audino',0 ,0], [532,'Timburr',0 ,0], [533,'Gurdurr',0 ,0],
  [534,'Conkeldurr',0 ,0], [535,'Tympole',0 ,0], [536,'Palpitoad',0 ,0], [537,'Seismitoad',0 ,0], [538,'Throh',0 ,0],
  [539,'Sawk',0 ,0], [540,'Sewaddle',0 ,0], [541,'Swadloon',0 ,0], [542,'Leavanny',0 ,0], [543,'Venipede',0 ,0],
  [544,'Whirlipede',0 ,0], [545,'Scolipede',0 ,0], [546,'Cottonee',0 ,0], [547,'Whimsicott',0 ,0], [548,'Petilil',0 ,0],
  [549,'Lilligant',0 ,0], [550,'Basculin',0 ,0], [551,'Sandile',0 ,0], [552,'Krokorok',0 ,0], [553,'Krookodile',0 ,0],
  [554,'Darumaka',0 ,0], [555,'Darmanitan',0 ,0], [556,'Maractus',0 ,0], [557,'Dwebble',0 ,0], [558,'Crustle',0 ,0],
  [559,'Scraggy',0 ,0], [560,'Scrafty',0 ,0], [561,'Sigilyph',0 ,0], [562,'Yamask',0 ,0], [563,'Cofagrigus',0 ,0],
  [564,'Tirtouga',0 ,0], [565,'Carracosta',0 ,0], [566,'Archen',0 ,0], [567,'Archeops',0 ,0], [568,'Trubbish',0 ,0],
  [569,'Garbodor',0 ,0], [570,'Zorua',0 ,0], [571,'Zoroark',0 ,0], [572,'Minccino',0 ,0], [573,'Cinccino',0 ,0],
  [574,'Gothita',0 ,0], [575,'Gothorita',0 ,0], [576,'Gothitelle',0 ,0], [577,'Solosis',0 ,0], [578,'Duosion',0 ,0],
  [579,'Reuniclus',0 ,0], [580,'Ducklett',0 ,0], [581,'Swanna',0 ,0], [582,'Vanillite',0 ,0], [583,'Vanillish',0 ,0],
  [584,'Vanilluxe',0 ,0], [585,'Deerling',0 ,0], [586,'Sawsbuck',0 ,0], [587,'Emolga',0 ,0], [588,'Karrablast',0 ,0],
  [589,'Escavalier',0 ,0], [590,'Foongus',0 ,0], [591,'Amoonguss',0 ,0], [592,'Frillish',0 ,0], [593,'Jellicent',0 ,0],
  [594,'Alomomola',0 ,0], [595,'Joltik',0 ,0], [596,'Galvantula',0 ,0], [597,'Ferroseed',0 ,0], [598,'Ferrothorn',0 ,0],
  [599,'Klink',0 ,0], [600,'Klang',0 ,0], [601,'Klinklang',0 ,0], [602,'Tynamo',0 ,0], [603,'Eelektrik',0 ,0],
  [604,'Eelektross',0 ,0], [605,'Elgyem',0 ,0], [606,'Beheeyem',0 ,0], [607,'Litwick',0 ,0], [608,'Lampent',0 ,0],
  [609,'Chandelure',0 ,0], [610,'Axew',0 ,0], [611,'Fraxure',0 ,0], [612,'Haxorus',0 ,0], [613,'Cubchoo',0 ,0],
  [614,'Beartic',0 ,0], [615,'Cryogonal',0 ,0], [616,'Shelmet',0 ,0], [617,'Accelgor',0 ,0], [618,'Stunfisk',0 ,0],
  [619,'Mienfoo',0 ,0], [620,'Mienshao',0 ,0], [621,'Druddigon',0 ,0], [622,'Golett',0 ,0], [623,'Golurk',0 ,0],
  [624,'Pawniard',0 ,0], [625,'Bisharp',0 ,0], [626,'Bouffalant',0 ,0], [627,'Rufflet',0 ,0], [628,'Braviary',0 ,0],
  [629,'Vullaby',0 ,0], [630,'Mandibuzz',0 ,0], [631,'Heatmor',0 ,0], [632,'Durant',0 ,0], [633,'Deino',0 ,0],
  [634,'Zweilous',0 ,0], [635,'Hydreigon',0 ,0], [636,'Larvesta',0 ,0], [637,'Volcarona',0 ,0], [638,'Cobalion',0 ,0],
  [639,'Terrakion',0 ,0], [640,'Virizion',0 ,0], [641,'Tornadus',0 ,0], [642,'Thundurus',0 ,0], [643,'Reshiram',0 ,0],
  [644,'Zekrom',0 ,0], [645,'Landorus',0 ,0], [646,'Kyurem',0 ,0], [647,'Keldeo',0 ,0], [648,'Meloetta',0 ,0],
  [649,'Genesect',0 ,0]


  
]

//SoneNr, Navn, Antall pkmn, Startindex, Sluttindex
let regions = [
  ['1', 'Kanto', '151', '0', '151', 'unlocked'],
  ['2', 'Johto', '100', '151', '251', 'locked'],
  ['3', 'Hoenn', '135', '251', '386', 'locked'],
  ['4', 'Sinnoh', '107', '386', '493', 'locked'],
  ['5', 'Unova', '156', '493', '649', 'locked']
]

//Badge bilder
var badge_info = [
  ["Kanto", 0, 10, 25, 50, 75, 100, 120, 140, 151,'#fb6868'],
  ["Johto", 0, 10, 20, 40, 50, 60, 80, 90, 100, '#77B65C'],
  ["Hoenn", 0, 10, 25, 50, 75, 100, 110, 125, 135,'#dd6b3f'],
  ["Sinnoh", 0, 10, 20, 40, 50, 75, 85, 100, 107,'#9f56ff'],
  ["Unova", 0, 10, 25, 50, 75, 100, 120, 140, 156,'#394da7']
]

//Hvor er vi? Kanto, Johto eller Hoenn? 0,1,2?
var current_region = 0

//Vanskelighetsgrad
var difficulty = 'pluss_level_1'

//Poeng før man får en pokemon
var max_points = 5
var current_points = 0

//Hvor mange resets vi har
var resets = 0

//Sjansen for en Shiny Pokemon
let chance_shiny_array = [20, 4, 2, 1]
let chance_shiny = chance_shiny_array[resets]


//Lyd variabler
var audio_rett = new Audio('Sounds/correct.mp3');


//Hvor mange pokemon har du fanget i den sonen du er i?
var antall_pokemon = 0

//Noen navn er litt annerledes nå vi skriver og ser de
let pokemon_name_exceptions = [['Mr.Mime', 'Mr-Mime'], ['Nidoran♀', 'nidoran-f'], ['Nidoran♂', 'nidoran-m'], 
                               ['Mime Jr.', 'mime-jr'], ['Giratina', 'giratina-altered'], ['Shaymin', 'shaymin-land']
]


//Hvilke typer pokeball-bilder vi har
let pokeball_img_array = ["Bilder/Pokeballs/pokeball.png", "Bilder/Pokeballs/greatball.png", 
                          "Bilder/Pokeballs/ultraball.png", "Bilder/Pokeballs/masterball.png"
]



//Om settings er synlig eller ikke
var settings = false

//Slik at vi lett kan bytte mellom sprites
var sprite_dir_nr = 1
var sprites_dir = [['Bilder/Knapper/sprites_use_2d.png', 'Bilder/Sprites/Sprites1', '2D'], 
                   ['Bilder/Knapper/sprites_use_3d.png', 'Bilder/Sprites/Sprites2', '3D']
]

//Skrur lyd av og på
var sound_volume = 0
var sound_dir = [["OFF", "Bilder/Knapper/music2.png"], ["ON", "Bilder/Knapper/music.png"]]

//Kan man jukse med koder?
var cheating = false

//Slik at du ikke scroller ned til bunn av pokedex når du loader inn alle pokemonene
var loading = true 



//-----------------------------------------------------------------------------------------------
function first_time_load(){
  console.log("No savedata found..")
  console.log("Creating new savedata.. done")
  
  //Vanskelighetsgrad loading
  localStorage.setItem('difficulty', 'pluss_level_1')

  //Pokedex loading
  localStorage.setItem('pokedex', pokedex_array)

  //Region loading
  localStorage.setItem('region', current_region)
  localStorage.setItem('region_lock', regions)

  //Favoritt loading
  localStorage.setItem('fav_path', "")    
  localStorage.setItem('fav_name', "")  
  difficulty = localStorage.getItem('difficulty')

  //Spritetype loading
  localStorage.setItem('sprites', sprite_dir_nr)

  //Sound volume
  localStorage.setItem('volume', sound_volume)

  //Badges
  localStorage.setItem('Kanto_badges', 0)
  localStorage.setItem('Johto_badges', 0)
  localStorage.setItem('Hoenn_badges', 0)
  localStorage.setItem('Sinnoh_badges', 0)
  localStorage.setItem('Unova_badges', 0)
}

function load_game(){
  //Load difficulty
  difficulty = localStorage.getItem('difficulty')
  if(difficulty == null){first_time_load()}
  document.getElementById("dropdown").value = difficulty
  change_difficulty(difficulty)

  //Load region
  current_region = localStorage.getItem('region')

  //Loader riktig sprite type
  sprite_dir_nr = localStorage.getItem('sprites')
  document.getElementById('sprites_change').src = sprites_dir[sprite_dir_nr][0]

  //Loader hvor mange resets vi har
  resets = localStorage.getItem('resets')
  if(resets == null){resets = 0}
  resets = parseInt(resets)
  make_stars()

  //Load Pokemon
  var temp = localStorage.getItem("pokedex")

  var temp = temp.split(",")
  var count = 0
  let new_array = []

  //Gjør save-data om til en liste
  for(i=0; i<pokedex_array.length; i++){
    var temp_row = []
    for(ii=0; ii<4; ii++){
      if(ii == 0 || ii == 2 || ii == 3){temp_row.push(parseInt(temp[count]))}
      else{temp_row.push(temp[count])}
      count += 1
    }
    new_array.push(temp_row)
  }
  //console.log(new_array)

  var pkmn_counter = 0
  for(i=regions[current_region][3]; i<regions[current_region][4]; i++){
    var shiny_nr = 1
    if(new_array[i][3] == 1){shiny_nr = 0}
    if(new_array[i][2] == 1){add_pokemon(i, shiny_nr), pkmn_counter+=1}
  }

  //Oppdaterer main array
  pokedex_array = new_array.slice(0)

  document.getElementById('pokedex_nr').innerHTML = "POKEDEX: " + pkmn_counter + "/" + (regions[current_region][2])
  antall_pokemon = pkmn_counter

  //Oppdaterer badges
  add_badges()

  //Loader inn fav pokemon
  var fav_path = localStorage.getItem('fav_path')    
  var fav_name = localStorage.getItem('fav_name')       
  document.getElementById("fav_img").src = fav_path
  document.getElementById("fav_text").textContent = fav_name

  //Loading inn regioner du har unlocked
  temp = localStorage.getItem("region_lock")
  temp = temp.split(",")
  count = 0
  new_array = []

  for(i=0; i<regions.length; i++){
    var temp_row = []
    for(ii=0; ii<6; ii++){
      if(ii == 0 || ii == 2 || ii == 3 || ii == 4){temp_row.push(parseInt(temp[count]))}
      else{temp_row.push(temp[count])}
      count += 1
    }
    new_array.push(temp_row)
  }

  regions = new_array.slice(0)
  //console.log(regions)

  //Gjør om knappene slik de skal være
  change_region_btn()  

  //Er lyden på?
  sound_volume = localStorage.getItem('volume')
  audio_rett.volume = sound_volume
  document.getElementById("sound_btn").src = sound_dir[sound_volume][1]

  //Badges
  var bad1 = localStorage.getItem('Kanto_badges')
  var bad2 = localStorage.getItem('Johto_badges')
  var bad3 = localStorage.getItem('Hoenn_badges')
  var bad4 = localStorage.getItem('Sinnoh_badges')
  var bad5 = localStorage.getItem('Unova_badges')

  loading = false //Loading ferdig

  //Sjekker hvor mange pokemon vi har totalt, har vi alle? 
  if(total_pkmn_check() == pokedex_array.length && resets != 3){
    document.getElementById('reset_btn').style.visibility = "visible"
  }
  
  console.log("--------------------------")
  console.log("Difficulty:", difficulty)
  console.log("Current Region:", regions[current_region][1])
  console.log("Pokedex:", antall_pokemon, "/", regions[current_region][2])
  console.log("National Pokedex:", total_pkmn_check(), "/", pokedex_array.length)
  console.log("All Pokemon:", pokedex_array.length)
  console.log("Favorite Pokemon:", fav_name)
  console.log("Unlocked Regions:")
  console.log("      -", regions[0][1], regions[0][5])
  console.log("      -", regions[1][1], regions[1][5])
  console.log("      -", regions[2][1], regions[2][5])
  console.log("      -", regions[3][1], regions[3][5])
  console.log("      -", regions[4][1], regions[4][5])
  console.log("Number of Badges:")
  console.log("      - Kanto:", bad1)
  console.log("      - Johto:", bad2)
  console.log("      - Hoenn:", bad3)
  console.log("      - Shinnoh:", bad4)
  console.log("      - Unova:", bad5)
  console.log("Sprite-type:", sprites_dir[sprite_dir_nr][2])
  console.log("Volume:",  sound_dir[sound_volume][0])
  console.log("Number of resets:", resets)
  console.log("Shiny chance:", 100/chance_shiny_array[resets] + "%")
  console.log("--------------------------")
}

//Hvis man skal gjøre om på difficulty
function change_difficulty(diff){
  localStorage.setItem('difficulty', diff)
  difficulty = diff
  var sym = ""
  if(diff == "pluss_level_1" || diff == "pluss_level_2" || diff == "pluss_level_3" || diff == "pluss_level_4" || 
  diff == "pluss_level_5" || diff == 'tiervenn_level_1'){sym = "+"}
  if(diff == "minus_level_1" || diff == "minus_level_2" || diff == "minus_level_3" || diff == "minus_level_4" || diff == "minus_level_5"){sym = "-"}
  if(diff == "multi_level_1" || diff == "multi_level_2"){sym = "*"}
  if(diff == "divisjon_level_1" || diff == "divisjon_level_2"){sym = ":"}
  document.getElementById("symbol").innerHTML = sym
  make_math()
}

//Lager nytt mattestykke
function make_math(){
  var n1 = 0
  var n2 = 0

  //Lag regnestykke men tall mellom 1-10
  if(difficulty == "pluss_level_1"){
    n1 = Math.floor(Math.random() * 5) + 2
    n2 = Math.floor(Math.random() * 5) + 2
  }

  //Lag regnestykke men tall mellom 1-20
  if(difficulty == "pluss_level_2"){
    n1 = Math.floor(Math.random() * 10) + 2
    n2 = Math.floor(Math.random() * 10) + 2
  }

  if(difficulty == "pluss_level_3"){
    n1 = Math.floor(Math.random() * 20) + 4
    n2 = Math.floor(Math.random() * 15) + 4
  }

  if(difficulty == "pluss_level_4"){
    n1 = Math.floor(Math.random() * 80) + 5
    n2 = Math.floor(Math.random() * 25) + 5
  }

  if(difficulty == "pluss_level_5"){
    n1 = Math.floor(Math.random() * 500) + 200
    n2 = Math.floor(Math.random() * 500) + 100
  }

  //Lag MINUS regnestykke men tall mellom 1-10
  if(difficulty == "minus_level_1"){
    n1 = Math.floor(Math.random()*10+1);
    n2 = Math.floor(Math.random()*10+1);
    //Flytter slik at n1 alltid er større enn n2
    if(n1 < n2){
      [n1, n2] = [n2, n1]
    }
  }

  //Lag MINUS regnestykke men tall mellom 1-20
  if(difficulty == "minus_level_2"){
    n1 = Math.floor(Math.random()*20+1);
    n2 = Math.floor(Math.random()*20+1);
    //Flytter slik at n1 alltid er større enn n2
    if(n1 < n2){
      [n1, n2] = [n2, n1]
      }
  }
  //Lag MINUS regnestykke level 3
  if(difficulty == "minus_level_3"){
    n1 = Math.floor(Math.random()*40+6);
    n2 = Math.floor(Math.random()*40+6);
    //Flytter slik at n1 alltid er større enn n2
    if(n1 < n2){
      [n1, n2] = [n2, n1]
    }
  }

  //Lag MINUS regnestykke level 4
  if(difficulty == "minus_level_4"){
    n1 = Math.floor(Math.random()*80)+1;
    n2 = Math.floor(Math.random()*80)+1;
    //Flytter slik at n1 alltid er større enn n2
    if(n1 < n2){
      [n1, n2] = [n2, n1]
    }
  }

  //Lag MINUS regnestykke level 5
  if(difficulty == "minus_level_5"){
    n1 = Math.floor(Math.random()*1000)+1;
    n2 = Math.floor(Math.random()*1000)+1;
    //Flytter slik at n1 alltid er større enn n2
    if(n1 < n2){
      [n1, n2] = [n2, n1]
    }
  }
  
  //Lag GANGE regnestykke innen for 1-5 gangetabellen.
  if(difficulty == "multi_level_1"){
    n1 = Math.floor(Math.random()*5+1);
    n2 = Math.floor(Math.random()*10+1);
  }

  //Lag GANGE regnestykke innen for 1-10 gangetabellen.
  if(difficulty == "multi_level_2"){
    n1 = Math.floor(Math.random()*10+1);
    n2 = Math.floor(Math.random()*10+1);
  }

  //Lag DELE regnestykke innen for 1-5 gangetabellen.
  if(difficulty == "divisjon_level_1"){
    n1 = Math.floor(Math.random()*5+1);
    n2 = Math.floor(Math.random()*10+1);
    n1 = n1*n2
  }

  //Lag DELE regnestykke innen for 1-5 gangetabellen.
  if(difficulty == "divisjon_level_2"){
    n1 = Math.floor(Math.random()*10+1);
    n2 = Math.floor(Math.random()*10+1);
    n1 = n1*n2
  }

  //Lager tall mellom 1-100 hvor enerne er tiervenner
  if(difficulty == "tiervenn_level_1"){
    let ti_tall_1 = Math.floor(Math.random()*9+1);
    let ti_tall_2 = Math.floor(Math.random()*(10-ti_tall_1));
    ti_tall_1 *= 10
    ti_tall_2 *= 10
    
    let ener_tall_1 = Math.floor(Math.random()*9+1);
    let ener_tall_2 = 10 - ener_tall_1 

    n1 = ti_tall_1 + ener_tall_1 
    n2 = ti_tall_2 + ener_tall_2
  }

  enable_button('check_btn')
  document.getElementById("number1").innerText = n1;  //Gjør om til nytt nummer i boks 1
  document.getElementById("number2").innerText = n2; //Gjør om til nytt nummer i boks 2
  document.getElementById("input").value = ""; //Fjerner forrige svar fra boksen
  document.getElementById('math_topp').innerText = "" //Fjerner medlingen i det røde feltet
  if(cheating == true){document.getElementById('input').value = "#"}
}

//Sjekker om svaret er riktig
function check_answer(){
  var n1 = parseInt(document.getElementById("number1").innerText)
  var n2 = parseInt(document.getElementById("number2").innerText)
  var user_answer = document.getElementById('input').value

  //Sjekker juksekoder
  cheats(user_answer)
  if(cheating == true){return}

  //Fjerner tastaturet på skjermen
  document.activeElement.blur();

  if(difficulty == "pluss_level_1" || difficulty == "pluss_level_2" || difficulty == "pluss_level_3" || 
     difficulty == "pluss_level_4" || difficulty == "pluss_level_5" || difficulty == "tiervenn_level_1"){
    if(user_answer == n1+n2){
      answer_is('correct')
    }else{answer_is('wrong')}
  }
  if(difficulty == "minus_level_1" || difficulty == "minus_level_2" || difficulty == "minus_level_3" || 
     difficulty == "minus_level_4" || difficulty == "minus_level_5"){
    if(user_answer == n1-n2){
      answer_is('correct')
    }else{answer_is('wrong')}
  }
  if(difficulty == "multi_level_1" || difficulty == "multi_level_2"){
    if(user_answer == n1*n2){
      answer_is('correct')
    }else{answer_is('wrong')}
  }
  if(difficulty == "divisjon_level_1" || difficulty == "divisjon_level_2"){
    if(user_answer == n1/n2){
      answer_is('correct')
    }else{answer_is('wrong')}
  }
  
}

//Hva som skjer hvis svar er rett eller feil
function answer_is(x){
  if(x == 'correct'){
    //Spiller av riktig lyd
    audio_rett.play()

    //Skru av og på riktige knapper
    enable_button('new_btn')

    //Skriver bra jobba i rødt felt
    document.getElementById('math_topp').innerText = "Bra jobba!"

    //Legger til poeng
    current_points += 1
    if(current_points >= max_points){
      get_pokeball()
      current_points = 0;
    }

    console.log("Poeng:", current_points, "/", max_points)

    //Resetter poeng firkantene
    for(i=0; i<max_points; i++){
      temp_id = 'poeng_' + (i+1)
      document.getElementById(temp_id).style.backgroundColor = '#fb6868'
    }

    //Lyser opp poeng firkantene
    for(i=0; i<current_points; i++){
      temp_id = 'poeng_' + (i+1)
      document.getElementById(temp_id).style.backgroundColor = 'rgb(93, 160, 110)'
    }
  }

  if(x == 'wrong'){
    console.log("Feil svar!")
    document.getElementById('math_topp').innerText = "Prøv igjen"
  }
}

//Får en pokeball
function get_pokeball(){
  //Sjekker om det er flere pokemon å få i denn sona
  if(antall_pokemon == regions[current_region][2]){
    console.log("No more Pokemon in this Region")
    return
  }

  console.log("Got One Pokeball!")

  //Gjør tingene inni matteboksen usynlig og skrur av knappene
  enable_button("none")
  document.getElementById("input").style.visibility = "hidden"
  document.getElementById("symbol").style.visibility = "hidden"
  document.getElementById("number1").style.visibility = "hidden"
  document.getElementById("number2").style.visibility = "hidden"

  //Gjør pokeball synlig
  document.getElementById("pokeball_img").style.visibility = "visible"
}

//Åpner pokeball
function open_pokeball(){
  console.log("Open Pokeball!")

  //Gjør tingene inni matteboksen synlig igjen
  document.getElementById("input").style.visibility = "visible"
  document.getElementById("symbol").style.visibility = "visible"
  document.getElementById("number1").style.visibility = "visible"
  document.getElementById("number2").style.visibility = "visible"

  //Gjør pokeball usynlig igjen
  document.getElementById("pokeball_img").style.visibility = "hidden"

  get_pokemon()
  make_math()
}

//Sjekker hvilken pokemon du skal få
function get_pokemon(ct){
  
  if(antall_pokemon == regions[current_region][2]){
    console.log("No more Pokemon in this Region")
    return
  }

  //Hvor mange pokemon har vi?
  antall_pokemon += 1
  document.getElementById('pokedex_nr').innerHTML = "POKEDEX: " + antall_pokemon + "/" + (regions[current_region][2])
  add_badges()

  //Sjekker om vi er ferdig med regionen
  //if(){}
  if(antall_pokemon == badge_info[current_region][5]){
    if(current_region != 4  && regions[parseInt(current_region)+1][5] == 'locked'){
    //console.log(parseInt(current_region)+1)
    regions[parseInt(current_region)+1][5] = 'unlocked'
    localStorage.setItem('region_lock', regions)
    change_region_btn()
    }
  }


  //En tom liste vi kan dytte inn alle pokemon vi ikke har.
  var temp_array = []

  //loader riktig pokedex inn i en temp_array. Bare de vi ikke har fanget
  for(i=regions[current_region][3]; i < regions[current_region][4]; i++){
    if(pokedex_array[i][2] == 0){
      temp_array.push(pokedex_array[i])
    }
  }

  //console.log(temp_array)

  //Denne finner et random tall.
  rand= Math.floor(Math.random()*temp_array.length); 
  temp_array[rand][2] = 1

  //Shiny or no Shiny? Vi bruker random tall til å lage path.
  shinycalc = Math.floor(Math.random()*chance_shiny);
  if(ct == 1){shinycalc = 0}
  if(shinycalc == 0){temp_array[rand][3] = 1}

  //Lagrer pokemon lokalt
  var id = pokedex_array.indexOf(temp_array[rand])
  localStorage.setItem("pokedex", pokedex_array)

  //console.log("ADD1:", temp_array[rand])
  console.log("You got: " + pokedex_array[id][1] + "  -  " + antall_pokemon + "/" + regions[current_region][2] +" pkmn")
  add_pokemon(id, shinycalc)
}

//Legger inn en spesifik pokemon
function add_pokemon(nr, shiny){

  //Skal vi bruke Shiny box eller ikke?
  if(shiny == 0) {var class_name_div = "pkmn_div_shiny";} 
  if(shiny != 0) {var class_name_div = "pkmn_div";}

  //Lager en Div som bildet og tekst skal legges inn i
  var iDiv = document.createElement('div');
  var temp_id = 'block' + pokedex_array[nr][0];
  iDiv.id = temp_id
  iDiv.className = class_name_div;
  document.getElementById('pokedex').appendChild(iDiv);


  //Lager variabel for boksen som pokemon og navn skal inn i
  var theDiv = document.getElementById(iDiv.id);


  //Vi lager bildet variablet
  var img = document.createElement("img");
  if(shiny == 0){path = sprites_dir[sprite_dir_nr][1] + "/" + pokedex_array[nr][0] + "s" + '.png'}
  if(shiny != 0){path = sprites_dir[sprite_dir_nr][1] + "/" + pokedex_array[nr][0] + '.png'}
  img.src = path 

  //Add image
  document.getElementById(iDiv.id).appendChild(img);

  //Legger til pokemon navn
  var content = document.createTextNode(pokedex_array[nr][1]);
  theDiv.appendChild(content);

  //Scroll to bottom 
  if(loading == false){document.getElementById(iDiv.id).scrollIntoView(false);}
  
  img.setAttribute("class", 'pkmn_img');
  img.setAttribute("id",  (pokedex_array[nr][0]-1));
}

//Skrur av og på knappene i mattespillet som det trengs
function enable_button(btn){
  if(btn == "check_btn"){
    //Skru av denne
    document.getElementById("new_btn").disabled = true;
    document.getElementById("new_btn").style.cursor = "default";
    document.getElementById("new_btn").style.backgroundColor = "rgb(167, 167, 167)";

    //Skru på denne
    document.getElementById("check_btn").disabled = false;
    document.getElementById("check_btn").style.cursor = "pointer";
    document.getElementById("check_btn").style.backgroundColor = "#fb6868";
  }

  if(btn == "new_btn"){
    //Skru på denne
    document.getElementById("new_btn").disabled = false;
    document.getElementById("new_btn").style.cursor = "pointer";
    document.getElementById("new_btn").style.backgroundColor = "rgb(93, 160, 110)";

    //Skru av denne
    document.getElementById("check_btn").disabled = true;
    document.getElementById("check_btn").style.cursor = "default";
    document.getElementById("check_btn").style.backgroundColor = "rgb(167, 167, 167)";
  }

  if(btn == "none"){
    //Skru av denne
    document.getElementById("new_btn").disabled = true;
    document.getElementById("new_btn").style.cursor = "default";
    document.getElementById("new_btn").style.backgroundColor = "rgb(167, 167, 167)";

    //Skru av denne
    document.getElementById("check_btn").disabled = true;
    document.getElementById("check_btn").style.cursor = "default";
    document.getElementById("check_btn").style.backgroundColor = "rgb(167, 167, 167)";
  }
}

//Bytter Region
function change_region(x){
  if(current_region == x){return}
  console.log("Traveling to:", regions[x][1])
  clear_pokedex('pokedex')
  current_region = x;
  localStorage.setItem('region', current_region)
  load_game()
  document.getElementById('pokedex').scrollTop = 0;
}

//Gjør om på utseende til region bytteknappene og skrur de av og på basert om dehar unlocked dem.
function change_region_btn(){
  for(i=0; i<regions.length; i++){
    var temp_id = regions[i][1] + '_btn'
    var temp_id2 = regions[i][1] + '_btn_img'
    if(regions[i][5] == 'unlocked'){
      document.getElementById(temp_id).style.backgroundColor = "white"
      document.getElementById(temp_id).style.border = "2px solid green"
      document.getElementById(temp_id).style.cursor = "pointer"
      document.getElementById(temp_id2).style.opacity = "100%"
      document.getElementById(temp_id).disabled = false
      document.getElementById(temp_id2).src = ("Bilder/Knapper/" + regions[i][1].toLowerCase() + "_starters.png")
    }
    if(regions[i][5] == 'locked'){
      document.getElementById(temp_id).disabled = true;
      document.getElementById(temp_id).style.cursor = "default"
      document.getElementById(temp_id2).src = ("Bilder/Knapper/" + regions[i][1].toLowerCase() + "_starters_locked.png")
      //console.log("LOCKED", temp_id)
    }

    if(regions[current_region][0] == regions[i][0]){
      document.getElementById(temp_id).style.backgroundColor = "rgb(158, 221, 133)"
      document.getElementById('pokedex_topp').style.backgroundColor = badge_info[current_region][10]
    }
  }
}

//Legger inn riktig Badgebilde
function add_badges(){
  for(i=0; i<badge_info.length; i++){
    if(badge_info[i][0] == regions[current_region][1]){
      for(ii=1; ii<10; ii++){
        if(antall_pokemon >= badge_info[i][ii]){
          path = 'Bilder/Badges/' + badge_info[i][0] + '/box_'+ parseInt(ii-1) + '.png'
          //console.log(path)
          localStorage.setItem((badge_info[i][0] + "_badges"), parseInt(ii-1))
        }
      }
    }
  }
  document.getElementById('badge_img').src = path
}

//Bytter Sprites
function change_sprites(x){
  console.log("Changed sprites!")
  if(sprite_dir_nr == 0){
    sprite_dir_nr = 1
  }
  else if(sprite_dir_nr == 1){
    sprite_dir_nr = 0
  }

  document.getElementById('sprites_change').src = sprites_dir[sprite_dir_nr][0]

  localStorage.setItem('sprites', sprite_dir_nr)

  if(x == 1){
    clear_pokedex('whole_dex')
    load_dex()
  }else{
    clear_pokedex('pokedex')
    load_game()
  }

}

//Skrur av og på lyd
function sound(){
  console.log("Changing volume...")
  if(sound_volume == 0){sound_volume = 1}
  else if(sound_volume == 1){sound_volume = 0}
  audio_rett.volume = sound_volume
  localStorage.setItem('volume', sound_volume)
  document.getElementById("sound_btn").src = sound_dir[sound_volume][1]

}

//Ordner alt som har med antall resets og bonuser
function make_stars(){
  if(resets > 0){
    document.getElementById('stars').style.visibility = "visible"
    chance_shiny = chance_shiny_array[resets]
    document.getElementById("pokeball_img").src = pokeball_img_array[resets]
    document.getElementById('reset_score').innerHTML = resets
  }
  if(resets == 1){
    max_points = 4
    document.getElementById('poeng_5').style.backgroundColor = 'gray'
  }
  if(resets == 2){
    max_points = 3
    document.getElementById('poeng_5').style.backgroundColor = 'gray'
    document.getElementById('poeng_4').style.backgroundColor = 'gray'
  }
  if(resets == 3){
    max_points = 2
    document.getElementById('poeng_5').style.backgroundColor = 'gray'
    document.getElementById('poeng_4').style.backgroundColor = 'gray'
    document.getElementById('poeng_3').style.backgroundColor = 'gray'
  }
}

//Fjerner alt som ligger i pokedexen når vi skal bytte region
function clear_pokedex(x){
  document.getElementById(x).innerHTML = ""
}

//Sjekker om vi trykker på et bilde
document.addEventListener('click',function(e){
  if(natdex == true){return}
  if(Number.isInteger(parseInt(e.target.id)) == true){
    console.log("Clicked on:", pokedex_array[e.target.id][1], " Id:", e.target.id, " PokedexNr:", pokedex_array[e.target.id][0])
    if(pokedex_array[e.target.id][3] == 1){
        var path = "Bilder/Sprites/Sprites3/" + pokedex_array[e.target.id][0] + ".png"
      }else{
      var path = "https://img.pokemondb.net/artwork/large/" + pokedex_array[e.target.id][1] + ".jpg"  
      path = path.toLowerCase()
      for(i=0; i<pokemon_name_exceptions.length; i++){
        if(pokedex_array[e.target.id][1] == pokemon_name_exceptions[i][0]) {
          console.log(pokedex_array[e.target.id][1], "-->", pokemon_name_exceptions[i][1])
          path = "https://img.pokemondb.net/artwork/large/" + pokemon_name_exceptions[i][1] + ".jpg" 
          path = path.toLowerCase()
        }
      }
    }
    console.log("   - " + path)
    localStorage.setItem('fav_path', path)     
    localStorage.setItem('fav_name', pokedex_array[e.target.id][1])     
    document.getElementById("fav_img").src = path
    document.getElementById("fav_text").textContent = pokedex_array[e.target.id][1] 
  }
  //Sjekker om vi trykker utonfor Region Div og lukker den
  if(e.target.id != 'show_region_btn' && document.getElementById("region_btn_div").style.maxHeight){show_regions()}
});

//Hva jukseknappene gjør
function cheats(jk){

  if(jk == "#enable"){
    cheating = true
    document.getElementById('input').style.color = 'orange'
    document.getElementById('input').style.backgroundColor = 'black'
  }
  if(jk == "#disable"){
    cheating = false
    document.getElementById('input').style.color = 'black'
    document.getElementById('input').style.backgroundColor = 'white'
    document.getElementById('input').value = ''
    document.activeElement.blur();
  }
    

  if(cheating == false){return}
  
  if(jk == "#right" || jk == "#r"){
    answer_is('correct')
  }

  if(jk == "#reset"){
    console.log("Resetting game..")
    localStorage.clear()
    location.reload();
  }

  if(jk == "#new"){
    resets += 1
    localStorage.setItem("resets", resets)
    make_stars()
  }

  if(jk == "#get" || jk == "#add"){
    get_pokemon()
  }

  if(jk == "#getshiny" || jk == "#addshiny"){
    get_pokemon(1)
  }

  var new_jk = jk.split(" ");

  if(new_jk[1] == "all"){
    new_jk[1] = regions[current_region][2]
  }

  if(new_jk[0] == '#get'){
    for(d=0; d<pokedex_array.length; d++){
      if(pokedex_array[d][1] == new_jk[1]){
        console.log(pokedex_array[d][1])
        pokedex_array[d][2] = 1
        localStorage.setItem("pokedex", pokedex_array)
        add_pokemon(d, 1)
      }
    }
  }

  if(new_jk[0] == '#getshiny'){
    for(d=0; d<pokedex_array.length; d++){
      if(pokedex_array[d][1] == new_jk[1]){
        console.log(pokedex_array[d][1])
        pokedex_array[d][2] = 1
        pokedex_array[d][3] = 1
        localStorage.setItem("pokedex", pokedex_array)
        add_pokemon(d, 0)
      }
    }
  }

  new_jk[1] = parseInt(new_jk[1])


  if(new_jk[0] == '#get' && new_jk[1] >= 0){
    for(d=0; d<new_jk[1]; d++){
      get_pokemon()
    }
  }

  if(new_jk[0] == '#getshiny' && new_jk[1] >= 0){
    for(d=0; d<new_jk[1]; d++){
      get_pokemon(1)
    }
  }


  document.getElementById('input').value = '#'
}

//Load National Pokedex
var natdex = false;
function load_dex(){
  natdex = true

  //Loader riktig sprite type
  sprite_dir_nr = localStorage.getItem('sprites')
  document.getElementById('sprites_change').src = sprites_dir[sprite_dir_nr][0]
  
  //Load Pokemon
  var temp = localStorage.getItem("pokedex")
  
  var temp = temp.split(",")
  var count = 0
  let new_array = []
  
  //Gjør save-data om til en liste
  for(i=0; i<pokedex_array.length; i++){
    var temp_row = []
    for(ii=0; ii<4; ii++){
      if(ii == 0 || ii == 2 || ii == 3){temp_row.push(parseInt(temp[count]))}
      else{temp_row.push(temp[count])}
      count += 1
    }
    new_array.push(temp_row)
  }
  
  //Oppdaterer main array
  pokedex_array = new_array.slice(0)

  var how_many_pokemon = 0
  
  for(i=0; i<pokedex_array.length; i++){

    //Skal vi bruke Shiny box eller ikke?
    if(pokedex_array[i][3] == 1){var class_name_div = "pkmn_div_shiny";} 
    if(pokedex_array[i][3] == 0) {var class_name_div = "pkmn_div";}

    //Lager en Div som bildet og tekst skal legges inn i
    var iDiv = document.createElement('div');
    var temp_id = 'block' + pokedex_array[i][0];
    iDiv.id = temp_id
    iDiv.className = class_name_div;
    document.getElementById('whole_dex').appendChild(iDiv);


    //Lager variabel for boksen som pokemon og navn skal inn i
    var theDiv = document.getElementById(iDiv.id);


    //Vi lager bildet variablet
    var img = document.createElement("img");
    if(pokedex_array[i][3] == 1){path = sprites_dir[sprite_dir_nr][1] + "/" + pokedex_array[i][0] + "s" + '.png'}
    if(pokedex_array[i][3] == 0){path = sprites_dir[sprite_dir_nr][1] + "/" + pokedex_array[i][0] + '.png'}
    img.src = path 

    //Add image
    document.getElementById(iDiv.id).appendChild(img);

    if(pokedex_array[i][2] == 0){img.setAttribute("class", 'pkmn_img_none');}
    if(pokedex_array[i][2] == 1){
      img.setAttribute("class", 'pkmn_img');
      //Legger til pokemon navn
      var content = document.createTextNode(pokedex_array[i][1]);
      theDiv.appendChild(content);
      how_many_pokemon += 1
    }

    img.setAttribute("id",  (pokedex_array[i][0]-1));
    document.getElementById('nat_dex_nr').innerHTML = "National Pokedex:" + '[' + how_many_pokemon + '/' + pokedex_array.length + ']'
  }
  load_dex_badges()
}

function load_dex_badges(){
  //Load Badges
  var bad1 = localStorage.getItem('Kanto_badges')
  var bad2 = localStorage.getItem('Johto_badges')
  var bad3 = localStorage.getItem('Hoenn_badges')
  var bad4 = localStorage.getItem('Sinnoh_badges')
  document.getElementById('Kanto_medal').src = 'Bilder/Badges/Kanto/box_'+ bad1 + '.png'
  document.getElementById('Johto_medal').src = 'Bilder/Badges/Johto/box_'+ bad2 + '.png'
  document.getElementById('Hoenn_medal').src = 'Bilder/Badges/Hoenn/box_'+ bad3 + '.png'
  document.getElementById('Sinnoh_medal').src = 'Bilder/Badges/Sinnoh/box_'+ bad4 + '.png'
}

//SJekker hvor mange pokemon vi har totalt
function total_pkmn_check(){
  var counter = 0
  for(i=0; i<pokedex_array.length; i++){
    if(pokedex_array[i][2] == 1){
      counter += 1
    }
  }
  return counter
}

//Resetter spillet og gir bonuser
function reset_game(){
  localStorage.clear()
  resets += 1
  localStorage.setItem('resets', resets)
  location.reload()
}

//Få frem region Div
function show_regions(){
  var content = document.getElementById("region_btn_div");
  var btn = document.getElementById('show_region_btn');

  if (content.style.maxHeight){
    //Gjør Div usynlig
    content.style.maxHeight = null;
    content.style.border = null
    //Gjør om på knappen tilbake
    btn.style.backgroundColor = ""
    btn.style.border = "2px white solid"
    btn.style.height = "40px"
  } else {
    //Gjør Div synlig
    content.style.maxHeight = content.scrollHeight + "px";
    content.style.borderBottom = '3px black solid'

    //Gjør om på knappen
    btn.style.backgroundColor = "rgb(209, 161, 89)"
    btn.style.borderBottom = "none"
    btn.style.height = "50px"
  } 
  
  
}



