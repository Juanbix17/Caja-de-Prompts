from flask import Flask, render_template, request, redirect

app = Flask(__name__)

comentarios = []

@app.route("/", methods=["GET", "POST"])
def inicio():

    if request.method == "POST":
        texto = request.form["texto"]
        comentarios.append(texto)

    return render_template("index.html", comentarios=comentarios)


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    if request.method == "POST":
        comentarios[id] = request.form["texto"]
        return redirect("/")

    return render_template("editar.html", texto=comentarios[id], id=id)


app.run(debug=True)

