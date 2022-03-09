#from dojos_and_ninjas import app
#from dojos_and_ninjas.controllers.dojos import Dojo
#from dojos_and_ninjas.controllers.ninjas import Ninja

from flask_app import app
from flask_app.controllers.authors import Author
from flask_app.controllers.books import Book

#from dojo_survey import app
#from dojo_survey.controllers import dojos

#from email_val import app
#from email_val.controllers import emails

#from login_and_reg import app
#from login_and_reg.controllers import users

#from recipes import app
#from recipes.controllers import users
#from recipes.controllers import recipes

if __name__=="__main__":   
    app.run(debug=True)    