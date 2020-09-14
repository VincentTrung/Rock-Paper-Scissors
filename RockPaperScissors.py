import random

playing = True

while playing:
    print ('Welcome to Rock, Paper, Scissors. Press any key to play against a bot')
    print ()
    score = 0 #track score
    loss = 0

    while playing:
        bot = random.randint(1, 3)  # randomize bot
        if bot == 1:
            COM = 'r'
        elif bot == 2:
            COM = 'p'
        else:
            COM = 's'
        print ("Press 'r' for rock, 'p' for paper, and 's' for scissors.")
        ans = input()

        #find winner
        if ans == COM:
            outcome = 'tied'
        elif (ans == 'r' and COM == 's') or (ans == 'p' and COM == 'r') or (ans == 's' and COM == 'p'): #all win scenarios
            outcome = 'won'
            score += 1
        elif (COM == 'r' and ans == 's') or (COM == 'p' and ans == 'r') or (COM == 's' and ans == 'p'):  # all lose scenarios
            outcome = 'lost'
            loss += 1
        else:
            print('invalid entry.')
            continue

        #make readable
        if ans == 'r':
            ans = 'Rock'
        elif ans == 's':
            ans = "Scissor"
        elif ans == 'p':
            ans = 'Paper'

        if COM == 'r':
            COM = 'Rock'
        elif COM == 's':
            COM = "Scissor"
        elif COM == 'p':
            COM = 'Paper'

        #UI / score
        print(' SCORE: ', score,'/', loss)
        print('PLAYER: ', ans)
        print('   BOT: ', COM)
        print('You ', outcome, ' this round.')

        print ()
        print("Press '0' to reset score, 'q' to quit, or any other key to continue")
        play = input()
        if play == '0':
            score = 0
            loss = 0
        elif play == 'q':
            playing = False
        else:
            continue
        print()
        print()

    print ('Thank you for playing!')
