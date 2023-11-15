define video_bottom_text_t = "This is zimu 字幕测试"
define video_bottom_text_t2 = "This is zimu 字幕测试"
style video_bottom_text_style:
    xalign 0.5
    yalign 0.80
    size 40
    outlines [(4, "#000000a0", 0, 0)]

style video_bottom_text_style2:
    xalign 0.5
    yalign 0.80
    size 40
    color "#fff"
    outlines [(4, "#000000a0", 0, 0)]

style video_bottom_text_vbox_style:
    xalign 0.5
    yalign 0.82
    color "#fff"

# Text(video_bottom_text_t, dynamic = True, style = "video_bottom_text_style", slow=True)
init python:
    def video_bottom_text_func(st,a):
        return VBox(
            Text(video_bottom_text_t, dynamic = True, style = "video_bottom_text_style"),
            Text(video_bottom_text_t2, dynamic = True, style = "video_bottom_text_style2"), 
            style = "video_bottom_text_vbox_style"
            ), None

image video_bottom_text = DynamicDisplayable(video_bottom_text_func)