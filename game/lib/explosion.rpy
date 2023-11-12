image videoer explosion = Movie(play="movies/explosion.webm",mask="movies/explosion_alpha.webm",loop=False)
image black_bg_2 = Solid("#000")
image white_bg_2 = Solid("#fff")
define config.layers += ["particle"]
define config.layers += ["explosion"]
define config.layers += ["on_explosion"]

label explosion:
    # 炸弹爆炸 开始
    play sound "audio/sfx/missile-fly-by-2.mp3"
    show black_bg_2 at Transform:
        alpha 0
        time 2.6
        easein 0.7 alpha 0.7
    pause 2.9
    show white_bg_2:
        alpha 1.0
        time 0.08
        alpha 0.0
        pause 0.1
    
    # stop music
    play sound "audio/sfx/explosion_boom2.wav"
    # play sound "audio/sfx/explosion_04.wav"
    hide videoer explosion onlayer explosion
    show videoer explosion onlayer explosion:
        zoom 2.5
        xalign 0.5
        yoffset -1200
        xoffset 50
    camera at shake_after_explosion
    camera explosion at shake_after_explosion
    # camera on_explosion at shake_after_explosion
    with None
    pause 1.0
    hide white_bg_2
    show snow onlayer particle at Transform:
        alpha 1.0
        time 10.0
        linear 4.0 alpha 0.0
    # show black_bg_2 at Transform:
    #     alpha 1.0
    #     easein 8 alpha 0.75
    # pause 5.0
    # stop music fadeout 4.0
    # hide videoer explosion onlayer explosion
    # show snow onlayer particle at Transform :
    #     alpha 1.0
    #     linear 4 alpha 0.0
    # 炸弹爆炸 结束
    return