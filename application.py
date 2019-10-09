from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Who are the debit card users?'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
