import time
import numpy as np
from drivers.chaos_gen import generate_sensor_chaos
from core.engine import TelemetryEngine
from storage.persistence import save_anomalies

def run_mission():
    print("Capturando sinais dos sensores...")
    raw_data = generate_sensor_chaos()
    engine = TelemetryEngine()
    
    print("Iniciando processamento vetorizado...")
    t0 = time.time()
    print("ANTES:", raw_data.max())
    clean_data = engine.process_batch(raw_data) 
    print("DEPOIS:", clean_data.max())
    anomalies = engine.detect_anomalies(clean_data)
    t1 = time.time()
    print(f"--- RESULTADOS DA MISSÃO ---")
    print(f"Tempo NumPy: {t1-t0:.4f}s")
    
    # A Prova de Integridade: Quantos sensores falharam?
    if anomalies.size > 0:
        print(f"🚨 Alerta! {anomalies.shape} sensores apresentaram anomalias.")
        print(f"Shape do Snapshot: {anomalies.shape}") # Deve ser (N, 10000)
    else:
        print("✅ Sistema Estável: Nenhuma anomalia detectada.")

    save_anomalies(anomalies)

if __name__ == "__main__":
    run_mission()