import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from autocorrect import spell
#from textblob import TextBlob
#from nltk.stem.porter import stem

def spCheck(w,neww):
    print("Do you want to replace "+w+" with "+neww+" ?")
    ans = input()
    if(ans=='y'):
        return neww
    else:
        return w

specialChar =  ['!','?','#',';',',','.']
text = "List enrollmant namber of student hardik. Allso give phone number of him."
#blob = TextBlob(text)
#print(blob.correct())

for char in text:
    if char in specialChar:
	    text = text.replace(char, '')

sp_dict = []
stri = ""
#f = open("/home/vraj/Project/en-basic.txt","r")
#for x in f:
#	print(x)

print(sp_dict)
print(text)

# Getting the stop words of English Language
stop_words = set(stopwords.words('english'))

#Tokenizes the paragraph into sentence
sent_text = nltk.sent_tokenize(text)


filtered_sentence = []

#Create a parse tree and remove stop words
for sentence in sent_text:
    tokenized_text = nltk.word_tokenize(sentence) #tokenize thbe sentence into words
    ps = PorterStemmer()
    for w in tokenized_text:
       neww = spell(w)
       if(neww==w):
           print("",end='')
       else:
           w=spCheck(w,neww)
       if w not in stop_words:
            filtered_sentence.append(ps.stem(w))
    #tagged = nltk.pos_tag(tokenized_text)
    #print(tagged)

tagged = nltk.pos_tag(filtered_sentence)
print(tagged)
print(filtered_sentence)
