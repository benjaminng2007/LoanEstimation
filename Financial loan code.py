import csv
from tabulate import tabulate


def description():
    return print('This program will estimate your loan and calculate its basic details')

def end_program():
    choice = input('Do you want to end this program? (type Y for yes and N for no): ')
    if choice == 'Y':
        exit()
    else:
        pass

class Menu:
    def __init__(self):
        self.choice = None

    def menu(self):
        print('-------------------------------------------------')
        print('Please enter 1 to read your file\nPlease enter 2 to show your loan statement\nPlease enter 3 to show apr, interest paid, and total payed\nPlease enter 4 to end program.')
        print('------------------------------------------------')
        choose = int(input('Please enter a choice: '))
        print()
        return choose

class ReadFile:
    def __init__(self):
        self.contents = []

    def read(self):
        while True:
            try:
                file_name = input('Please enter the csv file name of your loan statement: ')
                with open(file_name) as loan_statement:
                    contents = csv.reader(loan_statement)
                    for row in contents:
                        self.contents.append(row)
                return self.contents

            except FileNotFoundError:
                print('File is not found, please re-enter')
                end_program()


class LoanStatement(ReadFile):
    def __init__(self):
        super().__init__()

    def show_contents(self):
        print(tabulate(self.contents, tablefmt="fancy_grid"))

    def total_payed(self):
        total_payed = 0
        for row in self.contents[1:]:
            total_payed += float(row[3])
        return total_payed

    def interest_paid(self):
        interest_paid = 0
        total_amount = self.total_payed()
        for row in self.contents[1:2]:
            loan = float(row[2])
            interest_paid = total_amount - loan
        return interest_paid

    def apr(self):
        apr = 0
        for row in self.contents[1:2]:
            first_month_interest = float(row[5])
            loan = float(row[2])
            apr = ((first_month_interest / loan) * 12) * 100
        return apr


if __name__ == '__main__':
    menu_obj = Menu()
    statement = LoanStatement()

    while True:
        user_choice = menu_obj.menu()

        if user_choice == 1:
            statement.read()

        elif user_choice == 2:
            statement.show_contents()

        elif user_choice == 3:
            print(f'Your total payed fully for the loan is ${statement.total_payed()}')
            print(f'Your interest paid is ${statement.interest_paid():.2f}')
            print(f'Your apr is {statement.apr()}%')

        elif user_choice == 4:
            end_program()




