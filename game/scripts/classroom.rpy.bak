# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define miss_you = Character("Miss You", kind = nvl, who_suffix="\n游老师")
define student1 = Character("Student1", kind = nvl, who_suffix="\n学生1")
define student2 = Character("Student2", kind = nvl, who_suffix="\n学生2")
define student3 = Character("Student3", kind = nvl, who_suffix="\n学生3")

# 游戏在此开始。
label classroom:

    scene bg classroom at img_wandering with fade
    play music "audio/bgm/君がいるから.mp3"

    narrator "This is Miss Li, a Chinese female teacher. At this moment, a group of active and lively students is sitting in the classroom ,looking forward to the teacher’s lecture.
\n\n这是李老师，一位中国女老师。此时 一群活泼好动的学生，他们席地而坐，期待着老师的授课。"

    nvl clear

    miss_you """Good morning, everyone!In today's political class, I would like to discuss two countries that are relevant to recent international events. Can anyone guess which countries I'm referring to?
\n\n同学们好！今天的政治课我想和大家聊聊两个国家，跟最近国际上的事情相关，有哪个同学猜出来了吗？"""

    nvl clear

    student1 """It's Israel and Palestine.
\n\n是以色列和巴勒斯坦。"""

    nvl clear
    scene bg bg0 at img_wandering with dissolve


    miss_you """That's right. Palestine is located in the western part of Asia, adjacent to Israel. In that region, many children and families are living under the shadow of conflict.
\n\n是的。巴勒斯坦位于亚洲西部，与以色列相邻。在那里，有很多儿童和家庭都生活在冲突的阴影下。"""

    nvl clear

    student2 """Why does this conflict occur?
\n\n为什么会发生冲突呢？"""

    nvl clear

    scene bg bg1 at img_wandering with dissolve

    miss_you """This is due to complex factors such as geography, religion, and historical background. Nevertheless, they face violence, fear, and harm in this ongoing conflict. Some children have lost their homes and even their loved ones.
\n\n这是由于地域、宗教和历史背景等复杂原因所致。无论如何，他们在持续的冲突中，面临着暴力、恐惧和伤害。有些孩子失去了家园，甚至失去了亲人。"""

    nvl clear

    scene bg bg2 at img_wandering with dissolve

    student3 """What can we do?
\n\n老师，我们能做些什么吗？"""

    nvl clear

    miss_you """I just want to tell you that even though we live in a peaceful environment, there are still regions in the world engulfed in war.
\n\n我想告诉你们，尽管我们生活在和平的环境，世界的某些地区却依旧在战乱里。"""

    nvl clear

    scene bg bg3 at img_wandering with dissolve


    miss_you """As young people in China, you should understand the responsibilities of a great nation and strive tirelessly for the peace of both our country and the whole world.
\n\n你们作为中国的青年，要懂得中国应有的大国担当，为了国家更为了世界的和平不懈努力。"""

    nvl clear

    # show ct_text at truecenter with dissolve 
    call show_black_trans("Chapter 1  Home   巴以冲突中的一家") from _call_show_black_trans
    jump home
