# nepali_toolkit/cli.py
import typer
from nepali_toolkit import calendar, nid, unicode_converter, power_schedule

app = typer.Typer()

@app.command()
def convert_date(from_calendar: str = typer.Option(..., help="AD or BS"),
                 date: str = typer.Option(..., help="Date in YYYY-MM-DD format")):
    result = calendar.convert(from_calendar, date)
    typer.echo(f"Converted date: {result}")

@app.command()
def validate_nid(nid_number: str):
    valid = nid.validate(nid_number)
    typer.echo("✅ Valid NID" if valid else "❌ Invalid NID")

@app.command()
def convert_text(from_script: str = typer.Option(..., help="unicode or preeti"),
                 text: str = typer.Option(...)):
    converted = unicode_converter.convert(from_script, text)
    typer.echo(converted)

@app.command()
def power_schedule(ward: int):
    schedule = power_schedule.get_schedule(ward)
    typer.echo(f"Power schedule for ward {ward}: {schedule}")

if __name__ == "__main__":
    app()
# This script uses Typer to create a command-line interface (CLI) for the Nepali Toolkit.
# It provides commands for converting dates, validating NIDs, converting text between scripts,
# and fetching power schedules. Each command is defined as a function decorated with @app.command().
# The Typer library handles command-line arguments and options, making it easy to create user-friendly CLI applications.
# The script imports necessary modules from the nepali_toolkit package and uses Typer to define the CLI.
# The `convert_date` command converts dates between AD and BS formats.
# The `validate_nid` command checks the validity of a Nepali ID number.
# The `convert_text` command converts text between Unicode and Preeti scripts.
# The `power_schedule` command retrieves the power schedule for a specified ward.
# The script is designed to be run from the command line, and it uses Typer's built-in help system to provide usage information.
# The `if __name__ == "__main__":` block ensures that the app runs when the script is executed directly.
# The `app()` function starts the Typer application, allowing users to interact with the CLI.
# The script is structured to be modular and easy to extend, allowing for the addition of more commands in the future.
# The use of type hints and Typer's options makes the code self-documenting, providing clear information about the expected input types and formats.
# The script is designed to be user-friendly, with clear help messages for each command and option.
# The CLI can be run from the terminal, and users can access help information by using the `--help` option.
