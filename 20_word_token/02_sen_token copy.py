import nltk
nltk.download('punkt')
sentence_data = "Sun rises in the east. Sun sets in the west."

nltk_tokens = nltk.sent_tokenize(sentence_data)
print('sentence_data:')
print(sentence_data)
print('nltk_tokens:')
print(nltk_tokens)
