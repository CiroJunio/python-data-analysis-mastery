import math
from src.core.exceptions import SensorAnomalyError

def clean_record(raw_line: str) ->   tuple:
    """
    Lógica Pura: Transforma strings sujas em tuplas (id, valor).
    Exceção: Deve lançar SensorAnomalyError se valor > 1000.
    """

    data = raw_line.replace(':', ',') \
                   .replace('(', '') \
                   .replace(')', '') \
                   .replace("'", "") \
                   .strip()
    
    part = data.split(',')

    if len(part) == 2:
        identification = (part[0], "N/A")
        number = float(part[1])
    elif len(part) >= 3:
        identification = (part[0].strip(), part[1].strip())
        number = float(part[2])

    if (math.isinf(number) or math.isnan(number)):
        raise SensorAnomalyError(f"Dado corrompido: {type(number)}")

    if number > 1000:
        raise SensorAnomalyError(f"Anomalia detectada: {number}")

    return (identification, number)

    # TODO: Implementar lógica de fatiamento (slicing) e normalização 
    pass

def aggregate_peaks(data_stream):
    """
    Utiliza Sets para unicidade e Dicts para picos de temperatura.
    Retorna: (total_unicos, dict_picos)
    """

    sensores_vistos = set()
    picos_calor = dict()

    count = 0

    for linha in data_stream:
        try:
            info, valor = clean_record(linha)
            sensores_vistos.add(info)
            count = count + 1
            if (count >= 10000):
                print(f"Relatório da Janela: {picos_calor}")
                sensores_vistos.clear()
                picos_calor.clear()
                # O correto seria jogar esses dados para um bd ou em algum arquivo
                count = 0
            if info not in picos_calor or valor > picos_calor.get(info, 0):
                picos_calor[info] = valor
        except SensorAnomalyError as e:
            print(f"Pulando linha inválida: {e}")


    return len(sensores_vistos), picos_calor

    # TODO: Implementar usando apenas o stream (iteração única)
    pass