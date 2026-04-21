def clean_record(raw_line: str) -> tuple:
    """
    Lógica Pura: Transforma strings sujas em tuplas (id, valor).
    Exceção: Deve lançar SensorAnomalyError se valor > 1000.
    """

    data = raw_line.replace(':', ',').replace('(', '').replace(')', '')
    data = data.replace('SENS_01:25.5', '').strip()

    part = data.split(',')
    identification = (part[0], part[1])
    number = float(part[2])

    return (identification, number)

    # TODO: Implementar lógica de fatiamento (slicing) e normalização 
    pass

def aggregate_peaks(data_stream):
    """
    Utiliza Sets para unicidade e Dicts para picos de temperatura.
    Retorna: (total_unicos, dict_picos)
    """

    for data in data_stream:
        clean_record(data)
        clean = data.strip()

    # TODO: Implementar usando apenas o stream (iteração única)
    pass