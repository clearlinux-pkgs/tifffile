#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tifffile
Version  : 2021.4.8
Release  : 10
URL      : https://files.pythonhosted.org/packages/21/b5/d78caac27c0b612dc2765341829c5e3a547bd873ccc2f5cc68d35d64ad72/tifffile-2021.4.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/21/b5/d78caac27c0b612dc2765341829c5e3a547bd873ccc2f5cc68d35d64ad72/tifffile-2021.4.8.tar.gz
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
=========================
        
        Tifffile is a Python library to
        
        (1) store numpy arrays in TIFF (Tagged Image File Format) files, and
        (2) read image and metadata from TIFF-like files used in bioimaging.
        
        Image and metadata can be read from TIFF, BigTIFF, OME-TIFF, STK, LSM, SGI,
        NIHImage, ImageJ, MicroManager, FluoView, ScanImage, SEQ, GEL, SVS, SCN, SIS,
        ZIF (Zoomable Image File Format), QPTIFF (QPI), NDPI, and GeoTIFF files.
        
        Image data can be read as numpy arrays or zarr arrays/groups from strips,
        tiles, pages (IFDs), SubIFDs, higher order series, and pyramidal levels.
        
        Numpy arrays can be written to TIFF, BigTIFF, OME-TIFF, and ImageJ hyperstack
        compatible files in multi-page, volumetric, pyramidal, memory-mappable, tiled,
        predicted, or compressed form.
        
        A subset of the TIFF specification is supported, mainly 8, 16, 32 and 64-bit
        integer, 16, 32 and 64-bit float, grayscale and multi-sample images.
        Specifically, CCITT and OJPEG compression, chroma subsampling without JPEG
        compression, color space transformations, samples with differing types, or
        IPTC and XMP metadata are not implemented.
        
        TIFF, the Tagged Image File Format, was created by the Aldus Corporation and
        Adobe Systems Incorporated. BigTIFF allows for files larger than 4 GB.
        STK, LSM, FluoView, SGI, SEQ, GEL, QPTIFF, NDPI, SCN, ZIF, and OME-TIFF,
        are custom extensions defined by Molecular Devices (Universal Imaging
        Corporation), Carl Zeiss MicroImaging, Olympus, Silicon Graphics International,
        Media Cybernetics, Molecular Dynamics, PerkinElmer, Hamamatsu, Leica,
        ObjectivePathology, and the Open Microscopy Environment consortium,
        respectively.
        
        For command line usage run ``python -m tifffile --help``

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
%setup -q -n tifffile-2021.4.8
cd %{_builddir}/tifffile-2021.4.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1618014877
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tifffile
cp %{_builddir}/tifffile-2021.4.8/LICENSE %{buildroot}/usr/share/package-licenses/tifffile/7932e1a073ab773e326ed35b6b83cc80e5f03322
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
