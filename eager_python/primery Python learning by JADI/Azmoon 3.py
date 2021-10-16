## Azmoon 4 part 2
def count_consonants(s):
    s = str(s)
    s=s.lower()
    sum = 0
    vows = ('a', 'e', 'i', 'o', 'u')

    for i in range(len(s)):
            if (not(s[i] in vows) and ((s[i] > 'a' and s[i] <= 'z'))):
                    sum+=1

    return sum

## Azmoon 4 part 3
def find_longest_word(input_string):
    words = input_string.split()
    longest = ""

    for word in words:
        if len(word) >= len(longest):
            longest = word

    return longest
## Azmoon 4 part 4
def anagrams(my_string1, my_string2):
    pass
## Azmoon 4 part 5
def my_encryption(some_string):
    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    secret_key    = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"

    cadena=""  
    for x in range(len(some_string)):
      for y in range(len(character_set)):
         if some_string[x]==character_set[y]:
            cadena=cadena+str(secret_key[y])
    return cadena
