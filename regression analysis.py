import pandas as pd
import statsmodels.api as sm
import os

# Step 1: Load the Excel file
file_path = r'C:\Users\Administrator\Downloads\correlation analysis\Excel input\dummy.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# Step 2: Define the independent variables (anticipation, self-confidence, driving skill)
X = df[['anticipation', 'self_confidence', 'driving_skill']]

# Step 3: Add a constant term for the intercept
X = sm.add_constant(X)

# Step 4: Define the dependent variable (driving score)
y = df['driving_score']

# Step 5: Fit the regression model
model = sm.OLS(y, X).fit()

# Step 6: Print the regression results
print(model.summary())

summary = model.summary()

# Step 7: Extract specific results into a DataFrame-friendly format
results_dict = {
    'Parameters': model.params,
    'Standard Errors': model.bse,
    'P-Values': model.pvalues
}

# Step 8: Store additional single-value statistics as a separate DataFrame
single_value_stats = pd.DataFrame({
    'Stat': ['R-Squared', 'Adjusted R-Squared', 'F-Statistic', 'Prob (F-Statistic)', 'Log-Likelihood', 'AIC', 'BIC'],
    'Value': [model.rsquared, model.rsquared_adj, model.fvalue, model.f_pvalue, model.llf, model.aic, model.bic]
})

# Extract the file name from the input path
input_file_name = os.path.basename(file_path).replace('.xlsx', '')
output_folder = r'C:\Users\Administrator\Downloads\correlation analysis\Excel output'

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Step 9: Save the regression results to Excel
excel_output_file_path = os.path.join(output_folder, f'Regression_Results_{input_file_name}.xlsx')

with pd.ExcelWriter(excel_output_file_path, engine='openpyxl') as writer:
    # Save regression results in different sheets
    pd.DataFrame(results_dict).to_excel(writer, sheet_name='Regression Results', index=True)
    single_value_stats.to_excel(writer, sheet_name='Statistics', index=False)

print(f'Regression results saved to: {excel_output_file_path}')

# Step 10: Save the full summary as a text file
text_output_file_path = os.path.join(output_folder, f'Regression_Summary_{input_file_name}.txt')

with open(text_output_file_path, 'w') as f:
    f.write(summary.as_text())

print(f'Summary saved to: {text_output_file_path}')