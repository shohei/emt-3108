th1=get(ui1,'value');
th2=get(ui2,'value');
model_2dof_2d;
plot(xy(1,:),xy(2,:),'o-','linewidth',5);
axis equal;
axis([-10,10,-10,10]);
grid;