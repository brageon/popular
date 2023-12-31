import re, requests, json
from urllib.parse import urljoin 
from bs4 import BeautifulSoup
url = "https://www.remotepython.com/jobs/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
results = []
job_listing_boxes = soup.find_all(class_="item")
for item in job_listing_boxes:
    parsed = {}
    if title := item.find("h3"):
        parsed["title"] = title.get_text(strip=True)
    if item_url := item.find("h3").a["href"]:
        parsed["url"] = urljoin(url, item_url)
    if company := item.find("h5").find("span", class_="color-black"):
        parsed["company"] = company.text
    if location := item.select_one("h5 .color-white-mute"):
        parsed["location"] = location.text
    if posted_on := item.find("span", class_="color-white-mute", text=re.compile("posted:", re.I)):
        parsed["posted_on"] = posted_on.text.split("Posted:")[-1].strip()
    results.append(parsed)
for i in [results[item:item+1] for item in range(0,len(results),1) if item%1 == 0]:
    print(*i)
#with open("cell.txt", "a") as file:
#    file.write(str(results))		6-3, 3-5, 1-15
