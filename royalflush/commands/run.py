"""Command to run the RoyalFlush experiment."""

import json
from pathlib import Path
from typing import Any, Dict

import click

from royalflush.datatypes import Experiment


@click.command(name="run")
@click.argument("experiment_file", type=click.Path())
@click.pass_context
def run_cmd(ctx: click.Context, experiment_file: str) -> None:
    """
    Run the main RoyalFlush application with the provided JSON experiment file.

    Usage:
        royalflush run experiment.json

    Args:
        ctx (click.Context): The Click context object.
        experiment_file (str): Path to the JSON experiment file to load.
    """
    file_path: Path = Path(experiment_file)
    if not file_path.is_file():
        click.echo(f"Error: File '{experiment_file}' does not exist or it is not a file.")
        return

    if file_path.suffix.lower() != ".json":
        click.echo("Error: Only .json experiment files are supported.")
        return

    # Load JSON
    try:
        config_data: Dict[str, Any] = json.loads(file_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        click.echo(f"Error loading JSON data: {exc}")
        return

    experiment = Experiment.from_json(config_data)

    if ctx.obj.get("VERBOSE"):
        click.echo(f"Experiment loaded: {experiment}")

    # Your primary "run" logic goes here:
    click.echo("RoyalFlush is running with the given experiment configuration...")
