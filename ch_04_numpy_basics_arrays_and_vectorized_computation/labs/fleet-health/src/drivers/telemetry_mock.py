import numpy as np

def generate_fleet_matrix(trucks: int = 50, sensors: int = 1000) -> np.ndarray:
    """
    Gera uma matriz de temperaturas (float64).
    Média de 80°C, desvio de 25°C. Força a criação de ruído negativo e picos de crise.
    """
    # Fixando a seed para reprodutibilidade nos testes 
    np.random.seed(42) 
    
    # Gera a matriz bruta
    matrix = np.random.normal(loc=80.0, scale=25.0, size=(trucks, sensors))
    
    return matrix