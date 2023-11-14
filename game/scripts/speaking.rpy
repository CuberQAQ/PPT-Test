define american_officer= Character("American Officer", kind = nvl, who_suffix="\n美国国务卿")
define palestinian_ambassador_to_the_united_nations= Character("Palestinian Ambassador ", kind = nvl, who_suffix="\n巴勒斯坦驻联合国大使")
define chinese_diplomatist= Character("Chinese Diplomatist", kind = nvl, who_suffix="\n中国外交官")   

label speaking:

    scene bg white_house  at img_wandering with fade

    call hide_black_trans() from _call_hide_black_trans_5
    

    narrator"The scene switched to the White House.
\n\n场景转到了美国白宫。"
    nvl clear

    american_officer"It is undeniable that Hamas has taken the lead in the attacking, and Israel has the right to defend itself and fight back, all of which are to defend the human rights of the Israeli people, who have human rights.
\n\n不可否认，哈马斯率先发动了袭击，以色列有权自卫，有权反击，这一切都是为了捍卫以色列人民的人权，他们拥有人权。"
    nvl clear
    
    scene bg union at img_wandering with fade

    narrator"The scene switched to United Nations.
\n\n场景转到了联合国"
    nvl clear

    scene bg ambassador1 at img_wandering with dissolve

    palestinian_ambassador_to_the_united_nations"Aid workers were targeted and killed, Rescue teams are struggling to carry out their missions and continued with earth strikes. There is a severe shortage of rescue equipment, limited or no mobile Internet connection, there‘s no power, no water, no fuel.
\n\n救援人员成为袭击目标并被杀害，救援队正在努力执行他们的任务，并继续进行地面打击。救援设备严重短缺，有限或没有移动互联网连接，没有电，没有水，没有燃料。"
    nvl clear

    palestinian_ambassador_to_the_united_nations"Food supplies are running dangerous below, hospitals are over with the patients and injured by running out of medicines. Morgues are overflowing with bodies.
\n\n食物供应正在危险地运行,医院挤满了病人和因药品耗尽而受伤的人,停尸房里堆满了尸体。"
    nvl clear 

    scene bg ministry at img_wandering with fade
    play music "audio/bgm/ministry.mp3"
    narrator"The scene switched to ministry of foreign affairs of China.
\n\n场景转到了中国外交部。"
    nvl clear

    chinese_diplomatist"Dear friends, in recent days, a hospital in the Gaza Strip has been subjected to an airstrike,resulting in over 500 casualties. The Israeli-Palestinian conflict continues to escalate. China is willing to work together with countries around the world to promote an immediate ceasefire and halt the hostilities. 
\n\n各位朋友们，近日，加沙地带一医院遭遇空袭，超500人伤亡。巴以突不断升级，中方愿同世界各国一道，推动尽快停止战火，防止局势进一步升级甚至失控。"
    nvl clear

    chinese_diplomatist"We aim to prevent the situation from further escalating or even spiraling out of control. We strongly condemn any actions that harm civilians and violate international law. We call for the protection of civilians and the implementation of humanitarian assistance to prevent a more severe humanitarian catastrophe from unfolding.
\n\n我们都反对伤害平民的行为和违反国际法的做法，呼吁保护平民开展人道救援，防止出现更严重的人道主义灾难。" 
    nvl clear

    jump hospital_two