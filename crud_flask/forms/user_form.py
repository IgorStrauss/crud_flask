from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError


def ValidatePhone(form, field):
    if not field.data.isdigit():
        raise ValidationError("Celular deve conter apenas números")

    if len(field.data) != 11:
        raise ValueError("Celular deve ter 11 digitos")


class UserForm(FlaskForm):
    Firstname = StringField("Nome", validators=[DataRequired(), Length(min=4, max=35)])
    Lastname = StringField(
        "Sobrenome", validators=[DataRequired(), Length(min=4, max=35)]
    )
    Email = StringField(
        "Email (email@email.com)",
        validators=[
            DataRequired(),
            Email(message="Endereço de email inválido"),
            Length(max=50),
        ],
    )
    Phone = StringField(
        "Celular (Somente Números)",
        validators=[DataRequired(), Length(min=11, max=11), ValidatePhone],
    )
    Submit = SubmitField("Enviar")


class UpdateUserForm(FlaskForm):
    Firstname = StringField("Nome", validators=[DataRequired(), Length(min=4, max=35)])
    Lastname = StringField(
        "Sobrenome", validators=[DataRequired(), Length(min=4, max=35)]
    )
    Email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(message="Endereço de email inválido"),
            Length(max=50),
        ],
    )
    Phone = StringField(
        "Celular", validators=[DataRequired(), Length(min=11, max=11), ValidatePhone]
    )
    Submit = SubmitField("Enviar")
