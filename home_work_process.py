import os 
import multiprocessing

def print_numbers(num):
    try:
        for i in range(num + 1):
            print(i)
    except ValueError as e:
        print("Something went wrong: " + str(e) + ". Please enter a valid integer.")  # Error message

def main():
    print("The main PID is " + str(os.getpid()) + " and the main parent's PID is " + str(os.getppid()))
    
    try:
        num = int(input("Enter a valid number: "))  # Requesting a number from the user in the main process
        process = multiprocessing.Process(target=print_numbers, args=(num,))  # argument
        process.start()
        process.join()
    except ValueError as e:
        print("Something went wrong: " + str(e) + ". Please enter a valid integer.")  # Error message for invalid input

if __name__ == "__main__":   
    main()
