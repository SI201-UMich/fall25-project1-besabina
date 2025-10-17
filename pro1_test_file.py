import unittest
from project1 import avg_mass_by_species_sex, avg_bill_by_island

class TestPenguin(unittest.TestCase):

    '''Test Cases for avg_mass_by_species_sex'''
    # Edge Case - Empty data
    def test_avg_mass_empty_data(self):
        test_data = []
        result = avg_mass_by_species_sex(test_data)
        self.assertEqual(result, {})
    
    # Edge Case - Same mass for all
    def test_avg_mass_same_data(self):
        test_data = [
            {'species': 'Adelie', 'sex': 'male', 'body_mass_g': 3750.0},
            {'species': 'Adelie', 'sex': 'male', 'body_mass_g': 3750.0},
            {'species': 'Adelie', 'sex': 'male', 'body_mass_g': 3750.0}
        ]
        result = avg_mass_by_species_sex(test_data)
        self.assertEqual(result, {'Adelie': {'male': 3750.0}})

    # General Test - Single record
    def test_avg_mass_single_record(self):
        test_data = [
            {'species': 'Chinstrap', 'sex': 'female', 'body_mass_g': 3750.0},
            {'species': 'Chinstrap', 'sex': 'male', 'body_mass_g': 4985.2}
        ]
        result = avg_mass_by_species_sex(test_data)
        expected = {
            'Chinstrap': {'female': 3750.0, 'male': 4985.2}
        }
        self.assertEqual(result, expected)

    # General Test - Multiple species & sex
    def test_avg_mass_diff_species_sex(self):
        test_data = [
            {'species': 'Adelie', 'sex': 'male', 'body_mass_g': 3750.0},
            {'species': 'Adelie', 'sex': 'male', 'body_mass_g': 4000.0},
            {'species': 'Adelie', 'sex': 'female', 'body_mass_g': 3500.0},
            {'species': 'Gentoo', 'sex': 'female', 'body_mass_g': 4567.2},
            {'species': 'Gentoo', 'sex': 'female', 'body_mass_g': 3946.5}
        ]
        result = avg_mass_by_species_sex(test_data)
        expected = {
            'Adelie': {'male': 3875.0, 'female': 3500.0},
            'Gentoo': {'female': 4256.85}
        }
        self.assertAlmostEqual(result, expected)

    '''Test Cases for avg_bill_by_island'''
    # Edge Case - Empty data
    def test_avg_bill_empty_data(self):
        test_data = []
        result = avg_bill_by_island(test_data)
        self.assertEqual(result, {})

    # Edge Case - Very small bill measurement
    def test_avg_small_bill(self):
        test_data = [
            {'island': 'Torgersen', 'bill_length_mm': 10.0, 'bill_depth_mm': 6.0},
            {'island': 'Torgersen', 'bill_length_mm': 22.0, 'bill_depth_mm': 12.0}
        ]
        result = avg_bill_by_island(test_data)
        self.assertAlmostEqual(result['Torgersen'], 1.75)

    # General Case - Single island & multiple penguins
    def test_avg_bill_single_island_diff_penguins(self):
        test_data = [
            {'island': 'Dream', 'bill_length_mm': 35.69, 'bill_depth_mm': 18.0},
            {'island': 'Dream', 'bill_length_mm': 47.82, 'bill_depth_mm': 16.2},
            {'island': 'Dream', 'bill_length_mm': 50.01, 'bill_depth_mm': 19.3},
            {'island': 'Dream', 'bill_length_mm': 38.50, 'bill_depth_mm': 17.0},
            {'island': 'Dream', 'bill_length_mm': 41.20, 'bill_depth_mm': 17.7}
        ]
        result = avg_bill_by_island(test_data)
        self.assertAlmostEqual(result['Dream'], 2.423, places=2)
        self.assertEqual(len(result), 1)

    # General Case - Multiple islands & multiple ratios
    def test_avg_bill_multiple_islands(self):
        test_data = [
            {'island': 'Dream', 'bill_length_mm': 40.45, 'bill_depth_mm': 19.2},
            {'island': 'Torgersen', 'bill_length_mm': 34.73, 'bill_depth_mm': 18.0},
            {'island': 'Biscoe', 'bill_length_mm': 41.88, 'bill_depth_mm': 18.3},
            {'island': 'Biscoe', 'bill_length_mm': 49.34, 'bill_depth_mm': 19.4}
        ]
        result = avg_bill_by_island(test_data)
        self.assertAlmostEqual(result['Dream'], 2.107, places=3)
        self.assertAlmostEqual(result['Torgersen'], 1.929, places=3)
        self.assertAlmostEqual(result['Biscoe'], 2.416, places=3)
        self.assertEqual(len(result), 3)

if __name__ == "__main__":
    unittest.main()
