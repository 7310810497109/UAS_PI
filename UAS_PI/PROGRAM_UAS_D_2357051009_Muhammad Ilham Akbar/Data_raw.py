import csv

def read_csv(filepath):
    data = []
    with open(filepath, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                # Konversi data ke tipe yang sesuai
                row[2] = float(row[2])  # Fee
                row[3] = int(row[3])   # Duration
                row[4] = float(row[4])  # Percentage Discount
                if not (0 <= row[4] <= 1):
                    raise ValueError(f"Invalid discount value: {row[4]}")
                data.append(row)
            except (ValueError, IndexError) as e:
                print(f"Error processing row {row}: {e}")
    return data

def write_csv(data, filepath, headers):
    """
    Menulis data ke file CSV.
    """
    with open(filepath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)  # Tulis header
        writer.writerows(data)

def menghitung_total(row):
    fee_duration = row[2] * row[3]  # Fee * Duration
    discount = fee_duration * (row[4] / 100)  # Total Discount
    if row[1] == "PI":
        total = fee_duration - discount - (fee_duration * 0.02)  # Tambahan potongan 2% untuk kategori PI
    else:
        total = fee_duration - discount
    return total

def process_data(data):
    for row in data:
        total = menghitung_total(row)
        row.append(total)
    return data

