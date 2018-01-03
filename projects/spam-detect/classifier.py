import pandas
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

class Classifier:

    def __init__(self, path):
        df = pandas.read_csv(path, sep='\t', header=None, names=['label', 'text'])
        df['label'] = df.label.map({'ham':0, 'spam':1})
        self.frame = df
    
        self.cv = CountVectorizer()
        self.naive_bayes = MultinomialNB()

    def reset(self):
        self.cv = CountVectorizer()
        self.naive_bayes = MultinomialNB()        

    def train(self):
        x_train, x_test, y_train, y_test = train_test_split(self.frame['text'],
                                                            self.frame['label'],
                                                            random_state=1)
        training_data = self.cv.fit_transform(x_train)
        testing_data = self.cv.transform(x_test)
        
        self.naive_bayes.fit(training_data, y_train)        
        predictions = self.naive_bayes.predict(testing_data)
        self.scores = {
            'accuracy': accuracy_score(y_test, predictions),
            'precision': precision_score(y_test, predictions),
            'recall': recall_score(y_test, predictions),
            'f1': f1_score(y_test, predictions),
	}

    def classify(self, text):
        # this doesn't work --- why not?
        matrix = self.cv.transform(text)
        prediction = self.naive_bayes.predict(matrix)
        print(prediction)
        if prediction[0] == 1:
            return True
        return False
