﻿# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
define config.layers += ["flare"]
define teacher = Character("Teacher Li", kind = nvl, who_suffix="\n李老师")
define sister = Character("Sister", kind = nvl, who_suffix="\n姐姐")
define elder_brother = Character("Elder Brother", kind = nvl, who_suffix="\n哥哥")


label center_label_1:
    $ ct_text3_t = "Take Care 卧倒！"
    $ ct_text3_delay = 0.38
    $ ct_text3_speed = .024

    show ct_text3 onlayer explosion_under at ZoomEaseIn(begin=0.01,end=1.5,time=1.2), AlphaIn(end=0.9,time=0.6), Transform:
        time 1.07
        alpha 0.0
    return

label hide_center_label_1:
    hide ct_text3 onlayer explosion_under
    return

# 游戏在此开始。
label hospital_two:


    scene bg nurse at LinearUp(1500, 0),ImgWandering(2.2, 1.7, 20) with dissolve
    # call hide_black_trans()
    
    play music "audio/bgm/卒業.mp3"



    scene flare_mask onlayer flare
    call hide_black_trans()


    voice "audio/voice/narrator/hospital2_1.mp3"
    narrator"Meanwhile, inside the hospital, nurses are bandaging other injured patients while the elder brother went out to search for supplies.
\n\n与此同时，在医院里，护士在包扎其他伤员，哥哥外出寻找物资。"

    nvl clear

    voice "audio/voice/narrator/hospital2_2.mp3"
    narrator """The sister’s teacher was bandaging one of the injured.
\n\n姐姐的老师正在为一位伤员包扎。"""

    nvl clear

    scene bg madam at img_wandering with dissolve

    voice "audio/voice/teacher/hospital2_1.mp3"
    teacher "Is there anyone who can lend me your hand?
\n\n有谁能来搭把手？"

    nvl clear

    voice "audio/voice/sister/hospital2_1.mp3"
    sister "Madam, why you are here?
\n\n女士,您怎么在这？"

    nvl clear

    voice "audio/voice/teacher/hospital2_2.mp3"
    teacher "The school was also hit by an air raid.
\n\n学校也遭遇了空袭。"

    nvl clear

    # scene bg hospital2_3 at img_wandering with dissolve
    scene bg candle at ImgWandering(1.5, 1.0, 15)  with dissolve

    voice "audio/voice/sister/hospital2_2.mp3"
    sister "What is this? Is the flame of civilization about to be extinguished?
\n\n这算什么呢，文明的烛火要被熄灭了吗？"

    nvl clear

    voice "audio/voice/teacher/hospital2_3.mp3"
    teacher "Even if the storm is fierce, this cluster of candles will continue to burn.
\n\n即使风雨再大，这一簇烛火也会燃烧下去。"

    nvl clear

    # scene bg hospital2_4 at img_wandering with dissolve

    voice "audio/voice/sister/hospital2_3.mp3"
    sister "But, madam, we have already lost so much, can we truly recover?
\n\n但是，女士，我们已经失去了那么多，真的能够恢复吗？"

    nvl clear

    scene bg hospital_inside2 at img_wandering with dissolve

    voice "audio/voice/teacher/hospital2_4.mp3"
    teacher "The flames of war may destroy buildings, but they cannot destroy the culture within our hearts. Everything will be alright.
\n\n战火可以摧毁建筑，但无法摧毁我们心中的文化。一切都会好的。"
    # pause 0.1
    # $ nvl_anime = False
    nvl clear
    # with dissolve

   
    # play audio "audio/sfx/air_defense_warning.mp3" volume 0.4
    # pause
    # stop audio fadeout 20.0
    



    call explosion("center_label_1")
    # $ nvl_anime = True
    # hide ct_text3 onlayer explosion_under
    show bg ruins3 at Transform:
        alpha 0.0
        ease 2 alpha 1.0
        time 3.0
        matrixcolor SaturationMatrix(0.0)
        alpha 1.0

    $ ct_text_t = "The bomb hit the hospital\n      炸弹袭击了这家医院"
    scene flare_mask onlayer flare
    show ct_text onlayer on_explosion at alpha_in, Transform:
        time 1.0
        easein 6 zoom 0.8
    

    # nvl clear

    pause
    hide ct_text onlayer on_explosion with dissolve
    stop sound
    
    call show_black_trans("Ruins 废墟")
    call hide_explosion

    jump elder_brother_en

    # show ct_text at truecenter with dissolve 
