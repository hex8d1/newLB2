from bottle import route, run

@route('/')
def hello():
    return "Привет!"

if __name__ == '__main__':
    run(host='localhost', port=8000)