def process_signal(raw_signal): 
    print(f"DEBUG: Objeto Ingressante ID: {id(raw_signal)}")

    if raw_signal is None:
        return []
    
    if isinstance(raw_signal, str):
        return [raw_signal.strip()]
    
    try:
        iterator = iter(raw_signal)
        # Duck Typing: Uma nova lista mutável
        return [item.strip() if isinstance(item, str) else item for item in iterator]
    except TypeError:
        return [raw_signal]

def check_alert_status(temp):
    # Expressão Ternária
    return "CRITICAL" if temp > 25.0 else "NORMAL"