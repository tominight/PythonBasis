import numpy as np
import matplotlib.cm as cm

x = np.arange(10)
colorlist = iter(cm.rainbow(np.linspace(0, 1, len(x))))

class Vector3D:
    def __init__(self, x, y, z, name = None, colour = None):  #coordinates in x, y, z
        self.x = x
        self.y = y
        self.z = z
        self.name = name
        if colour is not None:
            self.colour = colour
        else:
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