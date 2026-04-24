from drivers.log_generator import generate_chaotic_log
from core.engine import (
    transaction_stream,
    parse_and_clean,
    filter_unique_transactions
)

def run():
    stream = transaction_stream('/data/archive.txt')
    clean = parse_and_clean(stream)
    

if __name__ == "__main__":
    run() 