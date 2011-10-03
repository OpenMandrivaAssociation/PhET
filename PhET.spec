%define		filename	PhET-Installer_linux.bin
%define		dirphet		/opt/PhET

Name:		PhET
Version:	0.9.4
Release:	%mkrel 1
Summary:	PhET: Free online physics, chemistry, biology, earth science and math simulations
License:	CC, GPL
Group:		Education
URL:		http://phet.colorado.edu
Source:		%filename
Patch:		PhET_Simulations.desktop-ru.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%description
Free educational simulations covering a diverse topics designed by the University
of Colorado available in various languages.

%prep
$RPM_SOURCE_DIR/%{filename} --prefix $RPM_BUILD_DIR --mode unattended
%patch -p0

%install
rm -rf %{buildroot}

%clean
rm -rf %{buildroot}
