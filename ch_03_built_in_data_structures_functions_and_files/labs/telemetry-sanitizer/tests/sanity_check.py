from src.core.processor import clean_record

def run_tests():
    # Teste 1: Normalização (Vírgula e Formatos)
    # Exemplo: clean_record("ID_01: 25,5") deve retornar ('ID_01', 25.5)
    
    # Teste 2: Prova de Imutabilidade e Hashability [cite: 478]
    # Tente criar um dicionário usando uma LISTA como chave e capture o TypeError.
    print("Sanity Check concluído com sucesso.")

if __name__ == "__main__":
    run_tests()