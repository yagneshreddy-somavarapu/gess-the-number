import random as rn
rand = rn.randint(1,25)
count = 0
while True:
   count += 1
   try :
        print("Guess the number in between 1 to 25")
        num = int(input())
        if num == rand:
           print(f'congrats you Won on {count}\'th attempt.')
           break
        elif rand > num:
           print("To low")
        elif rand < num:
           print("To high")
   except ValueError:
      print("lease Enter Valid Number")
     
   
