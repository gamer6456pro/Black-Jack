import random
userHand=[]
dealerHand=[]
doubleOnce=0
with open('Chips.txt','r') as f:
    Chips=f.read()
#This function just takes the deck and removes the brackets and makes it look better. 
def FormatDeckSoItLookGood():
    counter=0
    showndeck1=''
    for x in deck:
        counter+=1
        if counter==0:
            continue
        elif counter%4==0:
            showndeck1+=''.join(x)+'\n'
        elif counter%4!=0:
            showndeck1+=''.join(x)+" "
        
    return showndeck1
#This just makes the dealer or user hand look better
def format_dealer_user_hand(x):
    localUserHand = userHand[:]
    localDealerHand = dealerHand[:]
    RandomLengthOfLocalDealerHand=random.randrange(0,2)
    if x=='user':
        localUserHand=' '.join(localUserHand)
        return localUserHand
    elif x=='dealer':
        localDealerHand=' '.join(localDealerHand)
        return localDealerHand
    elif x=='specialDealer':
        return localDealerHand[RandomLengthOfLocalDealerHand]+' [Face down card]'
        


def Sum_of_dealer_user_hand(x):
    dealerHandMath=[]
    userHandMath=[]
    while True:
        if x=='dealer':
            dealerHandMath=[]
            for Integer in dealerHand:
                for replace in [' Hearts', ' Spades', ' Clubs', ' Diamonds']:
                    Integer = Integer.replace(replace,'')
                Integer=int(Integer)
                dealerHandMath.append(Integer)
            try:
                global SumOfDealerHandMath
                SumOfDealerHandMath=sum(dealerHandMath)
            except:
                print('Sum not valid!')
            if SumOfDealerHandMath<17:
                card=random.choice(deck)
                index=deck.index(card)
                removedCard=deck.pop(index)
                dealerHand.append(removedCard)
            if SumOfDealerHandMath>=17 and SumOfDealerHandMath<=21:
                return 'done'
            if SumOfDealerHandMath>21:
                return 'bust'    
            
        elif x=='user':
            for Integer in userHand:
                for replace in [' Hearts', ' Spades', ' Clubs', ' Diamonds']:
                    Integer = Integer.replace(replace,'')
                Integer=int(Integer)
                userHandMath.append(Integer)
            global SumOfUserHandMath
            SumOfUserHandMath=sum(userHandMath)
            if SumOfUserHandMath>21:
                return 'bust'
            return 'no bust'
    



deck=[]
showndeck=[]
print('Welcome to black jack!')
while True:
    try:
        Bet=int(input('How many chips do you want to bet? You currently have '+str(Chips)+' chips. You can go into debt in terms of chips\n'))
        if Bet<0:
            Bet=abs(Bet)
    except ValueError:
        print('\nYou must input a integer!')
        continue
    break
Chips=int(Chips)
Chips-=Bet
#deck1 is a local variable and not the actual deck
for rank in ["1","2","3","4","5","6","7","8","9",'10']:
    for suit in ['Hearts','Spades','Clubs','Diamonds']:
        deck1=rank,suit
        deck1=' '.join(deck1)
        deck.append(deck1)
        showndeck.append(deck1)
'''TOdo: give out cards, and read more of the rule'''
for x in range(2):
    card=random.choice(deck)
    index=deck.index(card)
    removedCard=deck.pop(index)
    userHand.append(removedCard)
for y in range(2):
    card=random.choice(deck)
    index=deck.index(card)
    removedCard=deck.pop(index)
    dealerHand.append(removedCard)
print('This is the dealer\'s hand: '+format_dealer_user_hand('specialDealer')+'\nThis is your hand: '+format_dealer_user_hand('user'))
while True:
    if Sum_of_dealer_user_hand('user')=='bust':
        print('You have busted!')
        with open('Chips.txt','w') as f:
            print('You have lost',str(Bet),'chips!')
            f.write(str(Chips))
        break
    choice=input('Choose to [stand], [hit], [check], [double] down, read the [rules], or [quit]')
    if choice=='hit': 
        card=random.choice(deck)
        index=deck.index(card)
        removedCard=deck.pop(index)
        userHand.append(removedCard)
        print ('This card has been drawn!',removedCard)
    elif choice=='check':
        while True:
            choiceType=input('Check both [hands] or the possible [cards] that you can draw:')
            if choiceType=='hands':
                print('\nThis is the dealer\'s hand: '+format_dealer_user_hand('specialDealer')+'\nThis is your hand: '+format_dealer_user_hand('user'))
                break
            elif choiceType=='cards':
                print('These are the possible cards that you can draw:\n' + FormatDeckSoItLookGood())
                break
            else:
                print('Invalid input!')
                continue
        continue
    elif choice=='stand':
        if Sum_of_dealer_user_hand('dealer')=='bust':
             print('The dealer totaled',str(SumOfDealerHandMath)+'!\nHe has busted!')
             with open('Chips.txt', 'w') as f:
                 print('You have gained',str(Bet),'chips!')
                 Chips+=Bet*2
                 f.write(str(Chips))
             break
        elif Sum_of_dealer_user_hand('dealer')=='done':
            if SumOfDealerHandMath>SumOfUserHandMath:
                print('You have lost! The dealer toatled: '+str(SumOfDealerHandMath),'\nWhile you totaled: '+str(SumOfUserHandMath))
                with open('Chips.txt','w') as f:
                    print('You have lost',str(Bet),'chips!')
                    f.write(str(Chips))
                break
            elif SumOfDealerHandMath==SumOfUserHandMath:
                print('You have tied! The dealer\'s deck totaled: '+str(SumOfDealerHandMath),'\nWhile your deck totaled: '+str(SumOfUserHandMath))
                with open('Chips.txt','w') as f:
                    print('\nYou haven\'t gained or lost any chips!')
                    Chips+=Bet
                    f.write(str(Chips))
                break
            elif SumOfDealerHandMath<SumOfUserHandMath:
                print('You have won! The dealer toatled: '+str(SumOfDealerHandMath),'\nWhile you totaled: '+str(SumOfUserHandMath))
                with open('Chips.txt', 'w') as f:
                    print('You have gained',str(Bet),'chips!')
                    Chips+=Bet*2
                    f.write(str(Chips))  
                break
    elif choice=='quit':
        print('Are you sure you want to quit?')
        quitcheck=input('Type quit again to quit. Otherwise enter any key \n')
        if quitcheck=='quit':
            Chips+=Bet
            break
        else:
            continue
    elif choice=='double':
        if doubleOnce==0:
            print('You have doubled your bet! Your total bet is now',str(Bet*2),'chips! Good luck! :)')
            Chips-=Bet
            int(Bet)*2
            doubleOnce+=1
        else:
            print('You have already doubled down! You can only do this once per game!')
            continue
    elif choice=='rules':
        print('\nIn this version of black jack there are 40 cards in total with the value of cards ranging form 1 to 10.')
        print('The goal of this game is to have your cards total as close to 21 without going over')
        print('Once you stand, the dealer will decide wether to hit or stand. If his cards total more than you, you lose, otherwise youwin!(or tie)')
        print('You can bet at the beginning. Doubling down doubles your bet during the game if you belive you have a favorable hand.')
        continue
    else:
        print('Please input a valid input!')
        continue

        #deck.pop(1) #have variable to find the thing that the random.choice found




# ----->  .pop removes a element from the list and returns it 