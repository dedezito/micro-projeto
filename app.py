from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return 'hello to biblioteca'
@app.route('/livros')
def livros():
    return 'O Senhor dos Anéis, O Pequeno Príncipe, Harry Potter e a Pedra Filosofal, O Hobbit...'
app.run()