clc; clear; close all;

m = 1;
b = 0.5;
k = 20;
F0 = 10;

tspan = [0 15];
y0 = [0; 0];
ode_func = @(t, y) [y(2); (F0 - b*y(2) - k*y(1))/m];
[t, y] = ode45(ode_func, tspan, y0);

plot(t, y(:,1))
grid on;