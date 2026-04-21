from src.core.processor import clean_record
from src.core.exceptions import SensorAnomalyError

def run_tests():
    # Teste de função pura
    assert clean_record("('SENS_01', 'LAB_A'), 23.5") == (('SENS_01', 'LAB_A'), 23.5)

    # Teste de resiliência
    assert clean_record("SENS_01:25.5") == (('SENS_01', 'N/A'), 25.5)

    # Teste de fronteira
    try:
        clean_record("SENS_X: 9999.9")
        raise AssertionError("A Funcao deveria ter barrado o 9999!")
    except SensorAnomalyError:
        print("Sucesso: Anomalia bloqueada corretamente.")

    # Teste 2: Prova de Imutabilidade e Hashability [cite: 478]
    info, valor = clean_record("SENS_01:25.5")
    
    try:
        test_map = {info: "Funcionou"}
        print("Sucesso: Identificacao e uma tupla (hash)")
    except TypeError:
        raise AssertionError("Falha: clean_record retornou diferente")

    print("Sanity Check concluído com sucesso.")

if __name__ == "__main__":
    run_tests()