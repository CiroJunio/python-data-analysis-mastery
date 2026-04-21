def split_signal(signal_string):
    if not isinstance(signal_string, str):
        return None

    try:
        # 1. Normalização
        clean_string = signal_string.replace(',', '.')
        # 2. Separação
        main_part = clean_string.split(';')[0]
        # 3. Extração
        parts = main_part.split(':')
        if len(parts) >= 2:
            return float(parts[1].strip())
            
    except (ValueError, IndexError, AttributeError):
        return None
    return None

def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False