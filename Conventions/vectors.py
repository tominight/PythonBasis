import numpy as np
import matplotlib.cm as cm

x = np.arange(10)
colorlist = iter(cm.rainbow(np.linspace(0, 1, len(x))))

class Vector3D:
    def __init__(self, x, y, z, name = None, colour = None, plotaura = False):  #coordinates in x, y, z
        self.x = x
        self.y = y
        self.z = z
        self.name = name
        if colour is not None:
            self.colour = colour
        else:
            self.colour = self.SetColour()
        self.plotaura = plotaura

    def UpdateCoordinates(self, x=None, y=None, z=None):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if z is not None:
            self.z = z
    
    def SetColour(self):
        colour = next(colorlist)
        return colour
    
    def TransformX(self, matrix): #TODO add length catch here.
        x = matrix[0,0]*self.x + matrix[0,1]*self.y + matrix[0,2]*self.z
        self.UpdateCoordinates(x=x)
    
    def TransformY(self, matrix):
        y = matrix[1,0]*self.x + matrix[1,1]*self.y + matrix[1,2]*self.z
        self.UpdateCoordinates(y=y)
    
    def TransformZ(self, matrix):
        z = matrix[2,0]*self.x + matrix[2,1]*self.y + matrix[2,2]*self.z
        self.UpdateCoordinates(z=z)