#coding=gbk
#coding=utf-8
import numpy as np
from matplotlib import colors, pyplot as plt
from PIL import Image
from wordcloud import WordCloud, wordcloud


def main():
	# txt=getText('������Ƶ.txt')
	f = open('������Ƶ.txt', 'r', encoding='gbk')
	text=f.read()

	color_list = ['#FF0000', '#a41a1a','#620000']  # ������ɫ����
	colormap = colors.ListedColormap(color_list)  # ����

	img = Image.open("photo.jpg")  # ������ͼƬ
	mask = np.array(img)  # ��ͼƬת��Ϊ����

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

