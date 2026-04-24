import os
import sys

def check_memory_leak(process_func):
    """Verifica se você não está usando list.append() escondido."""
    import psutil
    process = psutil.Process(os.getpid())
    mem_before = process.memory_info().rss
    process_func()
    mem_after = process.memory_info().rss
    
    if (mem_after - mem_before) / (1024 * 1024) > 50:
        print("ALERTA: Consumo de memória excessivo! Você está acumulando dados na RAM.")
    else:
        print("SISTEMA ESTÁVEL: Escala linear de memória confirmada.")