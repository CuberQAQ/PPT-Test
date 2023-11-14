define elder_brother = Character("Elder Brother", kind = nvl, who_suffix="\n哥哥")
define little_brother = Character("Little Brother", kind = nvl, who_suffix="\n弟弟")
define sister = Character("Sister", kind = nvl, who_suffix="\n姐姐")
define doctor = Character("Doctor", kind = nvl, who_suffix="\n医生")
define mother = Character("Mother", kind = nvl, who_suffix="\n妈妈")
define nurse= Character("Nurse", kind = nvl, who_suffix="\n护士")

label emergency:
    #scene bg emergency_and_corridor at img_wandering
    scene bg cannot_hold at img_wandering with dissolve 
    call hide_black_trans()

    play music "audio/bgm/Tassel.ogg"

    narrator "The older brother made his way through the crowd and entered the hospital.
\n\n哥哥穿过人群进入医院内部。"
    nvl clear

    elder_brother "Please, my younger brother is dying!
\n\n拜托了，我的弟弟就快不行了！"
    nvl clear

    nurse "Sorry, but you have to wait a bit, the people inside are very seriously injured, it will be over soon...
\n\n抱歉，但你要再等一下，里面的人伤得非常严重，马上就好……"
    nvl clear 

    scene bg docter1 at img_wandering with dissolve

    doctor "CPR!
\n\n准备心肺复苏！"
    nvl clear



    doctor "Faster, faster, faster！ Time is life!
\n\n快，快，再快！时间就是生命！"
    nvl clear

   
 
    nurse "Doctor, it doean’t work, the others can’t hold on either!
\n\n医生，不行了，另外几个也坚持不住了！"
    nvl clear

    doctor "Where are others?
\n\n还有其他人手吗？"
    nvl clear

    
 

    nurse "No one can be spared, they have gone to the bombing area for emergency treatment...
\n\n抽不出人了，大家都去轰炸区急救了……"
    nvl clear

    doctor "What the hell! Such a big hospital only left one nurse in the emergency room? What a joke!
\n\n这么大的医院只留了一个护士在急救室？搞什么鬼！"
    nvl clear

    scene bg docter2 at img_wandering with dissolve

    doctor "Come on, hang in there, you can do it!
\n\n加油，坚持住，你可以的！"
    nvl clear


    

    nurse "Stop, it’s too late, they are too badly injured, we have to save other people! There are still many wounded at the hospital gate!
\n\n停下，已经太晚了，他们伤得太重了，我们得去救其他人！还有好多伤员在医院门口！"
    nvl clear

    doctor "What are you talking about? I’m a doctor! Even though I know, you’re right. But... for so many days, one by one, lives die in front of me, and I’m powerless, what’s the point of my living...
\n\n你说的是什么话？我是医生啊！虽然我知道，你说的没错。但是……这么多天，一个个生命从我面前死去，而我却无能为力，我活着还有什么意义啊……"
    nvl clear

    elder_brother "Doctor, doctor, cheer up, my younger brother still needs you, you can save more people...
\n\n医生，医生，振作一点，我弟弟还需要你，你可以救更多人的……"
    nvl clear

    doctor "I’m useless, Before the war is over, the wounded will come in waves without count, I can’t save anyone, I can’t take it anymore! 
\n\n我是一个废物，只要战争一天不结束，数不清的伤员就会一波又一波地涌来，我谁也救不了，我再也忍受不了了！"
    nvl clear

    elder_brother "No, no, you are a doctor, it’s not your fault. Now, there are still people who can be saved... Please kneels and cries, save my younger brother! Please...
\n\n不，不，你可是医生啊，这不怪你。现在，还有能救的人……求求你了，救救我弟弟吧！求求你了……"
    nvl clear

    nurse "Yes, doctor. Calm down please.
\n\n是的，医生，请你冷静一点。"
    nvl clear  

    doctor "I’m sorry, let’s go.
\n\n对不起，我们走吧。"
    nvl clear

    call show_black_trans("Chapter 3  Announcement   国际态度") from _call_show_black_trans_1
    

    jump speaking



