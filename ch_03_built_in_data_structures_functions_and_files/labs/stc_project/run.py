from core.engine import transaction_stream, filter_unique_transactions
from core.schema import init_db
from drivers.log_generator import generate_chaotic_log

def run():
    path = "data/archive.txt"
    path_db = "data/final.db"
    init_db(path_db)
    # generate_chaotic_log(path, 10000)

    stream = transaction_stream(path)
    resultado = filter_unique_transactions(stream, path_db)
    
    print("Processamento concluído com sucesso!")
    for ativo, volume in resultado.items():
        print(f"Ativo: {ativo} | Volume Total: {volume:.2f}")

if __name__ == "__main__":
    run()