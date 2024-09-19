# Challenge 8

# Take the string:
# “jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsd
# xcvhgfdjhiopiwquhejkdsoiufghedjwshi”
# Find the index of a last vowel in the string.

text = "jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi"

last_a_position = text.rfind('a')
last_e_position = text.rfind('e')
last_i_position = text.rfind('i')
last_o_position = text.rfind('o')
last_u_position = text.rfind('u')

last_vowel_position = max(last_a_position,last_e_position,last_i_position,last_o_position,last_u_position)
print(last_vowel_position)