def stream_telemetry(file_path):
    """
    GENERATOR: Lê o arquivo linha a linha.
    Restrição: Proibido o uso de .readlines() ou list()
    """
    with open(file_path, 'r') as f: # Gerenciador de contexto para segurança 
        for line in f:
            if line.strip():
                yield line # Pausa a execução e entrega a linha 