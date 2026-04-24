from src.drivers.telemetry_mock import generate_fleet_matrix
from src.core.vector_ops import (
    sanitize_readings,
    calculate_truck_averages,
    count_crisis_sensors
)

def run_fleet_system():
    # Generator
    stream = generate_fleet_matrix()
    read = sanitize_readings(stream)
    calculate_truck = calculate_truck_averages(read)
    count = count_crisis_sensors(calculate_truck)

    print(f"Resultado Final: {count}")


if __name__ == "__main__":
    run_fleet_system()