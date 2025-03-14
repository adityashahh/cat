from flask import Flask, request, render_template
from textblob import TextBlob

app = Flask(__name__)

# Sentiment analysis function
def analyze_sentiment(text):
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment > 0:
        return "Happy 😀"
    elif sentiment < 0:
        return "Sad 😢"
    else:
        return "Neutral 😐"

# Homepage route
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form["text"]
        result = analyze_sentiment(text)  # Use our function
        return render_template("index.html", result=result)
    return render_template("index.html", result="")

if __name__ == "__main__":
    app.run(debug=True)
