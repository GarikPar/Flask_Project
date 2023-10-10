from flask import Flask, render_template

app = Flask("_ _name_ _")
menu = ["Download","Using","Makeing first project"]
dw = ["pip install flask", "from flask import Flask"]
using = ["first of all app = Flask(_ _name_ _)","after move above start to make app routes","simplest one is @app.route() decorator"]
project = ["Under @app.route() decorators write def functions"," functions should return what you want that your pages include"]

@app.route("/")
def main():
    return render_template('main.html', title = "Main")

@app.route("/introduction")
def index():
    return render_template('index.html', title = "Introduction", menu = menu)

@app.route("/download")
def second():
    return render_template('index.html', title="Download", menu = dw)

@app.route("/using")
def third():
    return render_template('index.html', title="Using", menu = using)

@app.route("/first project")
def forth():
    return render_template('index.html', title="First project", menu = project)

if __name__ == "__main__":
    app.run(debug=True)