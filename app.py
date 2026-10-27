from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def register():
    return render_template("register.html")


@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username", "User")
    return render_template("index.html", name=username)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)