# -*- encoding: utf-8 -*-
"""Collection of MySQL-related metrics."""
from cwmon.metrics import Metric


class _MysqlStatus():
    """Clean interface to ``SHOW STATUS`` info we want to report on."""

    def __init__(self, conn):
        with conn.cursor() as c:
            c.execute('SHOW STATUS')
            query_results = c.fetchall()
        status_dict = dict(
            ((r['Variable_name'], r['Value']) for r in query_results)
        )
        self.uptime = status_dict['Uptime']
        self.running_threads = status_dict['Threads_running']
        self.questions = status_dict['Questions']
        self.slow_queries = status_dict['Slow_queries']
        self.open_files = status_dict['Open_files']
        self.open_tables = status_dict['Open_tables']


class _MysqlSlaveStatus():
    """Clean interface to ``SHOW SLAVE STATUS`` info we want to report on."""

    def __init__(self, conn):
        with conn.cursor() as c:
            c.execute('SHOW SLAVE STATUS')
            query_results = c.fetchone()

        if query_results:
            self.seconds_behind_master = query_results['Seconds_Behind_Master']
            self.slave_io_running = query_results['Slave_IO_Running'] == 'Yes'
            self.slave_sql_running = query_results['Slave_SQL_Running'] == 'Yes'
        else:
            self.seconds_behind_master = None
            self.slave_io_running = 'No'
            self.slave_sql_running = 'No'


class DeadlocksMetric(Metric):
    """A :class:`~cwmon.metrics.Metric` for current INNODB deadlocks.

    .. note:: This only works on Percona Toolkit servers due to its
              reliance on a global status variable (``Innodb_deadlocks``)
              that is not defined for other variants of MySQL.
    """

    def __init__(self, conn):
        """Create a new ``Metric`` for the current number of deadlocks.

        :param conn: our connection to the DB
        :type conn: a `DB-API 2.0 Connection object`_

        .. _DB-API 2.0 Connection object: https://www.python.org/dev/peps/pep-0249/#connection-objects
        """
        self.conn = conn
        super().__init__('InnoDB Deadlocks')

    def _capture(self):
        with self.conn.cursor() as c:
            c.execute("SHOW GLOBAL STATUS LIKE 'innodb_deadlocks'")
            result = c.fetchone()
        if result is not None:
            self.value = result['Value']
        else:
            self.value = None
        self.unit = 'Innodb deadlocks'


class UptimeMetric(Metric):
    """A :class:`~cwmon.metrics.Metric` for the MySQL server's uptime."""

    def __init__(self, conn):
        """Create a new ``Metric`` for the server's uptime.

        :param conn: our connection to the DB
        :type conn: a `DB-API 2.0 Connection object`_

        .. _DB-API 2.0 Connection object: https://www.python.org/dev/peps/pep-0249/#connection-objects
        """
        self.conn = conn
        super().__init__('Uptime')

    def _capture(self):
        status_info = _MysqlStatus(self.conn)
        self.value = status_info.uptime
        self.unit = 'Seconds'


class RunningThreadsMetric(Metric):
    """A :class:`~cwmon.metrics.Metric` for the number of running threads."""

    def __init__(self, conn):
        """Create a new ``Metric`` for the number of running threads.

        :param conn: our connection to the DB
        :type conn: a `DB-API 2.0 Connection object`_

        .. _DB-API 2.0 Connection object: https://www.python.org/dev/peps/pep-0249/#connection-objects
        """
        self.conn = conn
        super().__init__('Running Threads')

    def _capture(self):
        status_info = _MysqlStatus(self.conn)
        self.value = status_info.running_threads
        self.unit = 'Threads'


class QuestionsMetric(Metric):
    """A :class:`~cwmon.metrics.Metric` for the number of questions."""

    def __init__(self, conn):
        """Create a new ``Metric`` for the number of questions.

        :param conn: our connection to the DB
        :type conn: a `DB-API 2.0 Connection object`_

        .. _DB-API 2.0 Connection object: https://www.python.org/dev/peps/pep-0249/#connection-objects
        """
        self.conn = conn
        super().__init__('Questions')

    def _capture(self):
        status_info = _MysqlStatus(self.conn)
        self.value = status_info.questions
        self.unit = 'Questions'


class SlowQueriesMetric(Metric):
    """A :class:`~cwmon.metrics.Metric` for the number of slow queries."""

    def __init__(self, conn):
        """Create a new ``Metric`` for the number of slow queries.

        :param conn: our connection to the DB
        :type conn: a `DB-API 2.0 Connection object`_

        .. _DB-API 2.0 Connection object: https://www.python.org/dev/peps/pep-0249/#connection-objects
        """
        self.conn = conn
        super().__init__('Slow Queries')

    def _capture(self):
        status_info = _MysqlStatus(self.conn)
        self.value = status_info.slow_queries
        self.unit = 'Queries'


class OpenFilesMetric(Metric):
    """A :class:`~cwmon.metrics.Metric` for the number of open files."""

    def __init__(self, conn):
        """Create a new ``Metric`` for the number of open files.

        :param conn: our connection to the DB
        :type conn: a `DB-API 2.0 Connection object`_

        .. _DB-API 2.0 Connection object: https://www.python.org/dev/peps/pep-0249/#connection-objects
        """
        self.conn = conn
        super().__init__('Open Files')

    def _capture(self):
        status_info = _MysqlStatus(self.conn)
        self.value = status_info.open_files
        self.unit = 'Files'


class OpenTablesMetric(Metric):
    """A :class:`~cwmon.metrics.Metric` for the number of open tables."""

    def __init__(self, conn):
        """Create a new ``Metric`` for the number of open tables.

        :param conn: our connection to the DB
        :type conn: a `DB-API 2.0 Connection object`_

        .. _DB-API 2.0 Connection object: https://www.python.org/dev/peps/pep-0249/#connection-objects
        """
        self.conn = conn
        super().__init__('Open Tables')

    def _capture(self):
        status_info = _MysqlStatus(self.conn)
        self.value = status_info.open_tables
        self.unit = 'Tables'


class SecondsBehindMasterMetric(Metric):
    """A :class:`~cwmon.metrics.Metric` for the slave lag."""

    def __init__(self, conn):
        """Create a new ``Metric`` for the slave lag.

        :param conn: our connection to the DB
        :type conn: a `DB-API 2.0 Connection object`_

        .. _DB-API 2.0 Connection object: https://www.python.org/dev/peps/pep-0249/#connection-objects
        """
        self.conn = conn
        super().__init__('Seconds Behind Master')

    def _capture(self):
        status_info = _MysqlSlaveStatus(self.conn)
        self.value = status_info.seconds_behind_master
        self.unit = 'Seconds'
