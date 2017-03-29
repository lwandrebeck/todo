# todo
a simplistic todo cli written in Bash, using SQLite.

## Features
- [x] Errors out properly if sqlite3 command is unavailable.
- [x] Add a New task (-n), creation timestamp automatically stored.
- [x] Mark a task as Completed (-c), completion timestamp automatically stored.
- [x] Delete a task (-d).
- [x] Display valid tasks by default (no args).
- [x] Display All tasks (-a), valid and completed ones.
- [x] Ability to choose SQLite database location via a simple ~/.todorc
- [x] Ability to tweak SQLite output via ~/.todosqliterc
- [x] Use classic, or FTS3 SQL and database format if available.
- [x] Use older database format if already existing.
- [x] Exit if a newer and unsupported database file format is present.
- [x] Ability to Search valid tasks (-s) by word.
- [x] Ability to Search valid and completed tasks (-S) by word.
- [x] Ability to mark as Unfinished (-u) a task previously marked as completed.
- [x] Enhanced display. (better could probably be found. Tailored for 132col terminal)
- [x] Man page.

## Todo (no pun intented)
- [ ] RPM Packaging.
- [ ] DEB Packaging.
- [ ] Add the possibility to choose db location at first launch ?

todo SQL database is very simple:

info table (single entry) |
------------------------- |
sqlmode (text not null) |
creation (date as text not null) |
todoversion (text not null) |
sqliteversion (text not null) |

todo table (one line per entry) |
------------------------------- |
title (text not null) |
creation (date as text not null) |
completed (date as text) |

date is date +"%Y-%m-%d %R:%S" formatted

rowid is automatically defined by SQLite.
