import pandas as pd

# Define input files and output file path
input_files = ['team_a.xlsx', 'team_b.xlsx', 'team_c.xlsx', 'team_d.xlsx','team_e.xlsx', 'team_f.xlsx', 'team_g.xlsx', 'team_h.xlsx', 'childrenbook.xlsx', 'circ.xlsx', 'cddvd.xlsx', 'techrep.xlsx','thesis.xlsx', 'lost2025.xlsx']  # List of Excel files to process
output_file = 'combined_output.xlsx'


# Initialize an empty list to store DataFrames
dfs_to_concat = []

# Iterate through each Excel file
for file_name in input_files:
    print(f"Processing file: {file_name}")
    
    # Read all sheets from the current Excel file into a dictionary of DataFrames
    try:
        sheets_dict = pd.read_excel(file_name, sheet_name=None, dtype={'accno': str})
    except Exception as e:
        print(f"Error reading {file_name}: {str(e)}")
        continue
    
    # Iterate through each sheet and extract the desired columns
    for sheet_name, df in sheets_dict.items():
        print(f" - Sheet: {sheet_name}")
        
        # Check if both 'accno', 'rackno', and 'team' columns exist in the current sheet
        if 'accno' in df.columns and 'rackno' in df.columns and 'team' in df.columns:
            print(f"   - Found 'accno', 'rackno', and 'team' columns")
            
            # Ensure 'accno' column is stored as string (object)
            df['accno'] = df['accno'].astype(str)
            
            # Append 'accno', 'rackno', and 'team' columns to the list
            dfs_to_concat.append(df[['accno', 'rackno', 'team']])
        else:
            print(f"   - Either 'accno', 'rackno', or 'team' column not found")

# Concatenate all DataFrames in the list
if dfs_to_concat:
    combined_df = pd.concat(dfs_to_concat, ignore_index=True)
    
    # Identify duplicates in the combined DataFrame
    duplicate_rows = combined_df[combined_df.duplicated(subset=['accno'], keep=False)]
    
    # Save the combined DataFrame and duplicates to a new Excel file
    try:
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            combined_df.to_excel(writer, sheet_name='Combined Data', index=False)
            duplicate_rows.to_excel(writer, sheet_name='Duplicates', index=False)
        print(f"Combined data and duplicates saved to {output_file}")
    except Exception as e:
        print(f"Error saving to {output_file}: {str(e)}")
else:
    print("No data found to combine.")
