# TODO
# - paths and deps for demo
%define		plugin	isotope
Summary:	jQuery plugin for magical layouts: filtering, sorting, and dynamic layouts
Name:		jquery-%{plugin}2
Version:	2.0.0
Release:	1
License:	MIT, Free for non-commercial use
Group:		Applications/WWW
Source0:	https://github.com/desandro/isotope/tarball/v%{version}/%{name}-%{version}.tgz
# Source0-md5:	6f791b4b421c825a0ea85b1bd8df8d5a
URL:		http://isotope.metafizzy.co/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	jquery >= 1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}2

%description
An exquisite jQuery plugin for magical layouts. Enables filtering,
sorting, and dynamic layouts.

%package demo
Summary:	Demo for jQuery.%{plugin}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu jQuery.%{plugin}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for jQuery.%{plugin}.

%prep
%setup -qc
mv *-%{plugin}-*/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p dist/%{plugin}.pkgd.min.js  $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p dist/%{plugin}.pkgd.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.mdown
%{_appdir}

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
