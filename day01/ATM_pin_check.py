# ATM PIN CHECK [3 ATTEMPTS]

correct_pin = 3579
attempt = 0
access_granted = False

while attempt < 3:
    attempt += 1

    print(f"Attempt : {attempt}")
    pin = int(input("Enter Your Pin: "))

    if pin == correct_pin:
        print("Access Granted!")
        access_granted = True
        break
    else:
        print(f"Wrong pin! {3 - attempt} attempts left.")        

if not access_granted:
    print("Account locked")

