def factorial_recursive(n):
    """
    Вычисляет факториал числа n рекурсивным методом
    """
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Пример использования
print(factorial_recursive(3))  # 120