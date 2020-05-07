import nltk
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()

word_data = "It originated from the idea that there are readers \
who prefer learning new skills from the comforts of their drawing rooms"
# First Word tokenization
nltk_tokens = nltk.word_tokenize(word_data)
print('nltk_tokens:')
print(nltk_tokens)
# Next find the roots of the wo
# rd
print('Actual words and Stem:')
for w in nltk_tokens:
       # print ("Actual: %s \t\t Stem: %s"  % (w, porter_stemmer.stem(w)))
       print ("Actual: {0:15}Stem:{1}".format (w, porter_stemmer.stem(w)))