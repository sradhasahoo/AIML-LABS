import csv

# Load dataset
with open(r"C:\Users\sradhanjali sahoo\OneDrive\Desktop\workload_data.csv") as file:
    reader = csv.reader(file)
    data = list(reader)

# Separate header and data
header = data[0]
rows = data[1:]

# Attributes are all columns except the target
attributes = header[:-1]
target = header[-1]

# Initialize hypothesis with the most specific values
hypothesis = ["Ø"] * len(attributes)

print("Find-S Algorithm")
print("-" * 50)

# Process each training example
for row in rows:

    # Get attributes and target value
    instance = row[:-1]
    target_value = row[-1].strip().lower()

    # Process only positive examples
    if target_value == "yes":

        for i in range(len(attributes)):

            # If hypothesis is empty, take the value
            if hypothesis[i] == "Ø":
                hypothesis[i] = instance[i]

            # If values are different, generalize to ?
            elif hypothesis[i] != instance[i]:
                hypothesis[i] = "?"

        print("Processed:", row)
        print("Hypothesis:", hypothesis)
        print()

# Final hypothesis
print("-" * 50)
print("Final Most Specific Hypothesis:")
print(hypothesis)