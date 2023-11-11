
define sister = Character("Sister", kind = nvl, who_suffix="\n姐姐")
define elder_brother = Character("Elder Brother", kind = nvl, who_suffix="\n哥哥")
define little_brother = Character("Little Brother", kind = nvl, who_suffix="\n弟弟")

image snow = SnowBlossom("particle/fire.png", count=6000, yspeed=(-1600, -1400), xspeed=(-350,350))

label home:

    scene bg bg4 at img_wandering
    play music "audio/bgm/時編み.mp3"
    call hide_black_trans() from _call_hide_black_trans
    pause 0.5

    narrator """Our story takes place amidst the Israeli-Palestinian conflict, with the last round of bombings occurring half a month ago. At this very moment, a surviving yet fragmented family is rekindling hope for their lives, as today marks the younger brother's birthday.
\n\n我们的故事发生在巴以冲突中，上一轮的轰炸发生在半个月前，此时此刻，幸存而残缺的一家人又重拾生活的希望，今天是弟弟的生日。"""

    nvl clear
    scene bg home at img_wandering with dissolve
    sister """Happy birthday, Kevin!
\n\n生日快乐，Kevin！"""

    nvl clear
    elder_brother """Make a wish, in this difficult time.
\n\n许个愿吧，在这艰难的时刻。"""


    nvl clear
    little_brother """If only Mom and Dad were here...
\n\n如果爸爸妈妈也在就好了……"""

    # $ renpy.display_menu(items, interact=True, screen='choice')

    nvl clear
    sister """It will all turn around.
\n\n一切都会好的。"""
    nvl clear

    stop music
    play music "audio/sfx/air_defense_warning.mp3" volume 0.4
    pause
    call explosion

    narrator """The bomb hit the home!
炸弹袭击了这个家!"""
    # $ ct_text_t = "The bomb hit the home!\n炸弹袭击了这个家!"
    # show ct_text
    

    nvl clear

    pause
    stop sound
    call show_black_trans("Chapter 2  Hospital   医院")
    jump hospital

