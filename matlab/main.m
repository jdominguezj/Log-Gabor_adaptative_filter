%% Read Image
I = double(imread('Data/Image.bmp'));

%% Automatic segmentation
[cx,cy,bounding_box,area,orientation,fftspectrum] = get_principal_component(I,80,'true');

%% Objetive function
s = 2000;
angl = 20;
wavelength = 20;
sigmaOnf = 0.55;
thetaSigma = 0.25;

[residue_sum,m,phased] = funcObj(fftspectrum,cx,cy,s,wavelength,sigmaOnf,thetaSigma,angl,'false');