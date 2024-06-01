from flask import render_template, request

from crud_flask.models.user_ import User, db


def init_app(app):
    @app.route("/", methods=["GET"], endpoint="home")
    def index():
        """Metodo renderizando a tabela de usuários com paginação"""
        Users = db.session.query(User).all()

        page = request.args.get("page", 1, type=int)
        per_page = 2
        start = (page - 1) * per_page
        end = start + per_page
        total_pages = (len(Users) - 1) // per_page + 1
        itens_on_page = Users[start:end]

        return (
            render_template(
                "crud/index.html",
                total_pages=total_pages,
                itens_on_page=itens_on_page,
                page=page,
            ),
            200,
        )
