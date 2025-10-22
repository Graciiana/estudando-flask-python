from flask import Flask, request, redirect, render_template

app = Flask(__name__)
lista:list[str]=[]

@app.route("/")
def home():
    return render_template("index.html", tarefas = lista)
    
@app.post("/teste")
def teste():
    titulo = request.form.get("ad_tarefa")
    lista.append(titulo)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)