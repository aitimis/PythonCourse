"""
Get text from input: abcdefg
return : bcdefgh

"""

text = input("Get text: ")
f_letter = text[0:1]
s_letter = text[1:2]
t_letter = text[2:3]
f1_letter = ord(f_letter) + 1
f2_letter = chr(f1_letter)
s1_letter = ord(s_letter) + 1
s2_letter = chr(s1_letter)
print(f2_letter,s2_letter, sep='')