#cse 4283 assignment 2


def BMI():    #BMI calculator function
    print("Body Mass Index Calculator: Select an option \n0:Calculate BMI \n1:exit")
    while(1):
        BMI_choice = input(": ")
        if BMI_choice == "0":
            print("please enter height")
            height_ft = int(input("feet: "))
            height_in = int(input("inches: "))
            weight_lbs = int(input("please enter weight in pounds: "))
            height_in = (height_ft * 12) + height_in
            height_m = height_in *0.025
            weight_kg = weight_lbs * 0.45
            bmi = weight_kg / (height_m ** 2)
            
            if bmi <= 18.5:
                category = "underweight"
            elif bmi > 18.5 and bmi <= 24.9:
                category = "normal weight"
            elif bmi >= 25 and bmi <= 29.9:
                category = "over weight"
            elif bmi >= 30:
                category = "obese"
            print("BMI:",bmi, category)
            BMI() #returns to allow for exit or to calculate again
        elif BMI_choice == "1":
            main() #returns to main menu 

def retirement(): #retirement age calculator
    print("Retirement Age Calculator: Select an option \n0:Claculate age \n1:exit")
    while(1):
        r_choice = input(":")
        if r_choice == "0":
            age = int(input("Please enter current age: "))
            a_salary = int(input("Please enter annual salary: "))
            per_savings = int(input("Please enter personal percentage saved: "))
            goal = int(input("Please enter desired personal savings goal: "))
            p_savings = (a_salary * per_savings)*.01
            yearly_savings = (((p_savings * 35))*.01) + p_savings
            total_savings = 0
            while total_savings < goal:
                total_savings = total_savings + yearly_savings
                age += 1
            if age >= 100: #life expectancy assumed to be less than 100
                print("Savings goal can not be met.")
            else:
                print("Savings goal will be met at age",age)

            
            retirement() #returns to function menu

        elif r_choice == "1":
            main() #returns to main menu
        


def main(): #main menu function
    print("Welcome! Please select a function: \n0:Body Mass Index Calculator \n1:Retirement Calculator \n2:Exit")

    while(1):
        choice = input(": ")
        if choice == "0":
            BMI()
            break
        elif choice == "1":
            retirement()
            break
        elif choice == "2": #program can be exited here
            break
    print("Goodbye!")


main() 