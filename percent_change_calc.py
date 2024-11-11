# Data containing all the weeks, formatted as an array
data = {
    "0mL": [
        [9.20, 10.98, 7.38, 7.20, 8.32],  # Week 0
        [12.35, 13.76, 13.78, 13.50, 13.98],  # Week 1
        [0, 0, 0, 0, 0] # Week 2
        # Future weeks can be added here
    ],
    "5mL": [
        [9.96, 9.33, 7.90, 7.94, 9.26],
        [14.50, 14.50, 13.00, 14.68, 13.96],
        [0, 0, 0, 0, 0]
    ],
    "10mL": [
        [7.80, 8.08, 9.74, 7.63, 8.18],
        [11.85, 12.24, 13.40, 12.70, 12.80],
        [0, 0, 0, 0, 0]
    ],
    "15mL": [
        [11.40, 9.24, 8.63, 8.03, 4.88],
        [14.60, 13.50, 14.08, 13.08, 8.83],
        [0, 0, 0, 0, 0]
    ],
    "20mL": [
        [8.75, 7.76, 7.45, 9.02, 8.32],
        [12.02, 12.82, 13.88, 16.20, 10.00],
         [0, 0, 0, 0, 0]
    ]
}
# Empty array which will store info for % change for each week
percent_change_table = {}

# Creates the percent table
def create_percent_table():
    for i in range(1, len(data["0mL"])):
        # Create a key for each week difference
        week_key = f"week_{i - 1} - week_{i}"
        if week_key not in percent_change_table:
            percent_change_table[week_key] = {
                '0mL': [],
                '5mL': [],
                '10mL': [],
                '15mL': [],
                '20mL': []
            }

# Calculates the percent change for the data provided
def percent_change(data):
    # Create percent table
    create_percent_table()
    
    # For every concentration/reading
    for conc, reading in data.items():
        # For every sample in each reading
        for i in range(1, len(reading)):
            # For every data point in each sample 
            for j in range(5):
                new_value = reading[i][j]
                old_value = reading[i - 1][j]
                week_key = f"week_{i - 1} - week_{i}"
                
                # This is just to avoid the divided by 0 error 
                try:                    
                    # You can change the format to whatever you wish
                    percent_change = int(round((new_value - old_value) / old_value, 2) * 100)
                except:
                    print("Divided by 0 error!")
                
                # Appends to the percent change table
                percent_change_table[week_key][conc].append(percent_change)

# Call function
percent_change(data)

# Shows table after finding percent change
for week_key, changes in percent_change_table.items():
    for conc, values in changes.items():
        print(f"{week_key} ({conc}): {values}")
    print("\n")
