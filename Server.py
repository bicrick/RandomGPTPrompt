import pandas as pd
import random
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

df = pd.read_csv("prompts.csv")
a_list = df['act'].values.tolist()
b_list = df['prompt'].values.tolist()
purpose = random.choice(a_list)
prompt = random.choice(b_list)
print(purpose + ": " + prompt)


port = int(os.environ.get("PORT",5000))
app = Flask(__name__)
CORS(app)

def RandomPrompt():
    purpose = random.choice(a_list)
    prompt = random.choice(b_list)

    return [purpose,prompt]

@app.route("/")
def sendJSON():
    response = RandomPrompt()
    return jsonify({"message": response})

@app.route('/home')
def home():
    return "This is a test"
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port) 

