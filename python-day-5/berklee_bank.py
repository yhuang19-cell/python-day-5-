bank_dict = {
    "Priya": {"balance": 100, "pin": "4821"},
    "Carlos": {"balance": 300, "pin": "1092"},
    "Amira": {"balance": 0, "pin": "0000"},
    "Jordan": {"balance": 7788, "pin": "9999"},
}
""""""
Name: print_welcome
Task: Prints the welcome message to the terminal
Input: None
Side effects(printing/display): the welcome message
Return: None

def print_welcome():
    print("Welcome to Berklee Bank!)")



""""""
Name:get_username
Task:Prompts the user for their name.
Input:None
Side effects(printing/display):Prompts user for input
Return:None

def get_username():
    name = input("What is your name?")
    return name


''''''
Name:get_pin
Task:Prompts the user for pin
Input:None
Side effect(printing/display):"What is your pin "
Return: return the pin
''''''
def get_pin():
    pin = input("What is your pin?")
    return pin

''''''
Name:Verify_Identify
Task:Take the name and pin and see if there's a valid user in the system. If so, get their data. If not, failed
Input:username, pin
Side Effect(printing/display)
Return: True if suer exists, False if not

def verify_identity(username, pin.):
    if bank_dict.get(username):
        users_values = bank_dict.get ("pin")
        return True
Print("Access Denied for", username, "with pin",pin)
return False


''''''
Name:get_menu_choice
Task:print the functionality of the bank(the commands they can do to the terminal, and ask what they want)
Input:None
Side Effect(printing/display): do you wanna deposit, withdraw, get balance, quit(they type their answer)
Return:the string the user typed in

def get_menu_choice():
    if bank_dict.get(username);
        users_values = bank_dict(username)
        balance = users

Name:deposit_money
Task:Ask the user how much they want to deposit then add that to the balance
Input:username
Side Effect(printing/display): prompting the user for the amount to deposit
Return:None

def deposit_money(username):
    deposit_amount =input("How muchwould you like to deposit?")
    if bank_dict.get(username):
        users_values = bank_dict.get("balance")
        new_bal = previous_bl + deposir_amount
        User_values.update({"balance": newbal})

Return: None

Name:withdraw_money（username)
Task:Ask the user how much they want to with draw. If they have enough, reduce balance. If not, tell them.
Input:username
Side effect(printing/display):prompts user for input and print the new balance.
Return:None

def withdraw_money(username):
    withdraw_amount = int(input("how much woudl you .iike to withdraw?"))
    if bank_dict.get(username)
    users_values = bank_dict.get(username)
        previous_bal = users_values.get ("balance")
        new_bal = previoius_bal - withdraw_amount
        if new_bal < 0:
            print("Insufficient funds...")
        else:
            users_values.update({"balance": new_bal})

Name:quit







def run_test():
    withdraw_money("Priya") #Ask for amount, if 200 fail
    withdraw_money("Priya") #Ask for amount, if 100 should succeed

    deposit_money("Priya") #Ask for amount, if 100 should succeed

    get_balance("Priya") #Print $100

    verify_identity("Priya")

    def main():
    print_welcome()
    name = get_username()
    pin = get_pin()
    valid = verify_identity(name, pin)
    if not valid:
        print("Access Denied")
        return
    while True:
        choice = get_menu_choice()
        if users_choice == "balance":
            get_balance(name)

        elif users_choice == "withdraw":
            withdrawe_money(name)

        elif users_choice == "deposit":
            deposit_money(name)
        
        elif users_choice == "quit":
            break

        else:
            print("You can't choose that...")





