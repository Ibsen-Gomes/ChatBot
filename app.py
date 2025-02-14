from flask import Flask, render_template, request, jsonify
from bot import ChatbotPTBR

app = Flask(__name__)
chatbot = ChatbotPTBR()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_bot_response():
    user_input = request.json["message"]
    response = chatbot.get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
