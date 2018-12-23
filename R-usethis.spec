#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-usethis
Version  : 1.4.0
Release  : 2
URL      : https://cran.r-project.org/src/contrib/usethis_1.4.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/usethis_1.4.0.tar.gz
Summary  : Automate Package and Project Setup
Group    : Development/Tools
License  : Apache-2.0 CC0-1.0 GPL-3.0 MIT
Requires: R-clipr
Requires: R-clisymbols
Requires: R-curl
Requires: R-desc
Requires: R-fs
Requires: R-gh
Requires: R-git2r
Requires: R-magick
Requires: R-rlang
Requires: R-rprojroot
Requires: R-rstudioapi
Requires: R-styler
Requires: R-whisker
BuildRequires : R-clipr
BuildRequires : R-clisymbols
BuildRequires : R-curl
BuildRequires : R-desc
BuildRequires : R-fs
BuildRequires : R-gh
BuildRequires : R-git2r
BuildRequires : R-magick
BuildRequires : R-rlang
BuildRequires : R-rprojroot
BuildRequires : R-rstudioapi
BuildRequires : R-styler
BuildRequires : R-whisker
BuildRequires : buildreq-R

%description
performed manually. This includes setting up unit testing, test 
    coverage, continuous integration, Git, 'GitHub', licenses, 'Rcpp', 'RStudio' 
    projects, and more.

%prep
%setup -q -c -n usethis

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540749133

%install
export SOURCE_DATE_EPOCH=1540749133
rm -rf %{buildroot}
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library usethis
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library usethis
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library usethis
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library usethis|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/usethis/DESCRIPTION
/usr/lib64/R/library/usethis/INDEX
/usr/lib64/R/library/usethis/Meta/Rd.rds
/usr/lib64/R/library/usethis/Meta/features.rds
/usr/lib64/R/library/usethis/Meta/hsearch.rds
/usr/lib64/R/library/usethis/Meta/links.rds
/usr/lib64/R/library/usethis/Meta/nsInfo.rds
/usr/lib64/R/library/usethis/Meta/package.rds
/usr/lib64/R/library/usethis/NAMESPACE
/usr/lib64/R/library/usethis/NEWS.md
/usr/lib64/R/library/usethis/R/usethis
/usr/lib64/R/library/usethis/R/usethis.rdb
/usr/lib64/R/library/usethis/R/usethis.rdx
/usr/lib64/R/library/usethis/WORDLIST
/usr/lib64/R/library/usethis/help/AnIndex
/usr/lib64/R/library/usethis/help/aliases.rds
/usr/lib64/R/library/usethis/help/figures/logo.png
/usr/lib64/R/library/usethis/help/figures/usethis-full-logo.png
/usr/lib64/R/library/usethis/help/paths.rds
/usr/lib64/R/library/usethis/help/usethis.rdb
/usr/lib64/R/library/usethis/help/usethis.rdx
/usr/lib64/R/library/usethis/html/00Index.html
/usr/lib64/R/library/usethis/html/R.css
/usr/lib64/R/library/usethis/templates/CODE_OF_CONDUCT.md
/usr/lib64/R/library/usethis/templates/NAMESPACE
/usr/lib64/R/library/usethis/templates/NEWS.md
/usr/lib64/R/library/usethis/templates/appveyor.yml
/usr/lib64/R/library/usethis/templates/codecov.yml
/usr/lib64/R/library/usethis/templates/cran-comments.md
/usr/lib64/R/library/usethis/templates/license-GPL-3.md
/usr/lib64/R/library/usethis/templates/license-apache-2.0.md
/usr/lib64/R/library/usethis/templates/license-cc0.md
/usr/lib64/R/library/usethis/templates/license-mit.md
/usr/lib64/R/library/usethis/templates/license-mit.txt
/usr/lib64/R/library/usethis/templates/package-README
/usr/lib64/R/library/usethis/templates/packagename-package.R
/usr/lib64/R/library/usethis/templates/pipe.R
/usr/lib64/R/library/usethis/templates/project-README
/usr/lib64/R/library/usethis/templates/readme-rmd-pre-commit.sh
/usr/lib64/R/library/usethis/templates/revdep-email.yml
/usr/lib64/R/library/usethis/templates/rmarkdown-template.Rmd
/usr/lib64/R/library/usethis/templates/rmarkdown-template.yml
/usr/lib64/R/library/usethis/templates/template.Rproj
/usr/lib64/R/library/usethis/templates/test-example.R
/usr/lib64/R/library/usethis/templates/testthat.R
/usr/lib64/R/library/usethis/templates/tidy-contributing.md
/usr/lib64/R/library/usethis/templates/tidy-eval.R
/usr/lib64/R/library/usethis/templates/tidy-issue.md
/usr/lib64/R/library/usethis/templates/tidy-support.md
/usr/lib64/R/library/usethis/templates/tidy-travis.yml
/usr/lib64/R/library/usethis/templates/travis.yml
