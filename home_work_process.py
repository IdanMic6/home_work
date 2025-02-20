import os 
import multiprocessing
import time


def print_numbers(num, queue):
    try:
         queue.put(num)
         for i in range(num + 1):
            print(i)
           
    except ValueError as e:
        print("Something went wrong: " + str(e) + ". Please enter a valid integer.")  # Error message

def main():
    print("The main PID is " + str(os.getpid()) + " and the main parent's PID is " + str(os.getppid()))
    
    try:
        num = int(input("Enter a valid number: "))  # Requesting a number from the user in the main process
        queue = multiprocessing.Queue() #created a queue 

        process = multiprocessing.Process(target=print_numbers, args=(num, queue))
        process.start()
        time.sleep(10)
        process.join()
        return_from_process = queue.get()
        print("The process returned " + str(return_from_process))
        print("Done")
        
    except ValueError as e:
        print("Something went wrong: " + str(e) + ". Please enter a valid integer.")  # Error message for invalid input

if __name__ == "__main__":   
    main()
