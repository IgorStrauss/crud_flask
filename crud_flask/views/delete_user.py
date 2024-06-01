from flask import redirect, request, url_for

from crud_flask.models.user_ import Phone, User, db


def init_app(app):
    @app.route(
        "/deletar/<int:user_id>", methods=["POST", "GET"], endpoint="deletar_user"
    )
    def delete_user(user_id):
        user_id = User.query.get_or_404(user_id)
        db.session.delete(user_id)
        db.session.commit()
        return redirect(url_for("home", user_id=user_id))

    @app.route(
        "/deletar-telefone/<int:phone_id>",
        methods=["POST"],
        endpoint="deletar_telefone",
    )
    def delete_phone_user(phone_id):
        phone_id = Phone.query.get_or_404(phone_id)
        db.session.delete(phone_id)
        db.session.commit()
        return redirect(url_for("home", phone_id=phone_id))

    return app
