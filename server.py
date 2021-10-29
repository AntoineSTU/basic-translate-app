from flask import Flask, request, jsonify
from translate import Translator

app = Flask(__name__)

translator = Translator()

@app.route("/hello-world", methods=['GET'])
def hello_world():
    return "Hello World", 200

@app.route("/translate", methods=['POST'])
def translate():
    try:
        content = request.json
        text = content["text"]
        lang = content["lang"] if "lang" in content else "fra"
        translations = translator.translate(text, to=lang)
        return jsonify({"translations": translations})
    except:
        return "Internal server error", 500