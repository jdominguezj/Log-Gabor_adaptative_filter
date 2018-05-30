#--------------------------------------------------------------------------------------
# parameter description:
# --------------------------
# I ----------- input fringe image
# T ----------- segmentation threshold
# D ----------- display results? ('true'/'false')
# return : x - y coordinates
#=====================================================================================

import numpy

# preprocessing

@mfunction("cx","cy","bounding_box","area","orientation","F") 
def get_principal_component_(I,T,D):
    Gx=hanning(size(I,2))
    Gxy=hanning(size(I,1))
    AA=Gy*Gx.cT
    AA=(AA-min(AA(mslice[:])))/(max(AA(mslice[:]))-min(AA(mslice[:])))

F = fft2(double(I))
Fim = fft2(double(I) *elmul* AA)
Ih = fftshift(abs(Fim))
Ih(mslice[:], mslice[end / 2 - 5:end / 2 + 5]).lvalue = 0
In = round(1024 * imnormalize(Ih))

if strcmp(D, mstring('true')):
    figure(700)
    imagesc(In)
    colormap("gray")
    hold("on")
    end
    h,w=size_(In,nargout=2)
    offset_w = round(w * 0.04)
    offset_h = round(h * 0.04)
