function class = compute_class(str)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
    if(strcmp('Dribbl',str(1:6)))
        class = 0;
    elseif (strcmp('Pass-L',str(1:6)))
        class = 1;
    elseif (strcmp('Pass-R',str(1:6)))
        class = 2;
    elseif (strcmp('Runnin',str(1:6)))
        class = 3;
    elseif (strcmp('Shot-L',str(1:6)))
        class = 4;
    elseif (strcmp('Shot-R',str(1:6)))
        class = 5;
    else (strcmp('Walkin',str(1:6)))
        class = 6;
    end
end

