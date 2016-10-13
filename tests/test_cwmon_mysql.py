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
    result = _run_mysql_metric('')

    assert result.output.startswith('Usage')
    assert result.exit_code == 0


def test_deadlocks():
    """Test the happy path for deadlock detection."""
    result = _run_mysql_metric('deadlocks')
    assert result.exit_code == 0


def test_uptime():
    """Test the happy path for uptime measurement."""
    result = _run_mysql_metric('uptime')
    assert result.exit_code == 0


def test_running_threads():
    """Test the happy path for measuring running threads."""
    result = _run_mysql_metric('running_threads')
    assert result.exit_code == 0


def test_questions():
    """Test the happy path for counting questions."""
    result = _run_mysql_metric('questions')
    assert result.exit_code == 0


def test_slow_queries():
    """Test the happy path for counting slow queries."""
    result = _run_mysql_metric('slow_queries')
    assert result.exit_code == 0


def test_open_files():
    """Test the happy path for counting open files."""
    result = _run_mysql_metric('open_files')
    assert result.exit_code == 0


def test_open_tables():
    """Test the happy path for counting open tables."""
    result = _run_mysql_metric('open_tables')
    assert result.exit_code == 0


def test_seconds_behind_master():
    """Test the happy path for measuring slave lag."""
    result = _run_mysql_metric('seconds_behind_master')
    assert result.exit_code == 0
