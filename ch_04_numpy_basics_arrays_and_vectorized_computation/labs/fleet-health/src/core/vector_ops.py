import numpy as np
from src.core.exceptions import InvalidFleetDataError

def validate_matrix(matrix: np.ndarray) -> None:
    """FAIL-FAST: Verifica se é um ndarray bidimensional de float64."""
    if not isinstance(matrix, np.ndarray):
        raise InvalidFleetDataError("O dado não é um ndarray do NumPy.")
    if matrix.ndim != 2:
        raise InvalidFleetDataError(f"Dimensão inválida. Esperado 2, recebido {matrix.ndim}.")
    if matrix.dtype != np.float64:
        raise InvalidFleetDataError("Tipagem inválida. O hardware exige float64.")

def sanitize_readings(matrix: np.ndarray) -> np.ndarray:
    """
    Missão 1: Substituir temperaturas negativas por 0.0.
    Obrigatório o uso de np.where.
    """
    validate_matrix(matrix)
    # TODO: Implementar vetorização
    raise NotImplementedError("Implemente a sanitização vetorial.")

def calculate_truck_averages(matrix: np.ndarray) -> np.ndarray:
    """
    Missão 2: Retornar a média de temperatura por caminhão.
    Dica: Qual eixo (axis) representa as linhas? 
    """
    validate_matrix(matrix)
    # TODO: Implementar agregação
    raise NotImplementedError("Implemente o cálculo de médias.")

def count_crisis_sensors(matrix: np.ndarray, threshold: float = 120.0) -> int:
    """
    Missão 3: Retornar o número exato de sensores operando acima do threshold.
    Obrigatório o uso de Boolean Indexing e agregações.
    """
    validate_matrix(matrix)
    # TODO: Implementar contagem com máscara booleana
    raise NotImplementedError("Implemente a contagem de crise.")