"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mcwmon_mysql` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``cwmon_mysql.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``cwmon_mysql.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import click
import oursql


@click.group()
@click.option('--host', default='127.0.0.1',
              help='The hostname where we can reach the DB.')
@click.option('--user', default='habnabit', help='The DB username')
@click.option('--passwd', default='foobar', help='The DB passwd')
@click.option('--db', default='example',
              help='The name of the specific DB to connect to')
@click.option('--port', default=3307,
              help='The port to use when connecting to the DB.')
@click.pass_context
def mysql(ctx, host, user, passwd, db, port):
    """Group MySQL monitoring commands for ``cwmon``."""
    ctx.obj.conn = oursql.connect(
        host=host,
        user=user,
        passwd=passwd,
        db=db,
        port=port
    )


@mysql.command()
@click.pass_obj
def echo(obj):
    """Echo out the info in ``obj`` (for debugging purposes)."""
    click.echo(obj.dry_run)
    click.echo(obj.conn)
