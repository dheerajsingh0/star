import turtle
sc=turtle.Screen()
sc.setup(600,600)
spiral=turtle.Turtle()
spiral.speed(8)
sc.bgcolor("gray")
col=("white","blue","red","green","black","pink","Purple","Brown")
c=0
for i in range(50):
  spiral.forward(i*10)
  spiral.right(144)
  spiral.color(col[c])
  if c==7:
    c=0
  else:
    c+=1
