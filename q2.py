def even_squares(numbers: list) -> list:
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n ** 2)
    return result

print(even_squares([1, 2, 3, 4])) 
