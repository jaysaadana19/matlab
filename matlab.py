import matlab.engine

def calculate_square_root(number):
    try:
        eng = matlab.engine.start_matlab()
        result = eng.sqrt(number)
        return result
    finally:
        eng.quit()

if __name__ == "__main__":
    input_number = float(input("Enter a number: "))
    square_root = calculate_square_root(input_number)
    print(f"The square root of {input_number} is {square_root}")
