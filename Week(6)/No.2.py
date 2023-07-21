#6511171_Wai_Yan_Paing_542_class06_as2
message = input("Enter a message: ")
result = ""
for i in message:
   if i.isupper():
        old_c = ord(i) 
        c_index = ord(i) - ord("A") 
        new_index = (c_index + 3) % 26 
        new_c = new_index + ord("A")
        new_character = chr(new_c) 
        result = result + new_character 
   elif i.islower:
        result += i 
print(result)
