import win32com.client
from pywintypes import com_error
from pathlib import Path


# Search string: Replace string
REPLACE_TXTS = {
    '{{A701}}': 'AgilentI5',
    '{{A702}}': 'AgilentI7'
}

nowdir = Path(__file__).absolute().parent

excel = win32com.client.Dispatch('Excel.Application')

excel.Visible = False

try:
    # open xlsx
    wb = excel.Workbooks.Add(str(nowdir / 'template.xlsx'))
    sheet = wb.WorkSheets(1)
    sheet.Activate()

    # Replace text in cell
    rg = sheet.Range(sheet.usedRange.Address)
    for search_txt, replace_Txt in REPLACE_TXTS.items():
        rg.Replace(search_txt, replace_Txt)

    # save as
    wb.SaveAs(str(nowdir / 'new.xlsx'))

except com_error as e:
    print('Failure.', e)
else:
    print('Success.')
finally:
    wb.Close(False)
    excel.Quit()
