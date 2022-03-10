from flask import Flask, request

app: Flask = Flask(__name__)


@app.route("/greeting", methods=["GET"])
def hello_world():
    return "Hello world!"

@app.route("/personal/<name>", methods=["GET"])
def personal_greeting(name: str):
    return f"Hello {name}!"

@app.route("/add/<num_one>/<num_two>", method=["GET"])
def addition_function(num_one: str, num_two: str):
    result =int(num_one) + int(num_two)
    return str(result)

@app.route("/list/<index>", methods=["GET"])
def get_phrase_from_list(index: str):
    global list
    return my_list[int(index)]

@app.route("/list", methods=["POST"])
def add_phrase_to_list():
    request_content = request.get_json()
    global = my_list
    my_list.append(request_content["key"])
    return "Phrase added sucessfully"
