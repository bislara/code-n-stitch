inp = input("please enter the text")

print("The original string : " + inp) 
  

res = [int(i) for i in inp.split() if i.isdigit()] 
# this basically makes a list of all the numbers

for i in res:
    if len(str(i))==10:
        print("the phone number in the text is:" + str(i))


