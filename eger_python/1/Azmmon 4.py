### Part 2:
def count_consonants(s):
    s = str(s)
    s=s.lower()
    sum = 0
    vows = ('a', 'e', 'i', 'o', 'u')

    for i in range(len(s)):
            if (not(s[i] in vows) and ((s[i] > 'a' and s[i] <= 'z'))):
                    sum+=1

    return sum
### Part3:
def find_longest_word(input_string):
    words = input_string.split()
    longest = ""

    for word in words:
        if len(word) >= len(longest):
            longest = word

    return longest

### Part 4:
def anagrams(my_string1, my_string2):
    st1 = my_string1.lower()
    st2 = my_string2.lower()
    p= ''
    sorted1 = p.join(sorted(st1))
    sorted2 = p.join(sorted(st2))
    #print(sorted1 , sorted2)
    if sorted1 == sorted2:
        return True
    else:
        return False
### Part 5:
def my_encryption(some_string):
    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    secret_key    = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"

    cadena=""  
    for x in range(len(some_string)):
      for y in range(len(character_set)):
         if some_string[x]==character_set[y]:
            cadena=cadena+str(secret_key[y])
    return cadena
