from stanfordcorenlp import StanfordCoreNLP
import json
import nltk
import chatbot.dataset as dataset

def upperfirst(sent):
    new_sent=''
    for word in nltk.word_tokenize(sent): 
        new_word=word[:1].upper() + word[1:]
        new_sent = new_sent +  ' ' + new_word
    return new_sent.strip()

sNLP = StanfordCoreNLP('http://localhost', port=9000,timeout=30000)
props = {
            'annotators': 'tokenize,ssplit,pos,lemma,ner,parse,depparse,dcoref,relation',
            'pipelineLanguage': 'en',
            'outputFormat': 'json'
        }

def parse_payment_query(query):
    person=None
    amount=None
    text = (upperfirst(query))
    output = json.loads(sNLP.annotate(text, properties=props))
    tokens=output['sentences'][0]['tokens']
    for token in tokens:
        print("token",token)
        if token['ner']=='PERSON' or token['ner']=='LOCATION' or token['pos']=='NNP':
            entity=str(token['word'])
            if entity in dataset.beneficiary:
                person = str(token['word'])
        if token['ner']=='NUMBER':
            amount = str(token['word'])
    print("person =>",person)
    print("amount =>",amount)
    return person,amount

def parse_details_query(query):
    amount=''
    text = (upperfirst(query))
    output = json.loads(sNLP.annotate(text, properties=props))
    tokens=output['sentences'][0]['tokens']   
    for token in tokens:
        if token['ner']=='NUMBER':
            amount = str(token['word']) 
    return amount



#parse_payment_query("pay kavya 100")

