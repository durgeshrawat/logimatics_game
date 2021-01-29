import random,time,os
maths_operators=['+','-','*','/','//','%']
nolist=['great !','nice !','great !','excellent !','good !','supup !']
score_file=os.path.isfile('/sdcard/test_yourbrain_score')
if score_file==False:
	f=open('/sdcard/test_yourbrain_score','w')
	f.write('0')
	f.close()
else :
	pass

def cl():
	try:
		os.system('clear')
	except:
		os.system('clr')
class gamelevel():
	def easy():
		score=0
		while True:
			print('\t\t\033[0;37;41m  LOGIMATICS  \033[0;37;40m\t')
			print('   '+'-'*15,'SCORE',score,'-'*15)
			op=random.randint(0,2)
			no1=random.randint(0,10)
			no2=random.randint(0,10)
			print(' ',no1,maths_operators[op],no2)
			ans1=eval(str(no1)+str(maths_operators[op])+str(no2))
			ans=int(input('  = '))
			if ans1==ans :
				score+=1
				no=random.randint(0,len(nolist)-1)
				print(' ',nolist[no])
			else :
				score-=1
				print('oops ! sorry try again ! after 3 seconds')
				print('Ans is :',ans1)
				time.sleep(1)
				for b in range(3,0,-1):
					time.sleep(1)
					print('try in '+str(b)+' seconds #')
			time.sleep(1)
			f=open('/sdcard/test_yourbrain_score','r')
			F=f.readlines()
			F=F[0]
			if score > int(F) :
				f=open('/sdcard/test_yourbrain_score','w')
				f.write(str(score))
				f.close()
			cl()
	def medium():
		score=0
		while True:
			print('\t\t\033[0;37;41m  LOGIMATICS  \033[0;37;40m\t')
			print('   '+'-'*15,'SCORE',score,'-'*15)
			op=random.randint(0,4)
			no1=random.randint(0,10)
			no2=random.randint(0,10)
			print(' ',no1,maths_operators[op],no2)
			ans1=eval(str(no1)+str(maths_operators[op])+str(no2))
			ans=int(input('  = '))
			if ans1==ans :
				score+=1
				no=random.randint(0,len(nolist)-1)
				print(' ',nolist[no])
			else :
				score-=1
				print('oops ! sorry try again ! after 3 seconds')
				print('Ans is :',ans1)
				time.sleep(1)
				for b in range(3,0,-1):
					time.sleep(1)
					print('try in '+str(b)+' seconds #')
			time.sleep(1)
			f=open('/sdcard/test_yourbrain_score','r')
			F=f.readlines()
			F=F[0]
			if score > int(F) :
				f=open('/sdcard/test_yourbrain_score','w')
				f.write(str(score))
				f.close()
			cl()
	def hard():
		score=0
		while True:
			print('\t\t\033[0;37;41m  LOGIMATICS  \033[0;37;40m\t')
			
			print('   '+'-'*15,'SCORE',score,'-'*15)
			op=random.randint(0,5)
			no1=random.randint(0,10)
			no2=random.randint(0,10)
			print(' ',no1,maths_operators[op],no2)
			ans1=eval(str(no1)+str(maths_operators[op])+str(no2))
			ans=str(input('  = '))
			if ans1==ans :
				score+=1
				no=random.randint(0,len(nolist)-1)
				print(' ',nolist[no])
			else :
				score-=1
				print('oops ! sorry try again ! after 3 seconds')
				print('Ans is :',ans1)
				time.sleep(1)
				for b in range(3,0,-1):
					time.sleep(1)
					print('try in '+str(b)+' seconds #')
			time.sleep(1)
			f=open('/sdcard/test_yourbrain_score','r')
			F=f.readlines()
			F=F[0]
			if score > int(F) :
				f=open('/sdcard/test_yourbrain_score','w')
				f.write(str(score))
				f.close()
			cl()

level="""
            
            \033[0;30;42m      #LEVEL SELECT#     \033[0;37;40m 
            \033[0;30;47m   [1]  EASY             \033[0;37;40m
            \033[0;30;47m   [2]  MEDIUM           \033[0;37;40m
            \033[0;30;47m   [3]  HARD             \033[0;37;40m
           
           """
bye="""
                                            
     | \033[0;30;41m  BYE BYE USER WITH EXIT COMMAND  \033[0;37;40m |
                                         
     """
def core():
    print("""
     \033[1;33;40m                                     
     \033[0;37;41m             LOGICMATICS             \033[1;33;40m 
     \033[0;37;41m          coded by DURGESH           \033[1;33;40m 
     \033[0;30;46m    -------------------------------  \033[1;33;40m 
     \033[0;34;46m    [1]  START                       \033[1;33;40m 
     \033[0;34;46m    [2]  HIGH SCORE                  \033[1;33;40m 
     \033[0;34;46m    [3]  HELP & MANUAL               \033[1;33;40m 
     \033[0;34;46m    [4]  ABOUT                       \033[1;33;40m 
     \033[0;34;46m    [5]  EXIT                        \033[1;33;40m 
                                           \033[0;37;40m
    """)
    choice=input('  > ')
    if choice == '1':
    	cl()
    	print(level)
    	choose_level=input('  > ')
    	if choose_level=='1':
    		cl()
    		time.sleep(1)
    		print('loading ...')
    		time.sleep(1)
    		print('constructing EASY lavel ...')
    		time.sleep(3)
    		cl()
    		try :
    			gamelevel.easy()
    		except :
    			print('  🚫 invalid entery redirecting on HOME WINDOW !')
    			time.sleep(1)
    	elif choose_level=='2':
    		cl()
    		time.sleep(1)
    		print('loading ...')
    		time.sleep(1)
    		print('constructing MEDIUM level ..')
    		time.sleep(3)
    		cl()
    		gamelevel.medium()
    		try :
    			gamelevel.medium()
    		except :
    			print('  🚫 invalid entery redirecting on HOME WINDOW !')
    			time.sleep(1)
    	elif choose_level=='3':
    		cl()
    		time.sleep(1)
    		print('loading ...')
    		time.sleep(1)
    		print('constructing HARD level ..')
    		time.sleep(3)
    		cl()
    		gamelevel.hard()
    		try :
    			gamelevel.hard()
    		except :
    			print('  🚫 invalid entery redirecting on HOME WINDOW !')
    			time.sleep(1)
    	else:
    		pass
    elif choice=='2':
    	cl()
    	f=open('/sdcard/test_yourbrain_score','r')
    	F=f.readlines()
    	F=F[0]
    	f.close()
    	print("""
        \033[0;30;47m    YOUR HIGH SCORE IS       \n\033[0;37;40m        \033[0;30;47m            """,F,"""             \033[0;37;40m""");print('\n   💡 Press Enter to go back On main Screen ');zz=input();cl();core()
    elif choice=='3':
    	cl()
    	print("""
    	[1] HOW TO START GAME
    	
    	As you open menu of help and manual
    	same as it enter command 1 to Start
    	game and then you face a level Select
    	window Then in this you have to select
    	level and BOOM ! you entered in game 
    	now enjoy game .
    	______________________________________
    	
    	[2] HOW TO QUIT FROM ANY WINDOW
    	
    	No need to know this becoz it is  
    	developed in USER FRIENDELY BEHAVIOUR
    	BY ME , but if You want know so 
    	press 5 To exit { if you want to exit
    	in select level Menu press any of your
    	wanted string as prompt value in front
    	of > it .
    	______________________________________
    	
    	""")
    	pre=input('\n	press any key to return HOME SCREEN ')
    	cl()
    	core()
    elif choice=='4':
    	cl()
    	print("""
                    \033[0;30;47m  ABOUT  \033[0;30;47m \033[0;37;40m
    	hello user,
    	It is game about imporoving your basic
    	maths calculations calculating quality
    	
    	developer""")
    	pre=input('\n	press any key to Return HOME SCREEN ')
    	cl()
    	core()
    elif choice=='5':
    	cl()
    	print(bye)
    	exit()
	  	
while True :
	core()
	time.sleep(1)
	cl()
	print('\n  ❌ INVALID ENTERY\n  press ENTER key to go on HOME WINDOW')
	en=input('\n  > ')
	cl()

