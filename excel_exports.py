import csv


# This file is a simple class that handles saving data contained within tables to csv files.
class ExportExcelData:
    def __init__(self, data, columns, filename, **kwargs):
        self.data = data
        self.columns = columns
        self.filename = filename

    @staticmethod
    def make_data_dict(column, row) -> dict:
        return dict(zip(column, row))

    def export_to_file(self):
        try:
            with open(f'{self.filename}', 'w', newline='') as csvfile:

                fieldnames = self.columns
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for item in self.data:
                    data_item = self.make_data_dict(self.columns, item)
                    print(data_item)
                    writer.writerow(data_item)
        except PermissionError:
            print("permission denied file may be open or encrypted..!")


# db = [(1.4, 'kim', '10-56-90'), (45.7, 'jame', '12-67-89'), (67.8, 'jok', '04-09-87')]
# export = ExportExcelData(data=db, columns=['a', 'b', 'c'], filename='toto')
# export.export_to_file()
