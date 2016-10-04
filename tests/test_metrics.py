# -*- encoding: utf-8 -*-
"""Tests for the various metrics reported by the monitoring CLI."""
from unittest import mock
import pytest

from cwmon_mysql import metrics


def _mock_connection():
    return mock.Mock()


def test_deadlocks_metric_happy_path():
    """Create a :class:`~metrics.DeadlocksMetric`."""
    m = metrics.DeadlocksMetric(_mock_connection())
    assert "Innodb deadlocks" == m.unit
