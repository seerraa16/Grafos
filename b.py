from collections import deque

def encontrar_camino(n, m, laberinto):
    def es_valido(x, y):
        return 0 <= x < n and 0 <= y < m and laberinto[x][y] != '#'
    
    inicio, fin = None, None
    for i in range(n):
        for j in range(m):
            if laberinto[i][j] == 'A':
                inicio = (i, j)
            elif laberinto[i][j] == 'B':
                fin = (i, j)

    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visitado = set()
    cola = deque([(inicio, [])])

    while cola:
        (x, y), ruta = cola.popleft()

        if (x, y) == fin:
            return "SÍ", len(ruta), ''.join(ruta)

        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if es_valido(nx, ny) and (nx, ny) not in visitado:
                cola.append(((nx, ny), ruta + [dir_movimiento(dx, dy)]))
                visitado.add((nx, ny))

    return "NO"

def dir_movimiento(dx, dy):
    if dx == -1:
        return 'U'
    elif dx == 1:
        return 'D'
    elif dy == -1:
        return 'L'
    elif dy == 1:
        return 'R'

n, m = map(int, input().split())
laberinto = [input() for _ in range(n)]

resultado = encontrar_camino(n, m, laberinto)
print(resultado)
