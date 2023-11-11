# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define teacher = Character("Miss You", kind = nvl, who_suffix="\n老师")
define sister = Character("Sister", kind = nvl, who_suffix="\n姐姐")
define elder_brother = Character("Elder Brother", kind = nvl, who_suffix="\n哥哥")


# 游戏在此开始。
label hospital:

    scene bg hospital2_1 at img_wandering with dissolve
    call hide_black_trans()

    narrator """Meanwhile, inside the hospital, nurses were bandaging other injured patients while the older brother went out to search for supplies.
\n\n与此同时，在医院里，护士在包扎其他伤员，哥哥外出寻找物资。"""

    nvl clear

    narrator """The sister’s teacher was bandaging one of the injured.
\n\n姐姐的老师正在为一位伤员包扎。"""

    nvl clear

    scene bg hospital2_2 at img_wandering with dissolve

    sister """Madom, why you are here?
\n\n女士,您怎么在这？"""

    nvl clear

    teacher """The school was also hit by an air raid.
\n\n学校也遭遇了空袭。"""

    nvl clear

    scene bg hospital2_3 at img_wandering with dissolve

    sister """What is this? Is the flame of civilization about to be extinguished?
\n\n这算什么呢，文明的烛火要被熄灭了吗？"""

    nvl clear

    teacher """Even if the storm is fierce, this cluster of candles will continue to burn.
\n\n即使风雨再大，这一簇烛火也会燃烧下去。"""

    nvl clear

    scene bg hospital2_4 at img_wandering with dissolve

    sister """But , madom, we have already lost so much, can we truly recover?
\n\n但是，女士，我们已经失去了那么多，真的能够恢复吗？"""

    nvl clear

    teacher """Even if the storm is fierce, this cluster of candles will continue to burn.
\n\n即使风雨再大，这一簇烛火也会燃烧下去。"""

    nvl clear


    call explosion

    call show_black_trans("Chapter 3  Ruins 废墟")
    jump ruins

    # show ct_text at truecenter with dissolve 
