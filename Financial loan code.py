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
        self.contents = None

    def read(self):
        while True:
            try:
                loan_rows = []
                file_name = input('Please enter the csv file name of your loan statement: ')
                with open(file_name) as loan_statement:
                    contents = csv.reader(loan_statement)
                    for row in contents:
                        loan_rows.append(row)
                self.contents = loan_rows
                return loan_rows

            except FileNotFoundError:
                end_program()
                print('Please enter the csv file again')

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
        interest = total_amount - loan
        print(f'{interest:.2f}')




if __name__ == '__main__':
    statement = LoanStatement()
    statement.read()
    statement.show_contents()
    print(statement.total_payed())
    statement.interest_paid()


