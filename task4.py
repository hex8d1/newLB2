from flask import Flask, request

app = Flask(__name__)

@app.route('/content', methods=['GET'])
def content_type_handler():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        return '{"message": "This is JSON"}', 200, {'Content-Type': 'application/json'}
    elif content_type == 'application/xml':
        return '<message>This is XML</message>', 200, {'Content-Type': 'application/xml'}
    else:
        return 'Text', 200, {'Content-Type': 'text/plain'}

if __name__ == "__main__":
    app.run(port=8000)
