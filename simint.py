# simple_interest.py

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def main():
    try:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the rate of interest: "))
        time = float(input("Enter the time period (in years): "))
        interest = calculate_simple_interest(principal, rate, time)
        print(f"\nSimple Interest = {interest:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()

