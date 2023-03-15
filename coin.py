

def playWithCoin(coins):
    '''print("playing with "+str("{:.2f}".format(coins, 2))+" coins")
    for i in range(1,4):
        print("do you want to pay: "+str("{:.2f}".format(coins+i, 2)))
    '''
    print("Accounting :")
    f = "{:.2f}".format
    fed_unem = round(coins*(0.008), 2) 
    state_unem = round(coins*(0.054), 2)
    social = round(coins*(0.062), 2)
    med = round(coins*(0.0145), 2)
    net_pay = coins - (social+med)
    print("Social Security Tax: "+str(f(social)))
    print("Medicare Tax: "+str(f(med)))
    print("Federal Unemployment Tax: "+str(f(fed_unem)))
    print("State Unemployment Tax: "+str(f(state_unem)))
    
    check = input("type \"exit\" to exit, or enter anything to continue: ")
    check = check.lower().strip()
    if (check == "exit"):
        return
    

    