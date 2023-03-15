from coin import playWithCoin




def play():
    while True:
        try:
            coin_amount = float(input("Enter Money amount: "))
            if coin_amount < 1:
                print("Money cannot be 0 or less")
                continue
            break
        except:
            print("Error: invalid money amount")
    x =  playWithCoin(coin_amount)
    


def main():
    print("Welcome to Accounting Calc")
    play()


if __name__ == "__main__":
    main()