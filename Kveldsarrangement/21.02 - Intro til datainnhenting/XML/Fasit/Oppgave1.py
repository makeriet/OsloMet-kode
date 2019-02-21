import xml.etree.ElementTree as ET
tree = ET.parse('../cddata.xml')
root = tree.getroot()

for artist in root.iter('ARTIST'):
    print(artist.text)
