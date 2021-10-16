# Sanjaqak Telegram BOT
# name: sjtset1_bot     username: @sanjaqak_test_bot
## IMPORT part ##
import json
import urllib
from urllib.request import urlopen
from urllib.parse import quote
import time
### DECODER ###
def decoder(resp):
    decoded = ""
    for line in resp:
        decoded += line.decode('utf-8')
    return decoded
## TOKEN ##
token   = "1340038194:AAF03lVxvrHeT-ALT5Ut-WYErRwuZ0wd7C0" #"1054367581:AAGMXx8dLgH_WrArcsZ5Tpbm2aAhhGVEcoA"
## URL ##
URL = "https://api.telegram.org/bot{}/".format(token)
## CMD ##
cmd='getme'
###  ####
resp = urlopen(URL + cmd)
line = decoder(resp)
gtm = json.loads(line)
print('line 25 : ' , URL+cmd)
print('line 26 : ' , resp)
##print(line)
##print(gtm)

### STATUS ###
status = True
while status :
    cmd = 'getUpdates'
    
    resp     = urlopen(URL+cmd)
    line     = decoder(resp)
    upds     = json.loads(line)
    print('line 38 : ' , URL+cmd)
    ## NOM ##
    nom = len(upds['result'])
    if nom !=0:
        if 'message' in upds['result'][0]:
            msg = upds['result'][0]['message']
            chid = str(msg['chat']['id'])   ## Id CHAT ##
            print('chid:  ' , chid)
            if 'text' in msg:
                command = msg['text']
                print(command) # for SHOW
                if command == '/start' or command == "MAIN":
                    message= " Please enter Prodouct PN"
                    cmd= "sendMessage"
                    txt= quote(message.encode('utf-8'))
                    keyboard ={'keyboard': [['HOME'],['OUTdoor']]}
                    keyboards = json.dumps(keyboard)
                    #print('222')
                    #print(keyboards)
                    print(URL + cmd + '?chat_id={}&text={}'.format(chid,txt) + '&replay_markup={}'.format(keyboards))
                    #resp = urlopen(URL + cmd + '?chat_id={}&text={}&reply_markup={}'.format(chid, txt, keyboards))
                    resp = urlopen(URL + cmd + '?chat_id={}&text={}'.format(chid,txt) + "&reply_markup={}")
                    print('111')
                else:
                    message = 'Wrong Order'
                    cmd = "sendMessage"
                    txt = quote(message.encode('utf-8'))
                    resp = urlopen(URL + cmd +
                                   '?chat_id={}&text={}'.format(chid, txt))

                line = decoder(resp)
                chek = json.loads(line)

                if chek['ok']:
                    uid = upds['result'][0]['update_id']
                    cmd = 'getUpdates'
                    urlopen(URL + cmd + '?offset={}'.format(uid + 1))
        elif 'callback_query' in upds['result'][0]:
            command = upds['result'][0]['callback_query']['data']
            chid = upds['result'][0]['callback_query']['data']['chat']['id']
            if command == 'callback_query':
                message= "'answer is ANSWER'"
                cmd='sendMessage'
                txt= quote(message.encode('utf-8'))
                keyboard={'imline_keyboadr':[[{'text':'query','url':'http://yahoo.com'}],[{'text':'IO','callback_data':'func1'}]]}
                keyboards=json.dumps(keyboard)
                resp=urlopen(URL +cmd + '?chat_id={}&text={}'.format(chid, txt)+'&reply_markup={}'.format(keyboards))


                #elif command == "موجودی": pass
            uid = upds['result'][0]['update_id']
            cmd = 'getUpdates'
            urlopen(URL + cmd + '?offset={}'.format(uid + 1))
        else:
            uid = upds['result'][0]['update_id']
            cmd = 'getUpdates'
            urlopen(URL+cmd+'?offset={}'.format(uid+1))
    print("!!WAITING!!")
    time.sleep(2)
