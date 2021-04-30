import random
import time
print("Welcome To Our Quiz Game!")
name = input("Please Enter Your Name: ")
print("I hope {} you know about quiz rules.".format(name))
print("We give you 2 minutes to answer those questions, so Hurry up!")
print()
print("Now The Game Start...")


questions = {'ques1': 'Who was the first Indian woman in Space?',
             'ques2': 'Who was the first Indian in space?',
             'ques3': 'Who was the first Man to Climb Mount Everest Without Oxygen?',
             'ques4': 'Who built the Jama Masjid?',
             'ques5': 'Who wrote the Indian National Anthem?'}

answers = {'ans1': 'Kalpana Chawla',
           'ans2': 'Rakesh Sharma',
           'ans3': 'Phu Dorji',
           'ans4': 'Shah Jahan',
           'ans5': 'Rabindranath Tagore'}

timeout = time.time() + 60*2

while True:
    question = random.choice(list(questions.keys()))
    print(questions[question])
    user = input()
    if user.lower() == answers['ans1'].lower() and question == 'ques1':
        print("Yes,It's Correct")
    elif user.lower() == answers['ans2'].lower() and question == 'ques2':
        print("Yes,It's Correct")
    elif user.lower() == answers['ans3'].lower() and question == 'ques3':
        print("Yes,It's Correct")
    elif user.lower() == answers['ans4'].lower() and question == 'ques4':
        print("Yes,It's Correct")
    elif user.lower() == answers['ans5'].lower() and question == 'ques5':
        print("Yes,It's Correct")
    else:
        print("No,It's Incorrect")
    test = 0
    if test == 5 or time.time() > timeout:
        break
    test = test - 1
