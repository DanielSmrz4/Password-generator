import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char = ['%', '#', '$', '!', '&', '(', ')', '*', '+', '?']

password = []

pass_letters = int(input("Kolik písmen chcete mít ve svém heslu? "))
pass_numbers = int(input("Kolik čísel chcete mít ve svém heslu? "))
pass_specials = int(input("Kolik speciálních znaků chcete mít ve svém heslu? "))

letter = random.choices(letters, k = pass_letters)
number = random.choices(numbers, k = pass_numbers)
special = random.choices(special_char, k = pass_specials)

password = letter + number + special
password = random.sample(password, k = len(password))

print(f"Vaše heslo je: {''.join(password)}")
