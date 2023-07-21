#6511171_Wai_Yan_Paing_542_class03_as3
shopping = int(input("Enter shopping amount (in Baht): "))
hours = int(input("Enter hours: "))
minutes =  int(input("Enter minutes: "))

# 120 + 24 = 144 % 30 = 24
#            144 / 30 = 4

# 120 + 54 = 174 % 30 = 24
#            174 / 30 = 5

first_condition = hours * 60 + minutes - 120
second_condition = hours * 60 + minutes - 60
third_condition = hours * 60 + minutes

if ( shopping >= 1500):

    if ( third_condition / 30 <= 4):

        print("The parking fee for the first 2 hours is free. You don't have to pay.")

    elif ( third_condition / 30 > 4):

        print("The parking fee is 30 baht.")

elif ( shopping >= 500):

    if ( minutes == 0 or first_condition % 30 == 0):

        print(f"The parking fee for the first 2 hours is free. You have to pay {(first_condition // 30) * 30 } Baht for the parking fee.")


    elif ( first_condition / 30 >= 1 or first_condition % 30 < 30 or first_condition % 30 > 0 ):

        print(f"The parking fee for the first 2 hours is free. You have to pay {((first_condition // 30) + 1) * 30 } Baht for the parking fee.")
    
    
elif (shopping < 500):
    if ( minutes == 0 or second_condition % 30 == 0):
        
        print(f"The parking fee for the first hour is free. You have to pay {(second_condition // 30) * 30 } Baht for the parking fee.")


    elif( second_condition / 30 >= 1 or second_condition % 30 < 30 ):

        print(f"The parking fee for the first hour is free. You have to pay {((second_condition // 30) + 1) * 30 } Baht for the parking fee.")