from click.testing import CliRunner
from pelican.cli import hello
from pelican.cli import catch_fish

def test_hello_world():
  runner = CliRunner()
  result = runner.invoke(hello, ['Peter'])
  assert result.exit_code == 0
  assert result.output == 'Hello Peter!\n'

def test_catch_sunfish():
  runner = CliRunner()
  result = runner.invoke(catch_fish, ['red eared sunfish'])
  assert result.exit_code == 0
  assert result.output == 'I\'ve got a red eared sunfish!\n'