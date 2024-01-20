"""Pet adoption application"""

from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from keys import FLASK_SECRET_KEY
from forms import AddPets, EditPet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///petAdoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = FLASK_SECRET_KEY

# toolbar = DebugToolbarExtension(app)

connect_db(app)
app.app_context().push()
db.create_all()

@app.route('/')
def list_pets():
    pets = Pet.query.order_by(Pet.name).all()
    return render_template("/pet_list.html", pets=pets)

@app.route('/add', methods= ["GET", "POST"])
def add_pet():
    """Adds a new pet"""

    form = AddPets()

    if form.validate_on_submit():
        pet_name = form.pet_name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name = pet_name, species=species, photo_url=photo_url, age=age, notes=notes)

        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    
    else:
        return render_template('/add_pet.html', form=form)
    
@app.route('/<int:pet_id>', methods= ["GET", "POST"])
def edit_pet(pet_id):
    """Edit a pet"""

    pet = Pet.query.get_or_404(pet_id)  
    form = EditPet(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        return redirect('/')
    
    else:
        return render_template ('pet_edit.html', pet=pet, form=form)
