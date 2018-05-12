
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB


count_vect = CountVectorizer()
tfidf_transformer = TfidfTransformer()


def train_model(record_lst,target):
    X_train_counts = count_vect.fit_transform(record_lst)
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
    clf = MultinomialNB().fit(X_train_tfidf, target)
    return clf
  
  
def test_model(clf,docs_new):   
    X_new_counts = count_vect.transform(docs_new)
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)
    predicted = clf.predict(X_new_tfidf)  
    return predicted 

    