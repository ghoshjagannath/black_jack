import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

agent=[]
computer=[]
is_game_on=True



def choose_card(user):
    user.append(random.choice(cards))

# adding 2 cards simultaneously
for _ in range(2):
    choose_card(agent)
    choose_card(computer)


##Printing agent  card as well as computer first  card to help agent guess 


print(f"Agent cards are {agent}")
print(f"computer first card is {computer[0]}")

# a computer calculation function 
#where  if computer has less than 17 no  then 
# it has to take new card for game . 
# and its score above 21  then return 0 for upcomming loop 

def computer_cal(user):
    if sum(user)<17:
        choose_card(user)
        if sum(user)>21:
            return 0
        else:
            return int(sum(user))



#It is a loop which decide if player or computer win this match
agent_name=input('Type your name-->')

if sum(agent)==21:
    print('you have won it')
else:
    print("lets play game")
    # print(agent)
    ami=True
    while ami:
        ans=input('Do you want to take cards --y/n-->')
        if ans=='y':
            print('Bringing new card')
            choose_card(agent)
            if sum(agent)>21:
                print(agent)
                print('you are bust')
                break
            elif sum(agent)==21:
                print(f'You {agent_name} have won the match')
                ami=False
            else:
                pass
            print(agent)
        else:
            data=computer_cal(computer)
            if sum(agent)>data:
                print(agent,computer)
                print(f'{agent_name} has won')
                break
            else:
                print(agent,computer)
                print("computer has won")
                ami=False
            

            
