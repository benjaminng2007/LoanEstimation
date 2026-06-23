import csv

def readfile():
    while True:
        try:
            loan_rows = []
            file_name = input('Please enter the csv file name of your loan statement: ')
            with open(file_name) as loan_statement:
                contents = csv.reader(loan_statement)
                for row in contents:
                    loan_rows.append(row)
            return loan_rows
        except FileNotFoundError:
            print('Please enter the csv file again')


def main():
    list2d = readfile()


if __name__ == '__main__':
    main()

