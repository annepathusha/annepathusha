import turtle as t


#arms
t.goto(-150,70)
rectangle(60,15,'grey')
t.goto(-50,110)
rectangle(15,40,'grey')

t.goto(10,70)
rectangle(60,15,'grey')
t.goto(55,110)
rectangle(15,40,'grey')


#neck
t.goto(-50,120)
rectangle(15,20,'grey')


#head
t.goto(-85,170)
rectangle(80,50,'red')


#eyes
t.goto(-60,160)
rectangle(30,10,'white')
t.goto(-60,160)
rectangle(5,5,'black')
t.goto(-45,155)
rectangle(5,5,'black')


#mouth
t.goto(-65,135)
t.right(5)
rectangle(40,5,'black')

t.hideturtle()
