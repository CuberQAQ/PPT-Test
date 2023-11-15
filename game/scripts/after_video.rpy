image videoer movie_after = Movie(play="movies/after.webm")
define config.layers += ["rolling_mask1"]
define config.layers += ["rolling_mask"]
define config.layers += ["rolling_text"]
image black_bg = Solid("#000")
image black_bg2 = Solid("#000")
label after_video:
    # call hide_black_trans() from _call_hide_black_trans
    stop music fadeout 2
    show black_bg with Dissolve(0.5)
    pause
    show black_bg2 onlayer rolling_mask1 at Transform:
        alpha 0.5
    hide flare_mask onlayer flare
    show videoer movie_after with dissolve
    play music "audio/one day.mp3"
    pause 8
    scene rolling_mask onlayer rolling_mask at Transform:
        alpha 0.0
        easein 5 alpha 1.0
        pause 55
        easeout 5 alpha 0

    show rolling_text onlayer rolling_text at Transform:
        yoffset 500
        linear 57.0 yoffset -4100
        
    pause
    hide videoer movie_after
    hide black_bg with dissolve
    hide black_bg2 onlayer rolling_mask1
    hide rolling_text onlayer rolling_text
    hide rolling_mask onlayer rolling_mask
    scene bg dove with dissolve
    pause