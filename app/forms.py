from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.fields.datetime import DateField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from datetime import date

from .models.users import User

from .models.dictionaries import Dictionary


class RegistrationForm(FlaskForm):
    name = StringField('ФИО', validators=[DataRequired(), Length(min=2, max=100)])
    login = StringField('Логин', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

    def validate_login(self, login):
        user = User.query.filter_by(login=login.data).first()
        if user:
            raise ValidationError('Данное имя пользователя уже занято. Пожалуйста, выберите другое...')


class LoginForm(FlaskForm):
    """Form to log in users"""
    login = StringField('Логин', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class AnimalForm(FlaskForm):
    AnimalKeepingLocation = StringField('Место рождения', validators=[DataRequired(), Length(min=2, max=20)])
    Ind_or_group = SelectField('Индивидуальный или групповой метод', choices=Dictionary.i_g, render_kw={'class': 'form-control'})
    AnimalSpecies = SelectField('Вид животного', choices=Dictionary.animal_species, render_kw={'class': 'form-control'})
    AnimalBreed = SelectField('Порода животного', choices=Dictionary.breed, render_kw={'class': 'form-control'})
    AnimalColour = SelectField('Масть\Окрас', choices=Dictionary.colour, render_kw={'class': 'form-control'})
    AnimalGender = SelectField('Пол животного', choices=Dictionary.gender, render_kw={'class': 'form-control'})
    Measure = IntegerField('Вес животного')
    ComplexDate = DateField('Дата Рождения',default=date.today)
