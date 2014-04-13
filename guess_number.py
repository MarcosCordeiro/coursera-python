
import random
import simplegui


high = 100

def new_game():
    global secret_number,remaining
    secret_number = random.randint(0, high)
    
    if high == 100:
        remaining = 7
    elif high == 1000:
        remaining = 10
        
    print
    print "New game. Range is from 0 to ",high
    print "Number of remaining guesses is " , remaining 
 
def range100():
    global low,high,remaining
    high=100
    remaining = 7
    new_game()

def range1000():
    global low,high,remaining
    high=1000
    remaining = 10
    new_game()
    
def input_guess(guess):
    global remaining,secret_number
    guess = int(guess)
    remaining -= 1
    print 
    print "Gues was ", guess
    print "Number of remaining guesses is " , remaining 
    if guess == secret_number:
        print "Correct!!!"    
        new_game()
    elif guess < secret_number:
        print "High!"
    elif guess > secret_number:
        print "Low!"
        
    if remaining == 0:
        print "You ran out of the guesses. The number was ", secret_number
        new_game()
    
f = simplegui.create_frame("Guess the number",200,200)

f.add_button("Range is [0 - 100]",range100,200)
f.add_button("Range is [0 - 1000]",range1000,200)
f.add_input("Enter the guess",input_guess,200)

new_game()
f.start()
