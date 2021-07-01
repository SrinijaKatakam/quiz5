import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from nltk.stem import PorterStemmer


nltk.download('stopwords')
ps = PorterStemmer()


word = []
with open('Shakespeare.txt', 'r', encoding="utf-8-sig") as fileinput:
    for line in fileinput:
        for words in line.split():
            word.append(words.lower())

text = " ".join(word)
finaltext = []
text_tokens = word_tokenize(text)

for word in text_tokens:
    if word not in stopwords.words():
        finaltext.append(word)
        print("working")

finaltext = [''.join(c for c in s if c not in string.punctuation) for s in finaltext]
finaltext = list(filter(None, finaltext))

print(finaltext)

finaltext = ' '.join(finaltext)
print(finaltext)

with open('Shakespeareedit.txt', "w") as output:
    output.write(str(finaltext))
