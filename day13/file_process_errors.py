def read_and_process_file(filepath: str) -> int:
    """Reads numbers from a file, sums them, handles errors."""
    total_sum = 0
    line_number = 0
    print(f"--- Starting processing for {filepath} ---")
    try:
        with open(filepath, "r") as f:
            for line in f:
                line_number += 1
                try:
                    num = int(line.strip())
                    total_sum += num
                except ValueError:
                    print(f"Warning: Could not convert line {line_number} ('{line.strip()}') to int. Skipping.")
        return total_sum
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return 0 
    except IOError as e:
        print(f"An IO error occurred reading '{filepath}': {e}")
        return 0
    finally:
        print(f"--- Processing complete for {filepath} ---")

sample_file = "day13/numbers_with_errors.txt"
with open(sample_file, "w") as f:
    f.write("10\n")
    f.write("20\n")
    f.write("abc\n") 
    f.write("30\n")
    f.write("  40 \n") 
    f.write("x50\n")  

result_sum = read_and_process_file(sample_file)
print(f"Sum of valid numbers: {result_sum}") 

result_non_existent = read_and_process_file("day13/no_such_file.txt")
print(f"Sum from non-existent file: {result_non_existent}")