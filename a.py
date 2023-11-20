def contar_habitaciones(n, m, mapa):
    def dfs(x, y):
        visitado[x][y] = True
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and mapa[nx][ny] == '.' and not visitado[nx][ny]:
                dfs(nx, ny)
    visitado = [[False] * m for _ in range(n)]
    habitaciones = 0
    for i in range(n):
        for j in range(m):
            if mapa[i][j] == '.' and not visitado[i][j]:
                habitaciones += 1
                dfs(i, j)

    return habitaciones

n, m = map(int, input().split())
mapa = [input() for _ in range(n)]


resultado = contar_habitaciones(n, m, mapa)
print(resultado)
