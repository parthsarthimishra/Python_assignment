# initializing an empty matrix
# class of matrix 
class matrix:
    def __init__(self,list):
        #self.m=[]
        self.m=list
        #print(self.m)

    def __add__(self,other):
        matrix=self.m
        matrix2=other.m
        R=len(self.m) 
        R2=len(other.m)
        C=len(self.m[0])
        C2=len(other.m[0])
        if R==R2 and C==C2 :
            sum=[]
            for i in range(R):
                row=[]
                for j in range(C):
                    element=matrix[i][j]+matrix2[i][j]
                    row.append(element)
                sum.append(row)
            return sum    
        else:
            return "Data not applicable for sum "

#subtract
    def __sub__(self, other):
        matrix=self.m
        matrix2=other.m
        R=len(self.m) 
        R2=len(other.m)
        C=len(self.m[0])
        C2=len(other.m[0])
        if R==R2 and C==C2 :
            sub=[]
            for i in range(R):
                row=[]
                for j in range(C):
                    element=matrix[i][j]-matrix2[i][j]
                    row.append(element)
                sub.append(row)
            return sub 
        else:
            return "Data not applicable for sub "
    
 #multiply
    def __mul__(self, other):
        def my_function(i,j,matrix , matrix2,C):
            summul=0
            for x in range(C):
                summul=summul +matrix[i][x]*matrix2[x][j]
            return summul
        matrix=self.m
        matrix2=other.m
        R=len(self.m) 
        R2=len(other.m)
        C=len(self.m[0])
        C2=len(other.m[0])
        
        if C==R2 :
            mul=[]
            for i in range(R):
                row=[]
                for j in range(C2):
                    element=my_function(i,j,matrix,matrix2,C)
                    row.append(element)
                mul.append(row)
            return mul 
        else:
            print("Dimensions of matrix not applicable for multiplication")

            

        

    #determinant
    def find_det(matrix):
        
        det=0
    
        index = list(range(len(matrix)))
     
    #for 2x2 end
        if len(matrix) == 2 and len(matrix[0]) == 2:
            det_2_2 = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
            return det_2_2
 
    
        for i in index: 
        
            As = matrix 
            As = As[1:] 
            height = len(As) 
            for j in range(height): 
                As[j] = As[j][0:i] + As[j][i+1:] 
            sign = (-1) ** (i % 2)     
            sub_det = find_det(As)
        
            det += sign * matrix[0][i] * sub_det 
        return det   


    #power 
    def __pow__(self,x):
        def call_mul(mat1,mat2):
            M1=matrix(mat1)
            M2=matrix(mat2)
            return M1*M2

        C=len(self.m)
        R=len(self.m[0])
        if C==R :
            res=self.m
            for i in range (x-1):
                res = call_mul(res,self.m)
                
            print("xhexk")
            return res
        else:
            return "not applicable matrix"             
# A=matrix([[2, 3],[4, 5]])
# B=matrix([[2, 3, 6],[4, 5, 6]])
#  C=A+B

# D=A-B
# print(D)
# E=A*B
# print(E)
# power = A**4
# print(power)
# det_mat = [[2,2],[3,4]]
# print(matrix.find_det(det_mat))

import unittest

class Testit(unittest.TestCase):
    def test_add(self):
        p1 = matrix([[2, 3], [4, 5]])
        p2 = matrix([[2, 3], [4, 5]])
        add = p1+p2
        self.assertEqual(add, [[4,6], [8, 10]])
    
    def test_mul(self):
        p1 = matrix([[2, 3, 6], [4, 5, 8]])
        p2 = matrix([[2, 3, 7], [4, 5, 7], [1, 1, 1]])
        multi = p1*p2
        self.assertEqual(multi, [[22, 27, 41], [36, 45, 71]])
    
    def test_pow(self):
        p1 = matrix([[2, 3, 4], [4, 3, 7], [5, 4, 1]])
        power = p1**3
        self.assertEqual(power, [[361, 333, 394], [526, 488, 607], [431, 382, 390]])


if __name__ == "__main__":
    unittest.main()



  


