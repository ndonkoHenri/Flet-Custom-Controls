import flet as ft
from paginated_dt import PaginatedDataTable
try:
    import simpledt  # pip install simpledatatable
except ImportError as error:
    print("Please install the `simpledatatable` python package using 'pip install simpledatatable'.\n"
          "See it's down at https://github.com/StanMathers/simple-datatable")
    exit(ImportError)

# this example shows how to use the PaginatedDataTable with classes of the `simpledatatable` python package
# see it's docs at: https://github.com/StanMathers/simple-datatable


def main(page: ft.Page):
    page.title = "Paginated DataTable Example 3"
    page.theme_mode = "light"
    page.scroll = ft.ScrollMode.AUTO
    page.window_always_on_top = True

    csv = simpledt.CSVDataTable("Test Data/day.csv")
    pdt = PaginatedDataTable(datatable=csv.datatable, table_title="The 31 Days!", rows_per_page=5)

    # change the borders of the data table
    pdt.datatable.border = ft.border.all(4, ft.colors.BLUE_ACCENT_700)

    # modify the rows in the data table
    for i in pdt.datarows:
        rownum = i.cells[0].content.value
        if int(rownum) % 2 == 0:
            i.color = ft.colors.GREEN

    # modify the columns in the data table
    for i in pdt.datacolumns:
        i.label = ft.Row([i.label, ft.Icon(ft.icons.AC_UNIT)])

    page.add(
        pdt
    )


ft.app(target=main)
