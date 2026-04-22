import random
import os

def generate_dirty_log(filename="data/telemetry.log", lines=10000):
    """Gera um arquivo de log ruidoso para testar a resiliência do pipeline."""
    
    # Garante que o diretório data/ existe 
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    sensors = [("SENS_01", "LAB_A"), ("SENS_02", "LAB_B"), ("SENS_03", "LAB_C")]
    
    # Usamos o gerenciador de contexto 'with' para segurança 
    with open(filename, "w") as f:
        for _ in range(lines):
            sensor = random.choice(sensors)
            # 1. Escolha aleatória de formato (ID:VALOR ou ID,VALOR)
            format_choice = random.random()
            temp = round(random.uniform(20.0, 35.0), 2)
            
            # 2. Injeção de Anomalias (Fail-Fast)
            if random.random() < 0.005: # 0.5% de chance de erro crítico
                temp = 9999.9
            
            if format_choice < 0.4:
                # Formato A: ID:VALOR com espaços 
                line = f"  {sensor} : {temp}  \n"
            elif format_choice < 0.8:
                # Formato B: ID,VALOR
                line = f"{sensor},{temp}\n"
            else:
                # Formato C: Duplicatas exatas para testar SETS 
                line = "SENS_01:25.5\n"
                
            f.write(line) # Escrita no arquivo 

    print(f">> Sucesso: Arquivo '{filename}' gerado com {lines} linhas.")

if __name__ == "__main__":
    generate_dirty_log()