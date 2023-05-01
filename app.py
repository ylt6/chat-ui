from flask import Flask, render_template, request
import openai
import os
import sys

from dotenv import find_dotenv, load_dotenv

_ = load_dotenv(find_dotenv())

if (api_key := os.getenv("OPENAI_API_KEY")) is None:
    print("Error: OPENAI_API_KEY environment variable is not set.")
    sys.exit(1)

openai.api_key = api_key

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get-response", methods=["POST"])
def get_response():
    response = get_completion(request.form["prompt"])
    # logging
    response_msg = ""
    if choices := response.get("choices"):
        if choices:
            response_msg = choices[0]["message"]["content"]

    return response_msg


def get_completion(prompt, model="gpt-3.5-turbo"):
    return openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt},
        ],
    )


if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))
