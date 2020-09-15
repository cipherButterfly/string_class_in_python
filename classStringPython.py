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

    def equals(self, string_2):
      try:
        i = 0
        s = 0
        while i < string_2.length():
          if self.String[i] == string_2[i]:
            s = s + 1
        if s == string_2.length():
          return True
        else:
          return False
      except:
        return False
    

     
     
# The below is just an example to run through all the functions of the String class
while true:
    print('Enter String')
    string_entered = input()
    final_string = String(string_entered)
    print('''
    Length(l)
    character_position(cp)
    equals(eq)
    ''')
    choice_entered = input()
    if choice_entered == "l":
        print(str(final_string.length()))
    elif choice_entered == "cp":
        print("Enter the character")
        char_character_entered = input()
        print(str(final_string.char_position(char_character_entered)))
    elif choice_entered == "eq":
      string_1 = input()
      string_2 = input()
      print(string_1.equals(string_2))
    else:
        print("Invalid input, try again")
  

