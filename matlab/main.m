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

%% Optimization with PSO

f = @(inputs) funcObj(fftspectrum,cx,cy,wavelength,round(inputs(1)),...
    inputs(2),inputs(3),angl,'false');

% optimun = PSO(f,10,[500 0.45 0.2],[6000 0.7 0.8],10,1000);



n = 10;
xmin = [2500 0.55 0.15];
xmax = [3500 0.65 0.3];
vmax = 10;
niter = 50;
d = length(xmin);

x = (xmax-xmin).*rand(n,d)+xmin;
v = (vmax/3+vmax/3)*rand(n,d) - vmax/3;


pb = x;
for i = 1:n
    if i == 1
        gb = pb(i,:);
    end
    
    if f(pb(i,:)) < f(gb)
        gb = pb(i,:);
    end
end


iters = 0;
C1 = 0.72984*2.05;
C2 = 0.72984*2.05;
while 1
    iters = iters + 1;
    disp(['iter = ',num2str(iters)])
    
    for i = 1:n
        if f(x(i,:)) < f(pb(i,:))
            pb(i,:) = x(i,:);
        end

        if f(pb(i,:)) < f(gb)
            gb = pb(i,:);
        end
    end

    
    for i = 1:n
        for j = 1:d
            v(i,j) = v(i,j) + C1*rand*(pb(i,j) - x(i,j)) + ...
                C2*rand*(gb(j)-x(i,j));
            x(i,j) = x(i,j) + v(i,j);
            if x(i,j) > xmax(j)
                x(i,j) = xmax(j);
            elseif x(i,j) < xmin(j)
                x(i,j) = xmin(j);
            end
        end
    end
    
    if iters == niter
        break
    end
end
