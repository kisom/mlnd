import classifier
from flask import Flask, jsonify

app = Flask(__name__)
default_dataset = './smsspamcollection/SMSSpamCollection'
engine = None

def load_engine(dataset=default_dataset):
    global engine
    engine = classifier.Classifier(dataset)
    engine.train()

@app.route('/classify/stats')
def stats():
    if not engine:
        load_engine()
    return jsonify(engine.scores)

@app.route('/classify/string:<text>')
def classify(text):
    if not engine:
        load_engine()
    return jsonify(text=text, result=engine.predict(text))

if __name__ == '__main__':
    load_engine()
