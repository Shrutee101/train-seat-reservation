class TrainCoach:
    def __init__(self):
        self.seats = []
        for i in range(10):
            row = [0] * 7
            if i == 9:
                row = [0] * 3
            self.seats.append(row)
    
    def __str__(self):
        res = ""
        for i, row in enumerate(self.seats):
            res += f"Row {i+1}: {' '.join(str(s) for s in row)}\n"
        return res
    
    def reserve(self, num_seats):
        for i, row in enumerate(self.seats):
            consecutive = 0
            start = -1
            for j, seat in enumerate(row):
                if seat == 0:
                    if consecutive == 0:
                        start = j
                    consecutive += 1
                    if consecutive == num_seats:
                        for k in range(start, start+num_seats):
                            self.seats[i][k] = 1
                        return f"Reserved {num_seats} seats in row {i+1}, seats {start+1} to {start+num_seats}"
                else:
                    consecutive = 0
        return "Sorry, could not reserve seats together. Trying booking nearby seats."
        

coach = TrainCoach()
while True:
    print(coach)
    num_seats = int(input("Enter number of seats to book: "))
    if num_seats > 7:
        print("Sorry, you can book up to 7 seats at a time.")
        continue
    result = coach.reserve(num_seats)
    if "Sorry" in result:
        print(result)
    else:
        print(result)
        response = input("Do you want to book more seats? (y/n)")
        if response.lower() == "n":
            break
