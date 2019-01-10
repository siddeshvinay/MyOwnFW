from Datatable import Test_data_lib
from ProjectSpecific import Genric_scripts
from Results import Log_Script
from  Testcase import Test_Case_lib as TCLib
from Driver import Execution
from Datatable import Test_data_lib as TC_Data
import unittest
import os



# FileName = os.path.abspath(__file__+"/../Controller.xlsx")
# SheetName = "Control_sheet"
# EC_status = "Execution_status"
# print(TC_Data.getExcutiondata(FileName, SheetName, "Execution_status", 5))



rowNum=None

class Main_Driver(unittest.TestCase):


    def setUp(self):
        pass

    def test_Runner(self):
        #FileName ="C:/Users/sjanagonnavar/DJFW/Datatable/Controller.xlsx"
        FileName = os.path.abspath(__file__ + "/../../Datatable/Controller.xlsx")
        RowCount=TC_Data.get_RowNumber(FileName,"Control_sheet")

        for i in range(RowCount):
            TC_Name=TC_Data.getExcutiondata(FileName, "Control_sheet", "Testcases_name", i)
            TC_Desp=TC_Data.getExcutiondata(FileName, "Control_sheet", "Descriptions", i)
            Run_Status=TC_Data.getExcutiondata(FileName, "Control_sheet", "Execution_status", i)

            if Run_Status=="Yes":
                TCID=TC_Name

                DataFileName=os.path.abspath(__file__+ "/../../Datatable/ExcelSheet.xlsx")
                methods=[]

                Dat_RowCount=TC_Data.get_RowNumber(DataFileName,"TC1")
                for j in range(Dat_RowCount):
                    TestCase_name = TC_Data.getExcutiondata(DataFileName,"TC1","TC_Function", j)
                    if TCID==TestCase_name:
                        rowNum=j
                        #TCLib.getRowNum(rowNum)


                        Function = TC_Data.getExcutiondata(DataFileName, "TC1", "Test_PackageName", j)
                        methods.append(Function)
                        print(methods)
                        for RunMethods in methods:
                            print(Function)
                            resultstatus = eval(Function)
                            print(resultstatus)




    def tearDown(self):
        os.environ.clear()

        pass

if __name__ == '__main__':
    unittest.main()