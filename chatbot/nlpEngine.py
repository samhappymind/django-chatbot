import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
import re, math

from collections import Counter


stopwords = nltk.corpus.stopwords.words('english')
stemmer = SnowballStemmer("english", ignore_stopwords=True)
lemmatizer = WordNetLemmatizer()


WORD = re.compile(r'\w+')
def tokenize_removestopword_tolower(sent):    
    filtered_token=[]
    for word in nltk.word_tokenize(sent):       
        if word not in stopwords:            
            if re.search('[a-zA-Z]', word):                               
                filtered_token.append(word[0].lower() + word[1:])
    return filtered_token

def tokenize_removestopword_lemmatize_stem(sent):    
    filtered_token=''
    for word in nltk.word_tokenize(sent):       
        if word not in stopwords:            
            if re.search('[a-zA-Z]', word):                               
                filtered_token = filtered_token + ' ' +(stemmer.stem(lemmatizer.lemmatize(word)))
    return filtered_token

def get_cosine(vec1, vec2):

    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator
    
def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

def get_highest_cosval_index(vector_data,query):
    tokens=[]
    filtered_str=tokenize_removestopword_lemmatize_stem(query)
    queryVec=text_to_vector(filtered_str)
    for item in vector_data:
        tokens.append(get_cosine(queryVec,item))
    cosVal=max(tokens)
    print ("cosval",cosVal)
    cosIndex=tokens.index(cosVal)
    print("cosIndex",cosIndex)
    return cosIndex,cosVal

print(type(tokenize_removestopword_lemmatize_stem('The details of last n transaction are a,b and c')))



