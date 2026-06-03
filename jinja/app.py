from flask import Flask, request, render_template_string,render_template


app = Flask(__name__)

def show_the_login_form():
    return render_template_string("""
        <h2>Login</h2>
        <form method="POST">
            <input type="text" name="usuario" placeholder="Usuário"><br><br>
            <input type="password" name="senha" placeholder="Senha"><br><br>
            <button type="submit">Entrar</button>
        </form>
    """)

def do_the_login():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    if usuario == 'admin' and senha == '123':
        return f"<h1>Bem-vindo, {usuario}!</h1>"
    else:
        return "<h1>Login inválido</h1>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
    
@app.route('/aluno', methods=['GET', 'POST'])
def aluno():
   
    usuario_dados = {"nome": "Ana", "email": "ana@email.com"}
    
    lista_alunos = [
        {"nome": "Ana", "nota": 8.5},
        {"nome": "Carlos", "nota": 6.0},
        {"nome": "Bruno", "nota": 7.0},
        {"nome": "Amanda", "nota": 5.5}
    ]

    return render_template(
        'aluno.html', 
        alunos=lista_alunos, 
        nome="Ana",      
        idade=17,          
        usuario=usuario_dados 
    )

if __name__ == "__main__":
    app.run(debug=True)

# site de consulta https://flask.palletsprojects.com/en/stable/quickstart/#html-escaping