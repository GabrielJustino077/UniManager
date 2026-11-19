from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.database.database import db
import os
from dotenv import load_dotenv


def create_app():

    app = Flask(__name__)

    load_dotenv()  #Carrega as variáveis de ambiente do arquivo .env
    app.config["SECRET_KEY"] = os.environ["SECRETY_KEY"]  

    #Configuração do banco de dados
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///unimanager.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    #Inicializa o banco
    db.init_app(app)

    #Importa os modelos
    from app.models.usuario import Usuario
    from app.models.curso import Curso

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
                session.clear()
                session["usuario_id"] = usuario.id
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

        print("Dashboard acessado")
        print("Usuário autenticado:", session.get("usuario_id"))

        if "usuario_id" not in session:
            return redirect(url_for("home"))

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

    @app.route("/cursos/cadastrar", methods=["GET", "POST"])
    def cadastrar_curso():

        if "usuario_id" not in session:
            return redirect(url_for("home"))

        if request.method == "POST":

            #Recebe os dados do formulário
            nome = (request.form.get("nome") or "").strip()
            duracao = request.form.get("duracao")

            #Converte a duração para inteiro
            try:
                duracao = int(duracao)
            except (ValueError, TypeError):
                return "Duração inválida", 400

            if not nome or duracao <1 or len(nome)> 100:
                return "Dados inválidos", 400

            #Cria um objeto Curso
            novo_curso = Curso(
                nome=nome,
                duracao=duracao
            )

            db.session.add(novo_curso)
            db.session.commit()

            return redirect(url_for("cadastrar_curso"))

        return render_template("cadastrar_curso.html")

    return app