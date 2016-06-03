# -*- encoding: utf-8 -*-
"""Collection of MySQL-related metrics."""
from cwmon.metrics import Metric


class DeadlocksMetric(Metric):
    """A :class:`~cwmon.metrics.Metric` for current INNODB deadlocks."""

    def __init__(self, conn):
        """Create a new ``Metric`` for the current number of deadlocks.

        :param conn: our connection to the DB
        :type conn: a `DB-API 2.0 Connection object`_

        .. _DB-API 2.0 Connection object: https://www.python.org/dev/peps/pep-0249/#connection-objects
        """
        self.conn = conn
        super().__init__("InnoDB Deadlocks")

    def _capture(self):
        with self.conn.cursor() as c:
            c.execute("SHOW GLOBAL STATUS LIKE 'innodb_deadlocks'")
            self.value = c.fetchone()['Value']
            self.unit = 'Innodb_deadlocks'
