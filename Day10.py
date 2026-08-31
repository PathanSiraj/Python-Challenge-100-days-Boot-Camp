import art
def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1-n2
def multiply (n1,n2):
    return  n1*n2
def division (n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":division
}
def calculator():
    print(art.logo)
    should_accum=True
    n1=float(input("What is your first number?"))
    while should_accum:
        for symbol in operations:
            print(symbol)
        operation_symbol=input("What is your symbol?")
        n2=float(input("What is your second number?"))
        answer=operations[operation_symbol](n1,n2)
        print(f"{n1}{operation_symbol}{n2}={answer}")
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if choice=="y":
            n1=answer
        else:
            should_accum=False
            print("\n"*20)

calculator()
