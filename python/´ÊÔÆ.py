#coding=gbk
#coding=utf-8
import numpy as np
from matplotlib import colors, pyplot as plt
from PIL import Image
from wordcloud import WordCloud, wordcloud


def main():
	# txt=getText('处理后词频.txt')
	f = open('处理后词频.txt', 'r', encoding='gbk')
	text=f.read()

	color_list = ['#FF0000', '#a41a1a','#620000']  # 建立颜色数组
	colormap = colors.ListedColormap(color_list)  # 调用

	img = Image.open("photo.jpg")  # 打开遮罩图片
	mask = np.array(img)  # 将图片转换为数组

	w=wordcloud.WordCloud(font_path='msyh.ttc',
						  mask=mask,
						  background_color='white',
						  width=800,
						  height=600,
						  max_words=40,
						  font_step=3,
						  colormap=colormap)

	w.generate(text)
	w.to_file('wordcloud.png')
	print('make wordCloud successfully!')
main()

