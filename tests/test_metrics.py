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
