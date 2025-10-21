from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.post("/teste/<user>")
def teste():
    return request.form.get("teste")
if __name__ == "__main__":
    app.run(debug=True)