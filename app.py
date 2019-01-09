import os
import json
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "randomstring323"

@app.route("/", methods=["GET", "POST"])

def question():
    data = []
    with open("data/quiz.json", "r") as json_data:
        data = json.load(json_data)
        return render_template('question1.html', quiz=data)
        
@app.route('/capitals', methods=['POST'])
def capitals():
        answer = request.form["capitals"]
        if answer == "Paris":
            return render_template('welcome.html') 
        else:
            return "<h4>is not correct, guess again.</h4>" 
    
@app.route('/welcome', methods=['POST'])
def welcome(request):
    return render_template('index.html')    
    
if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
          port=int(os.environ.get('PORT')),
          debug=True)