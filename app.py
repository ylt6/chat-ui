from flask import Flask, render_template, request
import openai
import os
import sys

api_key = os.environ.get('OPENAI_API_KEY')
if api_key is None:
    print("Error: OPENAI_API_KEY environment variable is not set.")
    sys.exit(1) 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-response", methods=["POST"])
def get_response():
    prompt = request.form["prompt"]
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},        
    ])
    print(response)
    # logging
    response_msg = ''
    if (choices := response.get('choices')):
        if choices:
            response_msg = choices[0]['message']['content']
    
    return response_msg

if __name__ == "__main__":
    app.run(debug=True)
