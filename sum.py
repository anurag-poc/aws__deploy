import csv

def process_csv(input_file, output_file):
    with open(input_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        rows = []

        for row in csvreader:
            a = float(row[0])
            b = float(row[1])
            c = a + b
            row.append(c)
            rows.append(row)

    with open(output_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        header.append('C')
        csvwriter.writerow(header)
        csvwriter.writerows(rows)

# Example usage:
process_csv('input.csv', 'output.csv')
