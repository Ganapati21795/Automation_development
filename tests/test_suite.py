"""
module will get the data from the excel
and run the scenarios accordingly.
we are loading all the scenarios in the module
and run the test whichever is needed from the excel

"""

import unittest
import HtmlTestRunner
from test_flow_delivery import TestDelivery
from test_flow_pick_up import TestPickUp
import pandas as pd
ts1 = unittest.TestLoader().loadTestsFromTestCase(TestDelivery)
ts2 = unittest.TestLoader().loadTestsFromTestCase(TestPickUp)

excel_file = pd.ExcelFile('./../utilities/TestData.xlsx')
file = pd.read_excel(excel_file, sheet_name = 'Tests')
# file = file.replace(np.nan, " ", regex=True)
def get_scenarios_from_the_excel():
    """
    function to get the data from the excel sheet
    """
    scenario_list = []
    for row in range(0, len(file.values)):
        testcase_dict = dict()
        testcase_dict['module'] = file.values[row][0]
        testcase_dict['test_scenarios'] = file.values[row][1]
        if testcase_dict['module'] == 'y':
            scenario_list.append(testcase_dict['test_scenarios'])
    return scenario_list


assignment_suite = get_scenarios_from_the_excel()
print(assignment_suite)

# create a test suite combining search_text and home_page_test
for val in assignment_suite:
    suite = unittest.TestSuite(eval(val))

# run the suite
if __name__ == '__main__':
    runner = HtmlTestRunner.HTMLTestRunner(output='./../outputs', report_title="Test Report", descriptions="Test Suite")
    runner.run(suite)


