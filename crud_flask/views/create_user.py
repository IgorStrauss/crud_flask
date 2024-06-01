from flask import flash, redirect, render_template, url_for

from crud_flask.forms.user_form import UserForm
from crud_flask.models.user_ import Phone, User, db


def init_app(app):
    @app.route("/cadastrar", methods=["GET", "POST"], endpoint="cadastrar")
    def create_user():
        """Metodo para cadastro de usuário incluindo o telefone"""
        form = UserForm()
        if form.validate_on_submit():
            new_user = User(
                Firstname=form.Firstname.data.upper(),
                Lastname=form.Lastname.data.upper(),
                Email=form.Email.data.upper(),
            )
            try:
                db.session.add(new_user)
                db.session.flush()
                new_phone = Phone(Cellphone=form.Phone.data, User_id=new_user.Id)
                db.session.add(new_phone)
                db.session.commit()
                flash(
                    "Usário(a) cadastrado(a) com sucesso!",
                    "success",
                )
                return redirect(url_for("home"))

            except Exception as e:
                if {e.args[0]} == "UNIQUE constraint failed: user.Email":
                    ...
                flash(
                    f"Erro ao cadastrar usuário, o Email {form.Email.data} já existe!",
                    "error",
                )
                return render_template("crud/create.html", form=form)
        return render_template("crud/create.html", form=form)

    return app
