import nltk
import string

# Get default English stopwords and extend with punctuation
stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(string.punctuation)
newStopWords = ['','kaun','kahan','kyun']
stopwords.extend(newStopWords)
#stopwords.append('')
#stopwords.append('kaun')

# Create tokenizer and stemmer
#tokenizer = nltk.tokenize.punkt.PunktWordTokenizer()

def is_ci_token_stopword_set_match(a, b, threshold=0.5):
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
"Give me address of student Hardik":"Select address from student where studnm=Hardik",
"In which branch does hardik study?":"Select branch from student where studnm=Hardik",
"Give me phone number of all students":"Select name,contact_no from student",
}

#test = input()
focus_sentence = "Kaun kahan kyun me address of professor hardik"


for key,value in sentences.items():
    print(is_ci_token_stopword_set_match(key,focus_sentence))
