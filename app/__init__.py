from flask import Flask, render_template, request, redirect, url_for, session

from werkzeug.security import generate_password_hash, check_password_hash

from app.database.database import db

def create_app():

    app = Flask(__name__)

    app.config["SECRET_KEY"] = "unimanager-chave-secreta"

    #Configuração do banco de dados
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///unimanager.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    #Inicializa o banco
    db.init_app(app)

    #Importa o modelo
    from app.models.usuario import Usuario

    #Cria as tabelas
    with app.app_context():
        db.create_all()

    #LOGIN

    @app.route("/", methods=["GET", "POST"])
    def home():

        mensagem = None

        if request.method == "POST":

            email = request.form.get("email")
            senha = request.form.get("senha")

            usuario = Usuario.query.filter_by(email=email).first()

            if usuario and check_password_hash(usuario.senha, senha):

                return redirect(url_for("dashboard"))

            else:

                mensagem = "❌ Email ou senha inválidos."

        return render_template(
            "login.html",
            mensagem=mensagem
        )

    #DASHBOARD

    @app.route("/dashboard")
    def dashboard():

        return render_template("dashboard.html")


    #CADASTRO

    @app.route("/cadastro", methods=["GET", "POST"])
    def cadastro():

        mensagem = None

        if request.method == "POST":

            nome = request.form.get("nome")
            email = request.form.get("email")
            senha = request.form.get("senha")

            senha_hash = generate_password_hash(senha)

            usuario = Usuario(
                nome=nome,
                email=email,
                senha=senha_hash
            )

            db.session.add(usuario)

            db.session.commit()

            mensagem = "✅ Usuário cadastrado com sucesso!"

        return render_template(
            "cadastro.html",
            mensagem=mensagem
        )

    return app