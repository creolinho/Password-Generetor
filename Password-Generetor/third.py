import random




class password:
            def __init__(self,password,lenght, master):
                self.password = password
                self.length = lenght


            def vowel_numbers(password):
                password = password.replace("a","4").replace("e","3").replace('i','1').replace('o','0').replace('u','5')
                return password

            def special_word(password):
                # characters to check if the password entered have, so it can be changed
                chars1 = set('is')
                chars2 = set('a.')
                chars3 = set('ec')

                if any((i in chars1)for i in password):
                            
                    password = password.replace('i','!').replace('s','$')
                    return password

                elif any((i in chars2)for i in password):
                            
                    password = password.replace('.','*').replace('a','@')
                    return password

                elif any((i in chars3)for i in password):
                            
                    password = password.replace('e','&').replace('c','ç')
                    return password

                else:
                    pass

                return password

            def captalization(password):
                return password[0].upper()

            def password_generator(length):
                pass_data = "qwertyuiopasdfgjklzxcvbnm1234567890[];',./!@#$%^&*()_+:<>?"
                password = "".join(random.sample(pass_data, length))
                return password

            def pronouceble_password(length):
                with open(f"{length}code.txt") as file:
                    word = file.readline()
                    



'''codigo com a classe, e lidando com erros e todas as funções
 que arrumam e fazem as senhas'''
while True:
    try:
        user_entry = input("enter the to turn it into the greates password")
        if user_entry.len() < 8:
            break

    except:
            print("the password needs to have at least 8 charatcters")
    
    else:
        
        pass




"""supostamente o codigo para uma barra com valores para entrada de lenght"""


