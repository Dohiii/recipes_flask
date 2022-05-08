from src.recipes import recipes_blueprint
from flask import render_template


@recipes_blueprint.route('/')
def index():
    return render_template('recipes/index.html')
