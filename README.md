# Library-Stock-verification
A set  of python scripts that can help you analyse the stock verification data in the Library using Excel as an input file
1. transform_excel.py converts columns to single row
change in these two lines

# Specify the input and output file paths
input_file = 'dvd.xlsx'  # Replace with your input Excel file path
output_file = 'stockdvd.xlsx'  # Replace with your desired output Excel file path

2. merge.py merges all the excel sheets into one sheet with all columns
Change in these two lines

# Define input files and output file path
input_files = ['oteama.xlsx', 'oteamb.xlsx', 'oteamc.xlsx', 'oteamd.xlsx', 'oteame.xlsx', 'oteamf.xlsx', 'oteamg.xlsx', 'oteamh.xlsx', 'oteamj.xlsx', 'circ.xlsx', 'lost.xlsx']  # List of Excel files to process
output_file = 'combined_output.xlsx'

3. svfinal1.py checks with the stock taken and stock available and output as sv file with status, missing accnos, duplicates, and accession number outside the stock series

# Load the input file and the reference stock file
input_file = 'gen.xlsx' - the actual accnos list
stock_file = 'stockgen.xlsx' -  the stock taken list of accnos, rackno, team details etc.
output_file = 'svgen.xlsx' - the output file with status of missing

4. dup.py will check the duplicates from the stock table and share with the details

# Load the input Excel file
input_file = 'stockcd.xlsx'  # Replace with your input file name - this is the complete stock file
output_file = 'duplicates_output.xlsx'  # Output file name - this is the output file

