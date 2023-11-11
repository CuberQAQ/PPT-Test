# transform ScreenShake(strength, time):
#     delay time
#     block:
#         xoffset -80
#         yoffset -80
#         ease 0.1 xoffset 40 yoffset 80
#         xoffset -80
#         yoffset -80
#         ease 0.1 xoffset 80 yoffset 80
#         xoffset -80
#         yoffset -80
#         ease 0.1 xoffset 80 yoffset 80
#         xoffset -80
#         yoffset -80
#         ease 0.1 xoffset 80 yoffset 80
#         xoffset 80
#         yoffset 80
#         ease 0.1 xoffset -80 yoffset -80
#         repeat time / 0.2
#     xoffset 0
#     yoffset 0

# 定义一个爆炸后的晃动效果的变换
transform shake_after_explosion:
    # 随机选择一个方向
    zoom 1.1
    xalign 0.5
    yalign 0.5
    block:
        choice:
        # 向左上方晃动
            # xanchor 0.0
            # yanchor 1.0
            xoffset -30
            yoffset -30
            # 使用easeout属性让图像在开始的时候快速移动，然后慢慢减速
            easeout 0.05 xoffset 30 yoffset 30
            # 使用easein属性让图像在结束的时候快速移动，然后慢慢加速
            easein 0.05 xoffset 0 yoffset 0
        choice:
            # 向右上方晃动
            # xanchor 1.0
            # yanchor 1.0
            xoffset 30
            yoffset -30
            easeout 0.05 xoffset -30 yoffset 30
            easein 0.05 xoffset 0 yoffset 0
        choice:
            # 向左下方晃动
            # xanchor 0.0
            # yanchor 0.0
            xoffset -30
            yoffset 30
            easeout 0.05 xoffset 30 yoffset -30
            easein 0.05 xoffset 0 yoffset 0
        choice:
            # 向右下方晃动
            # xanchor 1.0
            # yanchor 0.0
            xoffset 30
            yoffset 30
            easeout 0.05 xoffset -30 yoffset -30
            easein 0.05 xoffset 0 yoffset 0
        repeat 23
    # ease zoom 1
    