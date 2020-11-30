import nltk
import pandas as pd
import collections
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from matplotlib import rcParams

with open('processed_lyrics.txt', 'r', encoding='utf-8') as f:
    txt = f.read()

# data_processing
for ch in txt:
    if ch in "0123456789*:.()?,;[]":
        txt = txt.replace(ch, '')
txt = txt.lower()

# word cloud plot
wc = WordCloud(background_color='white',
           max_words=100,
           width=1500,
           height=900,
           margin=2,
           scale=2,
           random_state = 2000
)


frequency = dict(collections.Counter(txt.split()))
sorted_frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True)

# attach tags to words
words = []
fs = []
tags = []

for (word, f) in sorted_frequency:
    fs.append(f)
    words.append(word)

for (word, tag) in nltk.pos_tag(words):
    tags.append(tag)

# write to files
data = pd.DataFrame({'Words': words, 'Frequency': fs, 'Tags': tags})
data.to_csv('f.csv')

# part of speech analysis
Nouns = data[(data['Tags'] == 'NN') | (data['Tags'] == 'NNS') | (data['Tags'] == 'NNPS')]
Nouns = Nouns.reset_index(drop=True)
Verbs = data[(data['Tags'] == 'VB') | (data['Tags'] == 'VBG') | (data['Tags'] == 'VBN') | (data['Tags'] == 'VBP')
             | (data['Tags'] == 'VBD') | (data['Tags'] == 'VBZ')]

Verbs = Verbs.reset_index(drop=True)


pic = wc.generate_from_frequencies(frequency)
plt.imshow(pic.recolor())
rcParams.update({'font.size': 13})
plt.title('Most Frequent Words')
plt.axis("off")
plt.show()



