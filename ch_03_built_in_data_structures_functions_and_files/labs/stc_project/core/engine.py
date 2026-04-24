from typing import Generator, Tuple, Dict

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

    dict_stream = dict()
    visas = set()

    for line in stream:
        stream_clean = parse_and_clean(line)
        if stream_clean:
            if stream_clean not in visas:
                visas.add(stream_clean) 
                
                _, enterpise, values = stream_clean
                dict_stream[enterpise] = dict_stream.get(enterpise, 0.0) + values

    return dict_stream
    pass