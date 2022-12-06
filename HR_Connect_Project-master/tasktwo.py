import csv
from utils.dateformat import dateformat_convert
from utils.csv import add_value


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
            print(foo.readlines())

    @classmethod
    def read_csv_line_by_line(cls):
        """
        To Access line by line csv file
        :return: it is a Generator shows line
        """
        with open(cls.filename) as bar:
            yield bar.readlines()

    @classmethod
    def read_csv_employees_hire(cls):
        """
        TO Access employees details whose department id is in range 30 to 110
        and salary >4200 in  format hire date and name
        :return: Dictionary for Hire_date and Name of employees
        """
        hire = {}

        with open(cls.filename, encoding="utf8") as bar:
            csv_reader = csv.DictReader(bar)

            for lines in csv_reader:
                """
                for Access the employees details one bye one
                """
                if int(lines["DEPARTMENT_ID"]) > 30 \
                        and int(lines["SALARY"]) > 4200:

                    hire_date = lines["HIRE_DATE"]
                    date = dateformat_convert(hire_date)
                    first_name = lines["FIRST_NAME"]
                    last_name = lines["LAST_NAME"]
                    name = f"{first_name} {last_name}"

                    add_value(hire, date, name)
                    """
                    To store the names of employees in list format with 
                    hire date key
                    """

        print(hire)


hires = HandleCSV()

print("\nHIRE DATE of employee who is department is within range 30"
      "to 110 AND who is salary is > 4200.\n")
hires.read_csv_employees_hire()
