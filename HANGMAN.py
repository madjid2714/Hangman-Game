import random
print("H A N G M A N\n")
choose_input = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
you_won = 0
you_lost = 0
while True:
    
    if choose_input =="play":
        
        langages = ['python', 'java', 'swift', 'javascript']
        choice = random.choice(langages)
        temp = list(choice)
        replaced = []
        barred = "".join("-"*len(temp))
        replaced = list(barred)
        new_char=""
        print(barred)
        attempts = 8
        suggesed =""
        print(f"#attempts :{attempts}")
        while attempts > 0:
            user_input = input(f"Input a letter:")
        
            if len(user_input) != 1:       
                print("Please, input a single letter.")
                print(new_char) if new_char != "" else print(barred)
                continue
                
            if not user_input.islower():
                print("Please, enter a lowercase letter from the English alphabet")
                print(new_char) if new_char != "" else print(barred)
                continue
            
            if user_input in new_char or user_input in suggesed:
                print("You've already guessed this letter")      
                print(new_char) if new_char != "" else print(barred)
                continue
            
        
            test = False
            for g in range(len(choice)):
                if choice[g] == user_input:
                    replaced[g] = choice[g]
                    test = True
            new_char = "".join(replaced)
            if test == False:
                print("That letter doesn't appear in the word.")
                suggesed += user_input
                print(new_char)
                attempts -= 1
            else:
                print(new_char)
            if new_char == choice:
                print(f"You guessed the word {new_char}!")
                print("You survived!")
                you_won += 1
                break
        if attempts == 0:
            print("You lost!")
            you_lost += 1
        choose_input = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        continue
            
    elif choose_input =="results":
        print(f"You won: {you_won} times.")
        print(f"You lost: {you_lost} times.")
        choose_input = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        continue
        
    elif choose_input =="exit":
        break
    else:
        choose_input = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        continue
