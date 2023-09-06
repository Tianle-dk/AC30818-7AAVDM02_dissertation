#_*_ coding:utf-8 _*_

# import wordcloud
# import jieba
# import PIL .Image as image
# import numpy
# masks = numpy.array(image.open("img_2.png"))
# text = open("yingli.txt","r",encoding="UTF-8")
# rea = text.read()
# text.close()
# ls = jieba.lcut(rea)
# txt = "".join(ls)
# ciyun = wordcloud.WordCloud(font_path="msyh.ttc",max_words=25,random_state=3,width=700,height=700,background_color = "white",mask=masks)
#                             #background_color="white",mask=masks)
# ciyun.generate(txt)
# ciyun.to_file("yingli.png")
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

# 打开文本
# text = open("zong1.txt",'rb').read()
# # 中文分词
# text = ' '.join(jieba.cut(text))   # 利用jieba进行分词形成列表，将列表里面的词用空格分开并拼成长字符串。
# print(text[:100])  # 打印前100个字符

with open('"E:\pycharmfile\littleredbook\处理后词频.xlsx"','r',encoding="gb18030") as f:
# with open(r'E:\pycharmfile\cmau\word_freq.txt',encoding="utf-8") as f:
    text = f.read()
text = ' '.join(jieba.cut(text))   # 利用jieba进行分词形成列表，将列表里面的词用空格分开并拼成长字符串。
# print(text[:100])  # 打印前100个字符
# 生成对象
wc = WordCloud(font_path="SimHei.ttf", width=800, height=600, mode="RGBA", background_color=None).generate(text)

# 显示词云
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()

# 保存到文件
wc.to_file("1.png")
