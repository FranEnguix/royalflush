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
    def cli(ctx: click.Context, verbose: bool) -> None:
        """
        RoyalFlush command line tool that provides exactly three commands:
          1. run
          2. analyze-logs
          3. version

        Two global options are also available:
          --verbose, --help

        Args:
            ctx (click.Context): The current Click context object.
            verbose (bool): Whether verbose output is enabled.
        """
        ctx.ensure_object(dict)
        ctx.obj["VERBOSE"] = verbose
        if verbose:
            click.echo("Verbose mode enabled.")

    # Add subcommands to the main group
    cli.add_command(run_cmd)
    cli.add_command(analyze_logs_cmd)
    cli.add_command(version_cmd)
    cli.add_command(create_template_cmd)

    return cli


# Create a single instance of the CLI
cli = create_cli()

if __name__ == "__main__":
    # Execute the CLI when the module is run directly.
    sys.exit(cli.main())
