from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "<h1 style='color:green'>Greetings!</h1><br><h2>Welcome to my Flask App!</h2>\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)