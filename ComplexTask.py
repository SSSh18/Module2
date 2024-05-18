def generate_password(n):
    if n < 3 or n > 20:
        return "Число должно быть от 3 до 20"

    result = ""

    for i in range(1, n):
        for j in range(i, n):
            if n % (i + j) == 0 and i != j:
                result += str(i) + str(j)

    return result


n = int(input("Введите число от 3 до 20: "))
print(generate_password(n))
