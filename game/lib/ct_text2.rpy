define ct_text_t2 = ""
style ct_text_style2:
    xalign 0.5
    yalign 0.5
    size 40
    outlines [(4, "#000000a0", 0, 0)]


init python:
    def ct_text_func2(st, a):
        # st -= 0.5
        if st <= 0: #init
            return Text(_("_"), style = "ct_text_style2"), 0.01
        else:
            if st / 0.05 < ct_text_t2.__len__():
                return Text(ct_text_t2[:int(st/0.05)]+"_", style = "ct_text_style2"), 0.01
            else: 
                return Text(ct_text_t2 , style = "ct_text_style2"), None #+ (int(st * 5 % 2) == 0 and " " or "_")
                
        


image ct_text2 = DynamicDisplayable(ct_text_func2)
# image ct_text_bottom = DynamicDisplayable(ct_text_func)