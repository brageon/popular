import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
with open('website.txt', 'r', encoding='utf-8') as file:
    text = file.read().replace('\n', '')
tokens = word_tokenize(text)
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.casefold() not in stop_words]
frequencies = FreqDist(filtered_tokens)
for word, frequency in frequencies.most_common(10):
    print(f'{word}: {frequency}')
import requests
url = "https://raw.githubusercontent.com/schlende/practical-pandas-projects/master/datasets/google-play-store-11-2018.csv"
r = requests.get(url)
with open('andro.csv', 'w') as file:
    file.write(r.text)