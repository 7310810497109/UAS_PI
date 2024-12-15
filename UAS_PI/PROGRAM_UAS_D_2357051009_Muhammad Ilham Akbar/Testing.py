import unittest
from Data_raw import read_csv, process_data, write_csv
from statistics import Statistics

class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        """
        Menyiapkan data untuk pengujian.
        """
        self.test_file = "data.csv"  # File CSV yang diunggah
        self.processed_file = "processed_data.csv"
        self.headers = ["Charity", "Categories", "Fee", "Duration", "Percentage Discount", "Total"]
        self.data = [
             ["Spark", "DS", 20000, 30, 0.05],
             ["Hadoop", "DS", 25000, 40, 0.1],
             ["Pandas", "PI", 30000, 35, 0.05]
        ]

    def test_read_csv(self):
        """
        Menguji pembacaan file CSV.
        """
        try:
            data = read_csv(self.test_file)
            self.assertIsInstance(data, list)
            self.assertGreater(len(data), 0)  # Data tidak boleh kosong
        except Exception as e:
            self.fail(f"read_csv raised an exception: {e}")

    def test_process_data(self):
        """
        Menguji fungsi process_data.
        """
        try:
            processed_data = process_data(self.data)
            for row in processed_data:
                self.assertEqual(len(row), len(self.headers))
        except Exception as e:
            self.fail(f"process_data raised an exception: {e}")

    def test_write_csv(self):
        """
        Menguji penulisan data ke file CSV.
        """
        try:
            processed_data = process_data(self.data)
            write_csv(processed_data, self.processed_file, self.headers)
        except Exception as e:
            self.fail(f"write_csv raised an exception: {e}")

class TestStatistics(unittest.TestCase):

    def setUp(self):
        """
        Menyiapkan data untuk pengujian statistik.
        """
        self.data = [35, 20, 20, 30, 40]

    def test_mean(self):
        """
        Menguji perhitungan rata-rata.
        """
        stat = Statistics.mean(self.data)
        self.assertEqual(stat, 24)

    def test_median(self):
        """
        Menguji perhitungan median.
        """
        stat = Statistics.median(self.data)
        self.assertEqual(stat, 20)

    def test_mode(self):
        """
        Menguji perhitungan mode.
        """
        stat = Statistics.mode(self.data)
        self.assertEqual(stat, 20)

if __name__ == "__main__":
    unittest.main()
