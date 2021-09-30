clear; clc; close all;
s=tf('s');
G=3/(s^2+s+1);
K=pidtune(G,'pid')
loop=series(K,G);
closedLoop=feedback(loop,1);

% GEN100 Kp:1.3103935718536377, 
% Ki:0.9094977378845215, Kd:0.6930094361305237, 
%J:0.39028349787582434
K_GA = 1.31+0.909/s+0.693*s/(1+0.1*s);
[y_ga,t2] = step(feedback(K_GA*G,1));

sys = ss(G);
A=sys.A;
B=sys.B;
C=sys.C;
D=sys.D;

Q = 1;
R = 0.1;
N = 0;
[K,S,e] = lqi(sys,Q,R,N);
K1 = K(1:2);
K2 = K(3);
Ae = [A-B*K1 -B*K2
     -C 0];
Be = [B;1];
Ce = [C 0];
De = D;
sys2 = ss(Ae,Be,Ce,De);
[y3,t]=step(sys2,t2);

[y,t]=step(closedLoop,t2);
[y0,t]=step(G,t2);

plot(t,y,'b',t2,y_ga,'r',t2,y3,'k');
legend('MATLAB PID Tuner','GA','LQI')

big;

