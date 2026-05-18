from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
 return render_template('home.html')

@app.route('/')
def sobre(nome):
 return f'Olá {nome}! Seja bem vindo.'

if __name__ == "__main__":
  app.run(debug=True)
 
