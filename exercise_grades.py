def grades():
    """
    Ejercicio 11 - Promedio de Calificaciones

    Dadas tres notas, calcular e imprimir:
    1. El promedio de las tres notas
    2. La nota máxima
    3. La nota mínima
    4. Cuántos puntos faltan del promedio a 10
    """
    nota1 = 8
    nota2 = 7
    nota3 = 9

    suma = nota1 + nota2 + nota3 
    notas = nota1, nota2, nota3
    promedio = suma / 3
    notaMax = max(notas)
    notaMin = min(notas)
    
    
    
    print(promedio)
    print(notaMax)
    print(notaMin)
    print(10 - promedio)
grades()