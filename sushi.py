#!/usr/bin/env python3
## This is my first python script and I like sushi


name=input("What Is Your Name? ")

print("Hello " + name + "!")
    
sushi=input("Do You Like Sushi? (y/n) ")

if sushi=="y":
    print("Nice! Me Too!")
    favsushi=input("What's Your Favorite Kind? (Salmon or Tuna) ")
    if favsushi=="Salmon":
        print("That's My Favorite Too!")
    if favsushi=="Tuna":
        print("Eh, Tuna is Ok But Salmon is Better")
    spicymayo=input("Do You Like Spicy Mayo? (y/n) ")
    if spicymayo=="y":
        print("Me Too!")
    else:
        print("You Should Try It Sometime!")
else:
    print("Well, Looks Like We Can't Be Friends!")
