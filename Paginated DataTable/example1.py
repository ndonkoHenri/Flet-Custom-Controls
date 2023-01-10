import flet as ft
from simpledt import CSVDataTable       # pip install simpledatatable
from paginated_dt import PaginatedDataTable


def main(page: ft.Page):
    page.title = "Paginated DataTable Ex1"
    page.theme_mode = "light"
    page.scroll = ft.ScrollMode.AUTO
    page.window_always_on_top = True

    csv = CSVDataTable("Test Data/day.csv")
    pdt = PaginatedDataTable(datatable=csv.datatable, table_title="Customer Invoices", rows_per_page=5)

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
