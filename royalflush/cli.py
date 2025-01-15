"""Command Line Interface (CLI) entry point for the RoyalFlush package."""

import sys

import click

from royalflush.commands import analyze_logs_cmd, create_template_cmd, run_cmd, version_cmd


def create_cli() -> click.Group:
    """
    Factory function to create the RoyalFlush CLI.

    Returns:
        click.Group: The CLI group with all subcommands attached.
    """

    @click.group()
    @click.option("--verbose", is_flag=True, help="Enable verbose output")
    @click.pass_context
    def cli_fn(ctx: click.Context, verbose: bool) -> None:
        ctx.ensure_object(dict)
        ctx.obj["VERBOSE"] = verbose
        if verbose:
            click.echo("Verbose mode enabled.")

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
