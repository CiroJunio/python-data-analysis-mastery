import sqlite3

def init_db(db_path: str):
    with sqlite3.connect(db_path) as conn:

        conn.execute("DROP TABLE IF EXISTS transacoes")
        # Criando a tabela com nomes definitivos
        conn.execute("""
            CREATE TABLE IF NOT EXISTS transacoes (
                hash_id TEXT PRIMARY KEY,
                data_log TEXT,
                ativo TEXT,
                volume REAL
            )
        """)