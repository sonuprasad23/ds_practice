import sys

print("Script starting...")
user_input = input("Do you want to exit early? (yes/no): ")

if user_input.lower() == 'yes':
    print("Exiting early due to user request.")
    sys.exit(0) # 0 usually means successful exit
    # sys.exit("User chose to exit.") # Can exit with a message too
    # sys.exit(1) # Non-zero for error

print("Script continued to the end.")