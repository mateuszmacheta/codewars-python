def find_maximum_from_file(filename):
    try:
        with open(filename, 'r') as file:
            numbers = [int(line.strip()) for line in file]

        if numbers:
            return max(numbers)
        else:
            print("The file is empty.")
            return None
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    except ValueError:
        print("Error parsing numbers from the file.")
        return None

# Call the function and pass the filename
filename = 'nums.txt'
max_value = find_maximum_from_file(filename)

if max_value is not None:
    print(f"The maximum value from '{filename}' is: {max_value}")
