close all;

%Load an instance of each kind of move
% dri = csvread('data/Dribbling-1.csv',1,0);
% psl = csvread('data/Pass-Left-1.csv',1,0);
% psr = csvread('data/Pass-Right-1.csv',1,0);
% run = csvread('data/Running-1.csv',1,0);
% shl = csvread('data/Shot-Left-1.csv',1,0);
% shr = csvread('data/Shot-Right-1.csv',1,0);
% wlk = csvread('data/Walking-1.csv',1,0);
% 
% computeAndPlot_fft(dri, 'Dribbling');
% computeAndPlot_fft(psl, 'Pass Left');
% computeAndPlot_fft(psr, 'Pass Right');
% computeAndPlot_fft(run, 'Running');
% computeAndPlot_fft(shl, 'Shot Left');
% computeAndPlot_fft(shr, 'Shot Right');
% computeAndPlot_fft(wlk, 'Walking');

% w0 = csvread('data/Subject-000/Shot-Right-1.csv',1,0);
% w1 = csvread('data/Subject-001/Shot-Right-1.csv',1,0);
% w2 = csvread('data/Subject-002/Shot-Right-1.csv',1,0);
% w3 = csvread('data/Subject-003/Shot-Right-1.csv',1,0);
% w4 = csvread('data/Subject-004/Shot-Right-1.csv',1,0);
% w5 = csvread('data/Subject-005/Shot-Right-1.csv',1,0);
% w6 = csvread('data/Subject-006/Shot-Right-1.csv',1,0);
% w7 = csvread('data/Subject-007/Shot-Right-1.csv',1,0);
% w8 = csvread('data/Subject-008/Shot-Right-1.csv',1,0);
% w9 = csvread('data/Subject-009/Shot-Right-1.csv',1,0);
% w10 = csvread('data/Subject-010/Shot-Right-1.csv',1,0);
% 
% computeAndPlot_fft(w0, 'Shot-Right');
% computeAndPlot_fft(w1, 'Shot-Right');
% computeAndPlot_fft(w2, 'Shot-Right');
% computeAndPlot_fft(w3, 'Shot-Right');
% computeAndPlot_fft(w4, 'Shot-Right');
% computeAndPlot_fft(w5, 'Shot-Right');
% computeAndPlot_fft(w6, 'Shot-Right');
% computeAndPlot_fft(w7, 'Shot-Right');
% computeAndPlot_fft(w8, 'Shot-Right');
% computeAndPlot_fft(w9, 'Shot-Right');
% computeAndPlot_fft(w10, 'Shot-Right');
% 
% 
% 
% 

w0 = csvread('data/Subject-009/Dribbling-4.csv',1,0);

computeAndPlot_fft(w0, 'Dribbling');

