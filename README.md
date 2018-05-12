# django-chatbot
this is a payment service bot application implemented for wallet apps

Install Python 3.6 ,Anaconda 3.5.0.1
download stanford Core NLP server

start the core nlp server 
java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file input.txt

start django server 
python manage.py runserver 0.0.0.0:8000

and voila hit the request urls
 http://localhost:8000/chatbot?query='<type your query'>
 
This django bot serves payment requests/ fetches balance related info for your wallet and do general greetings
It is combined with business api's which are NON DISCLOSED and are triggered from android App



