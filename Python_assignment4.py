def read_and_modify_file(input_filename, output_filename):
    
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
        
        modified_content = content + "\n\nModified by Python script!"

        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"File modified successfully. New content written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read/write to the file '{input_filename}' or '{output_filename}'.")

def main():
    input_filename = input("Enter the filename to read: ")
    output_filename = input("Enter the output filename to write the modified content: ")

    read_and_modify_file(input_filename, output_filename)

if __name__ == "__main__":
    main()
