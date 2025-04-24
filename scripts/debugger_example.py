import numpy as np
import sys

def calculate_stats(data):
    """Calculates meand and standard deviation."""

    if not isinstance(data, np.ndarray):
        data=np.array(data)

    mean = np.mean(data)
    std_dev = np.std(data)
    varince = np.var(data)

    intermediate=(data-mean)/std_dev

    result = np.sum(intermediate**2) / (len(data)-1)

    print(f"Data :{data}")
    print(f"Mean :{mean:.2f}")
    print(f"Standard Deviation :{std_dev:.2f}")
    print(f"Variance :{varince:.2f}")
    print(f"Calculated Result(like variance?): {result:.2f}")

    return mean, std_dev

if __name__ == "__main__":
    # my_list=[1,5,3,8,2,9,4,7,6,0]

    my_list=["a","b","c"] # Uncomment to test bug

    m,s=calculate_stats(my_list)

    print("---Function Finished---")