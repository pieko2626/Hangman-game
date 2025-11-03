import random

while True:
    words = ['Dead By Daylight',
             'Overwatch',
             'The Sims',
             'Need For Speed',
             'League Of Legends',
             'Outlast']

    mark = '-'
    print(f"{mark*10}Welcome to the Hangman game - Games Edition!{mark*10} \n "
          f"To start please enter '1'.\n To exit, enter '2'.")


    try:
        user_choice = int(input("Your choice: "))
    except:
        raise ValueError("You were supposed to enter integer number :(")

    if user_choice == 1:
        print("Let's start!")
    elif user_choice == 2:
        print("See you soon!")
        exit()
    else:
        print("You were supposed to pick 1 or 2")
        continue

    word = random.choice(words)

    to_swap = "_"
    hidden = []

    for a in word:
        if a.isalpha():
            hidden.append(to_swap)
        else:
            hidden.append(a)

    to_guess = "".join(hidden)

    # print(word)
    # print(to_guess)

    word = word.upper()
    chances = 6
    used_letters = []
    guessed_letters = set()

    while chances > 0:

        print("-"*30)
        print(f"Chances remaining: {chances}")
        print(f"Used letters: {''.join(sorted(used_letters))}")
        print(f"Game: {''.join(hidden)}")

        user_input = input("Enter your letter: ").upper()
        if len(user_input) > 1:
            print("You were supposed to enter one letter!")
            continue
        elif not user_input.isalpha():
            print("You can only use letters! (A-Z)")
            continue
        elif user_input in guessed_letters:
            print(f"You have already used {user_input}!")
            continue

        guessed_letters.add(user_input)

        if user_input in word:
            print(f"{user_input} is here!")
            for index, letter_in_word in enumerate(word):
                if letter_in_word == user_input:
                    hidden[index] = user_input
        else:
            print(f"{user_input} is not here!")
            chances -= 1

        if '_' not in hidden:
            print(f"Congratulations! The game was: {word}. You won!")
            exit()

    if chances == 0:
        print(f"The game was: {word}. Try again!")
        while True:
            choice = input("Do you want to play again? (Y/N?)").upper()
            if choice == 'Y':
                break
            elif choice == 'N':
                print("Bye!")
                exit()
            else:
                print("Enter Y or N!!!!")
                continue




















