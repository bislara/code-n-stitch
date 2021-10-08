import turtle
import random
import time


wn = turtle.Screen()
# .title("Turtle Race")
wn.bgcolor("black")
# wn.setup(width=1000, height=1000)

#2 players:
#the one to get to the other side wins

player1= turtle.Turtle()
player1.color('red')#color of player one
player1.shape('turtle')#shape of player1 as turtle

player2= player1.clone()
player2.color('light blue')

#positioning players
player1.penup()
player1.goto(-300,200)
player2.penup()
player2.goto(-300,-200)

#drawing a finish line
player1.goto(300,-250)
player1.pendown()
player1.color('white')
player1.left(90)
player1.forward(500)
player1.write('Finish!',font=("Verdana",18, "normal"))

#player1 to starting position
player1.right(90)
player1.penup()
player1.color('red')
player1.goto(-300,200)

player1.pendown()
player2.pendown()

#values for die
die= [1,2,3,4,5,6]

#game code
def die_roll1(die):
	die1= random.choice(die)
	player1.write(die1,font=("Verdana",15, "normal"))
	player1.forward(30*die1)
	# time.sleep(1)

def die_roll2(die):
	die2=random.choice(die)
	player2.write(die2,font=("Verdana",15, "normal"))	
	player2.forward(30*die2)
	# time.sleep(1)

for i in range(30):
	if player1.pos() >= (300,250):
		print("Player one wins the race!")
		player1.write("			I win !!!",font=("Verdana",15, "normal"))
		break
	elif player2.pos() >= (300,-250):
		print("Player two wins the race!")
		player2.write("			I win !!!",font=("Verdana",15, "normal"))
		break
	else:
		p = input("Player 1 press Enter to roll the Die")
		die_roll1(die)
		q = input("Player 2 press Enter to roll the Die")
		die_roll2(die)
