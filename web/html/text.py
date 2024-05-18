from bs4 import BeautifulSoup
import requests as req
filenames = "t153779p47", "t153779p48", "t153779p49", "t153779p50", "t153779p52", "t153779p53", "t153779p54", "t153779p55", "t153779p56", "t153779p57", "t153779p58", "t153779p59", "t153779p60", "t153779p61", "t153779p62", "t153779p64", "t153779p65", "t153779p66", "t153779p67", "t153779p68", "t153779p69", "t153779p70", "t153779p71", "t153779p72","t153779p73", "t153779p80", "t153779p75", "t153779p76","t153779p77", "t153779p78", "t153779p79", "t153779p81", "t153779p82", "t153779p83", "t153779p84", "t153779p85", "t153779p86", "t153779p88", "t153779p89", "t153779p90", "t153779p91", "t153779p92"
# 74, 87
for fn in filenames:
    with open(fn, 'r', encoding='ISO-8859-1') as file: 
        test_str = file.read()
S = BeautifulSoup(test_str, 'lxml')
Tag = S.findAll('div', { "class" : "post-clamped-text" })
Vag = S.findAll('div', { "class" : "post_message" })
print(Tag, Vag)
'''
for k in (S.find_all('div', class_="post-clamped-text")):
    print(k)
Tag = S.select_one('li:nth-of-type(2)')
Tag.decompose()
print(S.body.prettify())
for tag in S.find_all('div class'):
    print(f'{tag.name}: {tag.text}')
'''