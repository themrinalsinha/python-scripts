from click.testing import CliRunner

# local app import
from app import cli

# unit testing
def test_say_in_cli():
    runner = CliRunner()
    # invoke (main command, [sub commands to test with param])
    result = runner.invoke(cli, ["say", "ASSHOLE"])
    assert result.output == "You said: ASSHOLE\n"
    assert result.exit_code == 0

def test_greet_hi_cli():
    runner = CliRunner()
    # invoke (main command, [sub commands to test with param])
    result = runner.invoke(cli, ["greet", "Mrinal"])
    assert result.output == "Hello, Mrinal\n"
    assert result.exit_code == 0


# to run it
# pip install pytest
# py.test -v
