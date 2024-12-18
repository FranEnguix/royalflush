import json
import os

import click


def load_config(file_path: str):
    try:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Configuration file '{file_path}' not found.")
        with open(file_path, mode="r", encoding="utf-8") as f:
            if file_path.endswith(".json"):
                return json.load(f)
            raise ValueError("Unsupported file type. Use .json.")
    except Exception as e:
        click.echo(f"Error loading configuration: {e}")
        return None


@click.group()
@click.option("--verbose", is_flag=True, help="Enable verbose output")
@click.pass_context
def cli(ctx, verbose):
    """Royal FLush command client tool."""
    ctx.ensure_object(dict)
    ctx.obj["VERBOSE"] = verbose
    if verbose:
        click.echo("Verbose mode enabled")


@cli.command()
@click.option("--config", type=click.Path(exists=True), required=True, help="Path to the configuration file")
@click.pass_context
def run(ctx, config):
    """Run the main Royalflush application."""
    # Load configuration
    config_data = load_config(config)

    if config_data is None:
        click.echo("Failed to load configuration.")
        return

    if ctx.obj["VERBOSE"]:
        click.echo(f"Configuration loaded: {config_data}")

    # Add your main execution logic here
    click.echo("Royalflush is running...")


@cli.command()
@click.option("--config", type=click.Path(exists=True), required=True, help="Path to the configuration file")
@click.pass_context
def launch_agents(ctx, config):
    """Launch agents based on the configuration."""
    # Load configuration
    config_data = load_config(config)

    if config_data is None:
        click.echo("Failed to load configuration.")
        return

    if ctx.obj["VERBOSE"]:
        click.echo(f"Configuration loaded: {config_data}")

    # Logic to launch agents goes here
    click.echo("Launching agents...")


@cli.command()
@click.option("--log-file", type=click.Path(), required=True, help="Path to the log file")
@click.pass_context
def analyze_logs(ctx, log_file):
    """Analyze the logs from a previous run."""
    # Check if log file exists
    if not os.path.isfile(log_file):
        click.echo(f"Log file '{log_file}' not found.")
        return

    # Load and analyze the log file
    if ctx.obj["VERBOSE"]:
        click.echo(f"Analyzing log file: {log_file}")

    # Example analysis logic
    click.echo("Log analysis complete.")


@cli.command()
@click.option("--output-dir", type=click.Path(), required=True, help="Directory to store the plots")
@click.pass_context
def generate_plots(ctx, output_dir):
    """Generate plots for the experiment results."""

    if ctx.obj["VERBOSE"]:
        click.echo(f"Generating plots in: {output_dir}")

    # Example plot generation logic
    click.echo("Plots generated successfully.")


def main():
    cli()
