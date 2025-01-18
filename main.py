class Main:
    def __init__(self):
        self.running = True
        self.options =  {"1", "2", "3", "4", "5"}

    def run(self):
        print("Welcome to the python calculator")
        print("Please select an option")
        while self.running:
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit \n")

            print("Enter your option:")
            option = input()

            if option not in self.options:
                print("Invalid option")
                continue

            match option:
                case "1":
                    print("Enter the first number:")
                    num1 = int(input())
                    print("Enter the second number:")
                    num2 = int(input())
                    print(f"The sum of {num1} and {num2} is {num1 + num2} \n")
                case "2":
                    print("Enter the first number:")
                    num1 = int(input())
                    print("Enter the second number:")
                    num2 = int(input())
                    print(f"The difference of {num1} and {num2} is {num1 - num2} \n")
                case "3":
                    print("Enter the first number:")
                    num1 = int(input())
                    print("Enter the second number:")
                    num2 = int(input())
                    print(f"The product of {num1} and {num2} is {num1 * num2} \n")
                case "4":
                    print("Enter the first number:")
                    num1 = int(input())
                    print("Enter the second number:")
                    num2 = int(input())
                    if num1 == 0 or num2 == 0:
                        print("Division by zero is not allowed \n")
                        continue
                    print(f"The division of {num1} and {num2} is {num1 / num2} \n")
                case "5":
                    print("Exiting calculator... \n")
                    self.running = False





if __name__ == "__main__":
    main = Main()
    main.run()