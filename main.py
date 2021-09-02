import csv as csv
import math

spreadsheet_file_path = "todo.csv"
priority_map = {
    '1': 'A',
    '2': 'B',
    '3': 'C'
}
output_string = ""

print('Converting CSV file to Org-mode file')

def getEffort(raw_effort):
    print(raw_effort)
    raw_effort = float(raw_effort)
    hours = math.floor((raw_effort * 60 / 60))
    minutes = math.floor((raw_effort * 60) - (hours * 60))
    # If a minute is equal to zero, then we need to treat it as a string
    # and add an extra zero. E.g.: '00' instead of '0'
    if minutes == 0:
        minutes = str(minutes) + '0'
    return f'{hours}:{minutes}'

with open(spreadsheet_file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are: {", ".join(row)}')
        else:                
            # Setup the values
            task_id = row[0]
            task_feature = row[1]
            task_step = row[2]
            task_effort = getEffort(row[5])
            task_priority = priority_map[row[6]]
            # Construct the output string
            output_string += f'* DO {task_feature}: {task_step}\n'
            output_string += f'   :PROPERTIES:\n'
            output_string += f'   :Effort:   {task_effort}\n'
            output_string += f'   :END:'
            output_string += '\n\n'
        # Advance the counter
        line_count += 1

print(output_string)
# Write the string to our org file
with open('todo.org', 'w') as f:
    f.write(output_string)
    f.close()

print("Org-mode file created! Have a nice day.")
    
