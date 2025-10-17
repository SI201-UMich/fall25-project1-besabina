import csv 

def read_file(file_name):
    try:
        # Opens file; handles header
        with open(file_name, "r", newline = "") as file:
            reader = csv.DictReader(file)
            penguin_list = []

            # Skip rows with NA values
            for row in reader:
                if 'NA' in row.values():
                    continue

                # Create inner dictionary; convert datatype when appropriate
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

                # Add cleaned dictionary to list
                penguin_list.append(inner_d)
            return penguin_list
    
    except:
        print("Failed to open file. Check for valid file name.")


def data_analysis(penguin_data):
    # Check data availability
    if not penguin_data:
        return "No data available to analyze."
     
    # Display column names
    variables = list(penguin_data[0].keys())
    print(f"Variables in penguin dataset: {variables}")

    # Display sample entry
    print(f"Sample entry: {penguin_data[0]}")

    # Display total rows in cleaned penguin dataset (no NA)
    print(f"Total rows: {len(penguin_data)}")

def avg_mass_by_species_sex(penguin_data):
    # Initialize empty dict to organize data by species, sex, body mass
    final_data = {}

    # Process each penguin record in dataset
    for row in penguin_data:
        species = row['species']
        sex = row['sex']
        mass = row['body_mass_g']

        # If species not in final_data, create entry for it
#        print(f"First final_data: {final_data}")
        if species not in final_data:
            final_data[species] = {}
        
        # If sex not in final_data, initialize entry, counter
        if sex not in final_data[species]:
            final_data[species][sex] = {'total': 0, 'count': 0}
        
        # Add penguin's mass to total for its species-sex group; increment count
        final_data[species][sex]['total'] += mass
        final_data[species][sex]['count'] += 1

#        print(f"Print Mass: {mass}")
    
#    print(f"Second final_data: {final_data}")

    average = {}
    # Iterate through each species in final_data; create entry for species
    for species, sex_data in final_data.items():
#        print(f"print species: {species}")
#        print(f"sex_data: {sex_data}")
        average[species] = {}

        # Iterate through each sex within species; calculate average
        for sex, stats in sex_data.items():
#            print(f"print sex: {sex}")
#            print(f"print stats: {stats}")
            average[species][sex] = stats['total']/stats['count']
        
    return average

def avg_bill_by_island(penguin_data):
    # Initialize empty dict to organize data by island
    island_data = {}

    # Process each penguin record in dataset
    for row in penguin_data:
        island = row['island']
        bill_length = row['bill_length_mm']
        bill_depth = row['bill_depth_mm']

        # Calculate bill ratio
        bill_ratio = bill_length / bill_depth
#        print(f"First bill_ratio: {bill_ratio}")
#        print(f"Print island_data: {island_data}")

        # If island not in dict, initialize entry, counter
        if island not in island_data:
            island_data[island] = {'total_ratio': 0, 'count': 0}

        # Add to penguin's ratio total and increment counter
        island_data[island]['total_ratio'] += bill_ratio
        island_data[island]['count'] += 1
    
#    print(f"print island_data[island]['total_ratio']: {island_data[island]['total_ratio']}")

    average_ratio = {}

    # Calculate average for each island
    for island, stats in island_data.items():
        average_ratio[island] = stats['total_ratio'] / stats['count']
#        print(f"print average_ratio[island]: {average_ratio[island]}")
    
    return average_ratio
    

def main():
    penguin_data = read_file('penguins.csv')
#    print(penguin_data)
    data_analysis(penguin_data)

    print("\n*** CALCULATION 1: Average body mass by species and sex ***")
    mass_dict = avg_mass_by_species_sex(penguin_data)
    for species, sex_data in mass_dict.items():
        print(f"{species} Penguins:")
        for sex, avg_mass in sex_data.items():
            print(f"   {sex}: {avg_mass:.3f} grams")

    print("\n*** CALCULATION 2: Average bill length to depth ratio by island ***")
    bill_ratio_dict = avg_bill_by_island(penguin_data)
    print("Bill Length-to_Depth Ratios: ")
    for island, ratio in bill_ratio_dict.items():
        print(f" {island}: {ratio:.3f}")

if __name__ == "__main__":
    main()


