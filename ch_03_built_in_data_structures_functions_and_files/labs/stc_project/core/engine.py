from typing import Generator, Tuple, Dict

def transaction_stream(path: str) -> Generator[bytes, None, None]:
    """Lê o arquivo em modo binário puro."""
    # Sua missão: Use 'rb' e yield 
    with open("../data/archive.txt", "rb") as f:
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
        print("Dados corrompidos!")
        return ()

    clean_edges = decodes.strip().title()
    split_line = clean_edges.split(',')

    try:
        dates, enterprise, values = split_line
        real_values = float(values)
        result = (dates, enterprise, real_values)
    except (UnicodeDecodeError, ValueError, IndexError):
        result = ()

    return result
    pass

def filter_unique_transactions(stream: Generator) -> Dict[str, float]:
    """Processa o fluxo garantindo unicidade sem estourar a RAM."""
    # Dica: O que é imutável serve de chave no Dict 
    pass