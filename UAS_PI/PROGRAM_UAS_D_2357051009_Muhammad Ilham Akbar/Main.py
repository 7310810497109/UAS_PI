from Data_raw import process_data
from Calculator_py import Statistics
from display import display_data, display_statistics

# Data awal
mydata = [
    ["Spark", "DS", 20000, 30, 5],
    ["Hadoop", "DS", 25000, 40, 10],
    ["Pandas", "PI", 30000, 35, 5],
    ["Java", "PI", 22000, 60, 5],
    ["Pyspark", "DS", 26000, 50, 5],
    ["Scala", "PI", 28000, 45, 10],
    ["Go", "DS", 24000, 40, 5],
    ["SQL", "PI", 30000, 30, 15],
    ["Ruby", "DS", 22000, 35, 10],
    ["Kotlin", "PI", 27000, 50, 0.05],
]

# Header untuk tabel
head = ["Course", "Categories", "Fee", "Duration", "Percentage Discount", "Total"]

# Proses data
processed_data = process_data(mydata)

# Ambil data Fee dan Total
fee_data = [row[2] for row in mydata]  # Ambil kolom Fee
total_data = [row[5] for row in mydata]  # Ambil kolom Total
statistics = {
    "Fee": {"mean": sum(fee_data) / len(fee_data), "median": sorted(fee_data)[len(fee_data)//2], "mode": max(set(fee_data), key=fee_data.count)},
    "Total": {"mean": sum(total_data) / len(total_data), "median": sorted(total_data)[len(total_data)//2], "mode": max(set(total_data), key=total_data.count)},
}

# Hitung statistik
statistics = Statistics()
fee_statistics = {
    "mean": statistics.mean(fee_data),
    "median": statistics.median(fee_data),
    "mode": statistics.mode(fee_data)
}
total_statistics = {
    "mean": statistics.mean(total_data),
    "median": statistics.median(total_data),
    "mode": statistics.mode(total_data)
}

# Tampilkan hasil
display_data(processed_data, head)
display_statistics(fee_statistics, "Fee")
display_statistics(total_statistics, "Total")
