#!/usr/bin/env python

import nltk
import matplotlib.pyplot as plt
import numpy as np

from wordcloud import WordCloud
from PIL import Image
from konlpy.tag import Komoran

plt.rcParams['font.family'] = 'NanumBarunGothic'

class Visualization :
    def __init__(self, wordList):
        self.wordList = wordList
        self.wordDict = dict(wordList)

    def makeWordCloud(self):
        alice_color_file = 'alice_color.png'
        alice_coloring = np.array(Image.open(alice_color_file))

        fontpath = "NanumBarunGothic.ttf"
        wordcloud = WordCloud(font_path = fontpath, mask = alice_coloring,
                              relative_scaling = 0.2, background_color = 'lightyellow')
        print(self.wordList)
        wordcloud = wordcloud.generate_from_frequencies(self.wordDict)

        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')

        filename = "xx_myWordCloud.png"
        plt.savefig(filename, dpi = 400 , bbox_inches = 'tight')
        print(filename + 'saved..')

    def makeBarChart(self):
        barcount = 10
        xlow, xhigh = -0.5, barcount -0.5
        result = self.wordList[:barcount]
        chardata =[]
        xdata = []
        mycolor = ['r','g','b','y','m','c','#FFF0F0', '#CCFFBB', '#05CCFF','#11CCFF']

        for idx in range(len(result)):
            chardata.append(result[idx][1])
            xdata.append(result[idx][0])

            value = str(chardata[idx]) + '건'
            plt.text(x=idx, y=chardata[idx] -5, s=value, fontsize=8, horizontalalignment='center')

        plt.xticks(range(barcount), xdata, rotation =45)
        plt.bar(range(barcount), chardata, align='center', color=mycolor)

        plt.title('상위' + str(barcount) + '빈도수')
        plt.xlim([xlow, xhigh])
        plt.xlabel('주요 키워드')
        plt.ylabel('빈도수')

        filename = "xx_myBarChart.png"
        plt.savefig(filename, dpi=400, bbox_inches = 'tight')
        print(filename + 'saved...')
filename= '노무현독도명연설.txt'
ko_con_text = open(filename, encoding='utf-8').read()
ko_con_text = ko_con_text.replace(' ', '')
print(ko_con_text)
print('-'*50)

komo = Komoran(userdic = 'user_dic.txt')
token_ko = komo.nouns(ko_con_text)
stop_word_file = 'stopword.txt'
stop_file = open(stop_word_file, 'rt', encoding='utf-8')
stop_words = [word.strip() for word in stop_file.readlines()]
token_ko = [each_word for each_word in token_ko if each_word not in stop_words]

ko = nltk.Text(tokens = token_ko)
print(type(ko))
print(type(ko.vocab()))
print(type(ko.vocab().most_common(50)))

data = ko.vocab().most_common(500)
wordList = list()

for word, count in data :
    if (count>=1 and len(word) >2):
        wordList.append((word, count))

print(wordList)
visual = Visualization(wordList)
visual.makeBarChart()
visual.makeWordCloud()


print('finished...')