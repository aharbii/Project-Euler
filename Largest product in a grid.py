grid = []
res = []
for grid_i in range(20):
	grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
	grid.append(grid_t)

for i in range(20):
    for j in range(17):
        res.append(grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3])
        res.append(grid[j][i]*grid[j+1][i]*grid[j+2][i]*grid[j+3][i])
for l in range(17):
    for k in range(17):
        res.append(grid[l][k]*grid[l+1][k+1]*grid[l+2][k+2]*grid[l+3][k+3])
        res.append(grid[::-1][l][k]*grid[::-1][l+1][k+1]*grid[::-1][l+2][k+2]*grid[::-1][l+3][k+3])
    

print(max(res))
