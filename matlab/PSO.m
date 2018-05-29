function gb = PSO(f,n,xmin,xmax,vmax,niter)


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
