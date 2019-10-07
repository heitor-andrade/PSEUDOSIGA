from flask import Flask, request, render_template, redirect
app = Flask(__name__)
import sqlite3
connection = sqlite3.connect('tabela.db')


#cursor.execute('CREATE TABLE user (id INTEGER PRIMARY KEY, usuário Text Not Null, senha INTEGER Not Null)')

@app.route("/")
def bkbbbbb():
    return render_template('Inicio.html')

@app.route("/logar", methods=['POST'])
def echo():
    global user
    global senha
    user = str(request.form["user"])
    senha = int(request.form["senha"])
    
    with sqlite3.connect('tabela.db') as connection:
        cursor = connection.cursor()
        find_user = ("SELECT * FROM users WHERE usuário = ? AND senha = ?")
        cursor.execute(find_user, (user, senha))
        results = cursor.fetchall()
           
    if results:
        for i in results:
            return 'bem vindo ' + user
    else: 
        return 'Usuário ou Senha incorretos.'
    
    

@app.route("/cadastrar", methods=['POST'])
def cadastrar():
    return render_template('cadastrar.html')


@app.route("/guardarcadastro", methods=['POST'])
def aprovado():
    with sqlite3.connect('tabela.db') as connection:
        cursor = connection.cursor()
        user = str(request.form["user"])
        senha = int(request.form["senha"])
        cursor.execute('INSERT INTO users(usuário, senha) VALUES(?, ?)', (user, senha))
        connection.commit()
    return redirect("/")    

@app.route("/provafinal", methods=['POST'])
def echo1():
    p3 = int(request.form["p3"])
    if ((2*p3+p1+p2)/4 < 5):
        return render_template('reprovado.html')
    else:
        return render_template('aprovado.html', algumagamejam = (2*p3+p1+p2)/4)

@app.route("/reprovado", methods=['POST'])
def echo2():
    return render_template('reprovado.html')

if __name__ == "__main__":
    app.run(debug=True)
