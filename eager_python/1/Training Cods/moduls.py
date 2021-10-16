import sys
def main():
    print('pythone version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)


    #import datetime
    #now = datetime.datetime.now()
    #print(now)
    #print(now.year,now.month,now.weekday(),now.day,now.hour, now.minute, now.second)

    #import random
    #print(random.randint(1,10))     # az dastor randrang(10) ham mistavan estefade kard
    #x=list(range(25))
    #print(x)
    #random.shuffle(x)
    #print(x)
    #andom.shuffle(x)


    #import urllib.request
    #page= urllib.request.urlopen('https://parsonline.com')
    #print(page)
    #for line in page: print(str(line,encoding='utf_8'),end=" ")


    #import os
    #print(os.name)
    #print(os.getenv('path'))
    #print(os.getcwd())
    #print(os.urandom(22))

if __name__ == '__main__':
    main()