import csv 

def read_file(file_name):
    try:
        with open(file_name, "r", newline = "") as file:
            reader = csv.DictReader(file)
            penguin_list = []

            for row in reader:
                if 'NA' in row.values():
                    continue

                inner_d = {
                    "species": row["species"],
                    "island": row["island"],
                    "bill_length_mm": float(row["bill_length_mm"]),
                    "bill_depth_mm": float(row["bill_depth_mm"]),
                    "flipper_length_mm": float(row["flipper_length_mm"]),
                    "body_mass_g": float(row["body_mass_g"]),
                    "sex": row["sex"],
                    "year": int(row["year"])
                }

                penguin_list.append(inner_d)
            return penguin_list
    
    except:
        print("Failed to open file. Check for valid file name.")


def main():
    penguin_data = read_file('penguins.csv')
    print(penguin_data)

if __name__ == "__main__":
    main()



