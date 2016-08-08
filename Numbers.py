'''
Created on 25-Jan-2016

@author: annervaz
'''

def matrix_multiply(matrix1,matrix2):
    
    result = [[0 for _ in xrange(0,len(matrix1))] for _ in xrange(0,len(matrix2[0]))]
    for i in xrange(0,len(matrix1)):
        for j in xrange(0,len(matrix2[0])):
            for k in xrange(0,len(matrix1[0])):
                result[i][j] += (matrix1[i][k]*matrix2[k][j])%1000
    return result

def matrix_power(matrix,n):
    
    if n == 1:
        return matrix   
    if n == 2:
        return matrix_multiply(matrix,matrix)

    matrix1 =  matrix_power(matrix,n/2)
    
    if n%2 == 0:
        return matrix_multiply(matrix1,matrix1)
    else:
        matrix1 = matrix_multiply(matrix1,matrix1)
        return matrix_multiply(matrix,matrix1)

def N_th_Fibnoacci(n):
    
    matrix = [[1, 1],[1, 0]]
    matrix = matrix_power(matrix,n)
    return matrix[0][1]

def last_3_digits_of(n):
    
    matrix = [[3, 5],[1, 3]]
    matrix = matrix_power(matrix,n)
    
    return (2*matrix[0][0]+999)%1000


if __name__ == '__main__':
    
    
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):
        
        n = int(raw_input())
        result = last_3_digits_of(n)
        if result < 100:
            result = str(0)+str(result)
        print 'Case #'+ str(testcase) + ': ' + str(result) 