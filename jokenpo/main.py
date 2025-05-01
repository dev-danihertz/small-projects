from colorama import init, Fore, Style

init()

def header():
    print(Fore.CYAN + "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" + Style.RESET_ALL)
    print("This is the game called JOKENPO. Or Rock, Paper or Scissors.")
    print("You have to choose: Rock(R), Paper(P) or Scissors(S).")
    print(Fore.CYAN + "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n" + Style.RESET_ALL)

header()

p1 = input("What is the player 1 name: ")
p2 = input("What is the player 2 name: ")

winner = ''
qty_p1 = 0
qty_p2 = 0
qty_draw = 0

print(f"\nplayer 1 = {p1}")
print(f"player 2 = {p2}\n")

def next_round():
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("NEXT ROUND")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

def full_name():
    global p1_choice
    global p2_choice
    if p1_choice.upper() == "R":
        p1_choice = Fore.RED + "Rock" + Style.RESET_ALL
    elif p1_choice.upper() == "P":
        p1_choice = Fore.RED + "Paper" + Style.RESET_ALL
    elif p1_choice.upper() == "S":
        p1_choice = Fore.RED + "Scissors" + Style.RESET_ALL
    else:
        print("We found an error. You probably typed something other than R, P or S")
    if p2_choice.upper() == "R":
        p2_choice = Fore.BLUE + "RocK" + Style.RESET_ALL
    elif p2_choice.upper() == "P":
        p2_choice = Fore.BLUE + "Paper" + Style.RESET_ALL
    elif p2_choice.upper() == "S":
        p2_choice = Fore.BLUE + "Scissors" + Style.RESET_ALL
    else:
        print("We found an error. You probably typed something other than R, P or S")


def possibilities():
    global p1
    global p2
    global winner
    if p1_choice == "R" and p2_choice == "R":
        winner = "Draw"
    elif p1_choice == 'R' and p2_choice == "P":
        winner = p2
    elif p1_choice == 'R' and p2_choice == "S":
        winner = p1
    elif p1_choice == 'P' and p2_choice == "R":
        winner = p1
    elif p1_choice == 'P' and p2_choice == "P":
        winner = "Draw"
    elif p1_choice == 'P' and p2_choice == "S":
        winner = p2
    elif p1_choice == 'S' and p2_choice == "R":
        winner = p2
    elif p1_choice == 'S' and p2_choice == "P":
        winner = p1
    elif p1_choice == 'S' and p2_choice == "S":
        winner = "Draw"
    



while True:
    p1_choice = input(f"{p1}, you choose R, P or S? ").upper()
    p2_choice = input(f"{p2}, you choose R, P or S? ").upper()
    possibilities()
    full_name()
    print(f"\n{p1} chose {p1_choice} e {p2} chose {p2_choice}\n")
    print(Fore.GREEN + f"###  the winner was: {F" ### {winner} ###"}\n" + Style.RESET_ALL)

    # NUMBER OF TIMES EACH PLAYER WON
    if winner == p1:
        qty_p1 += 1
    elif winner == p2:
        qty_p2 += 1
    elif winner == "Draw":
        qty_draw += 1

    # CHOOSE IF YOU WANT TO CONTINUE THE GAME OR STOP
    to_continue = input("press Enter to continue or press Q to quit the game: ")
    if to_continue == "Q" or to_continue == 'q':
        print("you chooseu quit the game. Thank you and see you soon\n")
        print("GAME RESULTS:\n")
    
        print(f"{p1} won {qty_p1} time(s), {p2} won {qty_p2} time(s) and there were {qty_draw} draw(s).\n")
        break
    else:
        print("you chooseu to_continue")
    next_round()