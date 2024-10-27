import numpy as np
X = np.array([[1, 2, 3, 4],
              [4, 5, 6, 2],
              [7, 8, 9, 1],
              [2, 5, 1, 5]])
# print(X[1,2]) # Truy cập vào phần tử thuộc dòng 1 và cột 2
# print(X[1:3,1:3]) # Truy cập vào các dòng từ 1 đến 2 và các cột từ 1 đến 2
# print(X[:2,:2]) # Truy cập vào 2 dòng, 2 cột đầu tiên
# print(X[-2:,-2:]) # Truy cập vào 2 dòng, 2 cột cuối cùng
# print(X[[0,2],:]) # Truy cập vào dòng 0 và 2. Cách lấy indices không liên tục
# 
# np.random.seed(1)
# matrix=np.random.randint(0,10,size=(3,2))
# print(matrix)

print(X[[1,3],0::3])