from typing import Generator, Tuple, Dict
import sqlite3

def transaction_stream(path: str) -> Generator[bytes, None, None]:
    """Lê o arquivo em modo binário puro."""
    # Sua missão: Use 'rb' e yield 
    path = "data/archive.txt"
    with open(path, "rb") as f:
        for line in f:
            yield line
    pass

def parse_and_clean(raw_line: bytes) -> Tuple[str, str, float]:
    """Decodifica, limpa e normaliza os dados."""
    # Sua missão: Trate UnicodeDecodeError aqui 
    # Lembre-se: Use .strip().title() para strings 
    try:
        decodes = raw_line.decode('utf-8')
    except UnicodeDecodeError:
        return ()

    parts = [p.strip().title() for p in decodes.split(',')]

    try:
        dates, enterprise, values = parts
        real_values = float(values)
        result = (dates, enterprise, real_values)
    except (UnicodeDecodeError, ValueError, IndexError):
        result = ()

    return result
    pass

def filter_unique_transactions(stream: Generator, db_path: str) -> Dict[str, float]:
    
    with sqlite3.connect(db_path) as conn:
        for line in stream:
            pepita = parse_and_clean(line)
            if pepita:
                d, e, v = pepita
                unique_key = f"{d}_{e}_{v}"
                conn.execute(
                    "INSERT OR IGNORE INTO transacoes (hash_id, data_log, ativo, volume) VALUES (?, ?, ?, ?)",
                    (unique_key, d, e, v)
                )
        
        cursor = conn.execute("SELECT ativo, SUM(volume) FROM transacoes GROUP BY ativo")
        return dict(cursor.fetchall())
                    



    return dict_stream
    pass