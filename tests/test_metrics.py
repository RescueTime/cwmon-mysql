# -*- encoding: utf-8 -*-
"""Tests for the various metrics reported by the monitoring CLI."""
import os
import pymysql
import pymysql.cursors
import pytest

from cwmon_mysql import metrics


@pytest.fixture
def mysql_conn():
    """A connection to the MySQL DB under test."""
    return pymysql.connect(
        host=os.getenv('MYSQL_HOST', '127.0.0.1'),
        user=os.getenv('MYSQL_USER', 'root'),
        password=os.getenv('MYSQL_PASSWD', ''),
        db=os.getenv('MYSQL_DB', ''),
        port=os.getenv('MYSQL_PORT', 3306),
        cursorclass=pymysql.cursors.DictCursor
    )


def test_deadlocks_metric_happy_path(mysql_conn):
    """Create a :class:`~metrics.DeadlocksMetric`."""
    m = metrics.DeadlocksMetric(mysql_conn)
    assert "Innodb deadlocks" == m.unit


def test_uptime_metric_happy_path(mysql_conn):
    """Create a :class:`~metrics.UptimeMetric`."""
    m = metrics.UptimeMetric(mysql_conn)
    assert "Seconds" == m.unit


def test_running_threads_metric_happy_path(mysql_conn):
    """Create a :class:`~metrics.RunningThreadsMetric`."""
    m = metrics.RunningThreadsMetric(mysql_conn)
    assert "Threads" == m.unit


def test_questions_metric_happy_path(mysql_conn):
    """Create a :class:`~metrics.QuestionsMetric`."""
    m = metrics.QuestionsMetric(mysql_conn)
    assert "Questions" == m.unit


def test_slow_queries_metric_happy_path(mysql_conn):
    """Create a :class:`~metrics.SlowQueriesMetric`."""
    m = metrics.SlowQueriesMetric(mysql_conn)
    assert "Queries" == m.unit


def test_open_files_metric_happy_path(mysql_conn):
    """Create a :class:`~metrics.OpenFilesMetric`."""
    m = metrics.OpenFilesMetric(mysql_conn)
    assert "Files" == m.unit


def test_open_tables_metric_happy_path(mysql_conn):
    """Create a :class:`~metrics.OpenTablesMetric`."""
    m = metrics.OpenTablesMetric(mysql_conn)
    assert "Tables" == m.unit


def test_seconds_behind_master_metric_happy_path(mysql_conn):
    """Create a :class:`~metrics.SecondsBehindMasterMetric`."""
    m = metrics.SecondsBehindMasterMetric(mysql_conn)
    assert "Seconds" == m.unit
