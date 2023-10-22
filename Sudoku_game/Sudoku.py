import csv 

def choosing_csv(filename, user_choice):

    with open(filename) as sudokus:
        csv_reader = csv.reader(sudokus)
        rows = list(csv_reader)
        templist = list(rows[user_choice])
        puzzle = templist[0]
       
        return str(puzzle)


print("Hello, welcome to sudoku game")

user_choice = int(input("Choose number from 1 to 20 to select your puzzle: "))
sudoku = list(choosing_csv("sudoku.csv", user_choice))
print("This is your puzzle\n", sudoku)

