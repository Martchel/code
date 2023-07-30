from bs4 import BeautifulSoup
import re

with open("index.html", 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

titres = soup.find_all("title")
titre = []

for t in titres:
  titre.append(t.string)
print(titre)

textes = soup.find_all("h1")
texte = []

for te in textes:
  texte.append(te.string)
print(texte)

description = soup.find_all(string = re.compile('Description :'))

name = soup.find_all("h2")
price = soup.find_all(string = re.compile('Prix :'))

names = []
prices = []

for n in name:
    names.append(n.string)
for p in price:
    prices.append(p.string)

name_and_price = []
for i in range (0,len(name)):
  name_and_price.append(names[i])
  name_and_price.append(prices[i])

print(prices)
print(name_and_price)

descriptions = []

for d in description:
  descriptions.append(d.string)

print(descriptions)

extract_price = [''.join(w.split(': ')[-1]) for w in prices]
no_euro=[''.join(w.split('€')[-2]) for w in extract_price]
conversion = [int(x)*1.2 for x in no_euro]
new_price = [str(x) for x in conversion ]


nprice = []
nprice = [x + '$' for x in new_price]
print (nprice)