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
- [x] database path customization at first launch
- [x] RPM Packaging.
- [x] DumP (-p) and imporT (-t, with a default backup before import, -T, without) of database in SQL format.
- [x] Backup (-b) and Restore (-r) of database in binary format.
- [x] Ability to move (-m) database to another directory, updates .todorc accordingly.
- [x] Ability to move (-M) database to another potentially non-existing directory, updates .todorc accordingly.
- [x] Ability to update (-e) database path if another database already exists.
- [x] Ability to update (-E) database path if another database already exists, and erase previous database file if possible.

## Todo (no pun intented)
- [ ] DEB Packaging.
- [ ] Would it be better to keep global variables way of bash (tododb, sqliteopts, actualsqlmode, sqlmode), or declare it as local and pass it as arguments to be really clean ?

## Won’t implement
- [ ] Allow a category personnal/job for each todo entry. NOPE (too much changes (hint: add a keyword or something in task description.))

## Known bugs
- None known right now.

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
