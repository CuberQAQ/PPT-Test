define elder_brother = Character("Elder Brother", kind = nvl, who_suffix="\n哥哥")
define little_brother = Character("Little Brother", kind = nvl, who_suffix="\n弟弟")
define sister = Character("Sister", kind = nvl, who_suffix="\n姐姐")
define doctor = Character("Doctor", kind = nvl, who_suffix="\n医生")
define mother = Character("Mother", kind = nvl, who_suffix="\n妈妈")
define nurse_1= Character("Nurse 1", kind = nvl, who_suffix="\n护士1")
define nurse_2= Character("Nurse 2", kind = nvl, who_suffix="\n护士2")
define nurse= Character("Nurse", kind = nvl, who_suffix="\n护士")



label hospital_one:
   
    scene bg mother at img_wandering with dissolve
   
    play music "audio/bgm/Fake Love.mp3"
    call hide_black_trans() from _call_hide_black_trans_5 
    

    narrator "In the recent bombing, the younger brother was seriously injured. The elder brother and sister were slightly injured. After being rescued, they were sent to the hospital and were waiting for treatment. At this time, a young mother appeared at the crowded hospital entrance.
\n\n在前不久的轰炸中，弟弟伤势较重。哥哥和姐姐身受轻伤。被人救出后，他们被送往医院等待治疗。此时，人满为患的医院门口出现了一位年轻母亲。"
    nvl clear


    mother"My kid, where is my kid? Where is he?
\n\n我的孩子，我的孩子在哪里？他在哪里？"
    nvl clear

    nurse_1 "Madam, you have to calm down, your kid may have already...
\n\n夫人，您要冷静，您的孩子可能已经……"
    nvl clear

    mother"No, no, no, they are liars, they killed my kid, they killed my kid, why did they kill my kid, why did they kill my kid?！
\n\n不，不，不，他们都是骗子，他们杀了我的孩子，他们杀了我的孩子，他们为什么要杀我的孩子，他们为什么要杀我的孩子？！"
    nvl clear

    scene bg hospital2 at img_wandering with fade
    nurse_1"Madam, he's here.
\n\n夫人，他在这里。"
    nvl clear

    mother"This...this is...is this my baby? Is this my baby?
\n\n这……这是……这是我的婴儿吗？这是我的婴儿吗？"
    nvl clear

    scene bg crying_mom at img_wandering with fade

    mother"My baby, what happened to you, why don’t you move, why don’t you cry, why don’t you smile? He’s just asleep, he’ll wake up soon, he’ll smile at me, he’ll call me mom, he’s my baby, my baby...
\n\n我的婴儿，你怎么了，你为什么不动了，你为什么不哭了，你为什么不笑？他只是睡着了，他一会儿就会醒来，他会对我笑，他会叫我妈妈，他是我的宝贝，我的宝贝......."
    nvl clear

    sister"Kevin, take care of yourself.
\n\n凯文，照顾好自己。"
    nvl clear

    mother"What a lovely face, if my kid grow up...
\n\n多么可爱的脸啊，如果我的孩子长大......"
    nvl clear

    scene bg younger_brother at img_wandering with fade

    little_brother"Grow up... I didn't grow up in Palestine, I could have been shot and lost my life at any time, I could have been killed walking normally, this is my life as a Palestinian.
\n\n长大……我在巴勒斯坦长不大，任何时候都可能被枪杀而失去生命，正常走路都可能被杀死，这就是我作为巴勒斯坦人的生活。"
    nvl clear

    little_brother"Brother, pain, I`m in so much pain... I feel like I am going to die...
\n\n哥哥，好痛，我好痛啊……我感觉我要不行了……"
    nvl clear
   
    sister"We can’t wait any longer! Go and find a doctor!
\n\n我们已经等不及了，你快去找找医生！ "
    nvl clear

    # scene bg hospital_inside2  at img_wandering with fade

    elder_brother "Excuse me, do you know where there is a doctor, my younger brother can’t hold on any longer!
\n\n你好，你知道哪里有医生吗，我弟弟要坚持不住了！"
    nvl clear

    nurse_2"In the emergency room on the second floor.
\n\n在二楼的急救室。"
    nvl clear

    nurse_2"It's too crowded here. All the wounded, move to another location!
\n\n太拥挤了，所有的伤员转移到另一位置！"
    nvl clear

    call show_black_trans("Emergency   急救室") from _call_show_black_trans_4 

    jump emergency
    
    

