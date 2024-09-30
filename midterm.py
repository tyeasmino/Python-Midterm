from colorama import Fore, Style

# Question 1
class Star_Cinema():    
    hall_list = []
    
    @classmethod
    def entry_hall(self,hall): 
        self.hall_list.append(hall)

# Qustion 2
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        # Question 9
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no   
        super().entry_hall(self)

    # Question 3
    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)   
        self.__show_list.append(show) 
        self.__seats[id] = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)] 
    
    # Question 4
    def book_seats(self, id, row, col):
        # 8-A
        if id not in self.__seats:
            print(f"Invalid show ID")
            return
            
        # 8-B
        # check seat row, col invalid  
        if row >= self.__rows or col >= self.__cols:
            print(f"Invalid seat number")
            return

        # 8-C
        # if seat is already booked  
        if self.__seats[id][row][col] == 1:
            print(Fore.RED + f"Seat already booked" + Style.RESET_ALL)
            return

        self.__seats[id][row][col] = 1
        print(Fore.GREEN + f'Seat({row+1},{col+1}) is booked for show {id}' + Style.RESET_ALL)

    # Quesion 5
    def view_show_list(self):
        for s in self.__show_list:
            print(f"Show ID: {s[0]}, Movie name: {s[1]}, Time: {s[2]}")

    # Question 6
    def view_available_seats(self, id):
        # 8-A
        if id not in self.__seats:
            print(f"Invalid show ID")
            return

        print(f"Available seats for the show {id}:")
        for row in self.__seats[id]:
            display = ""
            for s in row:
                if s == 1:
                    display += Fore.GREEN + '1 ' + Style.RESET_ALL
                else:
                    display += Fore.RED + '0 ' + Style.RESET_ALL         
            print(display)

sc = Star_Cinema()
hall1 = Hall(6, 8, 115)  
hall1.entry_show(542, 'Tiger3', '10:00 AM')
hall1.entry_show(265, 'Tiger', '3:30 PM')
hall1.entry_show(622, 'Pathan', '6:00 PM')
hall1.entry_show(345, 'Rolex', '9:00 PM')


# Question 7
run = True
while run:
    print(f"1. VIEW ALL SHOW OF TODAY")
    print(f"2. VIEW AVAILABLE SEATS")
    print(f"3. BOOK TICKET")
    print(f"4. EXIT")

    op = int(input(f'ENTER OPTION: '))
    if op == 1:
        print(f"-----------------------")
        hall1.view_show_list()
        print(f"-----------------------")
        
    elif op == 2:
        showid = int(input("ENTER SHOW ID: "))
        print(f"-----------------------")
        hall1.view_available_seats(showid)
        print(f"-----------------------")

    elif op == 3:
        bs = int(input("Enter show id: "))
        row = int(input("Enter seat row: "))
        col = int(input("Enter seat column: ")) 
        hall1.book_seats(bs, row-1, col-1)

    elif op == 4:
        run = False