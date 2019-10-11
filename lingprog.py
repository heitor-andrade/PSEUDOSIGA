from flask import Flask, request, render_template, redirect
app = Flask(__name__)
import sqlite3
connection = sqlite3.connect('tabela.db')

cursor = connection.cursor()
#cursor.execute('CREATE TABLE user (id INTEGER PRIMARY KEY, usuário Text Not Null, senha INTEGER Not Null)')
#cursor.execute('CREATE TABLE disciplinas (id INTEGER PRIMARY KEY,disciplina TEXT NOT NULL,codigo TEXT NOT NULL)')
#cursor.execute('CREATE TABLE inscricao (id INTEGER PRIMARY KEY, disciplina TEXT NOT NULL, alunos VARCHAR)')
#cursor.execute('ALTER TABLE disciplinas ADD alunos VARCHAR')
#cursor.execute('DELETE TABLE user')
#cursor.execute('ALTER TABLE disciplinas ADD idAlunos FOREIGN KEY (alunos) REFERENCES users(id)')

@app.route("/")
def template_inicio():
    return render_template('Inicio.html')

@app.route("/logar", methods=['POST'])
def template_logar():
    return render_template('logar.html')


@app.route("/cadastrar", methods=['POST'])
def template_cadastrar():
    return render_template('cadastrar.html')

@app.route("/disciplina", methods=['POST'])
def template_disciplina():
    return render_template('disciplina.html')

@app.route("/inscricao", methods=['POST'])
def template_inscricao():
    return render_template('inscricao.html')

@app.route("/guardarcadastro", methods=['POST'])
def cadastar_aluno():
    with sqlite3.connect('tabela.db') as connection:
        cursor = connection.cursor()
        user = str(request.form["user"])
        senha = int(request.form["senha"])
        cursor.execute('INSERT INTO users(usuário, senha) VALUES(?, ?)', (user, senha))
        connection.commit()
    return redirect("/")    

@app.route("/guardardisciplina", methods=['POST'])
def guardar_disciplina():
    with sqlite3.connect('tabela.db') as connection:
        cursor = connection.cursor()
        materia = str(request.form["materia"])
        codigo = str(request.form["codigo"])
        cursor.execute('INSERT INTO disciplinas (disciplina, codigo) VALUES(?, ?)', (materia, codigo))
        connection.commit()
    return redirect("/")


@app.route("/guardarlogin", methods=['POST'])
def logando():
    global user
    user = str(request.form["user"])
    senha = int(request.form["senha"])
    
    with sqlite3.connect('tabela.db') as connection:
        cursor = connection.cursor()
        find_user = ("SELECT * FROM users WHERE usuário = ? AND senha = ?")
        cursor.execute(find_user, (user, senha))
        results = cursor.fetchall()
           
    if results:
        for i in results:
            return render_template('disciplina.html')
    else:
        return 'deu ruim'

@app.route("/guardarinscricao", methods=['POST'])
def inscricao():
    try:
        with sqlite3.connect('tabela.db') as connection:
            disciplina = str(request.form["disciplina"])
            cursor = connection.cursor()
            update_disciplina = ("UPDATE disciplinas SET alunos = ? WHERE disciplina = ?")
            cursor.execute(update_disciplina, (user, disciplina))
            connection.commit()
        return redirect("/")
    except:
        return 'falha em se inscrever'
            


if __name__ == "__main__":
    app.run(debug=True)