import math_quiz_module

count = 0
score = 0
while count <= 3:
    print("""Please choose the game you want to play:
            1. Addition
            2. Subtraction
            3. Multplication
            """)
    game_prompt = "Put your choice here:"
    game_input = int(input(game_prompt))
    if game_input == 1:
        result = math_quiz_module.addition()
        if result[2] == True:
            score += 1
            print("Your answer \"{}\" is correct. You recieved 1 score.".format(result[0]))
        
        else:
            print("Your answer \"{0}\" is incorrect. You recieved 0 score. The correct answer is {1}".format(result[0], result[1]))

        count += 1
    
    elif game_input == 2:
        result = math_quiz_module.subtraction()
        if result[2] == True:
            score += 1
            print("Your answer \"{}\" is correct. You recieved 1 score.".format(result[0]))
        
        else:
            print("Your answer \"{0}\" is incorrect. You recieved 0 score. The correct answer is {1}".format(result[0], result[1]))
        count += 1

    elif game_input == 3:
        result = math_quiz_module.multiplication()
        if result[2] == True:
            score += 1
            print("Your answer \"{}\" is correct. You recieved 1 score.".format(result[0]))
        
        else:
            print("Your answer \"{0}\" is incorrect. You recieved 0 score. The correct answer is {1}".format(result[0], result[1]))
            
        count += 1
     
print("Final Score: {}".format(score))