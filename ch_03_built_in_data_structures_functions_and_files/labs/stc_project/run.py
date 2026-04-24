# No seu run.py
from core.engine import transaction_stream, filter_unique_transactions

def run():
    path = "data/archive.txt" # Ajuste o caminho para o Docker
    stream = transaction_stream(path)
    resultado = filter_unique_transactions(stream)
    
    print("Processamento concluído com sucesso!")
    for ativo, volume in resultado.items():
        print(f"Ativo: {ativo} | Volume Total: {volume:.2f}")

if __name__ == "__main__":
    run()