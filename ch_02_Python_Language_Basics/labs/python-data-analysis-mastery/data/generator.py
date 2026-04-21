import random

def get_dirty_telemetry():
    sensors = [
        ["TEMP: 22.5 ", "SENS:01"],
        ("TEMP:23.8", "SENS:02"),
        "TEMP:24,1;SENS:01",
        ["TEMP:ERROR", "SENS:03"],
        "       TEMP: 26.5 ; SENS:02    ",
        None
    ]
    return random.choice(sensors)