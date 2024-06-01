from flask import flash, redirect, render_template, url_for

from crud_flask.forms.user_form import UpdateUserForm
from crud_flask.models.user_ import User, db


def init_app(app):
    @app.route("/editar/<int:user_id>", methods=["POST", "GET"], endpoint="editar_user")
    def edit_user(user_id):
        """Função para editar dados do usúario e telefone"""
        form = UpdateUserForm()
        user = User.query.get_or_404(user_id)
        phone = user.Phone_user
        if form.validate_on_submit():
            if form.Firstname.data:
                user.Firstname = form.Firstname.data
            if form.Lastname.data:
                user.Lastname = form.Lastname.data
            if form.Email.data:
                user.Email = form.Email.data
            if form.Phone.data:
                phone.Cellphone = form.Phone.data
            db.session.commit()
            flash("Usário(a) editado(a) com sucesso!", "success")
            return redirect(url_for("home"))
        return render_template("crud/update.html", form=form, user=user)

    return app
