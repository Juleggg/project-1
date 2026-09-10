print("jestes baba czy chlop i ile masz lat")
plec = (input())
wiek = int(input())
if plec == "chlop" and wiek >= 15 and wiek <= 17:
    print("no i ok") 
    print("ile masz wzrostu (cm)")
    wzrost = input()
    if wzrost >= "160" and wzrost <= "210":
        print("jestes moze...rudy?")
        wlosy = input()
        if wlosy == "nie":
            print("nie jest zle. ostatnie pytanie... lubisz japuszka?")
            a = input()
            if a == "tak":
                print("dobra moze cos z cb bedzie")
            else: 
                print("to co ty tu robisz")
            
        else:
            print("rudy sie nie dostal")
    else:
        print("splywaj")
else:
    print("splywaj")