import csv
from typing import Dict


class HandleCSV:
    """Fetch the csv file"""

    filename = "employees.csv"

    @classmethod
    def read_entire_csv(cls):
        """
        Access the csv file
        :return:Read the csv files lines
        """
        with open(cls.filename, "r") as foo:
            return foo.readlines()

    @classmethod
    def read_csv_line_by_line(cls):
        """
        To Access line by line csv file
        :return: it is a Generator shows line
        """
        with open(cls.filename) as bar:
            yield bar.readlines()

    @classmethod
    def read_csv_employees_details(cls) -> Dict[str]:
        """
        To Access the employees' deatils whose salary > 9000  like name,email,
        phone number
        :return: Dictionary of the employees name,email,Phone number
        """
        salary = {}
        with open(cls.filename, encoding="utf8") as bar:
            csv_reader = csv.DictReader(bar)
            for lines1 in csv_reader:
                if int(lines1["SALARY"]) > 9000:
                    first_name = lines1["FIRST_NAME"]
                    last_name = lines1["LAST_NAME"]
                    name = f"{first_name} {last_name}"
                    email = lines1["EMAIL"]
                    phone_number = lines1["PHONE_NUMBER"]
                    salary.update({"name": name})
                    salary.update({"email": email})
                    salary.update({"Phone_Number": phone_number}, )
                    print(salary)


csvfile = HandleCSV()

file = csvfile.read_entire_csv()
print("entire file details \n ", file)
print("#"*100)

csvfile1 = csvfile.read_csv_line_by_line()
print("line by line details")

for lines in csvfile1:
    """
    To print lines one by one in csv file
    """
    print(lines)

print("###"*50, "\n")

print("Salary is Greater than 9000 Employees: \n ",)
csvfile.read_csv_employees_details()
