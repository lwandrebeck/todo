# todo
a simplistic todo cli written in Bash, using SQLite.

## Features
- [x] Errors out properly if sqlite3 command is unavailable.
- [x] Add a task (-n), creation timestamp automatically stored.
- [x] Mark a task as completed (-c), completion timestamp automatically stored.
- [x] Delete a task (-d).
- [x] Display valid tasks by default (no args).
- [x] Display all tasks (-a), valid and completed ones.
- [x] Ability to choose SQLite database location via a simple ~/.todorc
- [x] Ability to tweak SQLite output via ~/.todorc
- [x] Use classic, FTS3 or 4 database format and SQL according to SQLite version.
- [x] Use older database format if already existing.
- [x] Exit if a newer and unsupported database file format is present.
- [x] Ability to search valid tasks (-s) by word.
- [x] Ability to search valid and completed tasks (-S) by word.

## Todo (no pun intented)
- [ ] Enhance display
- [ ] Man page
- [ ] RPM Packaging
- [ ] DEB Packaging
