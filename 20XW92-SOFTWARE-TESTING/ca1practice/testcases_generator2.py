import pandas as pd

data = {
    'Test Case': [1, 2, 3, 4],
    'Order Value': [5, 0, 50, 100],
    'Expected Result': ['Success message', 'Error message: "Invalid Order"', 'Error message: "Only 10 Pizza can be ordered"', 'Error message: "Invalid Order"'],
    'Equivalence Class': ['Valid Range (1 to 10)', 'Invalid Range Below 1', 'Invalid Range Above 10', 'Invalid Three-Digit Numbers']
}

df = pd.DataFrame(data)

df.to_csv('20XW92-SOFTWARE-TESTING/ca1practice/testcases2.csv', index=False)