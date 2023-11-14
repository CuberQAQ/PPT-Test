# image bg black_trans_bg = Image()
define config.layers += ["black_trans_layer"]
# image tv = Fixed(Layer("broadcast"))
image black_bg = Solid("#000")
label show_black_trans(txt, stop_music=True):
    $ ct_text_t = txt
    # show tv
    show black_bg onlayer black_trans_layer with Dissolve(1.5)
    if stop_music:
        stop music fadeout 1.5
    pause
    play audio "audio/sfx/typing_keybroad.wav"
    pause 0.2
    hide ct_text onlayer black_trans_layer
    show ct_text onlayer black_trans_layer
    # scene bg new_bg at img_wandering with None
    return

label hide_black_trans():

    # show black_bg onlayer black_trans_layer
    pause 2.6
    hide black_bg onlayer black_trans_layer
    with Dissolve(2)
    hide ct_text onlayer black_trans_layer with Dissolve(time=1)
    return