%define name beediff
%define version 1.9
%define release %mkrel 5

Summary: Graphical file comparator
Name:    %{name}
Version: %{version}
Release: %{release}
License: GPLv2+
Group:   File tools
URL:     http://www.beesoft.org/index.php?id=beediff
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
