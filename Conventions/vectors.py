import numpy as np
import matplotlib.cm as cm

x = np.arange(10)
ys = [i+x+(i*x)**2 for i in range(10)]
colorlist = iter(cm.rainbow(np.linspace(0, 1, len(ys))))

class Vector3D:
    def __init__(self, x, y, z, name = None):  #coordinates in x, y, z
        self.x = x
        self.y = y
        self.z = z
        self.name = name
        self.colour = self.SetColour()

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