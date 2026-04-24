import numpy as np

def generate_sensor_chaos(n_sensors=1000, n_points=10000):
    """
    Gera dados brutos simulando sensores reais com ruído gaussiano.
    Injeta NaNs e picos impossíveis para testar a robustez.
    """
    # Aloca memória sem inicializar para performance extrema (Cuidado com lixo!) 
    data = np.empty((n_sensors, n_points), dtype=np.float64) 
    
    # Preenche com distribuição normal e picos de anomalia
    base_signal = np.random.normal(loc=0, scale=1.0, size=(n_sensors, n_points))
    
    # Injeção de "Caos": picos aleatórios de voltagem
    anomalies = np.random.choice([0, 50], size=(n_sensors, n_points), p=[0.95, 0.05])
    return base_signal + anomalies