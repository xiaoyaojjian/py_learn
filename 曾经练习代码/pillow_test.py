from PIL import Image
# open a jpg image file cd
im = Image.open('test.jpg')
# collect image size
w, h = im.size
print('Original image size: %s %s ' % (w, h))
# 缩放到50%
im.thumbnail((w//2, h//2))
print('Resize image to: %s %s' % (w//2, h//2))
# 将缩放后の图像有个jpeg保存起来
im.save('thumbnail.jpg', 'jpeg')

from PIL import ImageFilter  # 滤波 滤光
# 将之模糊化
im2 = im.filter(ImageFilter.BLUR)
im2.save('bulr.jpg', 'jpeg')

# 生成字母验证码图片

from PIL import ImageDraw, ImageFont, ImageFilter   # 绘图 # 绘字 # 滤光
import random
# 随机字母


def rndChar():
    return chr(random.randint(65, 90))  # 字母对应ascII码
# 随机颜色


def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
# 随机颜色2


def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
# 240X60
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# create Font object
font = ImageFont.truetype('c:/Windows/Fonts/Arial.ttf', 36)
# create Draw object
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# output words
for t in range(4):
    letter = rndChar()
    print('%d: %s' % (t+1,letter))
    draw.text((60 * t + 10, 10), letter, font=font, fill=rndColor2())
# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
