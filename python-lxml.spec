# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.23
# 
# >> macros
# << macros

Name:       python-lxml
Summary:    ElementTree-like Python bindings for libxml2 and libxslt
Version:    2.3.4
Release:    3
Group:      Development/Libraries
License:    BSD
URL:        http://lxml.de/
Source0:    http://pypi.python.org/packages/source/l/lxml/lxml-%{version}.tar.gz
Source100:  python-lxml.yaml
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  python-devel
BuildRequires:  python-setuptools-devel


%description
lxml provides a Python binding to the libxslt and libxml2 libraries.
It follows the ElementTree API as much as possible in order to provide
a more Pythonic interface to libxml2 and libxslt than the default
bindings.  In particular, lxml deals with Python Unicode strings
rather than encoded UTF-8 and handles memory management automatically,
unlike the default bindings.




%prep
%setup -q -n lxml-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
CFLAGS="%{optflags}" %{__python} -c 'import setuptools; execfile("setup.py")' build

# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre

# >> install post
%{__python} -c 'import setuptools; execfile("setup.py")' install --skip-build --root %{buildroot}

#Note that the test script only tests the in-place build (i.e., not install_post)
%if ! 0%{?qemu_user_space_build}
make test
%endif

# << install post






%files
%defattr(-,root,root,-)
# >> files
%doc README.rst LICENSES.txt PKG-INFO CREDITS.txt CHANGES.txt doc/
%{python_sitearch}/*
# << files


