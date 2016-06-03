# -*- encoding: utf-8 -*-
"""Tests for the monitoring CLI.

.. danger:: You **must** pass the `--dry-run` flag in all tests. Failure to do
            so will result in flooding AWS CloudWatch with bogus stats.
"""
from click.testing import CliRunner

from cwmon.cli import cwmon


def _run_mysql_metric(name, *args):
    runner = CliRunner()
    my_args = ['--dry-run', 'mysql']
    if name:
        my_args.append(name)
    my_args.extend(args)
    return runner.invoke(cwmon, my_args)


def test_mysql_registered_correctly():
    """Test the primary entrypoint of the CLI some more."""
    result = _run_mysql_metric('--help')

    assert result.output.startswith('Usage')
    assert result.exit_code == 0
