def single_insert_or_delete(s1, s2):

    if len(s1) == len(s2):
        for i in range(len(s1)):
            if s1[i].lower() != s2[i].lower():
                return 2
        return 0
    elif abs(len(s1) - len(s2)) > 1:
        return 2
    else:
        temp = ""
        if len(s1) < len(s2):
            temp = s2
            #print('temp:',temp)
            s2 = s1
            #print('s2',s2)
            s1 = temp
            #print('s1:',s1)
        obj = {}
        #print ('obj: ',obj)
        for i in s1:
            obj[i] = 0
        for j in s2:
            if j in obj:
                obj[j] = obj[j] + 1
                #print ('obj in loop: ',obj)
        num = 0
        for i in obj:
            if obj[i] == 0:
                num = num+1
                if num > 1:
                    return 2
        #print(obj)
        return 1 ,temp,s1,s2
