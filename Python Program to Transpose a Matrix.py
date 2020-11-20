#Python Program to Transpose a Matrix
X = [[3,4],  
[6,5],  
[7,9]]  
result = [[0,0,0],  
[0,0,0]]  
# iterate through rows  
for i in range(len(X)):  
    for j in range(len(X[0])):  
       result[j][i] = X[i][j]  
for r in result:  
    print(r)  
