# -*- coding = utf-8 -*-

'''
img         待转换图（Image对象
font_size   字符大小（默认15
up_size     源图片放大倍数（默认1.1
bg          背景颜色（默认白
chr_color   字符颜色（默认黑
'''

from PIL import Image,ImageFont
import numpy as np

def ascill_art(file):
    # 打开图片文件
    im = Image.open(file)

    # 通过灰度覆盖这张图片 降低图片的亮度
    im = im.convert("L")

    # 对图片进行降采样
    sample_rate = 0.15

    # 这段代码可以处理图片拉伸的情况
    font = ImageFont.truetype("simsun.ttf")
    aspect_ratdio = font.getsize("x")[0] / font.getsize("x")[1]

    new_im_size = np.array(
        [im.size[0] * sample_rate, im.size[1] * sample_rate * aspect_ratdio]
    ).astype(int)

    # 用新的的图片大小resize之前的
    im = im.resize(new_im_size)

    # 将图片转换成一个numpy字符
    im = np.array(im)

    # symbols中定义了 我们字符画中的所有字符
    # 按照字符亮度升序排列
    # 文件转换的时候会不断的查询这个symbols字符集
    symbols = np.array(list("$@B%8&WM#*oahkbdpqwm-_+~<>;:,\"^`'. "))

    # 设置这个字符集合的取值范围的最大和最小值[0,max_symbol_index)
    im = (im - im.min()) / (im.max() - im.min()) * (symbols.size - 1)

    # 完成字符的转换
    ascii = symbols[im.astype(int)]
    lines = "\n".join(("".join(r) for r in ascii))
    return lines

if __name__=="__main__":
    ascill_art("png03.png")



