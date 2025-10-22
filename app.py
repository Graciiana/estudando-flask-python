from flask import Flask, render_template

#Fazendo pedidos a uma funcao ou variavel global

app = Flask(__name__)
user_glob = None

@app.route("/<nome>")
def home(nome):
    global user_glob
    user_glob = nome
    return (f"Hello {nome}")


@app.route("/teste")
def test():
    return render_template("index.html", user = user_glob)

if __name__ == "__main__":
    app.run(debug=True)