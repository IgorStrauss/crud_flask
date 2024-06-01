from flask import render_template

from crud_flask.models.user_ import User


def init_app(app):
    @app.route("/perfil/<int:user_id>", methods=["POST", "GET"], endpoint="perfil_user")
    def profile_user(user_id):
        """Função para mostrar perfil de usuário"""
        user = User.query.get_or_404(user_id)
        return render_template("crud/detail.html", user=user)
