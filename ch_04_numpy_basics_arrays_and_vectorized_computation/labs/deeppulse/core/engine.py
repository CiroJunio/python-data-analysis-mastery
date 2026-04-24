import numpy as np

class TelemetryEngine:
    """
    Motor de processamento de telemetria ultra-rápido.
    Regra de Ouro: Proibido loops. Use a física do NumPy.
    """
    def __init__(self, threshold_sigma=3):
        self.threshold_sigma = threshold_sigma

    def process_batch(self, data: np.ndarray) -> np.ndarray:
        """
        Input: Array 2D (sensores, tempo) de dtype float64.
        Output: Array 'limpo' e normalizado.
        """
        # Média de cada sensor
        mean = data.mean(axis=1, keepdims=True)
        # Quanto cada sensor está vibrando
        std = data.std(axis=1, keepdims=True)
        # Centraliza os dados em zero
        np.subtract(data, mean, out=data)
        # Impede em dividir por zero
        std = np.where(std == 0, 1.0, std)
        # Coloca sensores na mesma escala
        np.divide(data, std, out=data)
        # Descobre a intensidade do desvio
        np.abs(data, out=data)

        return data

        # TODO: Implementar Normalização Vetorizada
        # TODO: Aplicar ufunc de suavização (ex: np.sqrt ou np.log) 
        pass

    def detect_anomalies(self, data: np.ndarray):
        """
        Deve retornar apenas os 'Snapshots' usando Fancy Indexing.
        """

        # TODO: Implementar Boolean Indexing para identificar desvios > 3 sigma 
        # TODO: Usar Fancy Indexing para extrair apenas as fatias problemáticas
        pass

class MemoryConstraintError(Exception):
    """Disparado quando uma operação força uma cópia desnecessária em vez de uma View."""
    pass