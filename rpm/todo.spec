Name:           todo
Version:        0.9.11
Release:        1%{?dist}
Summary:        Simple CLI todo list manager written in Bash, using SQLite to store your todo list data.

License:        GPLv3+
URL:            https://github.com/lwandrebeck/todo
Source0:        https://github.com/lwandrebeck/todo/archive/v%{version}.zip
BuildArch:      noarch

BuildRequires:  groff-base
Requires:       bash, sqlite, file

%description
simple CLI todo list manager written in Bash, using SQLite to store your todo list data.

%prep
%autosetup
%build
nroff -man man/todo.1 | gzip > man/todo.1.gz
%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
install -p -m 755 todo %{buildroot}/%{_bindir}
install -p -m 644  man/todo.1.gz %{buildroot}/%{_mandir}/man1/

%files
%{_bindir}/todo
%{_mandir}/man1/todo.1.gz

%license LICENSE
%doc README.md

%changelog
* Mon Jun 19 2017 Laurent Wandrebeck <l.wandrebeck@quelquesmots.fr> - 0.9.11
- 0.9.11 release. Several fixes thanks to FlashCode.

* Thu Jun 15 2017 Laurent Wandrebeck <l.wandrebeck@quelquesmots.fr> - 0.9.10
- 0.9.10 release.

* Wed Apr 05 2017 Laurent Wandrebeck <l.wandrebeck@quelquesmots.fr> - 0.9.9
- 0.9.9 release.

* Wed Apr 05 2017 Laurent Wandrebeck <l.wandrebeck@quelquesmots.fr> - 0.9.8
- 0.9.8 release.

* Mon Apr 03 2017 Laurent Wandrebeck <l.wandrebeck@quelquesmots.fr> - 0.9.7
- 0.9.7 release.

* Sun Apr 02 2017 Laurent Wandrebeck <l.wandrebeck@quelquesmots.fr> - 0.9.6
- 0.9.6 release.
- Add file as a dependency, who knows.

* Sat Apr 01 2017 Laurent Wandrebeck <l.wandrebeck@quelquesmots.fr> - 0.9.5
- 0.9.5 release.

* Sat Apr 01 2017 Laurent Wandrebeck <l.wandrebeck@quelquesmots.fr> - 0.9.4
- Initial packaging.
