define rolling_text_t = """
{color=#FF6969}{size=40}导演{/size}{/color}
李金言

{color=#FF6969}{size=40}编剧{/size}{/color}
唐  艺   古恩宇

{color=#FF6969}{size=40}后期{/size}{/color}
阮丽颖 洪鑫雯 文泽豪

{color=#FF6969}{size=40}哥哥{/size}{/color}
秦浩朗

{color=#FF6969}{size=40}姐姐{/size}{/color}
尤静宜

{color=#FF6969}{size=40}弟弟{/size}{/color}
孙江坤

{color=#FF6969}{size=40}旁白{/size}{/color}
古恩宇

{color=#FF6969}{size=40}中国外交官{/size}{/color}
胡紫涵

{color=#FF6969}{size=40}美国国务卿{/size}{/color}
梁子涵

{color=#FF6969}{size=40}巴勒斯坦大使{/size}{/color}
韩凤阁

{color=#FF6969}{size=40}母亲{/size}{/color}
游  欣

{color=#FF6969}{size=40}巴勒斯坦老师{/size}{/color}
李金言

{color=#FF6969}{size=40}医生{/size}{/color}
唐  艺

{color=#FF6969}{size=40}介绍者{/size}{/color}
罗淑芬

{color=#FF6969}{size=40}护士{/size}{/color}
陶滢宇 张晓薇 李可欣

{color=#FF6969}{size=40}群演{/size}{/color}
王铭晟 谢谦益 陈雅雯
陈贝贝 薛思彤 俞若珊
黎呈娟 邓梓彤 肖舞菲
段培欣 吴桢珠 陈子伶
李锐涛 利宇涛 杨健辉
曹柏圳 钟元彪 廖万精
邓可欣   阳飞翔 
杨  凌   覃  莹

{color=#FF6969}{size=40}后勤{/size}{/color}
单思远 谭旭君 冼  郸
王枫睿 陈冠旭 秦  睿

{color=#FF6969}{size=40}妆造{/size}{/color}
陈美逸 申  堰
古恩宇 游  欣
    
"""

style rolling_text_style:
    # yoffset 500
    yalign 0.0
    xalign 0.5
    size 48
    outlines [(2, "#000000a0", 0, 0)]
    # line_leading 5
    color "#fff"

    # caret Solid("#fff")

    # xalign 0.0

style rolling_vbox_style:
    xalign 0.07
    yalign 0.0
    yoffset 200

define rolling_text_max_size = 60

init python:
    # def rolling_text_trans():

    def rolling_text_func(st, a):
        lst = rolling_text_t.split('\n')
        wid_lst = list()
        n_off = st * 200
        tot = 0
        for item in lst:
            tot+=60
            wid_lst.append(Text(item, dynamic=True, style="rolling_text_style"))
            ++tot
        print(wid_lst)
        return VBox(*wid_lst,style="rolling_vbox_style", yoffset = 540 - n_off), None

image rolling_text = DynamicDisplayable(rolling_text_func)
  