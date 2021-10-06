import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    if flask.request.form.get("campus_id") =="hlee113":
        return flask.redirect("welcome")
    else:
        flask.flash("Wrong campus ID")
        return flask.redirect("/")

@app.route("/welcome")
def welcome():
    return "<h1>Welcome John!</h1>"
app.run()