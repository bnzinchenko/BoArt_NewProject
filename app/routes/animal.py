from flask import Blueprint, render_template, request, redirect
from ..extensions import db
from ..models.animal import Animal
from flask_login import login_required

animal = Blueprint('animal', __name__)

@animal.route('/', methods=['POST','GET'])
def all():
        animal = Animal.query.order_by(Animal.id).all()
        return render_template('animals/all.html',animal=animal)

@animal.route('/animal/<int:id>')
@login_required
def create_animal(id):
    animal = Animal(id=id)
    db.session.add(animal)
    db.session.commit()
    return "Animal created Successflully"

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