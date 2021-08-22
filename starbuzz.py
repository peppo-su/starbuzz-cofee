import urllib.request
page = urllib.request.urlopen("file:///C:/Users/Hol/Videos/platzi/git/pj1/hfp/prices-loyalty.html")
text = page.read().decode("utf8")
buscar = text.find(">$")
start = buscar + 2 
end = start + 4
print(text[start:end])