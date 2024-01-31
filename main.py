"""
Name: John Sharp
Filename: main.py
Description: 
User enters the information asked by the program to populate the object.
Checks are placed in the program to make sure the user enters the correct information type and vlaues. 

"""

class Vehicle:
    def __init__(self, type):
        self.type = type
    
    def Vehicle_type(self):
        print(f"Vehicle type: {self.type}")

class Automobile (Vehicle):
    def __init__(self, type, year, make, model, number_of_doors,type_of_roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.number_of_doors= number_of_doors
        self.type_of_roof = type_of_roof

    def Automobile_information(self):
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.number_of_doors}")
        print(f"Type of room: {self.type_of_roof}")

def main():
    #Varibles to check for correctly entered inputs
    year_check = False
    door_check = False
    roof_check = False

    type = input("Please enter the type of vehicle you have: ")
    
    while year_check == False:
        year = input("Please enter the year of the vehicle: ")
        try: #is the value a int?
            year = int(year)
            year_check = True
        except ValueError:
            print("Please enter year as a number value")
            print(" ") #used as breaks between errors or information changes

    make = input("Please enter the make of the vehicle: ")
    model = input("Please enter the model of the vehicle: ")
    
    while door_check == False:
        doors  = input("How many doors doe the vehicle have (2 or 4): ")
        if doors == "2" or doors == "4": #since input is entered as a string this forces the user to use the numeral value without forcing a change in data type
            door_check =True
        else:
            print("Please enter only 2 or 4 doors")
            print(" ")

    while roof_check == False:    
        roof = input("Which type of roof does the vehicel have (solid or sun roof): ")
        if roof == "Solid" or roof == "solid" or roof == "sun roof" or roof == "Sun roof" or roof == "Sun Roof": #allows for different capitalizations
            print(" ")
            roof_check = True
        else:
            print("Please enter one of the roof selections")
            print(" ")

    vehicel_1 = Automobile(type,year,make,model,doors,roof)
    vehicel_1.Vehicle_type()
    vehicel_1.Automobile_information()
  
if __name__ == "__main__":
    main()