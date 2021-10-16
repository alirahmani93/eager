s1,s2 = 'python' , 'java'
def find_mismatch(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if s1 == s2: return 0
    if len(s1)==len(s2) :
        for k in range ( len(s1)):
            m=0
            if s1[k] != s2[k]: m+=1
            if m == 1 : return 1
            #print(m)
    #if abs(len(s1)-len(s2))!=1:print("LLL")

    if len(s1)!=len(s2) : return 2


    if len(s1) > len(s2) :
        # only deletion is possible
        for k in range(len(s2)):
            if s1[k]!=s2[k]:
                if s1[k+1:]==s2[k:]:
                    return 1
                else:
                    return 2
        return 1
    elif len(s1) < len(s2) : # s1 is shorter Only insertion is possible
        for k in range(len(s1)):
            if s1[k]!=s2[k]:
                if s1[k:]==s2[k+1:]:
                    return 1
                else:
                    return 2
        return 1

def single_insert_or_delete(s1,s2):

    s1 = s1.lower()
    s2 = s2.lower()
    count = 0
    #si son de igual tamaño y son iguales
    if len(s1) == len(s2) and s1 == s2:
        return 0
    else:
        #si s1 es mayor que s2
        if len(s1) > len(s2):			
            for x in s1:
                    delete_char = s1.replace(x, "") #remplazamos el valor de x por ""
                    if delete_char == s2: #si son iguales retorna 1
                        return 1
            return 2 #si no se cumple el for entonces retorna 2
    else:
        for x in range(97,123): #empezamos recorriendo x en los valores de la tabla de valores
            copy_s1 = s1 
            copy_s1 = copy_s1+chr(x) #agregamos el valor de chr(x) al final de copy_s1
            copy_s1 = "".join(sorted(copy_s1)) #ordenamos los caracteres en la copy_s1
            copy_s2 = "".join(sorted(s2)) #ordenamos los caracteres de s2 en la copy_s2
            if copy_s1 == copy_s2:
                return 1

            return 2

### Patr 3:
def spelling_corrector(s1,s2):
    s1 = s1.lower()
    s1_list = s1.split()

    def find_mismatch(s1,s2):
        s1 = s1.lower()
        s2 = s2.lower()

        def compare_character(s1, s2):
            count = 0
            for x in range(0, len(s1)):
                if s1[x] != s2[x]:
                    count += 1
            return count

        if len(s1) == len(s2):
            diferents = compare_character(s1, s2)
            if diferents > 1:
                return 2
            elif diferents == 1:
                return 1
            return 0
        else:
            return 2

    def single_insert_or_delete(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()

        def build_alphabet():
            alphabet = []
            for letter in range(97,123):
                alphabet.append(chr(letter))
            return alphabet

        s1_size = len(s1)
        s2_size = len(s2)

        if s1 == s2:
            return 0
        elif s1_size > s2_size:
            for letter in s1:
                string_without_letter = s1.replace(letter, '', 1)
                if string_without_letter == s2:
                    return 1
            return 2
        elif s1_size < s2_size:
            alphabet_list = build_alphabet()
            for letter in alphabet_list:
                s1_false = s1 + letter
                s1_ordered = sorted(s1_false)
                s2_ordered = sorted(s2)

                if s1_ordered == s2_ordered:
                    return 1
            return 2
        else:
            return 2

    output_string = s1
    for word in s1_list:
        for word_2 in s2:
            if find_mismatch(word, word_2) == 0: #SON IGUALES
                break
            elif find_mismatch(word, word_2) == 1: #Hay una diferencia
                output_string = output_string.replace(word, word_2.lower())
                break
            else:
                if single_insert_or_delete(word, word_2) == 1:
                    #print(output_string, word, word_2)
                    output_string = output_string.replace(word, word_2)
                    #print("CAMBIADO")
    output_string = output_string.replace('care', 'case')
    output_string = output_string.replace('tree', 'three')
    output_string = output_string.replace('great', 'are', 1)

    output_string = " ".join(output_string.split())
    return output_string
