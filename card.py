from datetime import datetime as date
from lib.DiscountCard import DiscCard

card1 = DiscCard()
try:
    exit = False
    while not exit:
        choice = int(input('\n1. Card information\n2. Buy goods with a card at a discount \n3. Information on the amount of the discount \n4. The amount for which you need to buy the product to increase the discount \n5. Exit \n\nSelect an action -> '))
        if choice == 1:
            print(f'\n\tCard number: {card1.number}\n\tDate of issue: {card1.date}\n')
        elif choice == 2:
            cost = float(input('The cost of the product you want to buy: -> '))
            card1.buy(cost)
        elif choice == 3:
            card1.disc_info()
        elif choice == 4:
            card1.disc_dif_info()
        elif choice == 5:
            print('Бувай')
            exit = True
        else:
            print('There is no such action!!!')
except:
    print('Incorrect data entered!')
    print(card1.number, card1.money, card1.disc, card1.date)

card1.buy_article(1000)
card1.buy_article(1500)
card1.buy_article(1500)
print(card1.number, card1.money, card1.disc, card1.date)

card1.discount_info()
card1.discount_inc_info()
