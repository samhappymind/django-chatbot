import chatbot.TextCassification as txt_cls
from chatbot import nlpEngine
from chatbot import cache
from chatbot.cache import vec_arr
from chatbot import dataset

stanford_nlp = cache.get_stanford_nlp()
cos_tokens = [] 
def getBotResponse(model, query):
    response_obj = None
    response = txt_cls.test_model(model, [query])
    if response == 3:
        print(" payment query")
        person,amount=stanford_nlp.parse_payment_query(query)
        
        if person==None:
            if amount==None:
                response_obj=dataset.payment_response_data
            else:
                response_obj={"type":dataset.payment_response_data["type"],"data":[dataset.payment_response_data['data'][0],dataset.payment_response_data['data'][2],dataset.payment_response_data['data'][3]]}
                response_obj["amount"]=amount
                response_obj["payee"]=""
        else:
            if amount==None:
                response_obj={"type":dataset.payment_response_data["type"],"data":[dataset.payment_response_data['data'][1],dataset.payment_response_data['data'][2],dataset.payment_response_data['data'][3]]}
                response_obj["amount"]=""
                response_obj["payee"]=person
            else:
                data=dataset.payment_response_data['data'][3]
                response_obj={"type":dataset.payment_response_data["type"],"payee":person,"amount":amount,"data":[dataset.payment_response_data['data'][2],data]}
      
    elif response == 2: 
        print("details  query")      
        vec_arr = cache.get_query_vectors()
        cosval_indx,cosval=nlpEngine.get_highest_cosval_index(vec_arr,query)       
        ans = cache.get_query_ans(cosval_indx)
        response_obj = None
        print(" answer =>",ans)
        
        if " T" in ans:
            response_obj = dataset.query_response_data
            response_obj["type"]="4"
            response_obj["api"]="Transaction"
            response_obj["params"]="datepicker"
            response_obj["answer"]=ans
        else:
            response_obj={
                        "type": 2,
                        "api":"getUserBalance?username=",
                        "params":"any",
                        "answer":ans,
                        "data": [ dataset.query_response_data['data'][1] ,dataset.query_response_data['data'][2]]                       
                         } 
        
    else:
        print("greet query")
        vec_greet_arr = cache.get_greet_vectors()
        cosval_indx,cosval=nlpEngine.get_highest_cosval_index(vec_greet_arr,query)
        if(cosval < 0.5): 
            print(cosval) 
            response_obj = {"type": -1, "data" :"Please ask relevant questions"} 
        else:       
            ans = cache.get_greet_ans(cosval_indx) 
            print(ans)        
            response_obj = {"type": 1, "data" :str (ans)}  

    return response_obj

user1 = [{
        "acnumber" :"093423424",
        "availbalance":"4,454.54",
        "lasttransac":[{
                            "date":"23/2/2018",
                            "accountdetails" :"UPI/808509781053/raju",
                            "amount":"2,383.00",
                            "drorcr":"cr"
                              }],
        "detailedstatement":"",
        "moreoptions":""
        }
        ]   
user2 = [{
        "acnumber" :"876767867",
        "availbalance":"7,454.54",
        "lasttransac":[{
                            "date":"27/2/2018",
                            "accountdetails" :"UPI/808509781053/raju",
                            "amount":"2,383.00",
                            "drorcr":"cr"
                              }],
        "detailedstatement":"",
        "moreoptions":""
        }
        ]  
def getAccountInfo(query):
    if query == "samrat@gmail.com":
        return user1
    else:
        return user2

