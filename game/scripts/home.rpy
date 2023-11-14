# $ renpy.("flare")
define sister = Character("Sister", kind = nvl, who_suffix="\n姐姐")
define elder_brother = Character("Elder Brother", kind = nvl, who_suffix="\n哥哥")
define little_brother = Character("Little Brother", kind = nvl, who_suffix="\n弟弟")

image snow = SnowBlossom("particle/fire.png", count=600, yspeed=(-3200, -2800), xspeed=(-700,700))

transform alpha_in:
    zoom 1.0
    alpha 0.0
    # time 1.0
    easeout 2 alpha 0.8

label home:

    scene bg bg4 at img_wandering
    play music "audio/bgm/MerryChrismas.mp3"
    # call hide_black_trans() from _call_hide_black_trans
    # pause 0.5
    call hide_black_trans()


    narrator "Our story takes place in the Israeli-Palestinian conflict, with the last round of bombings occurring half a month ago. At this very moment, a surviving yet fragmented family is recolleting hope for their lives, as today marks the younger brother's birthday.
\n\n我们的故事发生在巴以冲突中，上一轮的轰炸发生在半个月前，此时此刻，幸存而残缺的一家人又重拾生活的希望，今天是弟弟的生日。"

    nvl clear
    scene bg home at img_wandering with dissolve
    sister "Happy birthday, Kevin!
\n\n生日快乐，Kevin！"

    nvl clear
    elder_brother "Make a wish, in this difficult time.
\n\n许个愿吧，在这艰难的时刻。"


    nvl clear
    little_brother "If only Mom and Dad were here...
\n\n如果爸爸妈妈也在就好了……"

    # $ renpy.display_menu(items, interact=True, screen='choice')

    nvl clear
    sister "It will all turn around.
\n\n一切都会好的。"
    nvl clear

    stop music fadeout 0.5
    
    scene bg home at Transform:
        time 3.0
        matrixcolor SaturationMatrix(0.0)
    call explosion 

#     narrator """The bomb hit the home!
# 炸弹袭击了这个家!"""
    $ ct_text_t = "The bomb hit the home\n      炸弹袭击了这个家"
    show ct_text onlayer on_explosion at alpha_in, Transform:
        time 1.0
        easein 6 zoom 0.8
    

    # nvl clear

    pause
    hide ct_text onlayer on_explosion 
    #with dissolve
    stop sound
    call show_black_trans("Chapter 2  Hospital   医院") 
    call hide_explosion 
    jump hospital_one

