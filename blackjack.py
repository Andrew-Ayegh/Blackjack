import random
import arts
print(arts.welcome)
print(arts.blackjack)
game_start = True

# deck of cards
cards = [1,2,3,4,5,6,7,8,9,10,"A","K","Q","J"]

#black jack ma xnumber
blackjack = 21

# players bank
player_money = 1000
print(f"\n\n\n You have ${player_money} in your account")

#Body Of the game
while game_start:
    #player's bet to begin game 
    bet = int(input(f"\nplace your bet...minimum of $10 maximum of ${player_money}...   "))
    
    #funtion for picking a random card from deck of cards
    def random_card():
        '''selects a random card from the deck of cards'''
        card = random.choice(cards)
        return card


    player_money -= bet
    print(f"\nYou have ${player_money} left")

    def blackjack_win(bet):
        '''blackjack bet winning'''
        win = bet * 1.5
        return win

    def win(bet):
        '''calculates player bet win'''
        winning = bet * 2
        return winning

    def surrender(bet):
        '''player's cash withdrawal after surrendering'''
        sur = bet/2
        return sur
    # while game_start:
    #player's instant Blackjack winning cash out 






    dealer_cards = random.choices(cards, k=2)
    player_cards = random.choices(cards, k=2)
    # print(f"dealer: {dealer_cards}")

    print(f"\nYour cards:  {player_cards}")
    print(f"\nDealer card:[{dealer_cards[0]}, '_'] ")

    # replacing A, Q, K and J with Numbers for dealer's card
    def dealer_replace(dealer_cards):
        '''replacing the lettered cards in dealer's set of cards'''
        for card in dealer_cards:
            if card == "A":
                a_index = dealer_cards.index("A")
                dealer_cards[a_index] = 11
            elif card == "Q":
                q_index = dealer_cards.index("Q")
                dealer_cards[q_index] = 10
            elif card == "K":
                k_index = dealer_cards.index("K")
                dealer_cards[k_index] = 10
            elif card == "J":
                j_index = dealer_cards.index("J")
                dealer_cards[j_index] = 10

    dealer_replace(dealer_cards)

    #replacing A, Q, K, J with numbers for player's card
    def player_replace(player_cards):
        '''replacing the lettered cards in player's set of cards'''
        for card in player_cards:
            if card == "A":
                choice = int(input("do you want ace to be a 1 or 11?  "))
                a_index = player_cards.index("A")
                player_cards[a_index] = choice
            elif card == "Q":
                q_index = player_cards.index("Q")
                player_cards[q_index] = 10
            elif card == "K":
                k_index = player_cards.index("K")
                player_cards[k_index] = 10
            elif card == "J":
                j_index = player_cards.index("J")
                player_cards[j_index] = 10
    # calling player replacing card function 
    player_replace(player_cards)

    #sum total of player and dealer card numbers
    dealer_sum = sum(dealer_cards)
    player_sum = sum(player_cards)

    def hit(cards):
        '''adds and extra card to player or dealers card set'''
        cards.extend([random_card()])
    #Black jack Determinant
    if player_sum == blackjack and dealer_sum == blackjack:
        print("\n Draw")
        player_money += bet
        
    elif player_sum == blackjack and dealer_sum != blackjack:
        print("\nBlackjack!!!...\nYou rock🏆😉")
        player_money += blackjack_win(bet)
        
    elif player_sum != blackjack and dealer_sum == blackjack:
        print(dealer_cards)
        print("\nDealer wins...")
    else:
    #pciking what move to take next
        continue_game= True 
        while continue_game:
            play = input('''\nchoose your play...
                        use 'h' for hit,
                        's' for surrender and 
                        'st' for stand.. HIT, STAND or SURRENDER:  ''').strip().lower()

            if play == 'h':
                hit(player_cards)
                player_replace(player_cards)
                player_sum = sum(player_cards)
                print(player_cards)
                if player_sum > blackjack:
                    print(f"BUST!")
                    print("\nyou return $0")
                    continue_game = False
            
            elif play == "s":
                print("SURRENDERED")
                player_money += surrender(bet)
                print(f"DEALER: {dealer_cards}, YOU: {player_cards}")
                continue_game = False
            elif play == "st":
                while dealer_sum < 17:
                    hit(dealer_cards)
                    dealer_replace(dealer_cards)
                    dealer_sum = sum(dealer_cards)
                
                if dealer_sum > blackjack:
                    player_money += win(bet)
                    print(f"dealer card{dealer_sum} > blackjack {blackjack}")
                    print("You win!!!🏆🌟🌟")
                    continue_game = False
                elif player_sum > dealer_sum:
                    print("You Win!!")
                    player_money += win(bet)
                    continue_game = False
                elif dealer_sum > player_sum:
                    print("Dealer wins")
                    print(dealer_cards)
                    continue_game = False

        print(f'you have ${player_money} left')
        if player_money > 0:
            play_again = input("do you wish to play again? y/n  ").strip().lower()
        if play_again == 'n':
            print("goodbye, see you again :)")
            game_start = False
        if player_money <= 0:
            game_start = False
            continue_game = False


