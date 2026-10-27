def generate(rng):
    n = 315
    snake = []
    for r in range(n):
        if r % 2 == 0:
            snake.append([1] * n)
        else:
            row = [0] * n
            row[n - 1 if (r // 2) % 2 == 0 else 0] = 1
            snake.append(row)
    snake[0][0] = 2
    scattered = [[rng.choices([0, 1, 2], [10, 80, 10])[0] for _ in range(316)] for _ in range(316)]
    one_source = [[1] * 316 for _ in range(316)]
    one_source[158][158] = 2
    return [[snake], [scattered], [one_source]]
