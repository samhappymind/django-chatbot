

from chatbot import TextCassification
from chatbot import dataset
from chatbot import nlpEngine
from chatbot import stanford_util
txt_cls_model = None

vec_arr=[]
vec_greet_arr=[]
def train_txt_cls_model():                     
    target = []                                                                                                   
    record = dataset.pay_qs + dataset.query_qs + dataset.greet_qs  
                                                                                                                  
    for sent_pay in  dataset.pay_qs:                                                                                          
        target.append(3)                                                                                          
    for sent_query in dataset.query_qs:                                                                                        
        target.append(2) 
        token_str=nlpEngine.tokenize_removestopword_lemmatize_stem(sent_query)
        vec_arr.append(nlpEngine.text_to_vector(token_str))                                    
    for greet_query in dataset.greet_qs:                                                                                  
        target.append(1)        
        token_str1=nlpEngine.tokenize_removestopword_lemmatize_stem(greet_query)
        vec_greet_arr.append(nlpEngine.text_to_vector(token_str1)) 
                         
    global  txt_cls_model                                                                              
    txt_cls_model = TextCassification.train_model(record, target)
    

def get_txt_classifier_model():    
    return txt_cls_model

def get_query_ans(index):
        return dataset.query_ans[index]
    
def get_greet_ans(index):
        return dataset.greet_ans[index]

def get_query_vectors():
    return vec_arr

def get_greet_vectors():
    return vec_greet_arr

def get_stanford_nlp():
    return stanford_util

train_txt_cls_model()
print("inside chatbot  cache")

# chatbot = ChatBot(
#     'Charlie',
#     trainer='chatterbot.trainers.ListTrainer'
# )
 
#chatbot.train(dataset.chatbot_train_set)






