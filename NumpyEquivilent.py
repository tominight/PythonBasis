import matplotlib.pyplot as plt
import numpy as np
from Conventions import PMNSDefine

def main():
    Plot3D()

def Plot3D():
    v = []
    for i in range(6):
        arr = np.zeros((3,1))
        v.append(arr)
    v[0][0] = 1.0
    v[0][1] = 1.0
    v[0][2] = 1.0
    #print(v)
    matrix = PMNSDefine.MixingParams().PMNS
    #matrix = [[1, 2, 3],
    #          [4, -1, 0],
    #          [0, 0, -1]]
    print(np.dot(matrix,v[0]))

    #v[0][0][0] = matrix[0,0]*v[0][0][0] + matrix[0,1]*v[0][1][0] + matrix[0,2]*v[0][0][2]

if __name__ == "__main__":
    main()