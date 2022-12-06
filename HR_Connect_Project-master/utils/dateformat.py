import datetime
from datetime import datetime
"""
Function to covert the date format in YYYY-MM-DD
"""
def dateformat_convert(date:datetime):
    """
    To Convert date format
    :param date: Date object
    :return: Date string in format "YYYY-MM-DD"
    """
    date_format = "%d-%b-%y"
    hire_date = datetime.strptime(date, date_format)
    hire_date = hire_date.date()
    return str(hire_date)