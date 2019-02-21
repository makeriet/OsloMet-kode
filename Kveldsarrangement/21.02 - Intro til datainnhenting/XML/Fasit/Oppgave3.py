import xml.etree.ElementTree as ET
tree = ET.parse('../cddata.xml')
root = tree.getroot()

CDCheapest = 0
CDExpensive = 0

for cd in root.iter('CD'):
    cdPrice = float(cd.find('PRICE').text)

    # Checks if it's cheaper than CDCheapest
    if CDCheapest == 0:
        CDCheapest = cd
    else:
        CDCheapestPrice = float(CDCheapest.find('PRICE').text)
        if cdPrice < CDCheapestPrice:
            CDCheapest = cd


    # Checks if it's more expensive than CDExpensive
    if CDExpensive == 0:
        CDExpensive = cd
    else:
        CDExpensivePrice = float(CDExpensive.find('PRICE').text)
        if cdPrice > CDExpensivePrice:
            CDExpensive = cd

print("The cheapes CD was", CDCheapest.find('TITLE').text, "by", CDCheapest.find('ARTIST').text, "at", CDCheapest.find('PRICE').text)
print("The most expensive CD was", CDExpensive.find('TITLE').text, "by", CDExpensive.find('ARTIST').text, "at", CDExpensive.find('PRICE').text)
