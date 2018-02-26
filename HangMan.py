import random

guess=[]

word_arr=[]

tries=4

words=["guerilla", "haberdashery", "insistent", "consistent", "hickey", "fabulous", "quintessential", "acquiesce",
       "intricate", "composition", "delicate", "metamorphosis"]

wc=random.randint(0,(len(words)-1))

word=list(words[wc])

    
print("Your word has %d letters"% len(word))

lw=len(word)

while lw > 0:
    guess.append("_ ")
    lw=lw-1

print(guess)
   
while guess != word_arr and tries > 0:

    x=input("Enter a letter: ")
    count=0
    for i in range(len(word)):
        
        if x==word[i]:
            guess.pop(i)
            guess.insert(i,str(x))
            
        else:
            count=count+1
            
    if count == len(word):
        tries=tries-1
        print("INCORRECT GUESS. YOU HAVE %d tries left." % (tries) )
    
    print(guess)
            
if guess == word_arr:
    print("Aye you won!")

elif tries==0:
    print("The man has well and truly been executed. Sorry!")
