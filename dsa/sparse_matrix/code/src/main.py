from sparse_matrix import SparseMatrix

def main():
    # Print options for the user
    print("Choose an operation to perform on two sparse matrices:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")

    # Get user's choice
    choice = input("Enter 1, 2 or 3: ").strip()

    # Get file paths from the user
    file1 = input("Enter the path to the first matrix file: ").strip()
    file2 = input("Enter the path to the second matrix file: ").strip()

    try:
        # Load the matrices from the given files
        matrix1 = SparseMatrix(filepath=file1)
        matrix2 = SparseMatrix(filepath=file2)

        # Perform the selected operation
        if choice == '1':
            result = matrix1.add(matrix2)
            print("\nResult of Addition:")
        elif choice == '2':
            result = matrix1.subtract(matrix2)
            print("\nResult of Subtraction:")
        elif choice == '3':
            result = matrix1.multiply(matrix2)
            print("\nResult of Multiplication:")
        else:
            print("Invalid option. Please enter 1, 2, or 3.")
            return

        # Print the result matrix
        print(result)

        # Ask user if they want to save the result
        save = input("\nDo you want to save the result to a file? (yes/no): ").strip().lower()
        if save == 'yes':
            output_path = input("Enter the output file path (e.g. result.txt): ").strip()
            try:
                with open(output_path, 'w') as f:
                    f.write(str(result))
                print(f"Result saved to: {output_path}")
            except Exception as e:
                print("Failed to save the file:", e)

    except Exception as error:
        print("An error occurred:")
        print(error)

# Start the program
if __name__ == '__main__':
    main()
