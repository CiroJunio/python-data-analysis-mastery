from src.drivers.io_handler import stream_telemetry
from src.core.processor import aggregate_peaks

def run_telemetry_system():
    path = 'data/telemetry.log' # Caminho relativo à raiz [cite: 970, 971]
    
    # Inicia o fluxo (Generator) [cite: 783, 796]
    stream = stream_telemetry(path)
    
    # Processa os dados de forma preguiçosa (Lazy Evaluation) [cite: 363, 801]
    result = aggregate_peaks(stream)
    
    print(f"Resultado Final: {result}")

if __name__ == "__main__":
    run_telemetry_system()