import classifier
from flask import Flask, jsonify, request

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
    stats = {
            'scores': engine.scores.copy(),
            'messages': engine.stats.copy(),
    }
    return jsonify(stats)

@app.route('/classify/check', methods=['POST'])
def classify():
    if not engine:
        load_engine()
    text = request.form['text']
    return jsonify(text=text, result=engine.classify([text]))

if __name__ == '__main__':
    load_engine()
