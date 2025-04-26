from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Heyy ,Devops!'

if __name__ == '__main__':
    app.run()

