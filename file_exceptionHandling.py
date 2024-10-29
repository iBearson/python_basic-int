def read_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            numbers = [float(line.strip()) for line in file]
        return numbers
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except ValueError:
        print("Error: The file contains invalid number format.")
        return None

def write_results_to_file(filename, total, average):
    try:
        with open(filename, 'w') as file:
            file.write(f"Sum: {total}\n")
            file.write(f"Average: {average}\n")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def main():
    input_filename = "numbers.txt"
    output_filename = "results.txt"

    numbers = read_numbers_from_file(input_filename)
    
    if numbers is not None:
        total = sum(numbers)
        average = total / len(numbers) if numbers else 0
        
        write_results_to_file(output_filename, total, average)
        print("Results written to 'results.txt'.")
    else:
        print("Failed to process the input file.")

if __name__ == "__main__":
    main()
