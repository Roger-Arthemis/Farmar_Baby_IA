import hashlib
import hmac
import os
import sqlite3
from contextlib import closing

# O banco fica na mesma pasta do projeto
CAMINHO_BANCO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "farmar_baby.db")


def _conectar():
    return sqlite3.connect(CAMINHO_BANCO)


def _gerar_hash(senha, salt=None):
    """Transforma a senha em hash (nunca guardamos a senha pura)"""
    if salt is None:
        salt = os.urandom(16)
    resultado = hashlib.pbkdf2_hmac("sha256", senha.encode("utf-8"), salt, 100_000)
    return salt.hex() + ":" + resultado.hex()


def _conferir_hash(senha, hash_guardado):
    salt_hex, _ = hash_guardado.split(":")
    novo = _gerar_hash(senha, bytes.fromhex(salt_hex))
    return hmac.compare_digest(novo, hash_guardado)


def criar_tabelas():
    """Cria a tabela de usuários (se não existir) e uma conta de profissional de teste"""
    with closing(_conectar()) as conexao:
        conexao.execute(
            """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                telefone TEXT NOT NULL,
                data_nasc TEXT NOT NULL,
                senha_hash TEXT NOT NULL,
                tipo TEXT NOT NULL DEFAULT 'gestante'
            )
            """
        )
        # Conta de teste para o painel do profissional (o cadastro só cria gestantes)
        existe = conexao.execute("SELECT 1 FROM usuarios WHERE tipo = 'profissional'").fetchone()
        if not existe:
            conexao.execute(
                "INSERT INTO usuarios (nome, email, telefone, data_nasc, senha_hash, tipo) VALUES (?, ?, ?, ?, ?, ?)",
                ("Profissional Teste", "profissional@farmarbaby.com", "00000000000", "01/01/1980", _gerar_hash("123456"), "profissional"),
            )
        conexao.commit()


def cadastrar_usuario(nome, email, telefone, data_nasc, senha, tipo="gestante"):
    """Salva um novo usuário. Retorna (True, mensagem) ou (False, motivo do erro)"""
    criar_tabelas()
    try:
        with closing(_conectar()) as conexao:
            conexao.execute(
                "INSERT INTO usuarios (nome, email, telefone, data_nasc, senha_hash, tipo) VALUES (?, ?, ?, ?, ?, ?)",
                (nome, email.lower(), telefone, data_nasc, _gerar_hash(senha), tipo),
            )
            conexao.commit()
        return True, "Cadastro realizado com sucesso!"
    except sqlite3.IntegrityError:
        return False, "Este e-mail já está cadastrado."


def validar_login(email, senha, tipo="gestante"):
    """Confere e-mail, senha e tipo. Retorna um dicionário com os dados ou None"""
    criar_tabelas()
    with closing(_conectar()) as conexao:
        linha = conexao.execute(
            "SELECT nome, email, tipo, senha_hash FROM usuarios WHERE email = ?",
            (email.strip().lower(),),
        ).fetchone()

    if linha is None:
        return None
    nome, email_banco, tipo_banco, senha_hash = linha
    if tipo_banco != tipo or not _conferir_hash(senha, senha_hash):
        return None
    return {"nome": nome, "email": email_banco, "tipo": tipo_banco}