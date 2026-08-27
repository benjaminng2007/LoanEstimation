import csv
from tabulate import tabulate

def description():
    print('This program will estimate your loan and calculate its basic details')

def end_program():
    choice = input('Do you want to end this program? (type Y for yes and N for no): ')
    if choice == 'Y':
        exit()
    else:
        pass

def menu():
    print('-------------------------------------------------')
    print('Please enter 1 to read your file\nPlease enter 2 to show your loan statement\nPlease enter 3 to show apr, interest paid, and total payed\nPlease enter 4 to end program.')
    print('------------------------------------------------')
    decision = int(input('Please enter a choice: '))
    print()
    return decision

class LoanStatement:
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

class UserInterface:
    def __init__(self):
        self.contents = None
        self.statement = LoanStatement()

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


    def choose(self):
        while True:
            user_choice = menu()

            if user_choice == 1:
                self.statement.read()

            elif user_choice == 2:
                self.statement.show_contents()

            elif user_choice == 3:
                print(f'Your total payed fully for the loan is ${self.statement.total_payed()}')
                print(f'Your interest paid is ${self.statement.interest_paid():.2f}')
                print(f'Your apr is {self.statement.apr()}%')

            elif user_choice == 4:
                end_program()

if __name__ == '__main__':
    description()
    menu()
    result = UserInterface()
    result.choose()






