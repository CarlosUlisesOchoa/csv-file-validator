import csv
import os
from datetime import datetime
import time

# Open the log file
with open('log.txt', 'a') as log_file:

    # Create the output directory if it doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')

    print("", file=log_file)

    # Loop through all the CSV files in the "input" directory
    for filename in os.listdir('input'):
        if filename.endswith('.csv'):
            # Print date, time, and file being processed
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Processing file: {filename}...", file=log_file)

            skipped_rows = 0

            # Start measuring time
            start_time = time.time()

            input_filepath = os.path.join('input', filename)
            output_filepath = os.path.join('output', filename)

            # Read the header to find the correct number of columns
            with open(input_filepath, 'r', encoding='utf-8') as infile:
                reader = csv.reader(infile)
                header = next(reader)
                correct_num_commas = len(header) - 1

            # Read each row and only write out the valid ones
            with open(input_filepath, 'r', encoding='utf-8') as infile, open(output_filepath, 'w', encoding='utf-8', newline='') as outfile:
                reader = csv.reader(infile)
                writer = csv.writer(outfile)

                # Skip header in the input file
                next(reader)

                # Write the header to the output CSV
                writer.writerow(header)

                # Check each row for the correct number of commas
                for line_number, row in enumerate(reader, start=1):
                    num_commas = len(row) - 1
                    if num_commas == correct_num_commas:
                        writer.writerow(row)
                    else:
                        truncated_row = ','.join(row)[:20]  # Convert the row back to a string and slice the first 20 characters
                        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Skipped invalid row in {filename} at line {line_number + 1}: {truncated_row}...", file=log_file)
                        skipped_rows += 1

            # End measuring time and calculate elapsed time
            elapsed_time = time.time() - start_time

            # Print date, time, and completion message
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Completed processing file: {filename}", file=log_file)
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Processed in {elapsed_time:.2f} seconds", file=log_file)
            if skipped_rows > 0:
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {skipped_rows} invalid rows skipped", file=log_file)
            print("")
            print("Script finished.")
            print("")
