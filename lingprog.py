from flask import Flask, request, render_template, redirect
app = Flask(__name__)
import sqlite3
connection = sqlite3.connect('tabela.db')

#cursor.execute('CREATE TABLE user (id INTEGER PRIMARY KEY, usuário Text Not Null, senha INTEGER Not Null)')
cursor = connection.cursor()
#cursor.execute('CREATE TABLE disciplinas (id INTEGER PRIMARY KEY,disciplina TEXT NOT NULL,codigo TEXT NOT NULL)')
@app.route("/")
def bkbbbbb():
    return render_template('Inicio.html')

@app.route("/logar", methods=['POST'])
def echo():
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

@app.route("/disciplina", methods=['POST'])
def disciplinar():
    return render_template('disciplina.html')


@app.route("/guardarcadastro", methods=['POST'])
def aprovado():
    with sqlite3.connect('tabela.db') as connection:
        cursor = connection.cursor()
        user = str(request.form["user"])
        senha = int(request.form["senha"])
        cursor.execute('INSERT INTO users(usuário, senha) VALUES(?, ?)', (user, senha))
        connection.commit()
    return redirect("/")    

@app.route("/guardardisciplina", methods=['POST'])
def cadisciplina():
    with sqlite3.connect('tabela.db') as connection:
        cursor = connection.cursor()
        materia = str(request.form["materia"])
        codigo = str(request.form["codigo"])
        cursor.execute('INSERT INTO disciplinas (disciplina, codigo) VALUES(?, ?)', (materia, codigo))
        connection.commit()
    return redirect("/")            


if __name__ == "__main__":
    app.run(debug=True)