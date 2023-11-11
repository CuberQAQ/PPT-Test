# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define teacher = Character("Miss You", kind = nvl, who_suffix="\n老师")
define sister = Character("Sister", kind = nvl, who_suffix="\n姐姐")
define elder_brother = Character("Elder Brother", kind = nvl, who_suffix="\n哥哥")


# 游戏在此开始。
label ruins:

    play music "audio/bgm/潮鳴り.mp3"
    pause 2.0
    scene bg ruins1 at img_wandering with dissolve
    call hide_black_trans()

    narrator """As the smoke cleared, the brother held onto supplies and carried a candle.
\n\n硝烟散去，哥哥抱着物资，拿着烛火。"""

    nvl clear

    scene bg ruins2 at img_wandering with dissolve

    narrator """He suppressed his emotions and, with a glimmer of hope, searched for his loved ones amidst the ruins of the hospital.Finally, he found his sister, barely clinging to life. 
\n\n他强忍住情绪，怀着一丝侥幸的心理，在医院的废墟中翻找他的亲人。他终于发现姐姐，姐姐奄奄一息。"""
    
    nvl clear

    scene bg ruins3 at img_wandering with dissolve

    sister """Hurry up…find your brother
\n\n快……找弟弟……"""

    nvl clear

    scene bg ruins4 at img_wandering with dissolve

    narrator """He fought back his grief and continued searching, stumbling and wiping away tears. Eventually, he came across his younger brother, trembling as he extended a trembling finger to check for any signs of life—there was nothing. He collapsed.
\n\n哥哥忍住悲痛，踉踉跄跄地继续翻找，边翻找边擦眼泪。最后翻到了弟弟，他颤颤巍巍地伸出手指探了探弟弟的鼻息——什么也没有，他崩溃了。"""

    nvl clear

    scene bg ruins5 at img_wandering with dissolve

    pause
    return

    # show ct_text at truecenter with dissolve 
    # call show_black_trans("Chapter 1  Home   巴以冲突中的一家") from _call_show_black_trans
