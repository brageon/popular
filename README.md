# Crash Course

Competitive analysis and industry proposals. Did this in April-May 2023 and that was before I used AI in September 2023. I made up the formula in bolag.py to determine KPI of industries.

```
Google Takeout, unselect all, and mark YouTube. (sum-1)/4
awk '{print gsub("YouTube",$0)}' mv2.html | awk 'BEGIN{sum=0}{sum=sum+$1}END{print sum}' 
python chunk.py # split file to 1 MB files
cp chunk.py chunk/ # change size to (256 * 256)
cd chunk, python chunk.py # split file to 64 KB files 
python views.py # print the twenty highest titles
```

Android chunking was done categorically with pandas; without using the size first.
1. Store: list, label, genre, miss.
2. CSV: max, synthes, septim.
3. Stats: review, stats. # interact 

YouTube was 26 MB after 2 years of daily watching with average cost of 1 GB surf. 
* Format: extract, soup, text
* Scraping: remote, quo*, seo, urls.
* YouTube: chunk, views. 

AWS-RunRemoteScript: Ansible Playbooks and scripts from Git. Glue, Athena to analyze S3 after Run. OpenSearch to browse notes. Elastic to browse IoT. Amplitude as API Gateway.
