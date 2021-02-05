def compare(dict1: dict, dict2: dict):
    """Compara la estructura de 2 dicccionarios y sus subdiccionarios de manera recursiva"""
    # Si los dict no son de tipo dict devuelve true dado que no compara
    if not isinstance(dict1, dict) and not isinstance(dict2, dict) : return True
    # Si solo uno es un dict devuelve false dado que no se mantiene el formato
    if type(dict1) != type(dict2): return False

    # Se compara las keys de los diccionarios
    if dict1.keys() != dict2.keys(): return False

    # Si son iguales se busca subdiccionarios
    for key in dict1:
        if compare(dict1[key], dict2[key]) is False: return False
    return True

