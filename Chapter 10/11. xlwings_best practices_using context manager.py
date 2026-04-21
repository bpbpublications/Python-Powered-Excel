import xlwings as xw

# xw.Book() support context managers

with xw.Book() as wb:
    # work with wb
    wb.sheets[0].range('A1').value = 1
    wb.save('using_context_mananger.xlsx')

# It worked but you can't see the changes live
# - Use context managers for short, self‑contained automation to guarantee resources are released.
# - Use manual control when you need the workbook or Excel instance to remain open for inspection, interactive debugging, or when multiple operations span separate code blocks.

# Prefer explicit saves (wb.save() or wb.close(save=True)) for predictable persistence; rely on AutoSave only


# xw.App() also supports automatic close/quit at app level:
    
with xw.App(visible=False) as app:
    with app.books.open('using_context_mananger.xlsx') as wb:
        # work with wb
        wb.sheets[0].range('A2').value = 10
        wb.save()

# manual control (no automatic close)
app = xw.App(visible=True)
wb = app.books.add()
# ... work ...
wb.save()
# keep workbook/app open until you explicitly close/quit