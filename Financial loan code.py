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
        return print(f'{interest_paid:.2f}')

    def apr(self):
        apr = 0
        for row in self.contents[1:2]:
            first_month_interest = float(row[5])
            print(first_month_interest)
            loan = float(row[2])
            print(loan)
            apr = ((first_month_interest / loan) * 12) * 100
        return print(apr)




if __name__ == '__main__':
    statement = LoanStatement()
    statement.read()
    statement.show_contents()

    print(statement.total_payed())
    statement.interest_paid()
    statement.apr()


