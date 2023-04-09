from flask import Flask, render_template, request, redirect, url_for
import queue

app = Flask(__name__)
secrets_queue = queue.Queue()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        secret = request.form.get("secret")
        if secret:
            secrets_queue.put(secret)
        return redirect(url_for("display_secret"))
    return render_template("index.html")

@app.route("/display-secret")
def display_secret():
    secret = secrets_queue.get() if not secrets_queue.empty() else None
    return render_template("display_secret.html", secret=secret)

if __name__ == "__main__":
    app.run(debug=True)