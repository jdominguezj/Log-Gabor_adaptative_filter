%% Read Image
I = double(imread('Data/Image.bmp'));

%% Automatic segmentation
[cx,cy,bounding_box,area,orientation,fftspectrum] = get_principal_component(I,80,'true');

%% Objetive function
s = 2900;
angl = 20.4;
wavelength = 20;
sigmaOnf = 0.6 ;
thetaSigma = 0.18;

[residue_sum,phased,gabor_filter] = funcObj(fftspectrum,cx,cy,wavelength,s,sigmaOnf,thetaSigma,angl,'false');

figure(1),imagesc(ifftshift(gabor_filter))
figure(2),imagesc(phased)