# coding: utf-8

from PIL import Image
import pytesseract

# （不推荐使用）这种方法实现只能识别数字，字符中文以及部分数字识别不出来(例如:1和7识别不了)
image = Image.open("666.png")
try:
    content = pytesseract.image_to_string(image)
    print(content)
except Exception as e:
    print('验证码获取失败')
    print(e)


