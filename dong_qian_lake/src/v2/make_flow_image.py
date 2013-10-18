# coding=UTF-8
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import textwrap

def draw_text(draw=None, point=(0,0),txt='',font=None, width=6):
    x,y = point

    for line in textwrap.wrap(txt,width=width):
        draw.text((x,y), line, (0,0,0),font)
        y +=font.getsize(line)[1]



#font = ImageFont.load_default()
font = ImageFont.truetype(u"/Library/Fonts/宋体.ttc",16)
img=Image.new("RGBA", (3500,800),(255,255,255))
draw = ImageDraw.Draw(img)
# main

draw_text(draw=draw,point=(10,300),txt=u'项目会商',font=font)
draw_text(draw=draw,point=(150,300),txt=u'土地挂拍',font=font)
draw_text(draw=draw,point=(250,300),txt=u'环评、水保、人防报告编制',font=font,width=8)
draw_text(draw=draw,point=(450,300),txt=u'环评、水保、人防批复',font=font, width=7)

draw_text(draw=draw,point=(600,400),txt=u'编制设计招标文件',font=font,width=5)
draw_text(draw=draw,point=(750,400),txt=u'设计勘察招标',font=font)
draw_text(draw=draw,point=(900,400),txt=u'勘察及方案设计',font=font,width=5)
draw_text(draw=draw,point=(1050,400),txt=u'专家方案设计',font=font)
draw_text(draw=draw,point=(1200,400),txt=u'编制日及交评文本',font=font,width=5)
draw_text(draw=draw,point=(1350,400),txt=u'部门会审',font=font)
draw_text(draw=draw,point=(1500,400),txt=u'方案公示及批复',font=font,width=5)
draw_text(draw=draw,point=(1650,400),txt=u'扩初设计',font=font)

draw_text(draw=draw,point=(1800,500),txt=u'施工图设计',font=font)
draw_text(draw=draw,point=(1950,500),txt=u'施工图审查',font=font)
draw_text(draw=draw,point=(2100,500),txt=u'日照分析报告',font=font)
draw_text(draw=draw,point=(2250,500),txt=u'规划放验线',font=font,width=8)
draw_text(draw=draw,point=(2400,500),txt=u'申请规划许可证',font=font,width=8)
draw_text(draw=draw,point=(2550,500),txt=u'监理施工招投标',font=font,width=8)
draw_text(draw=draw,point=(2700,500),txt=u'合同备案',font=font,width=8)
draw_text(draw=draw,point=(2850,500),txt=u'消防及质安监备案',font=font)
draw_text(draw=draw,point=(3000,500),txt=u'申请施工许可证',font=font)
draw_text(draw=draw,point=(3150,500),txt=u'施工准备',font=font)

#other
draw_text(draw=draw,point=(250,10),txt=u'签订出让合同',font=font)
draw_text(draw=draw,point=(600,300),txt=u'申请规划用地许可证',font=font,width=5)
draw_text(draw=draw,point=(750,10),txt=u'办理土地证',font=font)
draw_text(draw=draw,point=(1800,300),txt=u'可再生能源评估',font=font)
draw_text(draw=draw,point=(1800,400),txt=u'扩初会审',font=font)
draw_text(draw=draw,point=(1950,600),txt=u'人防施工图审查',font=font)
draw_text(draw=draw,point=(2100,600),txt=u'人防设计审批',font=font)
draw_text(draw=draw,point=(2100,200),txt=u'防雷设计审批',font=font)
draw_text(draw=draw,point=(2100,300),txt=u'交警批复',font=font)
draw_text(draw=draw,point=(2100,400),txt=u'经济技术指标复核',font=font,width=5)
draw_text(draw=draw,point=(2250,400),txt=u'白蚁防治费和墙改基金',font=font,width=5)

# other text
draw_text(draw=draw,point=(850,350),txt=u'建筑方案设计（合计55天）',font=font,width=20)
draw_text(draw=draw,point=(2300,700),txt=u'编制工程量清单，确定监理和施工招投标文件',font=font,width=11)

#draw_lines
# main lines
draw.line((10,350, 550,350), fill=(255,0,0))
draw.line((550,350, 550,450), fill=(255,0,0))
draw.line((550,450, 1750,450), fill=(255,0,0))
draw.line((1750,450, 1750,550), fill=(255,0,0))
draw.line((1750,550, 3300,550), fill=(255,0,0))

#other lines


draw = ImageDraw.Draw(img)
img.save("a_test.png")

img.show()
