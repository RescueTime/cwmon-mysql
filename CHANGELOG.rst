Changelog
=========

%%version%% (unreleased)
------------------------

New
~~~

- Expose new metrics on CLI. [Hank Gay]

- Happy path tests for new metrics. [Hank Gay]

- Add initial test for metrics. [Hank Gay]

- Add happy-path test of deadlocks subcommand. [Hank Gay]

- First draft of CLI for new deadlocks metric. [Hank Gay]

- First draft of an actual MySQL metric (InnoDB deadlocks). [Hank Gay]

- Add 'echo' subcommand to aid in debugging. [Hank Gay]

- Make all MySQL commands accept connection parameters. [Hank Gay]

- Stub in a MySQL command group under 'cwmon'. [Hank Gay]

Changes
~~~~~~~

- Tell Travis to run MySQL for us. [Hank Gay]

- Make deadlocks metric robust on non-Percona servers. [Hank Gay]

- Use real MySQL connection (as pytest fixture) when testing metrics.
  [Hank Gay]

- Change the defaults to improve testability. [Hank Gay]

- Remove 'echo' command, since we have an actual command now. [Hank Gay]

- Pull MySQL credentials from env vars to improve testability. [Hank
  Gay]

- Remove trailing blank line. [Hank Gay]

Fix
~~~

- Fix Seconds Behind Master metric (it was trying to use wrong status
  info as datasource). [Hank Gay]

- Stop manually associating mysql subgroup to cwmon group. [Hank Gay]

  The click-plugins library is already taking care of that for me.
  Removing the code that attempts to make the association manually causes
  the subgroup to start loading properly.

Other
~~~~~

- Bump version: 0.1.0 → 0.2.0. [Hank Gay]

- Dev: Add dependency on oursql. [Hank Gay]

- Register the 'mysql' command group as a plugin to cwmon. [Hank Gay]

- Doc: Fix license file to identify RescueTime as the copyright holder.
  [Hank Gay]

- Doc: Fix RST for coveralls badge. [Hank Gay]

- Doc: linkify 'cwmon' in short description. [Hank Gay]

- Doc: Do some badge tweaking. [Hank Gay]

- Don't point Travis-CI to non-existent tox envs. [Hank Gay]

- Doc: list 'tox' as a dev dependency. [Hank Gay]

- Doc: List some basic dev dependencies. [Hank Gay]

- Doc: Update package keywords. [Hank Gay]

- Stop pretending to support Python 2; this is Python 3-only. [Hank Gay]

- Doc: Point to RescueTime org instead of personal account for 3rd-party
  support services. [Hank Gay]

- Tell bumpversion not to tag in git (because we use git flow for that).
  [Hank Gay]

- Initial project skeleton. [Hank Gay]


