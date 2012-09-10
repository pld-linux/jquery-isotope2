# TODO
# - paths and deps for demo
%define		plugin	isotope
Summary:	jQuery plugin for magical layouts: filtering, sorting, and dynamic layouts
Name:		jquery-%{plugin}
Version:	1.5.18
Release:	1
License:	Free for non-commercial use
Group:		Applications/WWW
Source0:	https://github.com/desandro/isotope/tarball/v%{version}/%{name}-%{version}.tgz
# Source0-md5:	a3aa4e827877abc47ba72b4c06146311
URL:		http://isotope.metafizzy.co/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
BuildRequires:	yuicompressor
Requires:	jquery >= 1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

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

%build
install -d build/css

# pack .css
for css in css/*.css; do
	out=build/${css#*/jquery.}
%if 0%{!?debug:1}
	yuicompressor --charset UTF-8 $css -o $out
%else
	cp -a $css $out
%endif
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p jquery.%{plugin}.min.js  $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

cp -p build/css/style.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.css
cp -p css/style.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.css
ln -s %{plugin}-%{version}.min.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}.css

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a index.html $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.mdown
%{_appdir}

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
