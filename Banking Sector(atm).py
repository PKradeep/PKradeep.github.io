print"WELCOME TO MIMI BANK"
print"ENJOY YOUR BANKING"
a="pradeep"#global data declaration
b="1234"
e=50000

def condcheck(): #checking condition
           o=raw_input("TYPE 'D' FOR DEPOSIT/TYPE 'W' FOR WITHDRAWAL/TYPE 'T' FOR TRANSACTION:")  
           if(o=='d'):
                deposit()
           elif(o=='w'):
                withdrawal()
           elif(o=='t'):
                transaction()
def deposit(): #function for deposit
    global e
    print"YOUR  CURRENT ACCOUNT BALANCE IS",e
    i=int(input("ENTER YOUR DEPOSIT AMOUNT VALUE:"))
    e+=i
    print"PLEASE DEPOSIT YOUR CASH ON BLACK BOX"
    print"NOW,YOUR AVAILABLE BALANCE IS",e
    
    

def withdrawal(): #function for withdrawal
    global e
    print"YOUR  CURRENT ACCOUNT BALANCE IS",e
    g=int(input("ENTER YOUR WITHDRAWAL AMOUNT"))
    if(g<=e):
        e=e-g
        print"PLEASE COLLECT YOUR CASH"
        print"NOW,YOUR AVAILABLE BALANCE IS",e
              
    else:
        print"LIMIT EXCEED"    
def transaction(): #function for transation
    global e
    print"WELCOME",a,"FOR TRANSACTION"
    k=raw_input("ENTER YOUR IFSC CODE:")
    print"YOUR  CURRENT ACCOUNT BALANCE IS",e
    l=raw_input("ENTER ACCOUNT NUMBER FOR TRANSACTION:")
    if(l.isdigit()):
            print"THIS IS YOUR ACCOUNT NUMBER:",l
    else:
            print("YOUR ACCOUNT NUMBER IS NOT IN REQUIRED FORM")
    m=input("ENTER AMOUNT FOR TRANSACTION:")
    if(m<=e):
        e=e-m
        print"SHARING HAS  DONE SUCCESSFULLY" 
        print"NOW,YOUR AVAILABLE BALANCE IS",e

    else:
        print"LIMIT EXCEED"

i=0            #looping for login only for 3 times
while(i<3):
    c=raw_input("ENTER YOUR NAME:")
    d=raw_input("ENTER YOUR PIN:")
    if(a==c and b==d):
        print("YOUR LOGGED INN YOUR PAGE")
        break
    elif(a!=c and b==d):
        print("CHECK YOUR LOGIN-ID")
        
    elif(a==c and b!=d):
        print("CHECK YOUR LOGIN-ID")
    elif(a!=c and b!=d):
        print("YOU ARE NOT AUTHORIZED TO ACCESS THIS PAGE")
        
    else:
        print"YOU ARE NOT AUTHORIZED TO ACCESS THIS PAGE"
    i+=1
    if(i==3):
        print("LIMIT EXCEED")
if(a==c and b==d):
    condcheck()

    j=raw_input("IF YOU WANT CHANGE PASSWORD OR USERNAME:")
    if(j=='yes'):
       print"YOUR OLD USERNAME IS:",a
       print"YOUR OLD PASSWORD IS:",b
       print"TYPE 140134"
       while True:
          q=raw_input("TRY CAPTCHA:")
          if(q=='140134'):
             x=raw_input("YOUR NEW USERNAME IS:")
             y=raw_input("YOUR NEW PASSWORD:")
             a=x
             b=y
            
             
             print"YOUR NEW USERNAME/PASSWORD:",a,b
             break
            
          else:
             print"YOUR CAPTCHA IS WRONG"
          continue
    while True:        
          u=raw_input("DO YOU WANT TO CONTINUE YOUR TRANSACTION:")
          if(u=="yes"):
               condcheck()            
          elif(u=="no"):
               print("THANKS FOR CONTACTING MIMI BANK")
               break
          elif(u!='yes' or u!='no'):
               print("THANKS FOR CONTACTING MIMI BANK")
               break
          continue
        
             
