define ct_text3_t = ""
define ct_text3_delay = .3
define ct_text3_speed = .03
style ct_text3_style:
    xalign 0.5
    yalign 0.5
    size 60
    outlines [(4, "#000000a0", 0, 0)]
define ct_text3_style_t = "ct_text3_style"

style ct_text3_style_jp:
    xalign 0.5
    yalign 0.5
    # font "fonts/GenEiKoburiMin6-R.ttf"
    font "fonts/Minecraft Evenings Updated.ttf"
    size 160
    outlines [(6, "#000000a0", 0, 0)]

transform ZoomEaseIn(begin=4.6, end=1, time=1.5, dl=0):
    time dl
    zoom begin
    ease_circ time zoom end
define ct_text3_pre_len = 1
init python:
    def ct_text3_func(st, a):
        # st -= 0.5
        if st <= ct_text3_delay+ct_text3_speed * ct_text3_pre_len: #init
            return Text(_(ct_text3_t[0:ct_text3_pre_len]), style = ct_text3_style_t), 0.01
        else:
            if (st-ct_text3_delay) / ct_text3_speed < ct_text3_t.__len__():
                return Text(ct_text3_t[:int((st-ct_text3_delay)/ct_text3_speed)]+"", style = ct_text3_style_t), 0.01
            else: 
                return Text(ct_text3_t , style = ct_text3_style_t), None #+ (int(st * 5 % 2) == 0 and " " or "_")
                
        


image ct_text3 = DynamicDisplayable(ct_text3_func)
# image ct_text3_bottom = DynamicDisplayable(ct_text3_func)