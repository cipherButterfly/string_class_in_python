class String:
    def __init__(self, value):
        self.String = value
     
    def length(self):
        length = 0
        for c in self.String:
            length = length + 1
         
        return length
        
    def char_position(self, char_in):
        char_position = 0
        for c in self.String:
            if c == char_in:
                return char_position
                break
            char_position = char_position + 1
     
     
# The below is just an example to run through all the functions of the String class
while true:
    print('Enter String')
    string_entered = input()
    final_string = String(string_entered)
    print('Length(l) or character_position(cp)?')
    choice_entered = input()
    if choice_entered == "l":
        print(str(final_string.length()))
    elif choice_entered == "cp":
        print("Enter the character")
        char_character_entered = input()
        print(str(final_string.char_position(char_character_entered)))
    else:
        print("Invalid input, try again")
  

