# import pandas as pd

# # Define test cases based on BVA for the password length criteria [6-12]
# test_cases = {
#     "Test Case": [
#         "Password length less than 6",
#         "Password length exactly 6",
#         "Password length between 7 and 11",
#         "Password length exactly 12",
#         "Password length more than 12"
#     ],
#     "Input Password": [
#         "abc",   # Less than 6 characters
#         "abcdef",  # Exactly 6 characters
#         "abcdefg", # Between 7 and 11 characters (example: 7 characters)
#         "abcdefghijk", # Exactly 12 characters
#         "abcdefghijklm" # More than 12 characters
#     ],
#     "Expected Result": [
#         "Invalid - Password length less than 6",
#         "Valid - Password length exactly 6",
#         "Valid - Password length between 7 and 11",
#         "Valid - Password length exactly 12",
#         "Invalid - Password length more than 12"
#     ]
# }

# # Create a DataFrame
# df = pd.DataFrame(test_cases)

# # Save DataFrame to a CSV file
# csv_path = "20XW92-SOFTWARE-TESTING/ca1practice/testcases1.csv"
# df.to_csv(csv_path, index=False)

# csv_path

import pandas as pd

# Define the test cases
data = {
    'Test Case': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Purchase Value': [1, 50, 51, 200, 201, 500, 501, 50.01, 200.99, 500.01],
    'Expected Result': ['No discount', 'No discount', '5% discount', '5% discount', '10% discount', '10% discount', '15% discount', '5% discount', '10% discount', '15% discount'],
    'Test Type': ['Lower boundary', 'Upper boundary', 'Lower boundary', 'Upper boundary', 'Lower boundary', 'Upper boundary', 'Lower boundary', 'Just above boundary', 'Just below boundary', 'Just above boundary']
}

df = pd.DataFrame(data)

# Save DataFrame to a CSV file
csv_path = "20XW92-SOFTWARE-TESTING/ca1practice/testcases2.csv"
df.to_csv(csv_path, index=False)
