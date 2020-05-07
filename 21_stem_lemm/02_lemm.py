import nltk

from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
nltk.download('wordnet')
word_data = "It originated from the idea that there are readers \
who prefer learning new skills from the comforts of their drawing rooms"
nltk_tokens = nltk.word_tokenize(word_data)
for w in nltk_tokens:
       # Token 0 + space 15 + Token 1
       print("Actual: {0:15}Lemma: {1}".format(w,wordnet_lemmatizer.lemmatize(w)))
