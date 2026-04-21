def clean_record(raw_line: str) -> tuple:
    """
    Lógica Pura: Transforma strings sujas em tuplas (id, valor).
    Exceção: Deve lançar SensorAnomalyError se valor > 1000.
    """
    # TODO: Implementar lógica de fatiamento (slicing) e normalização 
    pass

def aggregate_peaks(data_stream):
    """
    Utiliza Sets para unicidade e Dicts para picos de temperatura.
    Retorna: (total_unicos, dict_picos)



    """
    # TODO: Implementar usando apenas o stream (iteração única)
    pass

def process_signal(raw_signal): 
    # print(f"DEBUG: Objeto Ingressante ID: {id(raw_signal)}")

    if raw_signal is None:
        return []
    
    if isinstance(raw_signal, str):
        return [raw_signal.strip()]
    
    try:
        iterator = iter(raw_signal)
        # Duck Typing: Uma nova lista mutável
        return [item.strip() if isinstance(item, str) else item for item in iterator]
    except TypeError:
        return [raw_signal]