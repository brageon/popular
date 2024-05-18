import requests
url = "https://pyscript.net/examples/simple_clock.html"
ur2 = "https://pyscript.net/examples/todo-pylist.html"
ur3 = "https://pyscript.net/examples/altair.html"
ur4 = "https://pyscript.net/examples/folium.html"
ur5 = "https://pyscript.net/examples/d3.html"
ur6 = "https://observablehq.com/@d3/learn-d3-shapes"
ur7 = "https://pyscript.net/examples/webgl/raycaster/index.html"
ur8 = "https://pyscript.net/examples/bokeh.html"
ur9 = "https://pyscript.net/examples/bokeh_interactive.html"
u10 = "https://pyscript.net/examples/panel_kmeans.html"
u11 = "https://pyscript.net/examples/panel_stream.html"
u12 = "https://pyscript.net/examples/panel.html"
u13 = "https://pyscript.net/examples/panel_deckgl.html"
u14 = "https://pyscript.net/examples/numpy_canvas_fractals.html"
r = requests.get(url)
with open('a.txt', 'w') as file:
    file.write(r.text)
r = requests.get(ur2)
with open('b.txt', 'w') as file:
    file.write(r.text)
r = requests.get(ur3)
with open('c.txt', 'w') as file:
    file.write(r.text)    
r = requests.get(ur4)
with open('d.txt', 'w') as file:
    file.write(r.text)
r = requests.get(ur5)
with open('e.txt', 'w') as file:
    file.write(r.text)
r = requests.get(ur6)
with open('f.txt', 'w') as file:
    file.write(r.text)    
r = requests.get(ur7)
with open('g.txt', 'w') as file:
    file.write(r.text)    
r = requests.get(ur8)
with open('h.txt', 'w') as file:
    file.write(r.text)    
r = requests.get(ur9)
with open('i.txt', 'w') as file:
    file.write(r.text)    
r = requests.get(u10)
with open('j.txt', 'w') as file:
    file.write(r.text)    
r = requests.get(u11)
with open('k.txt', 'w') as file:
    file.write(r.text)        
r = requests.get(u12)
with open('l.txt', 'w') as file:
    file.write(r.text)    
r = requests.get(u13)
with open('m.txt', 'w') as file:
    file.write(r.text)    
r = requests.get(u14)
with open('n.txt', 'w') as file:
    file.write(r.text)    