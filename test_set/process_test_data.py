import pandas as pd
import csv

read_file = pd.read_csv (r'annotations_revised.txt')
data = read_file.values.tolist()
col = read_file.columns.values.tolist()
data.insert(0, col)

with open('annotations_revised_test.csv', 'w', newline='') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(['file', 'label', 'from_line', 'to_line'])  
    for line in data:
        each_lien = line[0].split(";")
        crnt_file = each_lien[0]
        each_lien = each_lien[1:]
        for j in range(0, len(each_lien) - 1, 3):
            writer.writerow([crnt_file, each_lien[j], each_lien[j+1], each_lien[j+2]])

labels = pd.read_csv('annotations_revised_test.csv')

for i in range(109, 181, 1):
    read_file = pd.read_csv (r"sequences/"+ str(i) +".txt")
    crnt_file = read_file.values.tolist()
    crnt_file.insert(0, read_file.columns.values.tolist())
    
    crnt_label = labels.loc[labels['file'] == i]

    for label in crnt_label.iterrows():
        from_line = label[1]['from_line']
        to_line = label[1]['to_line']
        true_label = label[1]['label']
        data = crnt_file[from_line:to_line+1]

        with open('test_data.csv', 'a', newline='') as out_file:
            writer = csv.writer(out_file)
            for line in data:
                each_line = line[0].split(";")
                each_line.pop()
                each_line.insert(len(each_line)+1, true_label)
                writer.writerow(each_line)
