import pytest
from src.ingestor import process_signal, check_alert_status
from src.utils import split_signal

def test_sensor_metadata_immutability():
    """Prova que dados protegidos (tuplas) não podem ser alterados."""
    metadados = ("SENS:01", "REFRIGERADOR_A")
    
    with pytest.raises(TypeError):
        # Tenta mudar um valor interno da tupla
        metadados[0] = "SENS:EDITADO"

def test_split_signal_logic():
    """Valida se o parser de string está funcionando para casos reais."""
    # Caso com vírgula e ponto-e-vírgula
    assert split_signal("TEMP:24,1;SENS:01") == 24.1
    # Caso com sujeira de espaços
    assert split_signal("  TEMP: 26.5 ; SENS:02  ") == 26.5
    # Caso de erro
    assert split_signal("TEMP:ERROR") is None

def test_alert_ternary_logic():
    """Valida a expressão ternária de alerta."""
    assert check_alert_status(26.0) == "CRITICAL"
    assert check_alert_status(22.0) == "NORMAL"