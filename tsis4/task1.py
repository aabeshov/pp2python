import re
import csv
file = open('info', encoding="utf8")
text = file.read()



binPattern = r"\nБИН.*(?P<BIN>\b[0-9]+)"
ndcPattern = r"\nНДС.*(?P<NDC>\b[0-9]+)"
znmPattern = r"\nЗНМ.*(?P<ZNM>\b[A-Z]+[0-9]+)"
timeAndAdressPattern = r"\nВремя:(?P<Time>.*)\n(?P<Adress>.*)"
checkPattern = r"\nЧек.*(?P<Check>\b[№]?[0-9]+)"

BINtext = re.search(binPattern, text).group("BIN").strip()
NDCtext = re.search(ndcPattern, text).group("NDC").strip()
ZNMtext = re.search(znmPattern, text).group("ZNM").strip()
timeText = re.search(timeAndAdressPattern, text).group("Time").strip()
adressText = re.search(timeAndAdressPattern, text).group("Adress").strip()
checkText = re.search(checkPattern, text).group("Check").strip()

itemPatternText = r"(?P<name>.*)\n{1}(?P<count>.*)x(?P<price>.*)\n{1}(?P<total1>.*)\n{1}Стоимость\n{1}(?P<total2>.*)"
itemPattern = re.compile(itemPatternText)

items = [["БИН","НДС","ЗНМ","Чек","Наименование товара","Кол-во","Цена за единиц","Итого","Адрес", "Время"]]

for m in re.finditer(itemPattern, text):
    items.append([BINtext, NDCtext, ZNMtext, checkText, m.group("name").strip(), m.group("count").strip(), m.group("price").strip(), m.group("total1"), adressText, timeText])

with open('file.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerows(items)

file.close()