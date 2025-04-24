def sort_file_contents(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines]
        lines.sort()
        with open(output_file, 'w', encoding='utf-8') as file:
            for line in lines:
                file.write(line + '\n')
        print(f"Contents sorted and written to {output_file}")
    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    input_file = input("Enter the name of the input file: ")
    output_file = input("Enter the name of the output file: ")
    sort_file_contents(input_file, output_file)