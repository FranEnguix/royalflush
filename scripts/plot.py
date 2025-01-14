from typing import List

import pandas as pd
import plotly.express as px


# Load the dataset
def load_dataset(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)


def extract_agent_name(data: pd.DataFrame) -> pd.DataFrame:
    data["agent_name"] = data["agent"].str.split("@").str[0]
    return data


def get_unique_layers(data: pd.DataFrame) -> List[str]:
    return data["layer"].unique().tolist()


def generate_line_plots(data: pd.DataFrame, unique_layers: List[str]) -> None:
    for layer in unique_layers:
        # Filter data for the current layer
        layer_data = data[data["layer"] == layer]

        # Create the line plot
        fig = px.line(
            layer_data,
            x="algorithm_round",
            y="weight",
            color="agent_name",
            title=f"Convergence of Weights for Layer: {layer}",
            labels={"algorithm_round": "Epoch", "weight": "Weight Value", "agent_name": "Agent"},
        )

        # Update layout for better aesthetics
        fig.update_layout(legend_title="Agents", title_x=0.5)

        # Show the plot
        fig.show()


if __name__ == "__main__":
    # experiment_name: str = "2024_12_12_T_17_00_04_268639_Z"
    experiment_name: str = "2024_12_12_T_12_48_12_365453_Z"
    file_path: str = f"../logs/{experiment_name}/raw/nn_convergence.csv"
    data: pd.DataFrame = load_dataset(file_path)
    data = extract_agent_name(data)
    unique_layers: List[str] = get_unique_layers(data)
    generate_line_plots(data, unique_layers)
