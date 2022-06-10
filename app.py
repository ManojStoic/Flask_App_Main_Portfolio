from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def test_page():
    return render_template("index.html")

@app.route("/<string:pagename>")
def dynamic_page(pagename=None):
    return render_template(pagename)

if __name__ == "__main__":
    app.run()