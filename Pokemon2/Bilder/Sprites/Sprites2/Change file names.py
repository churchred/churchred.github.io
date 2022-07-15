import os


pokedex_array_kanto = [494,'Victini',0 ,0], [495,'Snivy',0 ,0], [496,'Servine',0 ,0], [497,'Serperior',0 ,0], [498,'Tepig',0 ,0],[499,'Pignite',0 ,0], [500,'Emboar',0 ,0], [501,'Oshawott',0 ,0], [502,'Dewott',0 ,0], [503,'Samurott',0 ,0],[504,'Patrat',0 ,0], [505,'Watchog',0 ,0], [506,'Lillipup',0 ,0], [507,'Herdier',0 ,0], [508,'Stoutland',0 ,0],[509,'Purrloin',0 ,0], [510,'Liepard',0 ,0], [511,'Pansage',0 ,0], [512,'Simisage',0 ,0], [513,'Pansear',0 ,0],[514,'Simisear',0 ,0], [515,'Panpour',0 ,0], [516,'Simipour',0 ,0], [517,'Munna',0 ,0], [518,'Musharna',0 ,0],[519,'Pidove',0 ,0], [520,'Tranquill',0 ,0], [521,'Unfezant',0 ,0], [522,'Blitzle',0 ,0], [523,'Zebstrika',0 ,0],[524,'Roggenrola',0 ,0], [525,'Boldore',0 ,0], [526,'Gigalith',0 ,0], [527,'Woobat',0 ,0], [528,'Swoobat',0 ,0],[529,'Drilbur',0 ,0], [530,'Excadrill',0 ,0], [531,'Audino',0 ,0], [532,'Timburr',0 ,0], [533,'Gurdurr',0 ,0],[534,'Conkeldurr',0 ,0], [535,'Tympole',0 ,0], [536,'Palpitoad',0 ,0], [537,'Seismitoad',0 ,0], [538,'Throh',0 ,0],[539,'Sawk',0 ,0], [540,'Sewaddle',0 ,0], [541,'Swadloon',0 ,0], [542,'Leavanny',0 ,0], [543,'Venipede',0 ,0],[544,'Whirlipede',0 ,0], [545,'Scolipede',0 ,0], [546,'Cottonee',0 ,0], [547,'Whimsicott',0 ,0], [548,'Petilil',0 ,0],[549,'Lilligant',0 ,0], [550,'Basculin',0 ,0], [551,'Sandile',0 ,0], [552,'Krokorok',0 ,0], [553,'Krookodile',0 ,0],[554,'Darumaka',0 ,0], [555,'Darmanitan',0 ,0], [556,'Maractus',0 ,0], [557,'Dwebble',0 ,0], [558,'Crustle',0 ,0],[559,'Scraggy',0 ,0], [560,'Scrafty',0 ,0], [561,'Sigilyph',0 ,0], [562,'Yamask',0 ,0], [563,'Cofagrigus',0 ,0],[564,'Tirtouga',0 ,0], [565,'Carracosta',0 ,0], [566,'Archen',0 ,0], [567,'Archeops',0 ,0], [568,'Trubbish',0 ,0],[569,'Garbodor',0 ,0], [570,'Zorua',0 ,0], [571,'Zoroark',0 ,0], [572,'Minccino',0 ,0], [573,'Cinccino',0 ,0],[574,'Gothita',0 ,0], [575,'Gothorita',0 ,0], [576,'Gothitelle',0 ,0], [577,'Solosis',0 ,0], [578,'Duosion',0 ,0],[579,'Reuniclus',0 ,0], [580,'Ducklett',0 ,0], [581,'Swanna',0 ,0], [582,'Vanillite',0 ,0], [583,'Vanillish',0 ,0],[584,'Vanilluxe',0 ,0], [585,'Deerling',0 ,0], [586,'Sawsbuck',0 ,0], [587,'Emolga',0 ,0], [588,'Karrablast',0 ,0],[589,'Escavalier',0 ,0], [590,'Foongus',0 ,0], [591,'Amoonguss',0 ,0], [592,'Frillish',0 ,0], [593,'Jellicent',0 ,0],[594,'Alomomola',0 ,0], [595,'Joltik',0 ,0], [596,'Galvantula',0 ,0], [597,'Ferroseed',0 ,0], [598,'Ferrothorn',0 ,0],[599,'Klink',0 ,0], [600,'Klang',0 ,0], [601,'Klinklang',0 ,0], [602,'Tynamo',0 ,0], [603,'Eelektrik',0 ,0],[604,'Eelektross',0 ,0], [605,'Elgyem',0 ,0], [606,'Beheeyem',0 ,0], [607,'Litwick',0 ,0], [608,'Lampent',0 ,0],[609,'Chandelure',0 ,0], [610,'Axew',0 ,0], [611,'Fraxure',0 ,0], [612,'Haxorus',0 ,0], [613,'Cubchoo',0 ,0],[614,'Beartic',0 ,0], [615,'Cryogonal',0 ,0], [616,'Shelmet',0 ,0], [617,'Accelgor',0 ,0], [618,'Stunfisk',0 ,0],[619,'Mienfoo',0 ,0], [620,'Mienshao',0 ,0], [621,'Druddigon',0 ,0], [622,'Golett',0 ,0], [623,'Golurk',0 ,0],[624,'Pawniard',0 ,0], [625,'Bisharp',0 ,0], [626,'Bouffalant',0 ,0], [627,'Rufflet',0 ,0], [628,'Braviary',0 ,0],[629,'Vullaby',0 ,0], [630,'Mandibuzz',0 ,0], [631,'Heatmor',0 ,0], [632,'Durant',0 ,0], [633,'Deino',0 ,0],[634,'Zweilous',0 ,0], [635,'Hydreigon',0 ,0], [636,'Larvesta',0 ,0], [637,'Volcarona',0 ,0], [638,'Cobalion',0 ,0],[639,'Terrakion',0 ,0], [640,'Virizion',0 ,0], [641,'Tornadus',0 ,0], [642,'Thundurus',0 ,0], [643,'Reshiram',0 ,0],[644,'Zekrom',0 ,0], [645,'Landorus',0 ,0], [646,'Kyurem',0 ,0], [647,'Keldeo',0 ,0], [648,'Meloetta',0 ,0],[649,'Genesect',0 ,0]

run_go = True

data = os.path.abspath("test/")
if run_go == True:
    for i, f in enumerate(os.listdir(data)):
        src = os.path.join(data, f)
        for ii in range(0, len(pokedex_array_kanto)):
            img_name_normy = str(pokedex_array_kanto[ii][1]) + ".png"
            img_name_shiny = str(pokedex_array_kanto[ii][1]) + " (1).png"
            img_name_normy = img_name_normy.lower()
            img_name_shiny = img_name_shiny.lower()
            new_name = ""
            new_name2 = ""
            
            if f == img_name_normy:
                new_name2 = str(pokedex_array_kanto[ii][0]) + ".png"
                print(f, "-->", new_name2)
                os.rename(src, new_name2)
                
            if f == img_name_shiny:
                new_name = str(pokedex_array_kanto[ii][0]) + "s" + ".png"
                print(f, "-->", new_name)
                os.rename(src, new_name)
