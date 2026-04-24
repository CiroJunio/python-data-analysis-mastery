import numpy as np
import os

def save_anomalies(anomalies: np.ndarray, path: str = "data/alert_snapshot.npz"):
    """
    Objetivo: Persistência binária ultra-eficiente.
    """
    # 1. A VÁLVULA DE SEGURANÇA
    # Se o array estiver vazio (size == 0), aborte a missão de escrita.
    # Charada: Qual atributo do ndarray diz o número total de elementos? [cite: 80]
    if anomalies.size == 0: # O atributo .size conta todos os elementos 
        print("Operação abortada: Nenhuma anomalia para salvar.")
        return

    os.makedirs(os.path.dirname(path), exist_ok=True)
    np.savez_compressed(path, anomalous_data=anomalies)

    # Após chamar o save_anomalies...
    if os.path.exists("data/alert_snapshot.npz"):
        file_size = os.path.getsize("data/alert_snapshot.npz") / 1024
        print(f"📦 Tamanho do Snapshot Comprimido: {file_size:.2f} KB")

    # 2. O COMPACTADOR INDUSTRIAL
    # Use a função que cria o arquivo comprimido.
    # Charada: Como passar o array para o arquivo dando a ele 
    # o 'apelido' interno de 'anomalous_data'? [cite: 1356, 1357]
    
    print(f"Dados persistidos em: {path}")