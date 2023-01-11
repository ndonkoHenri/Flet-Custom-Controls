import flet as ft
from paginated_dt import PaginatedDataTable


def main(page: ft.Page):
    page.title = "Paginated DataTable Example 1"
    page.theme_mode = "light"
    page.scroll = ft.ScrollMode.AUTO
    page.window_always_on_top = True

    # copied from the flet.DataTable docs: https://flet.dev/docs/controls/datatable#examples
    dt = ft.DataTable(
            width=700,
            bgcolor="yellow",
            border=ft.border.all(2, "red"),
            border_radius=10,
            vertical_lines=ft.border.BorderSide(3, "blue"),
            horizontal_lines=ft.border.BorderSide(1, "green"),
            sort_column_index=0,
            sort_ascending=True,
            heading_row_color=ft.colors.BLACK12,
            heading_row_height=100,
            data_row_color={ft.MaterialState.HOVERED: "0x30FF0000"},
            show_checkbox_column=True,
            divider_thickness=0,
            column_spacing=200,
            columns=[
                ft.DataColumn(
                    ft.Text("Column 1"),
                    on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
                ),
                ft.DataColumn(
                    ft.Text("Column 2"),
                    tooltip="This is a second column",
                    numeric=True,
                    on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
                ),
            ],
            rows=[
                ft.DataRow(
                    [ft.DataCell(ft.Text("A")), ft.DataCell(ft.Text("1"))],
                    selected=True,
                    on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                ),
                ft.DataRow([ft.DataCell(ft.Text("B")), ft.DataCell(ft.Text("2"))]),
            ],
        )

    pdt = PaginatedDataTable(datatable=dt, table_title="Sample Data", rows_per_page=5)

    page.add(
        pdt,
        dt
    )


ft.app(target=main)
