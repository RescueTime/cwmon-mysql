=====
Usage
=====

Monitoring a MySQL instance
===========================

Once you've install ``cwmon-mysql``, using it is as simple as invoking
``cwmon mysql``. The following caveats apply:

#) Your AWS API credentials need to be available in a manner
   understandable by boto3_.
#) You need to provide valid connection info for the MySQL instance
   to be monitored.

.. _boto3: http://boto3.readthedocs.io/en/latest/

To be truly useful, you probably need to automate this. The most
straightforward way to do this is probably via a crontab entry, e.g., ::

    3 * * * * cwmon mysql deadlocks uptime running_threads questions
      slow_queries open_files open_tables seconds_behind_master

.. note: This assumes that the cron job is running in a context where
         the above caveats are true. If not, then you would need to
         address that issue.
