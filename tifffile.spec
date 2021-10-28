#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tifffile
Version  : 2021.8.30
Release  : 15
URL      : https://files.pythonhosted.org/packages/4a/85/9db55907e0dcbcb72c24c78e38bbb39fb29196f691898bf71d02b027b832/tifffile-2021.8.30.tar.gz
Source0  : https://files.pythonhosted.org/packages/4a/85/9db55907e0dcbcb72c24c78e38bbb39fb29196f691898bf71d02b027b832/tifffile-2021.8.30.tar.gz
Summary  : Read and write TIFF files
Group    : Development/Tools
License  : BSD-3-Clause
Requires: tifffile-bin = %{version}-%{release}
Requires: tifffile-license = %{version}-%{release}
Requires: tifffile-python = %{version}-%{release}
Requires: tifffile-python3 = %{version}-%{release}
Requires: lxml
Requires: matplotlib
Requires: numpy
BuildRequires : buildreq-distutils3
BuildRequires : lxml
BuildRequires : matplotlib
BuildRequires : numpy

%description
Read and write TIFF files
=========================
Tifffile is a Python library to

%package bin
Summary: bin components for the tifffile package.
Group: Binaries
Requires: tifffile-license = %{version}-%{release}

%description bin
bin components for the tifffile package.


%package license
Summary: license components for the tifffile package.
Group: Default

%description license
license components for the tifffile package.


%package python
Summary: python components for the tifffile package.
Group: Default
Requires: tifffile-python3 = %{version}-%{release}

%description python
python components for the tifffile package.


%package python3
Summary: python3 components for the tifffile package.
Group: Default
Requires: python3-core
Provides: pypi(tifffile)
Requires: pypi(numpy)

%description python3
python3 components for the tifffile package.


%prep
%setup -q -n tifffile-2021.8.30
cd %{_builddir}/tifffile-2021.8.30

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1631570677
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tifffile
cp %{_builddir}/tifffile-2021.8.30/LICENSE %{buildroot}/usr/share/package-licenses/tifffile/7932e1a073ab773e326ed35b6b83cc80e5f03322
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lsm2bin
/usr/bin/tiff2fsspec
/usr/bin/tiffcomment
/usr/bin/tifffile

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tifffile/7932e1a073ab773e326ed35b6b83cc80e5f03322

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
