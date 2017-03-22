# todo
a simplistic todo cli written in Bash, using SQLite.

## Features
* Add a task (-a), creation timestamp automatically stored.
* Mark a task as completed (-c), completion timestamp automatically stored.
* Delete a task (-d)
* Display still valid tasks by default (no args)
* Display all tasks (-a), valid and completed ones.
* Ability to choose SQLite database location via a simple ~/.todorc
* Ability to tweak SQLite output via ~/.todorc

## Todo (no pun intented)
* Enhance display
* Properly check sqlite3 version so we use either FTS3 or 4.
* Ability to search task by pattern ?

