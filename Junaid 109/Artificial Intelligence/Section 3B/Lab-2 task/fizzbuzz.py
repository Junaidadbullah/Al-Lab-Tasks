import random
def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)
def fizz_buzzgame():
    score = 0
    number=0
    while True:
        num =random.randint(1, 10)
        number= number + num
        correct_answer = fizz_buzz(number)
        player_answer = input(f"What is your answer for {num}? ")
        print(f'Now this is your previous number {number}')

        if player_answer.strip().lower() == correct_answer.lower():
            print("you are right")
            score += 1
        else:
            print(f"sorry you loss and answer was '{correct_answer}'")
            break
    print(f"Your score is: {score}")





fizz_buzzgame()
