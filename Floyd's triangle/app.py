def floyd_maker(row):
    counter = 1
    for i in range(1,row+1):
        print(end=f"row {i} : ")
        for j in range(1,i+1):
            print(end=f" {counter} ")
            counter += 1
        print()

row = abs(int(input("Enter the number of rows you weanna see of floyd's triangle : ")))
floyd_maker(row)