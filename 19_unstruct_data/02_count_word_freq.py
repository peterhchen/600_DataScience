filename = r'../unstructured_data/input.txt'  

from collections import Counter

with open(filename) as f:
   replaceTxt = f.read().replace(',', '').replace ('\n', '')
   readSplit = replaceTxt.split()
   print ('readSplit:')
   print (readSplit)
   p = Counter(readSplit)
   print ('p:')
   print(p)