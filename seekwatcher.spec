Summary: Utility for visualizing block layer IO patterns and performance
Name: seekwatcher
Version: 0.12
Release: 4.1%{?dist}
License: GPLv2
BuildArch: noarch
Group: Development/System
Source: http://oss.oracle.com/~mason/seekwatcher/seekwatcher-%{version}.tar.bz2
Url: http://oss.oracle.com/~mason/seekwatcher/
Requires: blktrace, python, python-matplotlib, theora-tools
BuildRequires: python

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Patch0: seekwatcher-0.12-new-matplotlib.patch

%description
Seekwatcher generates graphs from blktrace runs to help visualize IO patterns
and performance. It can plot multiple blktrace runs together, making it easy
to compare the differences between different benchmark runs.

You should install the seekwatcher package if you need to visualize detailed
information about IO patterns.

%prep
%setup -q
%patch0 -p1

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp -p seekwatcher %{buildroot}/usr/bin
chmod +x %{buildroot}/usr/bin/seekwatcher

%clean
rm -rf %{buildroot}

%build

%files
%defattr(-,root,root,-)
%doc README.html COPYING
/usr/bin/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.12-4.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 30 2009 Eric Sandeen <sandeen@redhat.com> - 0.12-3
- Updates for new matplotlib

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jun 04 2008 Eric Sandeen <sandeen@redhat.com> - 0.12-1
- New upstream version, fixes IO plots for high block ranges.

* Mon Mar 14 2008 Eric Sandeen <sandeen@redhat.com> - 0.11-1
- New upstream version, includes support for multiple devices.

* Fri Mar 07 2008 Eric Sandeen <sandeen@redhat.com> - 0.10-1
- New upstream version, includes filtering for fewer dropped events.

* Fri Nov 30 2007 Eric Sandeen <sandeen@redhat.com> - 0.9-2
- More specfile fiddling

* Thu Nov 29 2007 Eric Sandeen <sandeen@redhat.com> - 0.8-2
- Add python to reqs/buildreqs

* Thu Nov 29 2007 Eric Sandeen <sandeen@redhat.com> - 0.8-1
- Update to 0.8, includes support for theora movies

* Mon Sep 10 2007 Eric Sandeen <sandeen@redhat.com> - 0.7-1
- New package, initial build.
