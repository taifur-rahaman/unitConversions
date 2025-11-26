import operations as op
def length_conversion():
    print("Length Conversion\n1. Inches to Centimeters\n2. Feets to Meters\n3. Yards to Meters\n4. Miles to Kilometers\n0. Back to Main Menu")
    
    choice = input("Enter Your Choice: ")
    
    match choice:
        case '1':
            op.in_to_cm()
        case '2':
            op.ft_to_m()
        case "3":
            op.yd_to_m()
        case "4":
            op.miles_to_km()
        case "0":
            return
        case _:
            print("Invalid Choice. Please Try Again.\n")

def area_conversion():
    print("Area Conversion\n1. Square Inches to Square Centimeters\n2. Square Feets to Square Meters\n3. Square Miles to Square Kilometers\n4. Acres to Hectares\n0. Back to Main Menu")
    
    choice = input("Enter Your Choice: ")
    
    match choice:
        case '1':
            sqin_to_sqcm()
        case '2':
            sqft_to_sqm()
        case "3":
            sqmile_to_sqkm()
        case "4":
            acres_to_hectares()
        case "0":
            return
        case _:
            print("Invalid Choice. Please Try Again.\n")

def weight_conversion():
    print("Weight Conversion\n1. Pounds to Kilograms\n2. Ounces to Grams\n0. Back to Main Menu")
    
    choice = input("Enter Your Choice: ")
    
    match choice:
        case '1':
            pounds_to_kg()
        case '2':
            ounces_to_grams()
        case "3":
            stones_to_kg()
        case "4":
            tons_to_metric_tons()
        case "0":
            return
        case _:
            print("Invalid Choice. Please Try Again.\n")