from flask import Flask, render_template, jsonify
from chatGPTYapper2000.chatGptYapper2000 import yap

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listen', methods=['POST'])
def listen():
    response_text = yap()
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=True)