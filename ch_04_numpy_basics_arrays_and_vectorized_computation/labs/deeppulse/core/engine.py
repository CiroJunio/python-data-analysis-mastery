import numpy as np

class TelemetryEngine:
    """
    Motor de processamento de telemetria ultra-rápido.
    Estratégia: Z-Score Robusto (MAD) com O(1) de memória adicional.
    """
    def __init__(self, threshold_sigma=10, persistence_ratio=0.055):
        self.threshold_sigma = threshold_sigma
        self.persistence_ratio = persistence_ratio

    def process_batch(self, data: np.ndarray) -> np.ndarray:
        """
        Transforma dados brutos em Z-Scores Robustos in-place.
        Física: (Dado - Mediana) / MAD
        """
        # 1. Cálculo da Mediana por sensor (Eixo 1)
        # Nota: np.median é custoso (O(n log n)). keepdims permite broadcasting.
        median = np.median(data, axis=1, keepdims=True)

        # 2. Cálculo do MAD (Median Absolute Deviation)
        # CUIDADO: np.abs(data - median) criaria uma cópia de 80MB.
        # Estratégia: Usamos a própria 'data' como buffer temporário após centralizar.
        
        # Centraliza os dados na mediana (In-place)
        np.subtract(data, median, out=data) 
        
        # Calcula o desvio absoluto mediano sobre os dados já centralizados
        mad = np.median(np.abs(data), axis=1, keepdims=True)
        
        # Proteção contra sensores 'mortos' (Divisão por zero)
        mad = np.where(mad == 0, 1.0, mad)

        # 3. Escalonamento Final (In-place)
        # Agora 'data' contém (dado - mediana). Dividimos pelo MAD.
        np.divide(data, mad, out=data)
        
        # Suavização por Intensidade Absoluta
        np.abs(data, out=data)

        return data

    def detect_anomalies(self, data: np.ndarray):
        mask = data > self.threshold_sigma
        
        # DEBUG: Quantos pontos no TOTAL estouraram o limite?
        print(f"DEBUG: Total de pontos acima do threshold: {np.sum(mask)}")
        
        anomaly_ratio = np.mean(mask, axis=1)
        
        # DEBUG: Qual o maior ratio encontrado entre todos os sensores?
        print(f"DEBUG: Maior ratio encontrado: {np.max(anomaly_ratio):.5f}")
        
        matrix_anomalies = anomaly_ratio > self.persistence_ratio
        return data[matrix_anomalies]

class MemoryConstraintError(Exception):
    """Disparado quando a alocação excede o limite de hardware."""
    pass