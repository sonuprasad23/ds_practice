class MyApplicationError(Exception):
    """Custom exception for this application."""
    pass

def perform_critical_task(condition_met):
    if not condition_met:
        raise MyApplicationError("Critical condition not met for task!")
    print("Critical task performed successfully.")

try:
    perform_critical_task(True)
    perform_critical_task(False) 
except MyApplicationError as e:
    print(f"Caught MyApplicationError: {e}")
except Exception as e:
    print(f"Caught a generic exception: {e}")