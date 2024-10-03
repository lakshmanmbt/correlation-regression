import pandas as pd

# Step 1: Load the Excel file
file_path = r'C:\Users\Administrator\Downloads\correlation analysis\Excel input\BHARATHI (763).xlsx'
# Replace 'your_file.xlsx' with the actual file path
df = pd.read_excel(file_path)

# Correlation matrix
correlation_matrix = df.corr()
print(correlation_matrix)
