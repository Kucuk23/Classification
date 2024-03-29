import csv

with open('2022_input_space.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  


    datasets = []
    current_dataset = []

    datasets.append(current_dataset)
    prev_hour = None
    for row in reader:
        timestamp_str = row[0]  # Zaman damgasını al
        current_hour = int(timestamp_str.split()[1].split(':')[0])  # Saati al

        if prev_hour is not None and current_hour != prev_hour + 1:
            current_dataset = []
            datasets.append(current_dataset)

        current_dataset.append(row)
        prev_hour = current_hour


for i, dataset in enumerate(datasets, start=1):
    filename = f"dataset_2022_{i}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header) 
        writer.writerows(dataset)  
    print(f"{filename} dosyasi olusturuldu.")














    