from bottle import route, run, request

@route('/', method='GET')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    run(host='localhost', port=8000)
