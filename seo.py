import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt') 
def seo_analysis(url):
    good = []
    bad = []
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Unable to access the website.")
        return
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('title').get_text()
    description = soup.find('meta', attrs={'name': 'description'})['content']
    if title:
        good.append("Title Exists! Great!")
    else:
        bad.append("Title does not exist! Add a Title")
    if description:
        good.append("Description Exists! Great!")
    else:
        bad.append("Description does not exist! Add a Meta Description")
    hs = ["h1", "h2", "h3", "h4", "h5", "h6"]
    h_tags = []
    for h in soup.find_all(hs):
        good.append(f"{h.name}-->{h.text.strip()}")
    h_tags.append(h.name)
    if 'h1' not in h_tags:
        bad.append("No H1 found!")
    for i in soup.find_all('img', alt=''):
        bad.append(f"No Alt: {i}")
    bod = soup.find('body').text
    words = [i.lower() for i in word_tokenize(bod)]
    sw = nltk.corpus.stopwords.words('english')
    new_words = []
    for i in words:
        if i not in sw and i.isalpha():
            new_words.append(i)
    freq = nltk.FreqDist(new_words)
    keywords= freq.most_common(10)
    print("Keywords: ", keywords)
    print("The Good: ", good)
    print("The Bad: ", bad)
seo_analysis("https://croisette.se")
#https://pythonology.eu/what-is-syntax-in-programming-and-linguistics/
