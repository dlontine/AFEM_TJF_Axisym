from numpy import *
from .isop2_4 import CSDIsoParametricQuad4 as BaseElement
# --------------------------------------------------------------------------- #
# --------------------- Axisymmetry Plane Strain Element--------------------- #
# --------------------------------------------------------------------------- #
class AxiSymQuad4(BaseElement):
    ndir = 3
    nshr = 1
    integration = 4
    gaussw = ones(4)
    gaussp = array([[-1., -1.], [ 1., -1.], [-1.,  1.], [ 1.,  1.]]) / sqrt(3.)
    def bmatrix(self, dN):
        B = zeros((4, 8))
        B[0, 0::2] = B[3, 1::2] = dN[0, :]
        B[1, 1::2] = B[3, 0::2] = dN[1, :]
		#B[2, 0::2] = Ne[:]/r #This is what I think we need to do to modify???? r needs to be re-defined
        return B
		
		#hahahaha