from art import logo
import random

def black_jack ():
  computer_card3=0
  computer_card4=0
  user_card4=0
  user_card3=0
  print(logo)
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  for user in range(2):
    user_cards1=0
    user_cards1=cards[random.randint(0,len(cards)-1)]
    user_cards2=0
    user_cards2=cards[random.randint(0,len(cards)-1)]
    score=user_cards1+user_cards2
  print(f"The users two cards are: [{user_cards1},{user_cards2}]= {score}")
  for user in range(2):
    computer_card1=0
    computer_card1=cards[random.randint(0,len(cards)-1)]
    computer_card2=cards[random.randint(0,len(cards)-1)]
    score1=computer_card1+computer_card2
  print(f"The computers card is: [{computer_card1}]") 
  if score==21:
    print(f'[{computer_card1},{computer_card2}]= {score1}')
    print ("Black jack YOu win!")
    return ""
  elif score1==21:
    print(f'[{computer_card1},{computer_card2}]= {score1}')
    print ("Black Jack Computer wins")
    return ""
  card_slect=input("Do you want another card?Type 'y' or 'n' ")
  flag=True
  if card_slect=='y':
    flag=True
    user_card3=0
  else:
    flag=False
    user_card3=0
  while flag:
    user_card3=cards[random.randint(0,len(cards)-1)]
    score+=user_card3
    print(f"THe user cars are: [{user_cards1},{user_cards2},{user_card3}]= {score}")
    if score>21:
       print(f'The computers cards are: [{computer_card1},{computer_card2}]= {score1}')
       print("YOu Bust, Computer wins")
       again=input("Do you want to play again? 'y' for yes and 'n' for no")
       if again=='y':
         print(black_jack())
    # return " "
       
    card_slect=input("Do you want another card?Type 'y' or 'n' ")
    if card_slect=='y':
      flag=False
      user_card4=0
      user_card4=cards[random.randint(0,len(cards)-1)]
      score+=user_card4
    if card_slect=="n":
      flag=False
      computer_card3=0
  if score1<=16:
    flag1=True
    computer_card3=0
    while flag1:
      computer_card3=cards[random.randint(0,len(cards)-1)]
      score1+=computer_card3
      computer_card4=0
      if score1<16:
        flag1=False
        computer_card4=cards[random.randint(0,len(cards)-1)]
        score+=computer_card4
      elif score1>21:
        flag1=False
        print(f"THe user cars are: [{user_cards1},{user_cards2},{user_card3}]= {score}")
        if computer_card4>0:
          print(f"The computers cards are: [{computer_card1},{computer_card2},{computer_card3},{computer_card4}= {score1}")
        else:
          print("Computer bust, You win!")
          print(f"The computers cards are: [{computer_card1},{computer_card2},{computer_card3}]= {score1}")
          again=input("Do you want to play again? 'y' for yes and 'n' for no")
          if again=='y':
            print(black_jack())
        return ""
      else:
        flag1=False
  if score1>score and score1<=21 and score<=21:
    if user_card4==0 and computer_card4==0:
      print(f"THe user cars are: [{user_cards1},{user_cards2},{user_card3}]= {score}")
      print(f'The computers cards are: [{computer_card1},{computer_card2},{computer_card3}]= {score1}')
    elif user_card4>0 and computer_card4==0:
      print(f"THe user cars are: [{user_cards1},{user_cards2},{user_card3},{user_card4}]= {score}")
      print(f'The computers cards are: [{computer_card1},{computer_card2},{computer_card3}]= {score1}')
    elif user_card4==0 and computer_card4>0:
      print(f"THe user cars are: [{user_cards1},{user_cards2},{user_card3}]= {score}")
      print(f'The computers cards are: [{computer_card1},{computer_card2},{computer_card3},{computer_card4}]= {score1}')
    elif user_card4>0 and computer_card4>0:
      print(f"THe user cars are: [{user_cards1},{user_cards2},{user_card3},{user_card4}]= {score}")
      print(f"The computers cards are [{computer_card1},{computer_card2},{computer_card3},{computer_card4}]= {score1}")
    elif user_card3==0 and computer_card3==0:
      print(f"THe user cars are: [{user_cards1},{user_cards2}]= {score}")
      print(f"The computers cards are [{computer_card1},{computer_card2}]= {score1}")
    elif user_card3==0 and computer_card3>0:
      print(f"THe user cars are: [{user_cards1},{user_cards2}]= {score}")
      print(f'The computers cards are: [{computer_card1},{computer_card2},{computer_card3}]= {score1}')
    elif user_card3>0 and computer_card3==0:
      print(f"THe user cars are: [{user_cards1},{user_cards2},{user_card3}]= {score}")
      print(f'The computers cards are: [{computer_card1},{computer_card2}]= {score1}')
    elif user_card3>0 and computer_card3>0:
      print(f"THe user cars are: [{user_cards1},{user_cards2},{user_card3}]= {score}")
      print(f"The computers cards are [{computer_card1},{computer_card2},{computer_card3}]= {score1}")
    print("Computer wins!")
    again=input("Do you want to play again? 'y' for yes and 'n' for no")
    if again=='y':
      print(black_jack())
    else:
      return ''
  elif score1==score and score1<=21 and score<=21:
    if user_card4==0 and computer_card4==0:
      print(f"THe user cars are: [{user_cards1},{user_cards2},{user_card3}]= {score}")
      print(f'The computers cards are: [{computer_card1},{computer_card2},{computer_card3}]= {score1}')
    elif user_card4>0 and computer_card4==0:
      print(f"THe user cars are: [{user_cards1},{user_cards2},{user_card3},{user_card4}]= {score}")
      print(f'The computers cards are: [{computer_card1},{computer_card2},{computer_card3}]= {score1}')
    elif user_card4==0 and computer_card4>0:
      print(f"THe user cars are: [{user_cards1},{user_cards2},{user_card3}]= {score}")
      print(f'The computers cards are: [{computer_card1},{computer_card2},{computer_card3},{computer_card4}]= {score1}')
    elif user_card4>0 and computer_card4>0:
      print(f"THe user cars are: [{user_cards1},{user_cards2},{user_card3},{user_card4}]= {score}")
      print(f"The computers cards are [{computer_card1},{computer_card2},{computer_card3},{computer_card4}]= {score1}")
    elif user_card3==0 and computer_card3==0:
      print(f"THe user cars are: [{user_cards1},{user_cards2}]= {score}")
      print(f"The computers cards are [{computer_card1},{computer_card2}]= {score1}")
    elif user_card3==0 and computer_card3>0:
      print(f"THe user cars are: [{user_cards1},{user_cards2}]= {score}")
      print(f'The computers cards are: [{computer_card1},{computer_card2},{computer_card3}]= {score1}')
    elif user_card3>0 and computer_card3==0:
      print(f"THe user cars are: [{user_cards1},{user_cards2},{user_card3}]= {score}")
      print(f'The computers cards are: [{computer_card1},{computer_card2}]= {score1}')
    elif user_card3>0 and computer_card3>0:
      print(f"THe user cars are: [{user_cards1},{user_cards2},{user_card3}]= {score}")
      print(f"The computers cards are [{computer_card1},{computer_card2},{computer_card3}]= {score1}")
    print("Game Draw")
    again=input("Do you want to play again? 'y' for yes and 'n' for no")
    if again=='y':
      print(black_jack())
    else:
      return  ""
  elif score1<score and score1<=21 and score<=21:
    if user_card4==0 and computer_card4==0:
      print(f"THe user cars are: [{user_cards1},{user_cards2},{user_card3}]= {score}")
      print(f'The computers cards are: [{computer_card1},{computer_card2},{computer_card3}]= {score1}')
    elif user_card4>0 and computer_card4==0:
      print(f"THe user cars are: [{user_cards1},{user_cards2},{user_card3},{user_card4}]= {score}")
      print(f'The computers cards are: [{computer_card1},{computer_card2},{computer_card3}]= {score1}')
    elif user_card4==0 and computer_card4>0:
      print(f"THe user cars are: [{user_cards1},{user_cards2},{user_card3}]= {score}")
      print(f'The computers cards are: [{computer_card1},{computer_card2},{computer_card3},{computer_card4}]= {score1}')
    elif user_card4>0 and computer_card4>0:
      print(f"THe user cars are: [{user_cards1},{user_cards2},{user_card3},{user_card4}]= {score}")
      print(f"The computers cards are [{computer_card1},{computer_card2},{computer_card3},{computer_card4}]= {score1}")
    elif user_card3==0 and computer_card3==0:
      print(f"THe user cars are: [{user_cards1},{user_cards2}]= {score}")
      print(f"The computers cards are [{computer_card1},{computer_card2}]= {score1}")
    elif user_card3==0 and computer_card3>0:
      print(f"THe user cars are: [{user_cards1},{user_cards2}]= {score}")
      print(f'The computers cards are: [{computer_card1},{computer_card2},{computer_card3}]= {score1}')
    elif user_card3>0 and computer_card3==0:
      print(f"THe user cars are: [{user_cards1},{user_cards2},{user_card3}]= {score}")
      print(f'The computers cards are: [{computer_card1},{computer_card2}]= {score1}')
    elif user_card3>0 and computer_card3>0:
      print(f"THe user cars are: [{user_cards1},{user_cards2},{user_card3}]= {score}")
      print(f"The computers cards are [{computer_card1},{computer_card2},{computer_card3}]= {score1}")
    print("You win!")
    again=input("Do you want to play again? 'y' for yes and 'n' for no")
    if again=='y':
      print(black_jack())
    else:
      return ''
print(black_jack())
    
    
