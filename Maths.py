import matplotlib.pyplot as plt
#before running this, you should install matplotlib by opening CMD (command prompt) and typing the prompt:
#pip install matplotlib
#wait for it to install, then run this code.
#Jazakallah

'''
This Python program allows the user to analyze and visualize
linear recurrence sequences of degree 1 or 2.
The main function, main(), interacts with the user to input
the degree of the recurrence relation and relevant coefficients.

For degree 1, it computes and writes the sequence to a file,
while for degree 2, it handles a two-term initialization and
then generates the sequence. The program analyzes each sequence
to determine whether it's increasing, decreasing, constant,
up-and-down oscillating, converging, or diverging.

Finally, it plots the sequence and displays its characteristics
using Matplotlib, helping users explore and understand the behavior of
linear recurrence sequences.
'''
# Function to solve a degree 2 recurrence relation and write the sequence to a file
def solve_and_write_to_file2(file_name, a0, a1, c1, c2, n):
    sequence = [a0, a1]  # Initialize with a0 and a1 for degree 2
    with open(file_name, 'w') as writer:
        writer.write(str(a0) + '\n')
        writer.write(str(a1) + '\n')
        for i in range(2, n):
            current_term = (c1 * sequence[i - 1]) + (c2 * sequence[i - 2])
            writer.write(str(current_term) + '\n')
            sequence.append(current_term)
    return sequence

# Function to solve a degree 1 recurrence relation and write the sequence to a file
def solve_and_write_to_file(file_name, a0, c, n):
    sequence = []
    with open(file_name, 'w') as writer:
        current_term = a0
        for _ in range(n):
            writer.write(str(current_term) + '\n')
            sequence.append(current_term)
            current_term = c * current_term
    return sequence

# Function to analyze a sequence and print its characteristics
def analyze_sequence(sequence):
    increasing = decreasing = constant =converging = diverging = True
    up_down = False

    for i in range(1, len(sequence)):
        if sequence[-i] > sequence[i]:
          increasing = constant = False
          decreasing = True
        elif sequence[-i] < sequence[i]:
          decreasing = constant = False
          increasing = True
        else:
          increasing = decreasing = False
          constant = True
    for i in range(1, len(sequence)):
        if i > 1 and ((sequence[i] > sequence[i - 1] and sequence[i - 1] < sequence[i - 2])
               or (sequence[i] < sequence[i - 1] and sequence[i - 1] > sequence[i - 2])):
          up_down = True

        elif abs(sequence[i]) >= abs(sequence[i - 1]):
          converging = False

        elif abs(sequence[i]) <= abs(sequence[i - 1]):
          diverging = False

    print("\nAnalysis of the sequence:")
    print("Increasing:", "yes" if increasing else "no")
    print("Decreasing:", "yes" if decreasing else "no")
    print("Constant:", "yes" if constant else "no")
    print("Up-down:", "yes" if up_down else "no")
    print("Diverging:", "yes" if diverging else "no")
    print("Converging:", "yes" if converging else "no")

    # Plot the sequence
    plt.plot(sequence)
    plt.title("Recurrence Graph")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid() 
    plt.show()

# Main function to interact with the user and call the appropriate functions
def main():
    while True:
        degree = int(input("Enter the degree (1 or 2) or 0 to exit: "))
        
        if degree == 0:
            break
        elif degree == 1:
            # User input for recurrence relation
            print(f"Linear Recurrence Relation of Degree {degree}")
            a0 = float(input("Enter the initial value a0: "))
            c = float(input("Enter the coefficient c: "))
            n = int(input("Enter the number of terms in the sequence: "))

            # Solve and write recurrence relation to file
            sequence = solve_and_write_to_file(f"degree{degree}_sequence.txt", a0, c, n)
            analyze_sequence(sequence)

        elif degree == 2:
            print(f"Linear Recurrence Relation of Degree {degree}")

            # User input for degree 2 recurrence relation
            print("\nLinear Recurrence Relation of Degree 2: an = c1 * an-1 + c2 * an-2")
            a0 = float(input("Enter the initial value a0: "))
            a1 = float(input("Enter the initial value a1: "))
            c1 = float(input("Enter the coefficient c1: "))  # Fix the variable name here
            c2 = float(input("Enter the coefficient c2: "))  # Fix the variable name here
            n2 = int(input("Enter the number of terms in the sequence: "))

            # Solve and write degree 2 recurrence relation to file
            sequence2 = solve_and_write_to_file2(f"degree{degree}_sequence.txt", a0, a1, c1, c2, n2)  # Fix the function call
            analyze_sequence(sequence2)
        else:
            print("WRONG INPUT, TRY AGAIN, Degree 1 or Degree 2?")

if __name__ == "__main__":
    main()
