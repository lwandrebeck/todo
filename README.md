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
- [x] Enhanced display. (better could probably be found. Tailored for 132col terminal)

## Todo (no pun intented)
- [ ] Man page.
- [ ] RPM Packaging.
- [ ] DEB Packaging.
- [ ] Add the possibility to choose db location at first launch ?
