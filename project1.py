# Name: Sabina Begum
# student ID: 94703436
# email: bsabina@umich.edu
# External resources: Runestone, GenAI, OH, Google sites, Previous HW
# - Runestone: viewed examples for write, nested dictionary, open() file, inner dictionary, test cases
# - GenAI: used to pseudocode, debug/understand errors, initialize new entries in a nested dictionary
# -OH: received help in function structure formation, submission clarity
# Google sites: learned about DictReader(), watched tutorials on nested dictionary, writing test cases
# Prvious HW: used previous HW test cases as example to write them here and import appropriate functions   

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
        print("No data available to analyze.")
        return
     
    # Display column names (all variables)
    variables = list(penguin_data[0].keys())
    print(f"Variables in penguin dataset: {variables}")

    # Display sample entry (first row)
    print(f"Sample entry: {penguin_data[0]}")

    # Display total rows in cleaned penguin dataset (no NA)
    print(f"Total rows: {len(penguin_data)}")

def avg_mass_by_species_sex(penguin_data):
    '''
    Calculates the average body mass for each species and sex combinations.
    INPUT: penguin_data (list of dictionary)
    OUTPUT: average (dictionary)
    '''
    # Initialize empty dict to organize data by species & sex
    final_data = {}

    # Process each penguin record in dataset
    for row in penguin_data:
        species = row['species']
        sex = row['sex']
        mass = row['body_mass_g']

        # If species not in final_data, create entry for it
        if species not in final_data:
            final_data[species] = {}
        
        # If sex not in species entry, initialize counter
        if sex not in final_data[species]:
            final_data[species][sex] = {'total': 0, 'count': 0}
        
        # Add penguin's mass to total & increment count
        final_data[species][sex]['total'] += mass
        final_data[species][sex]['count'] += 1

    average = {}

    # Iterate through each species in final_data
    for species, sex_data in final_data.items():
        average[species] = {}

        # Iterate through each sex within species & calculate average
        for sex, stats in sex_data.items():
            average[species][sex] = stats['total'] / stats['count']
        
    return average

def avg_bill_by_island(penguin_data):
    '''
    Calculates average bill length to depth ratio for penguins on each island
    INPUT: penguin_data (list of dictionary)
    OUTPUT: average_ratio (dictionary)
    '''
    # Initialize empty dict to organize data by island
    island_data = {}

    # Process each penguin record in dataset
    for row in penguin_data:
        island = row['island']
        bill_length = row['bill_length_mm']
        bill_depth = row['bill_depth_mm']

        # Calculate bill ratio
        bill_ratio = bill_length / bill_depth

        # If island not in dict, initialize counter
        if island not in island_data:
            island_data[island] = {'total_ratio': 0, 'count': 0}

        # Add ratio to total and increment counter
        island_data[island]['total_ratio'] += bill_ratio
        island_data[island]['count'] += 1
    
    average_ratio = {}

    # Calculate average ratio for each island
    for island, stats in island_data.items():
        average_ratio[island] = stats['total_ratio'] / stats['count']
    
    return average_ratio

def present_as_csv(results, filename = "project1_results.csv"):
    '''
    Write analysis results to a CSV file.
    INPUT: results (dictionary), filename (string)
    OUTPUT: None (CSV file)
    '''
    try:
        with open(filename, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            # Write header row
            writer.writerow(['Analysis Type', 'Variable', 'Group', 'Value', 'Units'])
            
            # write average mass results
            body_mass_results = results['avg_mass_by_species_sex']
            for species, sex_data in body_mass_results.items():
                for sex, avg_mass in sex_data.items():
                    writer.writerow([
                        'Average Body Mass',
                        species,
                        sex,
                        round(avg_mass, 3),
                        'grams'
                    ])
            
            # write average bill ratio results
            bill_ratio_results = results['avg_bill_by_island']
            for island, ratio in bill_ratio_results.items():
                writer.writerow([
                    'Bill Length/Depth Ratio',
                    island,
                    'All Penguins',
                    round(ratio, 3),
                    'ratio'
                ])
        return True
    except:
        print(f"Error. Cannot write to file.")
        return False


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
    print("Bill Length-to-Depth Ratios: ")
    for island, ratio in bill_ratio_dict.items():
        print(f" {island}: {ratio:.3f}")

    print("\n*** Writing result to file ***")
    result = {
        "avg_mass_by_species_sex": mass_dict,
        "avg_bill_by_island": bill_ratio_dict
    }
    success = present_as_csv(result)
    if success:
        print("Program successful!")
    else:
        print("Program failed.")

    return result

if __name__ == "__main__":
    main()


