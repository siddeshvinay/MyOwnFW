import xlrd
import xlsxwriter
import xlwt
#import xlutils
import logging
from Results import Log_Script as log
import os


'''
Created By:
Created Date:
Description: 
Reviewd By:
Modified By:
Parameters:
return Type:
'''
def get_RowNumber(Filename, SheetName):
    status="Fail"
    try:

        Open_XL=xlrd.open_workbook(Filename)
        XL_sheet=Open_XL.sheet_by_name(SheetName)
        XL_row=XL_sheet.nrows
        return XL_row

    except Exception as e:
        log.writelogs("unable to open the xl sheet", "Error")



''''
Created By:
Created Date:
Description: 
Reviewd By:
Modified By:
Parameters:
return Type:
'''
def get_ColCount(Filename,SheetName):
    status="Fail"
    try:
        Open_XL = xlrd.open_workbook(Filename)
        XL_sheet = Open_XL.sheet_by_name(SheetName)
        XL_CCount=XL_sheet.ncols
        return XL_CCount

        #print(XL_CCount)
    except Exception as e:
        log.writelogs("unable to open the xl sheet", "Error")



'''
Created By:
Created Date:
Description: 
Reviewd By:
Modified By:
Parameters:
return Type:
'''
def get_data(Filename,SheetName,Testdata):
    try:
        row = get_RowNumber(Filename, SheetName)
        column = get_ColCount(Filename, SheetName)
        open_Xl = xlrd.open_workbook(Filename)
        Xl_sheetName = open_Xl.sheet_by_name(SheetName)

        for i in range(0,column):
            lenta = Xl_sheetName.cell_value(0,i)

            if lenta==Testdata:
                Cell_Dat=Xl_sheetName.cell_value(1,i)

        return Cell_Dat


    except Exception as e:
        log.writelogs("unable to open the xl sheet", "Error")


'''
Created By:
Created Date:
Description: 
Reviewd By:
Modified By:
Parameters:
return Type:
'''
def load_Data_OS(FileName, SheetName):
    status="Fail"
    try:
        Open_XD=xlrd.open_workbook(FileName)
        xl_sheet=Open_XD.sheet_by_name(SheetName)

        ColumnName=xl_sheet.row_values(0)
        ColumnValues=xl_sheet.row_values(1)

        for i in range(len(ColumnName)):
            os.environ[ColumnName[i]]=str(ColumnValues[i])

    except Exception as e:
        log.writelogs("Unable to load the values to the OS", "Error")



def get_pageObjects(Filename,SheetName,Xp_name):
    try:
        get_Xpathvale=""
        row = get_RowNumber(Filename, SheetName)
        column = get_ColCount(Filename, SheetName)
        open_Xl = xlrd.open_workbook(Filename)
        Xl_sheetName = open_Xl.sheet_by_name(SheetName)

        for i in range(row-1):
            if Xp_name==Xl_sheetName.cell_value(i,0):
                get_Xpathvale=Xl_sheetName.cell_value(i,1)
    except Exception as e:
        log.writelogs("unable to get the row")
    return get_Xpathvale

#print(get_pageObjects("C:/Users/Dell/PycharmProjects/DJFW/Datatable/PageObjects.xlsx","PageObjects","Login"))




def load_Page_Objects(FileName, SheetName):
    status="Fail"
    try:
        Open_XD=xlrd.open_workbook(FileName)
        xl_sheet=Open_XD.sheet_by_name(SheetName)

        for i in range(xl_sheet.nrows):
            RowName = xl_sheet.cell_value(i,0)
            RowValues=xl_sheet.cell_value(i,1)
            os.environ[RowName]=str(RowValues)


    except Exception as e:
        log.writelogs("Unable to load the values to the OS", "Error")



# FileName="C:/Users/Dell/PycharmProjects/DJFW/Datatable/PageObjects.xlsx"
# SheetName="PageObjects"
# load_Page_Objects(FileName,SheetName)
# pas=os.environ.get("Logout")
# print(pas)


# def getCellData(Filename,SheetName,Execution_status, TCName):
#     row = get_RowNumber(Filename, SheetName)
#     column = get_ColCount(Filename, SheetName)
#     open_Xl = xlrd.open_workbook(Filename)
#     Xl_sheetName = open_Xl.sheet_by_name(SheetName)
#     rownum=None
#     for i in range(row):
#         if TCName==Xl_sheetName.cell_value(i,0):
#             rownum=i
#     colNum=None
#     for j in range(column):
#         if EC_status==Xl_sheetName.cell_value(0,j):
#             colNum=j
#
#     data=Xl_sheetName.cell_value(rownum,colNum)
#     return data





def getExcutiondata(FileName,SheetName,ColumName,Rownum):
    try:
        ColNum=0
        open_Xl = xlrd.open_workbook(FileName)
        Xl_sheetName = open_Xl.sheet_by_name(SheetName)

        first_row=Xl_sheetName.row_values(0)
        for i in first_row:
            if i==ColumName:
                break
            ColNum+=1
        celldata=Xl_sheetName.cell_value(Rownum,ColNum)
        return celldata

    except Exception as e:
        print(e)


# #FileName="C:/Users/sjanagonnavar/DJFW/Datatable/Controller.xlsx"
# FileName=os.path.abspath(__file__+"/../Controller.xlsx")
# SheetName="Control_sheet"
# EC_status="Execution_status"
# #TCname="TestCase_3"
# print(getExcutiondata(FileName,SheetName,"Execution_status", 5))




def getCelldata(FileName, Sheetname,ColName, RowNum):
    ColNum=0
    try:
        wb=xlrd.open_workbook(FileName)
        sheet=wb.sheet_by_name(Sheetname)

        firstRow=sheet.row_values(0)
        for data in firstRow:
            if data==ColName:
                break
            ColNum+=1

        celldata=sheet.cell_value(RowNum,ColNum)
        return celldata
    except Exception as e:
        print("unabel to fetch the data from the cell")






