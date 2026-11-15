print("Welcome to Quiz Game".upper().center(50))

playing = input("Do you want to play?\n")

if playing.lower() != "yes":
    print("Good Bye!")
    quit()

print("Okay! Lets play :)")

questions = {
    "What does CPU stand for?\n": "central processing unit",
    "What does GPU stand for?\n": "graphics processing unit",
    "What does PSU stand for?\n": "power supply unit",
    "What does RAM stand for?\n": "random access memory"
}

loq = len(questions) * 10
score_points = 0

for key, value in questions.items():
    answer = input(key)
    if answer.lower() == value:
        print("Correct!")
        score_points += 10
    else:
        print("Wrong!")

print("Your Score:", score_points)
