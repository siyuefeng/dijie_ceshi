import csv


class CsvHelper:
    csv_file = None

    def read_file(self, file):
        """
        读取 file 文件
        :param file: csv 文件的全名+路径
        :return:
        """
        self.csv_file = open(file, 'r', encoding="utf-8")
        csv_data = csv.reader(self.csv_file)
        return csv_data

    def close(self):
        """
        关闭 csv 文件
        :return:
        """
        if self.csv_file is not None:
            self.csv_file.close()
