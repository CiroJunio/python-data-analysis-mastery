from src.drivers.io_handler import stream_telemetry
from src.core.processor import aggregate_peaks
from src.core.processor import process_signal

def run_telemetry_system():
    path = 'data/telemetry.log'
    
    # Inicia o fluxo (Generator) 
    stream = stream_telemetry(path)
    
    process =  process_signal(stream)

    for _ in range(10):
        print(process[_])

    # Processa os dados de forma preguiçosa (Lazy Evaluation) 
    result = aggregate_peaks(stream)
    
    print(f"Resultado Final: {result}")

if __name__ == "__main__":
    run_telemetry_system()