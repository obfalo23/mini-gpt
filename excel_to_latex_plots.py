excel_x_cords = []
excel_y_cords = []

# function to ask for x cords from user and paste them in excel_x_cords
def ask_for_x_cords():
    print("Enter the x cords for the plot")
    print("Enter 'done' when you are done entering the x cords")
    while True:
        x_cord = input()
        if x_cord == 'done':
            break
        excel_x_cords.append(x_cord)
# function to aks for y cords form user and paste them in excel_y_cords
def ask_for_y_cords():
    print("Enter the y cords for the plot")
    print("Enter 'done' when you are done entering the y cords")
    while True:
        y_cord = input()
        if y_cord == 'done':
            break
        excel_y_cords.append(y_cord)
#function to change the comma decimal separator to dot from list of cords
def change_comma_to_dot(cords):
    for i in range(len(cords)):
        cords[i] = cords[i].replace(',','.')
    return cords



# function to join the excel_x_cords and excel_y_cords as (x,y) pairs and print them 
def print_cords():
    print("The x and y cords are:")
    for i in range(len(excel_x_cords)):
        print(f"({excel_x_cords[i]},{excel_y_cords[i]})")
 

ask_for_x_cords()
ask_for_y_cords()
excel_x_cords = change_comma_to_dot(excel_x_cords)
excel_y_cords = change_comma_to_dot(excel_y_cords)
print(excel_x_cords)
print(excel_y_cords)
print_cords()