%define name beediff
%define version 1.8
%define release %mkrel 1

Summary: Graphical file comparator
Name:    %{name}
Version: %{version}
Release: %{release}
License: GPLv2+
Group:   File tools
URL:     http://www.beesoft.org/beediff.html
Source0: %{name}_%{version}_src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Buildrequires: qt4-devel

%description
BeeDiff (beediff) is a graphical file comparator.
User have a possibilty to compare a two text files.
All differences are highlighted in colors.

%prep
%setup -q -n %{name}

%build
qmake
%make

%install
rm -rf $RPM_BUILD_ROOT

# mkdir -p %{buildroot}/%{_bindir} %{buildroot}/%{%_iconsdir}
install -D %{name} %{buildroot}/%{_bindir}/%{name}
install -D img/%{name}.png %{buildroot}/%{_iconsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc licence.txt
%{_bindir}/%{name}
%{_iconsdir}/%{name}.png


