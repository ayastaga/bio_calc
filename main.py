# MAIN CODE
class BioCalculator:
    def __init__(self, data, unc, decimal_place):
        self.data = data
        self.unc = unc
        self.decimal_place = decimal_place
        self.change_table = {}
        
    def create_table(self):
        for i in range(1, len(self.data["0mL"])):
            week_key = f"week_{i - 1} - week_{i}"
            if week_key not in self.change_table:
                self.change_table[week_key] = {
                    '0mL': [],
                    '5mL': [],
                    '10mL': [],
                    '15mL': [],
                    '20mL': []
                }
                
    def calculate_change_and_unc(self, new_value, old_value):
        difference = new_value - old_value
        
        percent_change = (difference / old_value) * 100
        
        numerator = abs((self.unc * 2) / difference)
        denominator = abs(self.unc / old_value)
        
        unc_change = abs((numerator + denominator) * percent_change)
        
        return round(percent_change, self.decimal_place), round(unc_change, self.decimal_place)

    def main(self):
        self.create_table()
        for conc, readings in self.data.items():
            for i in range(1, len(readings)):
                for j in range(5):
                    new_value = readings[i][j]
                    old_value = readings[i - 1][j]
                    week_key = f"week_{i - 1} - week_{i}"
                    
                    # Handles divide-by-zero error
                    try:
                        rate_change = self.calculate_change_and_unc(new_value, old_value)
                    except:
                        print("Divided by 0 error!")
                        rate_change = (None, None)

                    self.change_table[week_key][conc].append(rate_change)
 
    def display_table(self):
        for week_key, changes in self.change_table.items():
            for conc, values in changes.items():
                print(f"{week_key} ({conc}): {values}")
            print("\n")
        print("\n")

# !! FOR USER: YOU CAN CUSTOMIZE THE DATA TABLE, UNCERTAINTY VALUE (UNC), AND DECIMAL PLACE TO YOUR LIKING TO GET YOUR RESULTS !! 

data = {
    "0mL": [
        [9.20, 10.98, 7.38, 7.20, 8.32], # week 0
        [12.35, 13.76, 13.78, 13.50, 13.98], # week 1
        [0, 0, 0, 0, 0] # week 2 (sample)
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

unc = 0.05

decimal_place = 2

# INITIATES PROCESS
processor = BioCalculator(data, unc, decimal_place)
processor.main()
processor.display_table()
