% This file is part of Predict My Play.
%
% Copyright (C) 2019 Jorge Balzquez 	<jorgeblazher at gmail dot com>
%					 Miguel Bolsa	<miguellbolsa at gmail dot com>
%					 Miguel Crespo 		<mcrescas at gmail dot com>
%					 Juan Jose Gomez 	<jjgomez96 at hotmail com>
% For more information see <https://github.com/xewir/predictMyPlay>
%
% Predict My Play is free software: you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation, either version 3 of the License, or
% (at your option) any later version.
%
% Predict My Play is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
% GNU General Public License for more details.
%
% You should have received a copy of the GNU General Public License
% along with Predict My Play. If not, see <http://www.gnu.org/licenses/>.

function computeAndPlot_fft(X, label)
%Computes and plots the FFT of X
%   X signal to be processed
%   label: type of movement
    %Some useful data
    Fs = 1000;                              % Sampling frequency                    
    T = 1/Fs;                               % Sampling period       
    L = size(X,1);                        % Length of signal
    t = (0:L-1)*T;                          % Time vector
    
    %Compute FFT
    Y = fft(X); 
    P2 = abs(Y/L);
    P1 = P2(1:L/2+1,:);
    P1(2:end-1) = 2*P1(2:end-1);
    
    %Plot
    f = Fs*(0:(L/2))/L;
    figure;
    %Fourier Domain: accelerations
    subplot(4,2,1); 
    plot(f(1:30),P1(1:30,1:3),'LineWidth',2) 
    title(strcat(label,' - Left leg (Accel)'))
    xlabel('f (Hz)')
    ylabel('|P1(f)|')
    legend('X','Y','Z')
    grid on;

    subplot(4,2,2); 
    plot(f(1:30),P1(1:30,7:9),'LineWidth',2) 
    title(strcat(label,' - Right leg (Accel)'))
    xlabel('f (Hz)')
    ylabel('|P1(f)|')
    legend('X','Y','Z')
    grid on;
    
    %Fourier Domain: gyros
    subplot(4,2,3); 
    plot(f(1:30),P1(1:30,4:6),'LineWidth',2) 
    title(strcat(label,' - Left leg (Gyro)'))
    xlabel('f (Hz)')
    ylabel('|P1(f)|')
    legend('X','Y','Z')
    grid on;

    subplot(4,2,4); 
    plot(f(1:30),P1(1:30,10:12),'LineWidth',2) 
    title(strcat(label,' - Right leg (Gyro)'))
    xlabel('f (Hz)')
    ylabel('|P1(f)|')
    legend('X','Y','Z')
    grid on;
    
    %Time Domain: accelerations
    subplot(4,2,5); 
    plot(t,X(:,1:3),'LineWidth',2) 
    title(strcat(label,' - Left leg (Accel)'))
    xlabel('Time (s)')
    ylabel('a (g)')
    legend('X','Y','Z')
    grid on;

    subplot(4,2,6); 
    plot(t,X(:,7:9),'LineWidth',2) 
    title(strcat(label,' - Right leg (Accel)'))
    xlabel('Time (s)')
    ylabel('a (g)')
    legend('X','Y','Z')
    grid on;
    
    %Time Domain: gyros
    subplot(4,2,7); 
    plot(t,X(:,4:6),'LineWidth',2) 
    title(strcat(label,' - Left leg (Gyro)'))
    xlabel('Time (s)')
    ylabel('º/s')
    legend('X','Y','Z')
    grid on;

    subplot(4,2,8); 
    plot(t,X(:,10:12),'LineWidth',2) 
    title(strcat(label,' - Right leg (Gyro)'))
    xlabel('Time (s)')
    ylabel('º/s')
    legend('X','Y','Z')
    grid on;
end

