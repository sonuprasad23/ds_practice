# day12/log_analyzer.py
import sys
import json
from collections import Counter
from datetime import datetime # Not strictly needed for this parsing, but good to remember

def parse_log_line(line: str) -> str | None:
    """Parses a log line to extract the level.
    Returns log level string or None if format is incorrect."""
    parts = line.strip().split()
    if len(parts) >= 3: # Expect at least Date, Time, Level
        # Simple check, more robust parsing would use regex or datetime.strptime
        # For this exercise, assume level is the 3rd part
        return parts[2].upper() # Convert to uppercase for consistency
    return None

def analyze_logs(log_filepath: str) -> Counter:
    """Reads a log file and counts occurrences of each log level."""
    level_counts = Counter()
    try:
        with open(log_filepath, 'r') as f:
            for line in f:
                level = parse_log_line(line)
                if level:
                    level_counts[level] += 1
    except FileNotFoundError:
        print(f"Error: Log file '{log_filepath}' not found.")
        sys.exit(1) # Exit with an error code
    except Exception as e:
        print(f"An error occurred during log processing: {e}")
        sys.exit(1)
    return level_counts

def save_summary(summary_data: Counter, output_filepath: str):
    """Saves the summary data (Counter object) to a JSON file."""
    try:
        with open(output_filepath, 'w') as f:
            json.dump(dict(summary_data), f, indent=4) # Convert Counter to dict for json
        print(f"Log summary saved to '{output_filepath}'")
    except IOError:
        print(f"Error: Could not write summary to '{output_filepath}'.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python log_analyzer.py <log_file_path>")
        sys.exit(1)

    log_file = sys.argv[1]
    output_json_file = "day12/log_summary.json" # Output in day12 dir

    print(f"Analyzing log file: {log_file}...")
    counts = analyze_logs(log_file)

    if counts: # If any counts were found (file processed successfully)
        print("\nLog Level Counts:")
        for level, count in counts.items():
            print(f"  {level}: {count}")
        save_summary(counts, output_json_file)
    else:
        print("No log levels found or error in processing.")



#Create one log file as Sample.log
# and then run like this:
# python3 day12/log_analyzer.py day12/sample.log 
# in your terminal
