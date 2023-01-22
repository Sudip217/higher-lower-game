from game_data import data
from art import vs
from art import logo
from random import randint
from replit import clear


def compare_A():
    a = randint(0, len(data))
    first_key = data[a]
    global name1
    name1 = first_key['name']
    global follower_count1
    follower_count1 = first_key['follower_count']
    global description1
    description1 = first_key['description']
    global country1
    country1 = first_key['country']


def compare_B():
    a = randint(0, len(data))
    second_key = data[a]
    global name2
    name2 = second_key['name']
    global follower_count2
    follower_count2 = second_key['follower_count']
    global description2
    description2 = second_key['description']
    global country2
    country2 = second_key['country']


def show_interface():
    print(f"Compare A: {name1}, a {description1}, from {country1}")
    print(vs)
    print(f"Compare B: {name2}, a {description2}, from {country2}")
    global p
    p = input("Who has more followers? type 'A' or 'B':").lower()
    print(p)

def check_result():
    if p=="a":
        if follower_count1>follower_count2:
            return True
        else:
            return False
    elif p=="b":
        if follower_count2>follower_count1:
            return True
        else:
            return False
    else:
        print("Please enter right keyword.")

i=0
print(logo)
compare_A()
compare_B()
show_interface()
while check_result()==True:
    clear()
    print(f"You're right! Current score: {i}.")

print(f"Sorry, that's wrong. Final score: {i}.")
    

