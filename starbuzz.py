import urllib.request
import time
price = 99.99

while price > 4.74:
    time.sleep(3)
    page = urllib.request.urlopen("file:///C:/Users/Hol/Videos/platzi/git/pj1/hfp/prices-loyalty.html")
    text = page.read().decode("utf8")
    buscar = text.find(">$")
    start = buscar + 2 
    end = start + 4
    price = float(text[start:end])
    print("!!")
print("Buy! right now")
my_last_name = "lozano perez"
my_name = "Lucato frodo"
my_apodo = "ele"
# actualizar estado
# realize un cambio en el comentario
