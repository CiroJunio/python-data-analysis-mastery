import pytest
from src.ingestor import process_signal
from data.generator import get_dirty_telemetry
from src.utils import isiterable

def test_sensor_metadata_immutability():
    # Simulando uma tupla imutável [cite: 721-722]
    metadados = ("SENS:01", "REFRIGERADOR_A")
    
    with pytest.raises(TypeError):
        # TENTATIVA REAL DE MUTAÇÃO:
        # Isso falha porque tuplas não suportam atribuição de itens [cite: 723-727]
        metadados = "SENS:EDITADO"