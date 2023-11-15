# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define teacher = Character("Miss You", kind = nvl, who_suffix="\n老师")
define sister = Character("Sister", kind = nvl, who_suffix="\n姐姐")
define elder_brother = Character("Elder Brother", kind = nvl, who_suffix="\n哥哥")

image magic = "images/magic.png"

define config.layers += ["magic_text"]
image black_bg = Solid("#000")

style bottom_text:
    # color "#555555ff"
    xalign 0.5
    yalign 0.57
    # font "fonts/楷体_GB2312.ttf"
    size 42
    outlines [(3, "#000000a0", 0, 0)]

style bottom_text2:
    # color "#555555ff"
    xalign 0.5
    yalign 0.6
    size 42
    outlines [(3, "#000000a0", 0, 0)]

# style ct_text_add:
#     # font "GenEiKoburiMin6-R.ttf"
#     pass

define bottom_text_t = "不....这是什么世界！？"
define bottom_text_style = "bottom_text"
init python:
    def bottom_text_func(st, a):
        return Text(bottom_text_t, dynamic = True, style=bottom_text_style), None
image bottom_text = DynamicDisplayable(bottom_text_func)

# 游戏在此开始。
label elder_brother:

    play music "audio/bgm/ninelie.mp3"
    pause 2.0

    #TODO new img
    scene bg ruins1 at blood_gray_red, img_wandering with dissolve
    call hide_black_trans() from _call_hide_black_trans_2 

    scene bg elder_brother_ruin at blood_gray_red, img_wandering with dissolve

    narrator "As the smoke cleared, the brother held onto supplies and carried a candle.
\n\n硝烟散去，哥哥抱着物资，拿着烛火。"

    nvl clear

    # scene bg ruins2 at blood_gray_red, img_wandering with dissolve

    
    narrator "He suppressed his emotions and, with a glimmer of hope, searched for his loved ones amidst the ruins of the hospital. Finally, he found his sister, barely clinging to life.
\n\n他强忍住情绪，怀着一丝侥幸的心理，在医院的废墟中翻找他的亲人。他终于发现姐姐，姐姐奄奄一息。"
    
    nvl clear


    # scene bg ruins3 at blood_gray_red, img_wandering with dissolve

    sister "Hurry up... Find Kevin...
\n\n快……找弟弟……"

    nvl clear

    scene bg brother_crying at img_wandering with dissolve
    #TODO blood_grey_red

    
    narrator "He fought back his grief and continued searching, stumbling and wiping away tears. Eventually, he came across his younger brother, trembling as he extended a trembling finger to check for any signs of life—there was nothing. He collapsed.
\n\n哥哥忍住悲痛，踉踉跄跄地继续翻找，边翻找边擦眼泪。最后翻到了弟弟，他颤颤巍巍地伸出手指探了探弟弟的鼻息——什么也没有，他崩溃了。"

    nvl clear

    
    show black_bg at Transform:
        alpha 0.0
        time 0.15
        ease 1.2 alpha 0.3

    $ ct_text3_t = "これはどんな世界ですか？"
    $ ct_text3_delay = 4.3
    $ ct_text3_speed = 0.3
    $ ct_text3_pre_len = 1
    $ ct_text3_style_t = "ct_text3_style_jp"
    $ bottom_text_t = "不....这是什么世界！？"

    show ct_text3 onlayer magic_text at ZoomEaseIn(begin=20 ,end=0.9,time=10), AlphaIn(end=0.8,time=0.5), Transform:
        # time 1.07
        # alpha 0.0
        pass
    pause 0.55
    show magic  at Transform:
        alpha 0.8
        xalign 0.5
        yalign 0.5
        easeout 1 rotate 359
        block:
            rotate 0
            linear 0.01 rotate 359
            repeat 
        pass
    pause 10
    # show bottom_text
    with Dissolve(0.2) 
    pause
    # pause

    # with None
    hide bottom_text
    hide ct_text3
    with dissolve

    $ ct_text3_pre_len = 1

    # pause
    

    elder_brother "I have lost all my loved ones! They all perished in this raging war, one after another, leaving me behind...
\n\n我失去了所有的亲人！他们都在这场战火中丧命，一个接一个地离我而去...."
    nvl clear

    scene bg crying_brother at blood_gray_red, img_wandering with dissolve

    elder_brother "Oh, dear Allah! He is my last remaining family member... the very last one! He... he was such a lovely kid, always bringing joy to me with his singing, his smile so warm... But now, they are all gone. They have departed, leaving me in this bloody battlefield...
\n\n哦，天啊！这是我最后一个家人..最后一个！他...他是那个最容易笑的人，他唱歌时总是让我开心，他的微笑是如此温暖...现在，他们都离开了。他们离开我留下了这血腥的战场..."
    nvl clear

    elder_brother "This war... this endless cycle of hatred and destruction... I cannot bear it any more! I no longer seek vengeance; peace I only long for peace. I believe one day, we can put an end to this senseless slaughter, to the shedding of innocent blood!
\n\n这场战争..这场无尽的仇恨与毁灭....我再也无法忍受！我不再寻求仇恨，我只渴望和平。只要有一天，我们能够停止这种毫无意义的杀戮，停止无辜者的流血！"
    nvl clear

    # pause
    
    # jump qiaolang
    # call show_black_trans("Love and Peace 爱与和平") from _call_show_black_trans_2 

    jump after_video

    # show ct_text at truecenter with dissolve 
    # call show_black_trans("Chapter 1  Home   巴以冲突中的一家") from _call_show_black_trans

    
