image videoer explosion = Movie(play="movies/explosion.webm",mask="movies/explosion_alpha.webm",loop=False)
image black_bg_2 = Solid("#000")
image white_bg_2 = Solid("#fff")

label explosion:
    # 炸弹爆炸 开始
    play sound "audio/sfx/missile-fly-by-2.mp3"
    pause 2.9
    show white_bg_2:
        alpha 1.0
        time 0.08
        alpha 0.0
        pause 0.1
    show black_bg_2 at Transform:
        alpha 0.2
        ease 0.05 alpha 1
    # stop music
    play sound "audio/sfx/explosion_boom2.wav"
    # play sound "audio/sfx/explosion_04.wav"
    show videoer explosion:
        zoom 2
        xalign 0.5
        yoffset -800
    camera at shake_after_explosion
    with None
    pause 1.0
    hide white_bg_2
    show snow onlayer particle at Transform:
        alpha 1.0
        time 4.0
        linear 4.0 alpha 0.0
    show black_bg_2 at Transform:
        alpha 1.0
        easein 8 alpha 0.75
    pause 2.0
    stop music fadeout 4.0
    # show snow onlayer particle at Transform :
    #     alpha 1.0
    #     linear 4 alpha 0.0
    # 炸弹爆炸 结束
    return