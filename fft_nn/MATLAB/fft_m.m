function res = fft_m(X)
%FFT_M Summary of this function goes here
%   Detailed explanation goes here
    Fs = 1000;                              % Sampling frequency                    
    T = 1/Fs;                               % Sampling period       
    L = size(X,1);                        % Length of signal
    t = (0:L-1)*T;                          % Time vector
    
    %Compute FFT
    Y = fft(X); 
    P2 = abs(Y/L);
    P1 = P2(1:L/2+1,:);
    P1(2:end-1) = 2*P1(2:end-1);
    
    res = P1(1:30,:)';
    res = reshape(res,[1,360]);
end

