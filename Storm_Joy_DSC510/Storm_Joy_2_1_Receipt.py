def calculate_total_cost(number_of_feet):

# method to calculate the total installation cost for the fiber cable
# assignment 2_1
# Joy Storm

    total_cost = number_of_feet * 0.87
    return total_cost

if __name__ == '__main__':
    print("-----------WELCOME-------------")
    # Take company name as input from user
    company_name = input(" Enter your company name ")

    # Take number of feet of fibre cable as input
    number_of_feet = int(input(" Enter the number of feet of fibre cable "))

    # call the method to calculate the total installation cost
    installation_cost = calculate_total_cost(number_of_feet)

    # print the receipt consisting of company name , number of feet and installation cost
    print("--------- Your Receipt----------- ")
    print("Company name: {}".format(company_name))
    print("Number of feet of fiber cable: {}".format(number_of_feet))
    print("Installation cost: ${}".format(installation_cost))
