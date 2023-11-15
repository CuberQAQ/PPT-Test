image videoer movie_after = Movie(play="movies/after.webm")
define config.layers += ["rolling_mask1"]
define config.layers += ["rolling_mask"]
define config.layers += ["rolling_text"]
image black_bg = Solid("#000")
image black_bg2 = Solid("#000")

style text_widget_style:
    xalign 0.5
    yalign 0.5
    size 80
    color "#ffffff"
    outlines [(4, "#000000a0", 0, 0)]

image text_widget = Text("Thank you!", style = "text_widget_style")
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

    show rolling_text onlayer rolling_text at Transform:
        yoffset 500
        linear 65.0 yoffset -4750
        
    pause 63
    hide rolling_mask onlayer rolling_mask
    hide rolling_text onlayer rolling_text
    hide black_bg2 onlayer rolling_mask1
    hide videoer movie_after
    hide black_bg
    scene bg dove at img_wandering
    with dissolve
    pause 13
    stop music fadeout 3
        # easein 
    pause
    show text_widget with dissolve
    pause