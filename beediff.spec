%define name beediff
%define version 1.9
%define release 6

Summary: Graphical file comparator
Name:    %{name}
Version: %{version}
Release: %{release}
License: GPLv2+
Group:   File tools
URL:     https://www.beesoft.org/index.php?id=beediff
Source0: http://www.beesoft.org/download/%{name}_%{version}_src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: qt4-devel

%description
BeeDiff (beediff) is a graphical file comparator.
User have a possibilty to compare a two text files.
All differences are highlighted in colors.

%prep
%setup -q -n %{name}

%build
%qmake_qt4
%make

%install
rm -rf $RPM_BUILD_ROOT

install -D %{name} %{buildroot}/%{_bindir}/%{name}
install -D img/%{name}.png %{buildroot}/%{_iconsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc licence.txt
%{_bindir}/%{name}
%{_iconsdir}/%{name}.png


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9-5mdv2011.0
+ Revision: 610064
- rebuild

* Tue Jun 22 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.9-4mdv2010.1
+ Revision: 548543
- change url and source to the new location, (mdv #59882)

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 1.9-3mdv2010.0
+ Revision: 424030
- rebuild

* Sun Sep 14 2008 Funda Wang <fwang@mandriva.org> 1.9-2mdv2009.0
+ Revision: 284696
- rebuild with correct flags
- spec cleanup

* Sun Sep 14 2008 trem <trem@mandriva.org> 1.9-1mdv2009.0
+ Revision: 284666
- update to 1.9

* Tue Sep 02 2008 trem <trem@mandriva.org> 1.8-1mdv2009.0
+ Revision: 279339
- add description
- import beediff


* Sun Aug 31 2008 trem <trem@mandriva.org> 
- Initial build.
