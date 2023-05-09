def arraytask():
    array = ["", "", "", "", "", ""]
    for i in range(0, 6):
        array[i] = i
    print(array)
    for i in range(5, -1, -1):
        print(array[i])

def search_array(array, value):
    for i in range(0, len(array)):
        if array[i] == value:
            return i
    return -1

def search_2darray(array, value):
    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            if array[i][j] == value:
                return i
    return -1

def grid_game():
    global grid
    grid = [["", "","",""], ["", "", "",""], ["", "", "",""], ["", "", "",""], ["", "", "",""],["", "", "",""]]
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            grid[i][j] = "-"
    print(grid)


def update_grid(grid, x, y):
    grid[x][y] = "X"
    return grid

def car_park_gen():
    # 10 rows numbered 1-10 with 6 spaces each

    # 1. Create a 2D array to represent the car park
    # 2. Create a function to print the car park
    # 3. Create a function to add a car to the car park

    car_park = ["", "", "", "", "", "", "", "", "", ""] # 10 rows
    for i in range(0, len(car_park)):
        car_park[i] = ["", "", "", "", "", ""]
    for i in range(0, len(car_park)):
        for j in range(0, len(car_park[i])):
            car_park[i][j] = "-"

    return car_park


def print_car_park(car_park):
    for i in range(0, len(car_park)):
        for j in range(0, len(car_park[i])):
            print(car_park[i][j], end=" ")





def add_car(car_park, row, space):
    car_park[row][space] = "X"
    return car_park

if __name__ == "__main__":
    c = car_park_gen()
    print_car_park(c)
    add_car(c, 1, 2)
    print_car_park(c)






