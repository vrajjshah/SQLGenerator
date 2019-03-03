import nltk
import string
import sqlite3


connection = sqlite3.connect("student.db")
crsr = connection.cursor()

# Get default English stopwords and extend with punctuation
stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(string.punctuation)
newStopWords = ['','give','show','kyun']
stopwords.extend(newStopWords)
#stopwords.append('')
#stopwords.append('kaun')

# Create tokenizer and stemmer
#tokenizer = nltk.tokenize.punkt.PunktWordTokenizer()

def is_ci_token_stopword_set_match(a, b, threshold=0.7):
    """Check if a and b are matches."""
    tokens_a = [token.lower().strip(string.punctuation) for token in nltk.word_tokenize(a) \
                    if token.lower().strip(string.punctuation) not in stopwords]
    tokens_b = [token.lower().strip(string.punctuation) for token in nltk.word_tokenize(b) \
                    if token.lower().strip(string.punctuation) not in stopwords]

    # Calculate Jaccard similarity
    print(tokens_a)
    print(tokens_b)
    ratio = len(set(tokens_a).intersection(tokens_b)) / float(len(set(tokens_a).union(tokens_b)))
    print(ratio)
    return (ratio >= threshold)
sentences = {
"Give me address of student Hardik":"SELECT address FROM stud WHERE studnm LIKE '%hardik%'",
"In which branch does hardik study?":"Select branch from student where studnm=Hardik",
"Give me phone number of all students":"Select name,contact_no from student",
}

#test = input()
focus_sentence = "Show me address of student amisha"


for key,value in sentences.items():
    if(is_ci_token_stopword_set_match(key,focus_sentence)):
        print("inside")
        crsr.execute(value)
        ans= crsr.fetchall()
        for i in ans:
            print(i)

#crsr.execute("SELECT studid FROM stud WHERE city=\"VADODARA\"")
