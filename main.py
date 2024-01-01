password = 7982

old_pass = int(input("Enter Old Password : "))
new_pass = int(input("Enter New Password : "))
new_pass2 = int(input("Enter again new Password : "))


if old_pass == password:
    if new_pass == new_pass2:
        done = str(input("Yoy Haw a Changed a Password?y/n"))
        if done == "y":
            password = new_pass
            print(f"Your Password Has Been successfully Changed : {new_pass}")
        elif done == "n":
            exit()
        else:
            print("Your password change request has been cancelled")
    else:
        print("The entered password is not equal to repeating it")
else:
    print("The Password Entered Is Incorrect")