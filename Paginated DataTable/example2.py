import flet as ft
from paginated_dt import PaginatedDataTable


def main(page: ft.Page):
    page.title = "Paginated DataTable Example 2"
    page.theme_mode = "light"
    page.scroll = ft.ScrollMode.AUTO
    page.window_always_on_top = True

    # copied from the flet.DataTable docs: https://flet.dev/docs/controls/datatable#examples
    dt = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("First name")),
                ft.DataColumn(ft.Text("Last name")),
                ft.DataColumn(ft.Text("Age"), numeric=True),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("John")),
                        ft.DataCell(ft.Text("Smith")),
                        ft.DataCell(ft.Text("43")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Jack")),
                        ft.DataCell(ft.Text("Brown")),
                        ft.DataCell(ft.Text("19")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Alice")),
                        ft.DataCell(ft.Text("Wong")),
                        ft.DataCell(ft.Text("25")),
                    ],
                ),
            ],
        )

    # create an instance of the PaginatedDataTable
    pdt = PaginatedDataTable(datatable=dt, table_title="Sample Data", rows_per_page=5)

    page.add(
        pdt,
        dt
    )


ft.app(target=main)
