import seaborn as sns
from faicons import icon_svg

# Import data from shared.py
from shared import app_dir, df

from shiny import reactive
from shiny.express import input, render, ui

ui.page_opts(title="CYKELVENNERNES HJØRNE", window_title="CYKELVENNER", fillable=True)


with ui.sidebar(title="Filtre"):
    ui.input_checkbox_group(
        "hold",
        "Hold",
        ["INEOS Grenadiers", "Team Visma - Lease a Bike", "Alpecin - Deceuninck", "Lidl - Trek", "Decathlon AG2R La Mondiale", "UAE Emirates XRG"],
        selected=["INEOS Grenadiers", "Team Visma - Lease a Bike", "Alpecin - Deceuninck", "Lidl - Trek", "Decathlon AG2R La Mondiale", "UAE Emirates XRG"],
    )


with ui.layout_column_wrap(fill=False):
    with ui.value_box(showcase=icon_svg("person-biking")):
        "Antal ryttere"

        @render.text
        def count():
            return filtered_df().shape[0]

    with ui.value_box(showcase=icon_svg("ruler-horizontal")):
        "Gennemsnitspris"

        @render.text
        def bill_length():
            return f"{filtered_df()['RiderPrice'].mean():.1f} mil"

    with ui.value_box(showcase=icon_svg("ruler-vertical")):
        "Gennemsnitsprofit"

        @render.text
        def bill_depth():
            return f"{filtered_df()['PointsPerMillion'].mean():.1f} PPM"


with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Rytteroversigt")

        @render.data_frame
        def summary_statistics():
            cols = [
                "RiderName",
                "RiderTeam",
                "RiderPrice",
                "RiderName_PCS",
                "Points",
                "PointsPerMillion",
                "CheapoEligible"
            ]
            return render.DataGrid(filtered_df()[cols], filters=True)


ui.include_css(app_dir / "styles.css")


@reactive.calc
def filtered_df():
    filt_df = df[df["RiderTeam"].isin(input.hold())]
    return filt_df
