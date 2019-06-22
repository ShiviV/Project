from random import randint

player=input("Rock(r),Paper(p),Scissors(s)")
if (player=='r'):
    print('r')
elif (player=='p'):
    print('---')
elif(player=='s'):
    print('>8')

else:
    print("Wrong input")

print('Computers choice')

c=randint(1,3)

if(c==1):
    computer='r'
    print('O')
elif(c==2):
    computer='p'
    print('---')

else:
    computer='s'
    print('>8')
 


if(player==computer):
   print('Hah!no one wins')
        
    
    
elif(player=='r' and computer=='s'):
     print('Player wins')
        
    
    
elif(player=='r' and computer=='p'):
     print('Computer wins')
        
    
elif(player=='s' and computer=='p'):
     print('Player wins')
        
    
    
elif(player=='s' and computer=='r'):
     print('Computer wins')
       
    

elif(player=='p' and computer=='r'):
     print('Player wins')
        
    

elif(player=='p' and computer=='s'):
     print('Computer wins')
        
    

else:
    print('Huh')
        

    
 
    
    