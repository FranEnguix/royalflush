"""Command Line Interface (CLI) entry point for the RoyalFlush package."""

import sys

import click

from royalflush._commands.analyze_logs import analyze_logs_cmd
from royalflush._commands.create_template import create_template_cmd
from royalflush._commands.run import run_cmd
from royalflush._commands.version import version_cmd


def create_cli() -> click.Group:
    """
    Factory function to create the RoyalFlush CLI.

    Returns:
        click.Group: The CLI group with all subcommands attached.
    """

    @click.group()
    def cli_fn():
        """Royal FLush CLI"""

    # def cli_fn(ctx: click.Context, verbose: bool) -> None:
    # ctx.ensure_object(dict)
    # ctx.obj["VERBOSE"] = verbose
    # if verbose:
    #     click.echo("Verbose mode enabled.")

    # @cli_fn.command()
    # @click.option("--create-template", default="experiment.json", help="Template")
    # def template(template_file: str) -> None:
    #     """
    #     Create a JSON template for the experiment.

    #     Usage:
    #     royalflush create-template [<filename>]

    #     If <filename> is not provided, it defaults to 'template.json'.

    #     Example:
    #     royalflush create-template
    #     royalflush create-template experiment.json

    #     The resulting JSON has the following structure:
    #     {
    #         "uuid4": "generate_new_uuid4",
    #         "algorithm": "ACoL",
    #         "algorithm_rounds": 10,
    #         "consensus_iterations": 10,
    #         "training_epochs": 1,
    #         "graph_path": "/data/user/graphs/star.gml",
    #         "dataset": "cifar100",
    #         "distribution": "non_iid diritchlet 0.1",
    #         "ann": "cnn5"
    #     }

    #     Args:
    #         ctx (click.Context): The Click context object.
    #         template_file (str): Filename where the JSON is created. Defaults to "template.json".
    #     """
    #     if not template_file:
    #         template_file = "template.json"

    #     file_path = Path(template_file)

    #     if file_path.exists():
    #         click.echo(f"Error: File '{template_file}' already exists.")
    #         return

    #     template_data = {
    #         "uuid4": "generate_new_uuid4",
    #         "algorithm": "ACoL",
    #         "algorithm_rounds": 10,
    #         "consensus_iterations": 10,
    #         "training_epochs": 1,
    #         "graph_path": "/data/user/graphs/star.gml",
    #         "dataset": "cifar100",
    #         "distribution": "non_iid diritchlet 0.1",
    #         "ann": "cnn5",
    #     }

    #     try:
    #         file_path.write_text(json.dumps(template_data, indent=4), encoding="utf-8")
    #     except OSError as exc:
    #         click.echo(f"Error creating template file: {exc}")
    #         return

    #     click.echo(f"Template created at '{template_file}'.")

    # Add subcommands to the main group
    cli_fn.add_command(run_cmd)
    cli_fn.add_command(analyze_logs_cmd)
    cli_fn.add_command(version_cmd)
    cli_fn.add_command(create_template_cmd)

    return cli_fn


# Create a single instance of the CLI
cli = create_cli()

if __name__ == "__main__":
    sys.exit(cli.main())
