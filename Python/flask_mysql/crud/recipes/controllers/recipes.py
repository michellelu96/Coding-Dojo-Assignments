from flask import render_template,redirect,session,request, flash
from recipes import app
from recipes.models.user import User
from recipes.models.recipe import Recipe

#show recipe info!
@app.route('/recipes/<int:id>')
def show_recipe(id):
    data = {
        'id':id
    }
    user_data={
        'id':session['user_id']
    }
    return render_template("recipes_name.html",recipe=Recipe.get_one(data),user_info=User.get_by_id(user_data))

#new recipes page
@app.route('/recipe/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id':session['user_id']
    }
    return render_template("new_recipes.html",user=User.get_by_id(data))

#create new recipe
@app.route('/recipe/create',methods =['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipe/new')
    data = {
        'name':request.form['name'],
        "description":request.form['description'],
        "instructions":request.form['instructions'],
        "under30":request.form['under30'],
        "date_made":request.form['date_made'],
        "user_id":request.form['user_id']
    }
    Recipe.save_recipe(data)
    return redirect('/success')

    #edit recipes
@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id':id
    }
    return render_template("edit_recipes.html",recipe=Recipe.get_one(data))

#update the recipe
@app.route('/recipes/update',methods=['POST'])
def update_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect('new/recipe')
    data = {
        'name':request.form['name'],
        "description":request.form['description'],
        "instructions":request.form['instructions'],
        "under30":request.form['under30'],
        "date_made":request.form['date_made'],
        "user_id":request.form['user_id']
    }
    Recipe.update(data)
    return redirect ('/dashboard')

#destroy the recipe
@app.route('/recipe/destroy/<int:id>')
def destroy_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Recipe.destroy(data)
    return redirect('/success')
    
