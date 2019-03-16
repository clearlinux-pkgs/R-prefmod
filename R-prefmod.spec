#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-prefmod
Version  : 0.8.34
Release  : 6
URL      : https://cran.r-project.org/src/contrib/prefmod_0.8-34.tar.gz
Source0  : https://cran.r-project.org/src/contrib/prefmod_0.8-34.tar.gz
Summary  : Utilities to Fit Paired Comparison Models for Preferences
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-prefmod-lib
Requires: R-colorspace
Requires: R-gnm
BuildRequires : R-colorspace
BuildRequires : R-gnm
BuildRequires : clr-R-helpers

%description
No detailed description available

%package lib
Summary: lib components for the R-prefmod package.
Group: Libraries

%description lib
lib components for the R-prefmod package.


%prep
%setup -q -c -n prefmod

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530443102

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530443102
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library prefmod
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library prefmod
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library prefmod
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library prefmod|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/prefmod/CITATION
/usr/lib64/R/library/prefmod/DESCRIPTION
/usr/lib64/R/library/prefmod/INDEX
/usr/lib64/R/library/prefmod/Meta/Rd.rds
/usr/lib64/R/library/prefmod/Meta/data.rds
/usr/lib64/R/library/prefmod/Meta/features.rds
/usr/lib64/R/library/prefmod/Meta/hsearch.rds
/usr/lib64/R/library/prefmod/Meta/links.rds
/usr/lib64/R/library/prefmod/Meta/nsInfo.rds
/usr/lib64/R/library/prefmod/Meta/package.rds
/usr/lib64/R/library/prefmod/NAMESPACE
/usr/lib64/R/library/prefmod/NEWS
/usr/lib64/R/library/prefmod/NEWS.Rd
/usr/lib64/R/library/prefmod/NEWS.pdf
/usr/lib64/R/library/prefmod/R/prefmod
/usr/lib64/R/library/prefmod/R/prefmod.rdb
/usr/lib64/R/library/prefmod/R/prefmod.rdx
/usr/lib64/R/library/prefmod/data/Rdata.rdb
/usr/lib64/R/library/prefmod/data/Rdata.rds
/usr/lib64/R/library/prefmod/data/Rdata.rdx
/usr/lib64/R/library/prefmod/help/AnIndex
/usr/lib64/R/library/prefmod/help/aliases.rds
/usr/lib64/R/library/prefmod/help/paths.rds
/usr/lib64/R/library/prefmod/help/prefmod.rdb
/usr/lib64/R/library/prefmod/help/prefmod.rdx
/usr/lib64/R/library/prefmod/html/00Index.html
/usr/lib64/R/library/prefmod/html/R.css
/usr/lib64/R/library/prefmod/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/prefmod/libs/prefmod.so
/usr/lib64/R/library/prefmod/libs/prefmod.so.avx2
/usr/lib64/R/library/prefmod/libs/prefmod.so.avx512
