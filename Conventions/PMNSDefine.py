import numpy as np

class MixingParams:

    def __init__(self, inverted=0): 
        self.updatetheta()
        #self.dcp = -1.601
        self.dcp = 0

        self.dm21_2 = 7.42 * 10 ** (-5)
        if inverted == 0:
            self.dm32_2 = 2.494 * 10 ** (-3)
        else:
            self.dm32_2 = - 2.494 * 10 ** (-3)

        self.dm31_2 = self.dm32_2 + self.dm21_2

        self.PMNS = np.zeros((3, 3), dtype=complex)
        self.setPMNS()
        self.PMNSConj = self.PMNS.conj().T
        #self.PMNSNeat = (np.sign(np.real(self.PMNS)) * np.abs(self.PMNS))

    def updatetheta(self, theta12 = np.arcsin(np.sqrt(0.307)), theta23 = np.arcsin(np.sqrt(0.561)), theta13 = np.arcsin(np.sqrt(0.022))):
        self.theta12 = theta12
        self.theta23 = theta23
        self.theta13 = theta13
    

    def setPMNS(self): #Thanks Andres :) 
        # set abbreviations
        S12 = np.sin(self.theta12)
        S23 = np.sin(self.theta23)
        S13 = np.sin(self.theta13)
        C12 = np.sqrt(1 - S12 * S12)
        C23 = np.sqrt(1 - S23 * S23)
        C13 = np.sqrt(1 - S13 * S13)
        cd = np.cos(self.dcp)
        sd = np.sin(self.dcp)
        # e row
        self.PMNS[0, 0] = complex(C12 * C13, 0)
        self.PMNS[0, 1] = complex(S12 * C13, 0)
        self.PMNS[0, 2] = complex(S13 * cd, -S13 * sd)
        # mu row
        self.PMNS[1, 0] = complex(-S12 * C23 - C12 * S23 * S13 * cd, -C12 * S23 * S13 * sd)
        self.PMNS[1, 1] = complex(C12 * C23 - S12 * S23 * S13 * cd, -S12 * S23 * S13 * sd)
        self.PMNS[1, 2] = complex(S23 * C13, 0)
        # tau row
        self.PMNS[2, 0] = complex(S12 * S23 - C12 * C23 * S13 * cd, -C12 * C23 * S13 * sd)
        self.PMNS[2, 1] = complex(-C12 * S23 - S12 * C23 * S13 * cd, -S12 * C23 * S13 * sd)
        self.PMNS[2, 2] = complex(C23 * C13, 0)
