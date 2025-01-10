def FileHandling(input_file, output_file):
    try:
        with open(input_file, 'r') as file:  #reading the file
            content = file.read()
        word_count = len(content.split())
        with open(output_file, 'w') as file: #writing the result in new file->word_count.txt
            file.write(f"The number of words in '{input_file}' is: {word_count}")  #counting the no.of words
        print(f"Word count written to '{output_file}' successfully!") 
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "word_count.txt"
    FileHandling(input_file, output_file)
