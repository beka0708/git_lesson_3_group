def sum_even_numbers(a, b):
    if a > b:
        return f"Ошибка: a должно быть меньше или равным b"

    total_sum = 0
    for num in range(a, b + 1):
        if num % 2 == 0:
            total_sum += num

    return total_sum


print(sum_even_numbers(1, 5))   # 2, 4

