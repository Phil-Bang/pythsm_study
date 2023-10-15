import flet as ft
import sampledata

data = sampledata.alldata
keys = list(data.keys())
values = list(data.values())
    
def std_sht():
    txt1 = ft.Text("Standard Sheet",
                   color = ft.colors.BLACK,
                   weight = "bold",
                   text_align = ft.TextAlign.RIGHT,
                   font_family = "HDText")
    return ft.Column(
        controls = [ft.Container(content = txt1, padding=10)],
    )

def paint_area():
    txt2 = ft.Text("Paint Area Sheet",
                   color = ft.colors.BLACK,
                   weight = "bold",
                   text_align = ft.TextAlign.RIGHT,
                   font_family = "HDText")
    return ft.Column(
        controls=[ft.Container(content = txt2, padding=10)],
    )

def mh_calc(page):
    option_text = ft.Text(
                color = ft.colors.BLACK,
                weight = "bold",
                text_align = ft.TextAlign.RIGHT,
                width = 47,
                font_family = "HDText")
                
    def add_btn_clicked(e):
        option_text.value = f"{line4_dd.value}"
        page.update()

    t = ft.Text()
    def textbox_changed(e):
        t.value = e.control.value
        page.update()

    line1_btn1 = ft.ElevatedButton(
        width = 130,
        bgcolor = ft.colors.LIGHT_BLUE_700,
        color = ft.colors.WHITE,
        content = ft.Row(
            [
                ft.Text("Initialize", size = 16.5),
                ft.Icon(ft.icons.KEYBOARD_DOUBLE_ARROW_RIGHT_ROUNDED),
            ]
        )             
    )
    
    line1_btn2 = ft.ElevatedButton(
        width = 130,
        bgcolor = ft.colors.LIGHT_BLUE_700,
        color = ft.colors.WHITE,
        content = ft.Row(
            [
                ft.Text("Execute", size= 16.5),
                ft.Icon(ft.icons.KEYBOARD_DOUBLE_ARROW_RIGHT_ROUNDED)
            ]
        )
    )

    line1_btn3 = ft.ElevatedButton(
        width = 130,
        bgcolor = ft.colors.LIGHT_BLUE_700,
        color = ft.colors.WHITE,
        content = ft.Row(
            [
                ft.Text("Add", size= 16.5),
                ft.Icon(ft.icons.KEYBOARD_DOUBLE_ARROW_RIGHT_ROUNDED)
            ]
        ),
        on_click = add_btn_clicked )

    line1_total = ft.Row(
        [
            line1_btn1,
            ft.Text("                                                    "),
            line1_btn2,
            ft.Text("                                                    "),
            line1_btn3
        ]
    )

    line2_input_txt = ft.TextField(
        hint_text= "Instruction Sentence",
        on_change = textbox_changed,
        width = 490,
        height = 40,
        border_color=ft.colors.BLACK38,
        border_width= 1.2,
        text_size= 15
    )

    line2_symbol_txt = ft.Text(
        size = 15,
        width = 285,
        color = ft.colors.BLACK,
        weight = ft.FontWeight.BOLD,
        text_align = ft.TextAlign.RIGHT,
        font_family = "HDText"
    )
    line2_symbol_txt.value = values[6]

    line2_total = ft.Row(
        [
            line2_input_txt,
            ft.Text("   "),
            ft.Container(
                content = ft.Text(
                    "SYMBOL",
                    color = ft.colors.WHITE,
                    weight = ft.FontWeight.BOLD,
                    size = 15,
                    width = 80,
                    text_align = ft.TextAlign.CENTER
                ),
                bgcolor = ft.colors.BLACK87,
                padding = 7,
                shadow = ft.BoxShadow(
                    spread_radius = 0.5,
                    blur_radius = 10,
                    color = ft.colors.BLUE_GREY_300,
                    offset = ft.Offset(0, 0),
                    blur_style = ft.ShadowBlurStyle.OUTER,
                )
            ),
            ft.Text(" "),
            ft.Container(
                content = ft.Row(
                    [
                        line2_symbol_txt,
                    ]
                ),
                bgcolor = ft.colors.LIGHT_BLUE_50,
                padding = 7,
                shadow = ft.BoxShadow(
                    spread_radius = 0,
                    blur_radius = 1,
                    color = ft.colors.BLUE_GREY_300,
                    offset = ft.Offset(0, 0),
                    blur_style = ft.ShadowBlurStyle.OUTER,
                )                    
            )
        ]
    )

    line3_input_txt1 = ft.TextField(
        hint_text = "LENGTH",
        on_change = textbox_changed,
        width = 115,
        height = 35,
        border_color=ft.colors.BLACK45,
        border_width= 1.2,
        text_size = 14,
        filled = True)
    
    line3_input_txt2 = ft.TextField(
        hint_text = "WIDTH",
        on_change = textbox_changed,
        width = 115,
        height = 35,
        border_color=ft.colors.BLACK45,
        border_width= 1.2,
        text_size = 14,
        filled = True)
    
    line3_input_txt3 = ft.TextField(
        hint_text = "AREA",
        on_change = textbox_changed,
        width = 115,
        height = 35,
        border_color = ft.colors.BLACK45,
        border_width = 1.2,
        text_size = 14,
        filled = True)
    
    line3_input_txt4 = ft.TextField(
        hint_text = "Q'TY",
        on_change = textbox_changed,
        width = 115,
        height = 35,
        border_color = ft.colors.BLACK45,
        border_width = 1.2,
        text_size = 14,
        filled = True)
    
    line3_mod_txt = ft.Text(
        size = 15,
        width = 285,
        color = ft.colors.BLACK,
        weight = ft.FontWeight.BOLD,
        text_align = ft.TextAlign.RIGHT,
        font_family = "HDText" )
    
    line3_mod_txt.value = values[7]

    line3_total = ft.Row(
        [
            line3_input_txt1,
            line3_input_txt2,
            line3_input_txt3,
            line3_input_txt4,
            ft.Text("   "),
            ft.Container(
                content = ft.Text(
                    "MOD",
                    color = ft.colors.WHITE,
                    weight = ft.FontWeight.BOLD,
                    size = 15,
                    width = 80,
                    text_align = ft.TextAlign.CENTER
                ),
                bgcolor = ft.colors.BLACK87,
                padding = 7,
                shadow = ft.BoxShadow(
                    spread_radius = 0.5,
                    blur_radius = 10,
                    color = ft.colors.BLUE_GREY_300,
                    offset = ft.Offset(0, 0),
                    blur_style = ft.ShadowBlurStyle.OUTER,
                )
            ),
            ft.Text(" "),
            ft.Container(
                content = ft.Row(
                    [
                        line3_mod_txt,
                    ]
                ),
                bgcolor = ft.colors.LIGHT_BLUE_50,
                padding = 7,
                shadow = ft.BoxShadow(
                    spread_radius = 0,
                    blur_radius = 1,
                    color = ft.colors.BLUE_GREY_300,
                    offset = ft.Offset(0, 0),
                    blur_style = ft.ShadowBlurStyle.OUTER,
                )                    
            )
        ]
    )

    line4_dd = ft.Dropdown(
        # on_change = dropdown_changed,
        label = "SPEC",
        width = 490,
        height = 40,
        color = ft.colors.WHITE,
        autofocus= True,
        options = [
            ft.dropdown.Option("option01"),
            ft.dropdown.Option("option02"),
            ft.dropdown.Option("option03")
        ]
    )
   
    line4_total = ft.Row(
        [
            line4_dd,
            ft.Text("   "),
            ft.Container(
                content = ft.Text(
                    "MH",
                    color = ft.colors.WHITE,
                    weight = ft.FontWeight.BOLD,
                    size = 15,
                    width = 80,
                    text_align = ft.TextAlign.CENTER ),
                bgcolor = ft.colors.BLACK87,
                padding = 7,
                shadow = ft.BoxShadow(
                    spread_radius = 1,
                    blur_radius = 10,
                    color = ft.colors.BLUE_GREY_300,
                    offset = ft.Offset(0, 0),
                    blur_style = ft.ShadowBlurStyle.OUTER,
                )
            ),
            ft.Text(" "),
            ft.Container(
                content = ft.Row(
                    [
                        ft.Text(
                            "2.0",
                            size = 15,
                            width = 285,
                            color = ft.colors.BLACK,
                            weight = ft.FontWeight.BOLD,
                            text_align = ft.TextAlign.RIGHT,
                            font_family = "HDText" ),
                    ]
                ),
                bgcolor = ft.colors.LIGHT_BLUE_50,
                padding = 7,
                shadow = ft.BoxShadow(
                    spread_radius = 0,
                    blur_radius = 1,
                    color = ft.colors.BLUE_GREY_300,
                    offset = ft.Offset(0, 0),
                    blur_style = ft.ShadowBlurStyle.OUTER,
                )                    
            )
        ]
    )

    line_1234_total = ft.Container(
        content = ft.Column(
            [
                ft.Text(" "),
                line1_total,
                line2_total,
                line3_total,
                line4_total,
                ft.Text(" "),
                ft.Divider(height = 1, color=ft.colors.BLACK45)
            ]
        )
    )

    dt = ft.DataTable(
        width = 1100,
        height = 300,
        bgcolor = ft.colors.WHITE,
        border = ft.border.all(0,color=ft.colors.BLACK45),
        border_radius = 6,
        heading_row_color = ft.colors.BLACK26,
        heading_row_height = 20,
        divider_thickness = 0,
        column_spacing = 1,
        columns = [
            # 0 Number
            ft.DataColumn(ft.Text(keys[0],
                                color = ft.colors.BLACK,
                                weight = "bold",
                                width = 40,
                                text_align=ft.TextAlign.CENTER,
                                font_family = "HDText"
                                )),
            # 1 Instruction
            ft.DataColumn(ft.Text(keys[1],
                                color = ft.colors.BLACK,
                                weight = "bold",
                                width = 300,
                                text_align=ft.TextAlign.CENTER,
                                font_family = "HDText"
                                )),
            # 2 Length
            ft.DataColumn(ft.Text(keys[2],
                                color = ft.colors.BLACK,
                                weight = "bold",
                                width = 60,
                                text_align=ft.TextAlign.CENTER,
                                font_family = "HDText"
                                )),
            # 3 Width
            ft.DataColumn(ft.Text(keys[3],
                                color = ft.colors.BLACK,
                                weight = "bold",
                                width = 60,
                                text_align=ft.TextAlign.CENTER,
                                font_family = "HDText"
                                )),
            # 4 Area
            ft.DataColumn(ft.Text(keys[4],
                                color = ft.colors.BLACK,
                                weight = "bold",
                                width = 60,
                                text_align=ft.TextAlign.CENTER,
                                font_family = "HDText"
                                )),
            # 5 Q'TY
            ft.DataColumn(ft.Text(keys[5],
                                color = ft.colors.BLACK,
                                weight = "bold",
                                width = 60,
                                text_align=ft.TextAlign.CENTER,
                                font_family = "HDText"
                                )),
            # 6 SPEC
            ft.DataColumn(ft.Text("SPEC",
                                color = ft.colors.BLACK,
                                weight = "bold",
                                width = 150,
                                text_align=ft.TextAlign.CENTER,
                                font_family = "HDText"
                                )),
            # 7 Symbol
            ft.DataColumn(ft.Text(keys[6],
                                color = ft.colors.BLACK,
                                weight = "bold",
                                width = 150,
                                text_align=ft.TextAlign.CENTER,
                                font_family = "HDText"
                                )),
            # 8 Mod
            ft.DataColumn(ft.Text(keys[7],
                                color = ft.colors.BLACK,
                                weight = "bold",
                                width = 60,
                                text_align = ft.TextAlign.CENTER,
                                font_family = "HDText"
                                )),
            # 9 MH
            ft.DataColumn(ft.Text(keys[8],
                                color = ft.colors.BLACK,
                                weight = "bold",
                                width = 60,
                                text_align = ft.TextAlign.CENTER,
                                font_family = "HDText"
                                ))
        ],
        rows = [
            ft.DataRow(
                [
                    # 0 Number
                    ft.DataCell(ft.Text(values[0],
                                        color = ft.colors.BLACK,
                                        weight = "bold",
                                        text_align = ft.TextAlign.CENTER,
                                        width = 40,
                                        font_family = "HDText"
                                        )),
                    # 1 Instrunction
                    ft.DataCell(ft.Text(values[1],
                                        color = ft.colors.BLACK,
                                        weight = "bold",
                                        text_align = ft.TextAlign.LEFT,
                                        width = 290,
                                        font_family = "HDText"
                                        )),
                    # 2 Length
                    ft.DataCell(ft.Text(values[2],
                                        color = ft.colors.BLACK,
                                        weight = "bold",
                                        text_align = ft.TextAlign.RIGHT,
                                        width = 50,
                                        font_family = "HDText"
                                        )),
                    # 3 Width
                    ft.DataCell(ft.Text(values[3],
                                        color = ft.colors.BLACK,
                                        weight = "bold",
                                        text_align = ft.TextAlign.RIGHT,
                                        width = 50,
                                        font_family = "HDText"
                                        )),
                    # 4 Area
                    ft.DataCell(ft.Text(values[4],
                                        color = ft.colors.BLACK,
                                        weight = "bold",
                                        text_align = ft.TextAlign.RIGHT,
                                        width = 50,
                                        font_family = "HDText"
                                        )),
                    # 5 Q'TY
                    ft.DataCell(ft.Text(values[5],
                                        color = ft.colors.BLACK,
                                        weight = "bold",
                                        text_align = ft.TextAlign.RIGHT,
                                        width = 50,
                                        font_family = "HDText"
                                        )),
                    # 6 SPEC
                    ft.DataCell(option_text),
                    # 7 Symbol
                    ft.DataCell(ft.Text(values[6],
                                        color = ft.colors.BLACK,
                                        weight = "bold",
                                        text_align = ft.TextAlign.CENTER,
                                        width = 150,
                                        font_family = "HDText"
                                        )),
                    # 8 Mod
                    ft.DataCell(ft.Text(values[7],
                                        color = ft.colors.BLACK,
                                        weight = "bold",
                                        text_align = ft.TextAlign.RIGHT,
                                        width = 47,
                                        font_family = "HDText"
                                        )),
                    # 9 MH
                    ft.DataCell(ft.Text(values[8],
                                        color = ft.colors.BLACK,
                                        weight = "bold",
                                        text_align = ft.TextAlign.RIGHT,
                                        width = 42,
                                        font_family = "HDText"
                                        ))
                ],
            )
        ]
    )
    
    return ft.Column(
        expand = True,
        alignment = ft.MainAxisAlignment.CENTER,
        controls = [line_1234_total, dt]
    )
    
def tab_menu(page):
    def tabs_changed(e):
        print(f"Tabs changed to {e.control.selected_index}")
    
    menu = ft.Tabs(
        selected_index = 0,
        animation_duration = 300,
        scrollable = True,
        expand = True,
        on_change = tabs_changed,
        tabs = [
            ft.Tab(
                tab_content = ft.Row(
                    [
                        ft.Icon(ft.icons.DRIVE_FILE_RENAME_OUTLINE_SHARP),
                        ft.Text("Standard Sheet",
                                font_family = "HDText",
                                size = 15,
                                weight = "bold")
                    ]
                ),
                content = std_sht()
            ),
            ft.Tab(
                tab_content = ft.Row(
                    [
                        ft.Icon(ft.icons.DRIVE_FILE_RENAME_OUTLINE_SHARP),
                        ft.Text("Paint Area Sheet",
                                font_family = "HDText",
                                size = 15,
                                weight = "bold")
                    ]
                ),
                content = paint_area()),
            ft.Tab(
                 tab_content = ft.Row(
                    [
                        ft.Icon(ft.icons.CALCULATE),
                        ft.Text("MH Calculation",
                                font_family = "HDText",
                                size = 15,
                                weight = "bold")
                    ]
                ),
                content = mh_calc(page))
        ]
    )
    return ft.Column(
        expand = True,
        alignment = ft.MainAxisAlignment.CENTER,
        controls = [menu]
    )

def main(page: ft.Page):
    page.fonts = {
        "HDText" : "<font path>"
    }
    page.title = "Paint Manufacturing Engineering"
    page.window_width = 1100
    page.window_height = 700
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT
    page.appbar = ft.AppBar(
        leading = ft.Icon(
            ft.icons.EDIT_SQUARE,
            color = ft.colors.WHITE,
            size = 30),
        leading_width = 50,
        title = ft.Text(
            "MH Editor",
            size = 30,
            weight = ft.FontWeight.BOLD,
            color = ft.colors.WHITE,
            font_family = "HDSansText"
        ),
        center_title = False,
        bgcolor = ft.colors.ON_SURFACE_VARIANT
    )
    page.add(tab_menu(page))

if __name__ == "__main__":
    ft.app(target = main)

