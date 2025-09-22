import pandas as pd


def draw(data, columns):
    data_frame = pd.DataFrame(data)

    # data_frame.columns = columns

    # table = data_frame.style.format(
    #     {
    #         "Bearing 1 Lifespan (hours)": "{:,.0f}",
    #         "Bearing 2 Lifespan (hours)": "{:,.0f}",
    #         "Bearing 3 Lifespan (hours)": "{:,.0f}",
    #         "First Expiration (hours)": "{:,.0f}",
    #         "Cumulative Time (hours)": "{:,.0f}",
    #         "Random Number (Delay)": "{:,.0f}",
    #         "Delay Time (minutes)": "{:,.0f}",
    #     }
    # ).highlight_min(
    #     subset=["Bearing 1 Lifespan (hours)", "Bearing 2 Lifespan (hours)", "Bearing 3 Lifespan (hours)"],
    #     color="lightcoral",
    # ).highlight_max(
    #     subset=["Bearing 1 Lifespan (hours)", "Bearing 2 Lifespan (hours)", "Bearing 3 Lifespan (hours)"],
    #     color="lightgreen",
    # ).background_gradient(
    #     subset=["Cumulative Time (hours)", "Delay Time (minutes)"],
    #     cmap="Blues",
    # ).set_caption(
    #     "Simulation Results: Bearing Lifespans and Fixer Delays"
    # )

    table = data_frame.style.set_table_styles(
        [
            {"selector": "thead th", "props": [("color", "white"), ("background-color", "black"), ("border", "0.5px solid white")]},
            {"selector": "tbody td", "props": [("color", "white"), ("background-color", "black"), ("border", "0.5px solid white")]},
            {"selector": "table", "props": [("border-collapse", "separate"), ("border-spacing", "5px"), ("border", "0.5px solid white")]},
        ]
    ).set_properties(
        **{
            "color": "white",
            "background-color": "black",
            "border": "0.5px solid white",
        }
    )

    return table


