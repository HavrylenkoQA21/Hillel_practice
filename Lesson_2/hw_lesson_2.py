# The English language has five vowels: A, E, I, O, and U
# Please count each vowel occurrence in text
# bellow ( sum of lower and capital cases)
# and write output as table smth like this
# -----------------
# | vowel | count |
# -----------------
# |   a   |  11   |
# |   e   |  23   |
#   ...
# -----------------

# then modify text where each vowel replaced with
# A->À;  a->à ; E-> É ; e->é; I->Í , i->í ; O->Ó ; o->ó; U->Ú; u->ú
# ex. "Í wàndéréd lónély...."   and print it

# Text str
poem_text = """I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze. 

Continuous as the stars that shine
And twinkle on the Milky Way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance."""

# № 1 Vowels Table
sep_num = 20  # Count of equals
print(sep_num * '=')  # Print equals
print(f"| {'vowel':^6} | {'count':^7} |")  # create and print columns name
print(sep_num * '=')

vowels_dict = {  # create dict for columns
 "a": poem_text.count("a"),
 "e": poem_text.count("e"),
 "i": poem_text.count("i"),
 "o": poem_text.count("o"),
 "u": poem_text.count("u"),
 "A": poem_text.count("A"),
 "E": poem_text.count("E"),
 "I": poem_text.count("I"),
 "O": poem_text.count("O"),
 "U": poem_text.count("U")
 }
# definition of vowel and count values
for vowel, count in vowels_dict.items():
    print(f"| {vowel:^7}|  {count:^6.0f} |")  # print values for each columns
print(sep_num * '=')

# № 2 Replace vowels
modify_a = poem_text.replace('a', 'à')
modify_e = modify_a.replace('e', 'é')
modify_i = modify_e.replace('i', 'í')
modify_o = modify_i.replace('o', 'ó')
modify_u = modify_o.replace('u', 'ú')
modify_A = modify_u.replace('A', 'À')
modify_E = modify_A.replace('E', 'É')
modify_I = modify_E.replace('I', 'Í')
modify_O = modify_I.replace('O', 'Ó')
modify_U = modify_O.replace('U', 'Ú')
print(modify_U)
