import copy

def isPossible(y,x,n,grid):		#y,x instead of x,y because the array indices are refrred this way. 
	if(checkRow(y,x,n,grid) and checkCol(y,x,n,grid) and checkSquare(y,x,n,grid)):
		return True
	return False

def checkRow(y,x,n,grid):
	for i in range(9):
		if grid[y][i]==n:
			return False
	return True


def checkCol(y,x,n,grid):
	for i in range(9):
		if grid[i][x]==n:
			return False
	return True

def checkSquare(y,x,n,grid):
	x0 = (x//3)*3
	y0 = (y//3)*3
	for i in range(3):
		for j in range(3):
			if grid[y0+j][x0+i]==n:
				return False
	return True


def solve(grid):
	for i in range(9):
		for j in range(9):
			if grid[i][j]==0:		#Blanks are represented by 0
				for n in range(1,10):
					if isPossible(i,j,n,grid):
						grid[i][j]=n
						if not solve(grid):
							grid[i][j]=0
						else:
							return True
						
				return False
	return True

def solve_sudoku(grid):
	s1 =copy.deepcopy(grid)
	solve(grid)
	if(s1!=grid):
		return s1,grid
	else:
		return s1,["No Solution Found"]


if __name__=='__main__':
	grid=[[3,0,6,5,0,8,4,0,0], 
		  [5,2,0,0,0,0,0,0,0], 
		  [0,8,7,0,0,0,0,3,1], 
		  [0,0,3,0,1,0,0,8,0], 
		  [9,0,0,8,6,3,0,0,5], 
		  [0,5,0,0,9,0,6,0,0], 
		  [1,3,0,0,0,0,2,5,0], 
		  [0,0,0,0,0,0,0,7,4], 
		  [0,0,5,2,0,6,3,0,0]] 

	orig,solved = solve_sudoku(grid)
	print(original,"\n",solved)



