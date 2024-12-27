from flask import Flask, request

app = Flask(__name__)

@app.route('/currency', methods=['GET'])
def currency():
    today_param = request.args.get("today")
    key_value   = request.args.get("key")
    return "USD - 41,5"

if __name__ == "__main__":
    app.run(port=8000)