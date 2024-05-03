from add import add
from subtract import subtract
from multiply import multiply
from divide import divide
from exponentiation import exponentiation
from module import module
from sqrt import sqrt

operations = {
    1:[add, 1],
    2:[subtract, 1],
    3:[multiply, 2],
    4:[divide, 2],
    5:[exponentiation, 4],
    6:[module, 4],
    7:[sqrt, 6]
}

def main():
    score = 0
    while True:
        print("\n===== MENU =====")
        for index, value in operations.items():
            print(f"{index}. {(value[0].__name__).title()}")
        
        option = int(input("Choise an option: "))
        if option == 0:
            break
        
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: ")) if option not in [7] else None
        answer = int(input("Enter your answer: "))
        operation = operations.get(option)
        if operation:
            result = operation[0](num1, num2)
            if result and result == answer:
                score += operation[1]
                print(f"Correct +{operation[1]} points!")
            else:
                print("Incorrect")
                break
    
    print(f"\n===== GAME OVER =====\nYou score is {score}\nKeep going!")    
    

if __name__ == "__main__":
    main()