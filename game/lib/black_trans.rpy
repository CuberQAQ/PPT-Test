# image bg black_trans_bg = Image()
define config.layers += ["black_trans_layer"]
define config.layers += ["particle"]
# image tv = Fixed(Layer("broadcast"))
image black_bg = Solid("#000")
label show_black_trans(txt, stop_music=True):
    $ ct_text_t = txt
    # show tv
    show black_bg onlayer black_trans_layer with Dissolve(1.5)
    pause
    if stop_music:
        stop music fadeout 1.5
    pause 0.5
    show ct_text onlayer black_trans_layer at Transform
    # scene bg new_bg at img_wandering with None
    return

label hide_black_trans():

    # show black_bg onlayer black_trans_layer
    pause 2.6
    hide black_bg onlayer black_trans_layer
    with Dissolve(2)
    hide ct_text onlayer black_trans_layer with Dissolve(time=1)
    return