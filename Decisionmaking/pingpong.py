# read a number 15 PINGPONG
# display PING if number is divisible / 3
# display PONG if number is divisible / 5
# display PINGPONG if number is divisible / 15
# fizz buzz

number=int(input("enter number")) #30


if number%15==0: #30%3

    print("PINGPONG")

elif number%5==0:

    print("PONG")

elif number%3==0:

    print("PING")