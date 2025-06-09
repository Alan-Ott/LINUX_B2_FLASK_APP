# /home/apps/myapp.py -> ? Cela ressemble à un copié collé d'un outil de type chatgpt

#!usr/bin/python3 si vous voulez executer le script avec ./myapp.py, autrement cela n'est pas necessaire
from flask import Flask
app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome to flask application'

@app.route('/test')
def test():
    return 'This is test route of myapp flask application'


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)


# Prennez de la place, la lisibilité est essentielle
