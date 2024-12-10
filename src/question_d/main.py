#add import
import question_d

def menu():
    selection = int( input( """
Stock List Menu:
1- Display Stock Report
2- Exit program
"""))
    return selection

def main():
    while True:
        choice = menu()

        if choice == 1:
            list_display = question_d.Stock.get_stock_list()
            print(f"Stock Purchase history:  \n {list_display}")
            for stock in list_display:
                print(stock.get_symbol() + ' ' + stock.get_company_name())
        elif choice == 2:
            print('Quitting...')
            break
            
        else:
            print('Invalid choice. Select 1 or 2 from menu.')
         

main()