import random

def generate_chaotic_log(filename: str, lines: int = 10000):
    assets = ['Apple', 'google', 'BITCOIN', 'ETH##', '  tesla  ']
    with open(filename, 'wb') as f:
        for _ in range(lines):
            # Inserindo ruído: Duplicatas propositais e bytes corrompidos
            asset = random.choice(assets)
            val = random.uniform(10, 1000)
            line = f"2026-04-24,{asset},{val:.2f}\n".encode('utf-8')
            
            if random.random() < 0.01: # 1% de chance de corromper o byte
                line = line[:-2] + b'\xff\xfe' + b'\n'
                
            f.write(line)
    print(f"Caos gerado em {filename}")