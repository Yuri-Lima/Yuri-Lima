# # Project: Numbers in words
# # Author: Yuri Lima
# # Email: y.m.lima19@gmail.com
# # GitHub: https://github.com/Yuri-Lima
# # Goals: The main ideia this project is in the future i will create a API.
# # This API will help developments find every numbers in words.

from .convertnumbers import Convert_numbers_english
#====================================================================================================

number_typed = list()

print('Please give me a number (Max = 13 Decimal Places):')

number_typed = '1'

word = Convert_numbers_english(number_typed)
word.start_convertion()

print(word.number_in_word())
print(word.even_or_odd())

