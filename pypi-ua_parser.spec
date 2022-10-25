#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ua_parser
Version  : 0.16.1
Release  : 41
URL      : https://files.pythonhosted.org/packages/ab/e0/6be7ec0f1d3a485126fcce33c34ff8c41745e5b5ad43e500037f30e40064/ua-parser-0.16.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/ab/e0/6be7ec0f1d3a485126fcce33c34ff8c41745e5b5ad43e500037f30e40064/ua-parser-0.16.1.tar.gz
Summary  : Python port of Browserscope's user agent parser
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-ua_parser-license = %{version}-%{release}
Requires: pypi-ua_parser-python = %{version}-%{release}
Requires: pypi-ua_parser-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pyyaml)

%description
uap-python
==========
A python implementation of the UA Parser (https://github.com/ua-parser,
formerly https://github.com/tobie/ua-parser)

%package license
Summary: license components for the pypi-ua_parser package.
Group: Default

%description license
license components for the pypi-ua_parser package.


%package python
Summary: python components for the pypi-ua_parser package.
Group: Default
Requires: pypi-ua_parser-python3 = %{version}-%{release}

%description python
python components for the pypi-ua_parser package.


%package python3
Summary: python3 components for the pypi-ua_parser package.
Group: Default
Requires: python3-core
Provides: pypi(ua_parser)

%description python3
python3 components for the pypi-ua_parser package.


%prep
%setup -q -n ua-parser-0.16.1
cd %{_builddir}/ua-parser-0.16.1
pushd ..
cp -a ua-parser-0.16.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666724600
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ua_parser
cp %{_builddir}/ua-parser-%{version}/ua_parser/LICENSE %{buildroot}/usr/share/package-licenses/pypi-ua_parser/c0204dc0e6cdf836b06fd8a9c55fd9ff5ca60245 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ua_parser/c0204dc0e6cdf836b06fd8a9c55fd9ff5ca60245

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
