from flask import Flask, render_template

import feedparser

app = Flask(__name__)

BBC_FEED = {'bbc':'http://feeds.bbci.co.uk/news/rss.xml',
            'cnn': 'http://rss.cnn.com/rss/edition.rss',
            'fox': 'http://feeds.foxnews.com/foxnews/latest',
            'iol': 'http://www.iol.co.za/cmlink/1.640'}

@app.route('/')
@app.route('/<origin>')
def get_news(origin):
    feed = feedparser.parse(BBC_FEED[origin])
    return render_template("home.html", context=feed['entries'])

if __name__ == '__main__':
    app.run(port=5000, debug=True)