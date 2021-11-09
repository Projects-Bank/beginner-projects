fruits_to_buy = ["apple", "mango", "avocado", "banana", "orange"]

fruit_i_bought = input("Tell me which fruit you bought: ")

am_i_in_trouble = "not yet"

if fruit_i_bought in fruits_to_buy:
    am_i_in_trouble = "nope!"
else:
    am_i_in_trouble = "ya bet!"

print(am_i_in_trouble)