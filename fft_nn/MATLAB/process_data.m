clear all, close all

res = [];

for i = 0 : 9
    folder = strcat('data/Subject-00',num2str(i))
    files = dir(folder);
    
    for file = files'
        if (strcmp('.',file.name)||strcmp('..',file.name)||strcmp('.DS_Store',file.name))
            continue;
        end
        class = compute_class(file.name);
        strcat(folder,'/',file.name)
        csv = csvread(strcat(folder,'/',file.name),1,0);
        res = [res; class fft_m(csv)];
    end
end

folder = 'data/Subject-010'
files = dir(folder);
 
for file = files'
    if (strcmp('.',file.name)||strcmp('..',file.name)||strcmp('.DS_Store',file.name))
        continue;
    end
    class = compute_class(file.name);
    strcat(folder,'/',file.name)
    csv = csvread(strcat(folder,'/',file.name),1,0);
    res = [res; class fft_m(csv)];
end