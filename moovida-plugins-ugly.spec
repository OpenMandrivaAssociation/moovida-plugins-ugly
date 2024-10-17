%define debug_package	%{nil}

%define oname	elisa-plugins-ugly

Summary:	'Ugly' plugins for the Moovida media center
Name:		moovida-plugins-ugly
Version:	1.0.9
Release:	3
Source0:	http://www.moovida.com/media/public/%{name}-%{version}.tar.gz
License:	GPLv3 and MIT
Group:		Development/Python
URL:		https://www.moovida.com
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python-setuptools
BuildRequires:	python-devel
BuildRequires:	python-twisted
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils
BuildRequires:	gstreamer0.10-python
BuildRequires:	moovida-core >= %{version}
Requires:	moovida-plugins-good >= %{version}
Suggests:	twill
# For LIRC input support
Suggests:	python-lirc
%rename elisa-plugins-ugly

%description
Moovida is a project to create an open source cross platform media center 
solution. This package contains 'ugly' plugins for Moovida.

%prep
%setup -q -n %{oname}-%{version}

%build

%install
python setup.py install --root=%{buildroot} --single-version-externally-managed --compile --optimize=2
# already in -good
rm -f %{buildroot}%{py_puresitedir}/elisa/plugins/__init__*

%files
%{py_puresitedir}/elisa/plugins/*
%{py_puresitedir}/elisa_plugin_*-py%{py_ver}.egg-info
%{py_puresitedir}/elisa_plugin_*-py%{py_ver}-nspkg.pth

