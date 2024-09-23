import random, csv

# File path to save the CSV file
file_path = "./random_data.csv"

# Generate random data in the format requested
def generate_random_row():
    col1 = random.randint(1, 2, 3)
    col2 = random.randint(1000371, 1001371)
    col3 = round(random.uniform(0.5, 10.0), 1)
    col4 = round(col3 * random.uniform(3, 6), 2)  # Make column 4 somewhat dependent on column 3
    col5 = random.choice(["Y", "N"])
    return (col1, col2, col3, col4, col5)

# Generate 100 random rows
rows = [generate_random_row() for _ in range(100)]

# Save to a CSV file
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["col1", "col2", "col3", "col4", "col5"])  # Writing the header
    writer.writerows(rows)
