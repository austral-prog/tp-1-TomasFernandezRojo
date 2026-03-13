def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665
    horas = total_segundos // 3600
    segundosRestantes = total_segundos - 3600
    minutosrestantes = segundosRestantes // 60
    
    print(horas)
    print(segundosRestantes)
    print(minutosrestantes)
time()