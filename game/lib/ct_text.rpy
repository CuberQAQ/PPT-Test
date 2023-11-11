define ct_text_t = ""
style ct_text_style:
    xalign 0.5
    yalign 0.5
    size 60
    outlines [(4, "#000000a0", 0, 0)]


init python:
    def ct_text_func(st, a):
        # st -= 0.5
        if st <= 0: #init
            return Text(_("_"), style = "ct_text_style"), 0.01
        else:
            if st / 0.05 < ct_text_t.__len__():
                return Text(ct_text_t[:int(st/0.05)]+"_", style = "ct_text_style"), 0.01
            else: 
                return Text(ct_text_t , style = "ct_text_style"), None #+ (int(st * 5 % 2) == 0 and " " or "_")
                
        


image ct_text = DynamicDisplayable(ct_text_func)
# image ct_text_bottom = DynamicDisplayable(ct_text_func)