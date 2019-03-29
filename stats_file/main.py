# this is a text analysis program
# date : 2019.3.28
# author by : qiming
import os
import stats
import requests
import numpy as np
import wordcloud
from pyquery import PyQuery
from PIL import Image
import matplotlib.pyplot as plt

# 用户输入信息
url =input('请输入需要分析的网页地址(url)：')

# 访问url获取网页内容
response = requests.get(url)

# 提取网页文本
document = PyQuery (response.text)
content = document ('#js_content').text() 

# 统计前100词频
cnList = stats.stats_text(content,100)

# 绘制云图
mask = np.array(Image.open('image.png'))
word = wordcloud.WordCloud(background_color='white',font_path='SourceHanSansSC-Medium.otf', mask=mask, width=500, height=500)
word.generate_from_frequencies(dict(cnList))
#word.recolor(color_func=wordcloud.ImageColorGenerator(mask))
plt.imshow(word, interpolation='bilinear')
plt.axis("off")
plt.show()

