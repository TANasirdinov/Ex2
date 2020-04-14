from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def gallery():
    gal_file = open("gal.txt", "r", encoding="utf-8")
    gal_list = [row for row in gal_file]
    gal_file.close()
    return render_template('gallery.html', gal_list=gal_list)

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/add-pic", methods=["POST"])
def add_pic():
    picture = request.form.get("picture")
    gal_file = open('gal.txt', 'a+', encoding="utf-8")
    gal_file.write(str(picture) + "\n")
    gal_file.close()
    return render_template("success.html")