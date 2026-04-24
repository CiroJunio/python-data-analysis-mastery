import time
import numpy as np
from drivers.chaos_gen import generate_sensor_chaos
from core.engine import TelemetryEngine
# from io.persistence import ... (implementar depois)

def run_mission():
    print("Capturando sinais dos sensores...")
    raw_data = generate_sensor_chaos()
    engine = TelemetryEngine()
    
    print("Iniciando processamento vetorizado...")
    t0 = time.time()
    clean_data = engine.process_batch(raw_data) 
    anomalies = engine.detect_anomalies(clean_data)
    t1 = time.time()

    print(f"Missão concluída em {t1-t0:.4f}s")
    print(f"Anomalias detectadas: {anomalies.shape}") 

if __name__ == "__main__":
    run_mission()