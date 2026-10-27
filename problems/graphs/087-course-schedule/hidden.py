def generate(rng):
    layers, width = 50, 1000
    n = layers * width
    label = list(range(n))
    rng.shuffle(label)
    requires = {}
    for layer in range(1, layers):
        for i in range(width):
            node = layer * width + i
            requires[node] = [(layer - 1) * width + j for j in rng.sample(range(width), 2)]
    edges = [[label[a], label[b]] for a, bs in requires.items() for b in bs]
    rng.shuffle(edges)
    top = layers * width - 1 - rng.randrange(width)
    low = top
    while low >= width:
        low = rng.choice(requires[low])
    cyclic = edges + [[label[low], label[top]]]
    rng.shuffle(cyclic)
    return [[n, edges], [n, cyclic]]
