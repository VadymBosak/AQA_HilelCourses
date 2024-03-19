# 1

import csv


def from_csv_to_html(csv_file, html_file):
    # Відкриття CSV-файлу для читання
    with open(csv_file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # Відкриття HTML-файлу для запису
        with open(html_file, mode='w') as html_file:
            # Початок HTML-файлу
            html_file.write("<html>\n<body>\n<table border='1'>\n")

            # Читання рядків з CSV і запис у HTML
            for row in csv_reader:
                html_file.write("<tr>\n")
                for key, value in row.items():
                    html_file.write(f"<td><{key}>{value}</{key}></td>\n")
                html_file.write("</tr>\n")

            # Закриття тегів HTML-файлу
            html_file.write("</table>\n</body>\n</html>")

    print(f"HTML файл '{html_file}' успішно створено!")


# Приклад використання
from_csv_to_html('input.csv', 'output.html')



# 2

class Reader:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.data = None

    def read_file(self):
        with open(self.__file_path, 'r') as f:
            self.data = f.read()


class Writer:
    def __init__(self, file_path):
        self.__file_path = file_path

    def write_data(self, data):
        with open(self.__file_path, 'a') as f:
            f.write(data + '\n')


class ProxyReaderWriter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.reader = Reader(file_path)
        self.writer = Writer(file_path)
        self.data = None
        self.last_write = None

    def read(self):
        if self.data is None:
            self.reader.read_file()
            self.data = self.reader.data
        return self.data

    def write(self, row):
        if self.last_write != row:
            self.writer.write_data(row)
            self.last_write = row
            # Після запису в файл читаємо файл знову, щоб оновити дані
            self.read()


# Приклад використання класу ProxyReaderWriter
if __name__ == "__main__":
    proxy_rw = ProxyReaderWriter(file_path='tst_file.txt')

    proxy_rw.read()
    proxy_rw.read()
    proxy_rw.read()

    proxy_rw.write('asd')  # буде запис
    proxy_rw.write('asd')  # не буде запису
    proxy_rw.write('asd2')  # буде запис
    proxy_rw.write('asd')  # буде запис

    print(proxy_rw.data)
