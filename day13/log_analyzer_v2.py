# day13/log_analyzer_v2.py
import sys
import json
from collections import Counter
from datetime import datetime

class InvalidLogFormatError(Exception): # Custom Exception
    """Raised when a log line does not conform to the expected format."""
    pass

LOG_LEVEL_ORDER = {"INFO": 1, "WARNING": 2, "ERROR": 3} # For min_level filtering

def parse_log_line(line: str) -> tuple[datetime | None, str | None]:
    """Parses a log line to extract timestamp and level.
    Returns (timestamp_obj, log_level_str) or (None, None) if format is incorrect.
    Raises InvalidLogFormatError for fundamental format issues.
    """
    parts = line.strip().split(maxsplit=2) # Split into at most 3 parts: date, time, rest
    if len(parts) < 3:
        raise InvalidLogFormatError(f"Line too short: '{line.strip()}'")

    date_str, time_str, message_part = parts
    try:
        timestamp = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print(f"Warning: Invalid date/time format in line: '{line.strip()}'")
        return None, None # Cannot parse timestamp

    # Level is assumed to be the first word of message_part
    level_parts = message_part.split(maxsplit=1)
    if not level_parts:
        raise InvalidLogFormatError(f"Missing level and message: '{line.strip()}'")
    
    level = level_parts[0].upper()
    if level not in LOG_LEVEL_ORDER:
        print(f"Warning: Unknown log level '{level}' in line: '{line.strip()}'")
        return timestamp, None # Valid timestamp, but unknown level

    return timestamp, level


def analyze_logs(log_filepath: str, min_level_str: str | None = None) -> Counter:
    level_counts = Counter()
    min_level_val = 0
    if min_level_str:
        min_level_val = LOG_LEVEL_ORDER.get(min_level_str.upper(), 0)
        if min_level_val == 0:
            print(f"Warning: Invalid --min-level '{min_level_str}'. Ignoring filter.")

    try:
        with open(log_filepath, 'r') as f:
            for i, line in enumerate(f, 1):
                try:
                    timestamp, level = parse_log_line(line)
                    if level:
                        current_level_val = LOG_LEVEL_ORDER.get(level, 0)
                        if current_level_val >= min_level_val:
                            level_counts[level] += 1
                except InvalidLogFormatError as e:
                    print(f"Warning (Line {i}): Malformed log entry. {e}")
                # Other ValueErrors from strptime are handled in parse_log_line

    except FileNotFoundError:
        print(f"Error: Log file '{log_filepath}' not found.")
        sys.exit(1)
    except IOError as e:
        print(f"An IO error occurred processing '{log_filepath}': {e}")
        sys.exit(1)
    return level_counts

def save_summary(summary_data: Counter, output_filepath: str):
    try:
        with open(output_filepath, 'w') as f:
            json.dump(dict(summary_data), f, indent=4)
        print(f"Log summary saved to '{output_filepath}'")
    except IOError:
        print(f"Error: Could not write summary to '{output_filepath}'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python log_analyzer_v2.py <log_file_path> [--min-level LEVEL]")
        sys.exit(1)

    log_file = sys.argv[1]
    min_level_filter = None

    if "--min-level" in sys.argv:
        try:
            idx = sys.argv.index("--min-level")
            min_level_filter = sys.argv[idx + 1]
        except IndexError:
            print("Error: --min-level option requires a LEVEL argument (INFO, WARNING, ERROR).")
            sys.exit(1)

    output_json_file = "day13/log_summary_v2.json"

    print(f"Analyzing log file: {log_file}...")
    counts = analyze_logs(log_file, min_level_filter)

    if counts:
        print("\nLog Level Counts:")
        for level, count in counts.items():
            print(f"  {level}: {count}")
        save_summary(counts, output_json_file)
    else:
        print("No matching log levels found or error in processing.")