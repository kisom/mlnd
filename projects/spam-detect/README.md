# SMS spam detection service

This is a [Flask](https://flask.pocoo.org) app to run a simple microservice
for classifying text messages as spam or not. It is built on the SMS Spam
Collection v.1 (found in `smsspamcollection/`), and presents two endpoints
to users:

1. GET /classify/stats
2. POST /classify/check

The stats endpoint returns the number of unique messages that have been
classified so far as well as the training scores for the model. The
classifier uses multinomial naive Bayes trained on the data set to build
its predictive model.

To run, call `./run.sh`. Setting the `HOST` and `PORT` environment variables
will change the listening address and port, which defaults to
`127.0.0.1:5000`.

For example:

```
$ curl -X POST -F "text=this is a new text" http://127.0.0.1:5000/classify/check
{
  "result": false,
  "text": "this is a new text"
}
$ curl -X POST -F "text=Free entry in 2 a wkly comp to win" http://127.0.0.1:5000/classify/check
{
  "result": true,
  "text": "Free entry in 2 a wkly comp to win"
}
$ curl http://127.0.0.1:5000/classify/stats
{
  "messages": {
    "ham": 1,
    "spam": 1
  },
  "scores": {
    "accuracy": 0.98851399856424982,
    "f1": 0.9560439560439562,
    "precision": 0.97206703910614523,
    "recall": 0.94054054054054059
  }
```

