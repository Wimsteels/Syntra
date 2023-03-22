from flask import Flask, render_template, request
from sql import get_data

app = Flask(__name__)
app.template_folder = 'templates'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addRecipe")
def addRecipe():
    return render_template("addRecipe.html")

@app.route("/chooseRecipe")
def chooseRecipe():
    data = get_data.getData("reciperevolutiondb","recepten")
    return render_template("chooseRecipe.html",data = data)

if __name__ == '__main__':
    app.run()