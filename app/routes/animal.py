from flask import Blueprint, render_template, request, redirect

from ..forms import AnimalForm
from ..extensions import db
from ..models.animal import Animal
from flask_login import login_required

animal = Blueprint('animal', __name__)

@animal.route('/', methods=['POST','GET'])
def all():
        animal = Animal.query.order_by(Animal.id).all()
        return render_template('animals/all.html',animal=animal)

@animal.route('/animal/create')
@login_required
def create():
    form = AnimalForm()
    if request.method == 'POST':
        Ind_or_group = request.form.get('Ind_or_group')
        AnimalSpecies = request.form.get('AnimalSpecies')
        AnimalBreed = request.form.get('AnimalBreed')
        AnimalColour = request.form.get("AnimalColour")
        AnimalGender = request.form.get("AnimalGender")
        Measure = request.form.get("Measure")
        ComplexDate = request.form.get("ComplexDate")
        AnimalKeepingLocation = request.form.get("AnimalKeepingLocation")

        animal = Animal(Ind_or_group=Ind_or_group,
                        AnimalSpecies=AnimalSpecies,
                        AnimalBreed=AnimalBreed,
                        AnimalColour=AnimalColour,
                        AnimalGender=AnimalGender,
                        Measure=Measure,
                        ComplexDate = ComplexDate,
                        AnimalKeepingLocation=AnimalKeepingLocation,
                        )

        try:
            db.session.add(animal)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(str(e))
    else:
        return render_template('animals/create.html', form=form)

@animal.route('//<int:id>/update', methods=['POST', 'GET'])
@login_required
def update(id):
    animal = Animal.query.get(id)
    if request.method =='POST':
        # post.teacher = request.form.get('teacher')
        # post.subject = request.form.get('subject')
        # post.student = request.form.get('stu')

        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(str(e))
    else:
        return render_template('animals/update.html', animal=animal)


@animal.route('/animal/<int:id>/delete', methods=['POST', 'GET'])
@login_required
def delete(id):
    animal = Animal.query.get(id)
    try:
            db.session.delete(animal)
            db.session.commit()
            return redirect('/')
    except Exception as e:
            print(str(e))
            return str(e)