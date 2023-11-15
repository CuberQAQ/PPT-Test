image videoer explosion = Movie(play="movies/explosion.webm",mask="movies/explosion_alpha.webm",loop=False)
image black_bg_2 = Solid("#000")
image white_bg_2 = Solid("#fff")
define config.layers += ["explosion_bg"]
define config.layers += ["explosion_under"]
define config.layers += ["explosion_bg2"]
define config.layers += ["particle"]
define config.layers += ["explosion"]
define config.layers += ["on_explosion"]

label explosion(center_label=False, hide_center_label=False):
    # 炸弹爆炸 开始
    stop music fadeout 20
    stop audio
    play sound "audio/sfx/missile-fly-by-2.mp3" volume 1
    pause 0.5
    play audio "audio/sfx/air_defense_warning.mp3" volume 0.4
    pause 0.01
    stop audio fadeout 20.0
    
    show black_bg_2 onlayer explosion_bg at Transform:
        alpha 0
        time 1.8
        easein 0.4 alpha 0.8
    
    pause 1.3
    if center_label:
        call expression center_label from _call_expression
    pause 1
    show white_bg_2 onlayer explosion_bg2:
        alpha 1.0
        time 0.08
        alpha 0.0
        pause 0.1
    
    # stop music
    play sound "audio/sfx/explosion_boom2.wav"
    # play music "audio/sfx/explosion_04.wav" volume 2.0
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
    if hide_center_label:
        call expression hide_center_label
    hide white_bg_2 onlayer explosion_bg2
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

label hide_explosion:
    hide black_bg_2 onlayer explosion_bg
    hide videoer explosion onlayer explosion
    return