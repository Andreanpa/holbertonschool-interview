def pascal_triangle(n):
    if n <= 0: 
        return []
    
    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for y in range(1. i):
            current = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(current)
        
        row.append(1)
        triangle.append(row)
    
    return triangle
