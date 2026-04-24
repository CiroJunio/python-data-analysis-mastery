import sqlite3

def init_db(db_path: str):
    with sqlite3.connect(db_path) as conn:
        # Tabela com restrição de UNICIDADE para tratar duplicatas
        conn.execute("""
            CREATE TABLE IF NOT EXISTS transacoes (
                hash_id TEXT PRIMARY KEY, 
                ativo TEXT,
                volume REAL
            )
        """)