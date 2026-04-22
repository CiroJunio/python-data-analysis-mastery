import numpy as np
from src.core.vector_ops import (
    sanitize_readings, 
    calculate_truck_averages, 
    count_crisis_sensors
)
from src.core.exceptions import InvalidFleetDataError

def run_tests():
    print("🧪 Iniciando Multímetro de Matrizes...")
    
    # Matriz controlada para teste (5 caminhões, 4 sensores)
    test_matrix = np.array([
        [100.0, -5.0, 90.0, 150.0],
        [80.0,  80.0, 80.0, 80.0],
        [-10.0, -20.0, 0.0, 50.0],
        [130.0, 125.0, 140.0, 110.0],
        [75.0,  75.0,  75.0,  75.0]
    ], dtype=np.float64)

    # Teste 1: Fail-Fast

    # Teste 2: Sanitização (Sem negativos)

    # Teste 3: Agregação por Eixo (Shape e Cálculo)

    # Teste 4: Boolean Indexing


    print("🚀 NÚCLEO MATEMÁTICO APROVADO!")

if __name__ == "__main__":
    run_tests()