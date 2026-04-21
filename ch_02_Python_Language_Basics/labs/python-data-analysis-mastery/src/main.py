import datetime
from src.ingestor import process_signal, check_alert_status
from src.utils import split_signal
from data.generator import get_dirty_telemetry

def run_telemetry_system():
    system_config = {"env": "lab", "threshold": 25.0}
    print(f"\n--- INICIANDO SISTEMA [ID CONFIG: {id(system_config)}] ---")

    start_time = datetime.datetime.now()
    raw_signal = get_dirty_telemetry()
    print(f"Sinal Bruto: {raw_signal} (Tipo: {type(raw_signal)})") 

    try:
        processed_data = process_signal(raw_signal)
        
        for item in processed_data:
            # Apenas temperatura
            if item and isinstance(item, str) and "TEMP" in item.upper():
                value = split_signal(item)
                
                if value is not None:
                    status = check_alert_status(value)
                    print(f" >> ALERTA: {item} | VALOR: {value:.2f}°C | STATUS: {status}")
                else:
                    print(f" >> AVISO: Dado malformado ignorado: {item}")
            
    except Exception as e:
        print(f"!! FALHA CRÍTICA NO PIPELINE: {e}")

    latency = datetime.datetime.now() - start_time
    print(f"--- FIM DO CICLO [Latência: {latency.total_seconds():.6f}s] ---\n")

if __name__ == "__main__":
    run_telemetry_system()