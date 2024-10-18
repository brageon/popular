from bs4 import BeautifulSoup
import csv

def html_to_csv_and_count_titles(html_file):
  titles = []
  with open(html_file, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')
    
    for element in soup.find_all(string=lambda text: text and "Tittade på" in text):
      # Find the corresponding href attribute within the next sibling "a" tag
      next_sibling = element.next_sibling
      if next_sibling and next_sibling.name == 'a':
        title = next_sibling.text.strip()
        titles.append(title)
        
  with open('mv.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title'])
    for title in titles:
      writer.writerow([title])

  from collections import Counter
  title_counts = Counter(titles)
  top_20_titles = title_counts.most_common(20)

  print("Top 20 Titles and Occurrences:")
  for title, count in top_20_titles:
    print(f"{title}: {count}")

if __name__ == '__main__':
  html_file = 'mv2.html'
  html_to_csv_and_count_titles(html_file)