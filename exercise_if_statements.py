# Create a list and store in a variable
# list of countries 
countries_to_guess = ["Canada" , "Mexico" , "France"] 


# Create an input for the guess and store in another variable
# guess country
country_i_guessed = input("What country did you guess: ") 

whats_your_answer = "sorry wrong answer!" 



# Create the if statements

# if guess == country 
if country_i_guessed in countries_to_guess: 
    whats_your_answer = "correct!" 
# if guess != country

# if
# else 
else: 
    whats_your_answer = whats_your_answer 
    # print(whats_your_answer)



# print whatever you want to show
print(whats_your_answer) 
# print(the country you guesses isn't on the list)