


def Generate_CSV(file_name,list1):
    csv_file_name=f"C:\softwares\Output_CSV_files\{file_name}.csv"
    with open(csv_file_name,"a",encoding="utf-8") as f1:
        f1.writelines(",".join(list1))
        f1.writelines("\n")
