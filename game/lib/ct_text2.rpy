# define ct_text_t1 = ""
# define ct_text_t2 = ""
# style ct_text_style1:
#     xalign 0.5
#     yalign 0.5
#     size 60
#     outlines [(4, "#000000a0", 0, 0)]

# style ct_text_style2:
#     xalign 0.5
#     yalign 0.5
#     size 60
#     outlines [(4, "#000000a0", 0, 0)]


# init python:
#     def ct_text2_t1_func(st, a):
#         # st -= 0.5
#         if st <= 0: #init
#             return Text(_("_"), style = "ct_text_style1"), 0.01
#         else:
#             if st / 0.07 < ct_text_t1.__len__():
#                 return Text(ct_text_t1[:int(st/0.07)]+"_", style = "ct_text_style1"), 0.01
#             else: 
#                 return Text(ct_text_t1 , style = "ct_text_style1"), None #+ (int(st * 5 % 2) == 0 and " " or "_")
                


# # image ct_text = DynamicDisplayable(ct_text_func)
# # image ct_text_bottom = DynamicDisplayable(ct_text_func)

# style ct_text2_vbox_style:
#     xalign 0.5
#     yalign 0.5


# init python:
#     def ct_text2_func(st,a):
#         ct_text_t = ct_text_t1
#         return VBox(
#             DynamicDisplayable(ct_text2_t1_func), # Text(ct_text_t1, dynamic = True, style = "ct_text_style2"),
#             Text(ct_text_t2, dynamic = True, style = "ct_text_style2"), 
#             style = "ct_text2_vbox_style"
#             ), None
# image ct_text2 = DynamicDisplayable(ct_text2_func)


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