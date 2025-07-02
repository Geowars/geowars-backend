
from flask import Flask
from generate_token_news import generate_all_token_news

app = Flask(__name__)

@app.route('/update')
def update_news():
    generate_all_token_news()
    return "News updated successfully", 200
