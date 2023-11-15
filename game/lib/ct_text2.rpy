define ct_text_t2 = ""
style ct_text_style2:
    xalign 0.5
    yalign 0.5
    size 40
    outlines [(4, "#000000a0", 0, 0)]


init python:
    def ct_text_func2(st, a):
        # st -= 0.5
        return Text(_(ct_text_t2), style = "ct_text_style2", slow=True), None



image ct_text2 = DynamicDisplayable(ct_text_func2)
# image ct_text_bottom = DynamicDisplayable(ct_text_func)