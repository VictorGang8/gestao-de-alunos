import sqlite3

DB_NAME = 'alunos.db'


def conectar():
    return sqlite3.connect(DB_NAME)


def criar_tabela():
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER,
                curso TEXT NOT NULL
            )
            '''
        )
        conexao.commit()


def cadastrar_aluno(nome, idade, curso):
    nome = (nome or '').strip()
    curso = (curso or '').strip()

    if not nome or not curso:
        raise ValueError('Nome e curso são obrigatórios.')

    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute(
            '''
            INSERT INTO alunos (nome, idade, curso)
            VALUES (?, ?, ?)
            ''',
            (nome, int(idade), curso),
        )
        conexao.commit()


def listar_alunos():
    with conectar() as conexao:
        cursor = conexao.cursor()
        return cursor.execute(
            'SELECT id, nome, idade, curso FROM alunos ORDER BY nome'
        ).fetchall()


def excluir_aluno(aluno_id):
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM alunos WHERE id = ?', (aluno_id,))
        conexao.commit()
        return cursor.rowcount


def quantidade_alunos():
    with conectar() as conexao:
        cursor = conexao.cursor()
        return cursor.execute('SELECT COUNT(*) FROM alunos').fetchone()[0]