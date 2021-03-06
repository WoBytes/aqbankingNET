#
# spec file for package aqankingNET for openSUSE / SUSE 
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           aqbankingNET

# Version is set/replaced by OBS by a timestamp when using git
Version:	1.0   

Release:        1
Summary:	A common language runtime (CLR) wrapper library for aqbanking

License:       	MIT/X11 
URL:           	https://github.com/Dynalon/aqbankingNET
BuildArch:      i586 x86_64

BuildRequires: 	mono-devel >= 2.2
BuildRequires:  git
BuildRequires:  swig >= 1.3
BuildRequires:	aqbanking-devel >= 5.0.0

Requires:	mono-core >= 2.2
Requires:	aqbanking >= 5.0.0

Source: %{name}-%{version}.tar

%description
A common language runtime (CLR) wrapper library for aqbanking. Allows C# and
other CLR/.NET compatible languages to use aqbanking on Linux/UNIX using mono.

%define gitrepo git://github.com/Dynalon/aqbankingNET.git

%define source_tar %{name}-%{version}.tar
%define source_folder %{name}-%{version}

%prep
%setup

%build
make

%install
# GAC_ROOT is not _libdir as its never(!) lib64
make DESTDIR=%{buildroot}/usr GAC_ROOT=%{buildroot}/usr/lib/ install

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%preun
gacutil -u aqbankingNET > /dev/null

%postun
/sbin/ldconfig

%files
#define the files that actually get included in the rpm
%defattr(-,root,root)
/usr/lib/mono/gac/aqbankingNET5/
/usr/lib/mono/aqbankingNET/
%{_libdir}/*.so

%changelog
