import json
html = """
<html>
  <head>
  </head>
  <body>
    <script id="__NEXT_DATA__" type="application/json">
      {"product": {"id": 1, "name": "first product"}}
    </script>
  </body>
</html
"""

# using parsel
from parsel import Selector
selector = Selector(html)
data = selector.css("#__NEXT_DATA__::text").get()
data = json.loads(data)
print(data['product'])
# {"id": 1, "name": "first product"}

# using beautifulsoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(html)
data = soup.select_one("#__NEXT_DATA__").text
data = json.loads(data)
print(data['product'])
# {"id": 1, "name": "first product"}

