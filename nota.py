def calcular_nota(nota: float) -> str:
    if nota >= 9:
        return "A"
    elif nota >= 7 and nota <= 8.9:
        return "B"
    elif nota >= 5 and nota <= 6.9:
        return "C"
    elif nota >= 3 and nota <= 4.9:
        return "D"
    elif nota <= 3:
        return "F"
    