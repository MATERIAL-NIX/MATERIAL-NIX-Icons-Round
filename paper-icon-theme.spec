# Spec file for package MATERIAL-NIX-Round
#
# Copyright (c) 2016 Sam Hewitt <sam@snwh.org>
# Copyright (c) 2016 Adam Harley <https://plus.google.com/u/0/communities/103720848213793037553>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#


# GitHub Stuff
%global commit0 40-CHARACTER-HASH-VALUE

name:       MATERIAL-NIX-Icons-Round
version:    0.1
release:    1

Summary:    MATERIAL*NIX Round Icon theme
Group:      System/GUI/Other
License:    CC-BY-SA-4.0
Url:        https://plus.google.com/u/0/communities/103720848213793037553
Source0:    https://github.com/MATERIAL-NIX/%{name}/archive/%{commit0}.tar.gz
Requires:   hicolor-icon-theme, gnome-icon-theme
BuildArch:  noarch


%description
MATERIAL*NIX Round Icon Theme

%prep
%setup -qn %{name}-%{commit0}

# Delete dead icon symlinks
find -L . -type l -delete

%build

%install
install -dpm 0755 $RPM_BUILD_ROOT%{_datadir}/icons/
cp -a MATERIAL-NIX-Round/ $RPM_BUILD_ROOT%{_datadir}/icons/

%files
%doc AUTHORS COPYING
%{_datadir}/icons/MATERIAL-NIX-Round/
