import datetime
import unittest

def symbol(symbolInput):    
    if len(symbolInput) < 1 or len(symbolInput) > 7:
        raise ValueError("The value you entered is not between the range of 1-7")
    if symbolInput.islower():
        raise ValueError("The value you entered must be all uppercase")
    else:
        return symbolInput

def chartType(chartInput):
    if chartInput != 1 and chartInput != 2:
        raise ValueError("The value you entered is not equal to 1 0r 2")
    else:
        return chartInput

def timeSeries(timeSeriesInput):
    if timeSeriesInput not in range(1,5):    
        raise ValueError("The value you entered must be in the range of 1-4")
    else:
        return timeSeriesInput

def startDate(dateInput):
    containsLetter = any(map(str.isalpha, dateInput))
    if containsLetter == True:
        raise ValueError("Date cannot have any letters in it")
    if len(dateInput) != 10:
        raise ValueError("Date format is not correct, remember to put it in YYYY-MM-DD format")
    date_list = dateInput.split("-")
    if (len(date_list[0]) != 4) or (len(date_list[1]) != 2) or (len(date_list[2]) != 2):
        raise ValueError("Date format is not correct, remember to put it in YYYY-MM-DD format")
    else:
        return dateInput

def endDate(dateInput):
    containsLetter = any(map(str.isalpha, dateInput))
    if containsLetter == True:
        raise ValueError("Date cannot have any letters in it")
    if len(dateInput) != 10:
        raise ValueError("Date format is not correct, remember to put it in YYYY-MM-DD format")
        raise ValueError("Date format is not correct, remember to put it in YYYY-MM-DD format")
    date_list = dateInput.split("-")
    if (len(date_list[0]) != 4) or (len(date_list[1]) != 2) or (len(date_list[2]) != 2):
        raise ValueError("Date format is not correct, remember to put it in YYYY-MM-DD format")
    else:
        return dateInput
class inputTests(Exception):
    def __init__(self, msg, error_code):
        super().__init__(msg)
        self.error_code = error_code
    
def errorException(var):
    if var.isalpha:
        raise MyExcept("The symbol contains numbers", 4444)
    else:
        return True

class TestingInputs(unittest.TestCase):

    def setUp(self):
        print("setUp")
        self.num = 1

    def testSymbol(self):

        symbol("JILL")

    def testChartType(self):
        result = chartType(self.num)
        self.assertEqual(result, 1)

        self.num = 2
        result2 = chartType(self.num)
        self.assertEqual(result2, 2)


    def testTimeSeries(self):
        result = timeSeries(self.num)
        self.assertEqual(result, 1)

        self.num = 3
        result2 = timeSeries(self.num)
        self.assertEqual(result2, 3)


    def testStartDate(self):
        self.testDate = "2020-10-15"
        result = startDate(self.testDate)
        self.assertEqual(result, self.testDate)


    def testEndDate(self):
        self.testDate = "2021-08-08"
        result = startDate(self.testDate)
        self.assertEqual(result, self.testDate)


if __name__ == '__main__':
    unittest.main()