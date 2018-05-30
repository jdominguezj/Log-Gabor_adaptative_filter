#--------------------------------------------------------------------------------------
# parameter description:
# --------------------------
# I ----------- input fringe image
# T ----------- segmentation threshold
# D ----------- display results? ('true'/'false')
# return : x - y coordinates
#=====================================================================================

import numpy as np
import matplotlib.pyplot as plt
from colormap import Colormap
from numpy import matrix

# preprocessing

@mfunction("cx","cy","bounding_box","area","orientation","F") 
def get_principal_component(I,T,D):
    Gx=hanning(size(I,2))
    Gxy=hanning(size((I,1))
    AA=Gy*Gx.cT
    AA=(AA-min(AA(mslice[:])))/(max(AA(mslice[:]))-min(AA(mslice[:])))

c=Colormap()

F = fft2(double(I))
Fim = fft2(double(I) *elmul* AA)
Ih = fftshift(abs(Fim))
Ih(mslice[:], mslice[end / 2 - 5:end / 2 + 5]).lvalue = 0
In = round(1024 * imnormalize(Ih))

if strcmp(D, mstring('true')):
                figure(700)
                imagesc(In)
                c=Colormap()
                c.plot_colormap('greys')
                pyplot.hold(True)
    h,w=size_(In,nargout=2)
    offset_w = round(w * 0.04)
    offset_h = round(h * 0.04)

seed_tl = mcat([offset_h, offset_w])
seed_tr = mcat([offset_h, w - offset_w])
seed_bl = mcat([h - offset_h, offset_w])
seed_br = mcat([h - offset_h, w - offset_w])

if strcmp(D, mstring('true')):
   plot(offset_w, offset_h, mstring('sr'))
   plot(w - offset_w, offset_h, mstring('sr'))
   plot(offset_w, h - offset_h, mstring('sr'))
   plot(w - offset_w, h - offset_h, mstring('sr'))

S = zeros(h, w)
S(seed_tl(1), seed_tl(2)).lvalue = 1
S(seed_tr(1), seed_tr(2)).lvalue = 1
S(seed_bl(1), seed_bl(2)).lvalue = 1
S(seed_br(1), seed_br(2)).lvalue = 1

mask = not regiongrow(In, S, T)
if strcmp(D, mstring('true')):
   figure(799)
   imagesc(mask)
   c=Colormap()
                c.plot_colormap('greys')   figure(800)
   imagesc(In)
   pyplot.hold(True)

I2 = In *elmul* mask
marco = regionprops(mask, I2, mstring('BoundingBox'), mstring('Area'), mstring('Orientation'))
talla = size(marco, 1)
Areas = zeros(mcat([talla, 1]))
Rec = zeros(mcat([talla, 4])); print Rec
centroides = zeros(mcat([talla, 2]))

orientation = zeros(mcat([talla, 1]))
for i in mslice[1:talla]:
   Areas(i).lvalue = marco(i).Area
   orientation(i).lvalue = marco(i).Orientation
   Rec(i, mslice[:]).lvalue = marco(i).BoundingBox
   b = round(Rec(i, mslice[:])); print b

   subregion = I2(mslice[b(2):b(2) + b(4)], mslice[b(1):b(1) + b(3)])
   max(subregion(mslice[:]))
   [rows_r, cols_r] = ind2sub(mcat([size(subregion, 1), size(subregion, 2)]), idx)
   centroides(i, mslice[:]).lvalue = mcat([cols_r + b(1) - 1, rows_r + b(2) - 1])
   if strcmp(D, mstring('true')):
       rectangle(mstring('Position'), Rec(i, mslice[:]), mstring('EdgeColor'), mstring('r'))
       plot(centroides(i, 1), centroides(i, 2), mstring('+b'))
 
