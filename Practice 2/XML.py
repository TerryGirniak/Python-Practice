import xml.etree.ElementTree as ET
from collections import Counter

root = ET.Element("root")
wordEl = ET.SubElement(root, "words_count")

wordListRaw = open("sadok.txt", "r").read().split()
wordListRaw = filter(None, wordListRaw)
wordList = []

for word in wordListRaw:
    word = word.replace(",", "").replace(".", "")
    wordList.append(word)

counter = Counter(wordList)

for word, count in counter.items():
    ET.SubElement(wordEl, "word", name = word).text = str(count)

tree = ET.ElementTree(root)
tree.write("c.xml")
