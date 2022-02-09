import urllib.request
import time
price = 99.99

while price > 4.74:
    time.sleep(5)
    page = urllib.request.urlopen("file:///C:/Users/Hol/Videos/platzi/git/pj1/hfp/prices-loyalty.html")
    text = page.read().decode("utf8")
    buscar = text.find(">$")
    start = buscar + 2 
    end = start + 4
    price = float(text[start:end])
    print("!!")
print("Buy! right now")