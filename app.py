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

@app.route("/materialen")
def materialen():
    data = get_data.getData("reciperevolutiondb","materialen")
    return render_template("materialen.html",data = data)

@app.route("/chooseIngredient")
def chooseIngredient():
    data = get_data.getData("reciperevolutiondb","ingrediënten")
    return render_template("chooseIngredient.html",data = data)

@app.route("/chooseRecipeIngredient")
def chooseRecipeIngredient():
    data = get_data.getData("reciperevolutiondb","recepten_ingrediënten")
    return render_template("chooseRecipeIngredient.html",data = data)

@app.route("/categorieën")
def categorieën():
    data = get_data.getData("reciperevolutiondb","categorieën")
    return render_template("categorieën.html",data = data)

@app.route("/recepten_materialen")
def recepten_materialen():
    data = get_data.getData("reciperevolutiondb","recepten_materialen")
    return render_template("recepten_materialen.html",data = data)


if __name__ == '__main__':
    app.run()