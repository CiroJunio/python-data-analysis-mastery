from drivers.log_generator import generate_chaotic_log

def run():
    generate_chaotic_log("data/archive.txt", 10000)

if __name__ == "__main__":
    run() # O gatilho que faltava