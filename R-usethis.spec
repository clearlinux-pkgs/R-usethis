#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-usethis
Version  : 2.0.1
Release  : 27
URL      : https://cran.r-project.org/src/contrib/usethis_2.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/usethis_2.0.1.tar.gz
Summary  : Automate Package and Project Setup
Group    : Development/Tools
License  : AGPL-3.0 Apache-2.0 CC-BY-4.0 CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0 MIT
Requires: R-cli
Requires: R-clipr
Requires: R-crayon
Requires: R-curl
Requires: R-desc
Requires: R-fs
Requires: R-gert
Requires: R-gh
Requires: R-glue
Requires: R-jsonlite
Requires: R-lifecycle
Requires: R-purrr
Requires: R-rappdirs
Requires: R-rlang
Requires: R-rprojroot
Requires: R-rstudioapi
Requires: R-whisker
Requires: R-withr
Requires: R-yaml
BuildRequires : R-cli
BuildRequires : R-clipr
BuildRequires : R-crayon
BuildRequires : R-curl
BuildRequires : R-desc
BuildRequires : R-fs
BuildRequires : R-gert
BuildRequires : R-gh
BuildRequires : R-glue
BuildRequires : R-jsonlite
BuildRequires : R-lifecycle
BuildRequires : R-purrr
BuildRequires : R-rappdirs
BuildRequires : R-rlang
BuildRequires : R-rprojroot
BuildRequires : R-rstudioapi
BuildRequires : R-whisker
BuildRequires : R-withr
BuildRequires : R-yaml
BuildRequires : buildreq-R

%description
otherwise performed manually. This includes setting up unit testing,
    test coverage, continuous integration, Git, 'GitHub', licenses,
    'Rcpp', 'RStudio' projects, and more.

%prep
%setup -q -c -n usethis
cd %{_builddir}/usethis

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1612974715

%install
export SOURCE_DATE_EPOCH=1612974715
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc usethis || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/usethis/DESCRIPTION
/usr/lib64/R/library/usethis/INDEX
/usr/lib64/R/library/usethis/LICENSE
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
/usr/lib64/R/library/usethis/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/usethis/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/usethis/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/usethis/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/usethis/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/usethis/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/usethis/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/usethis/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/usethis/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/usethis/help/figures/logo.png
/usr/lib64/R/library/usethis/help/paths.rds
/usr/lib64/R/library/usethis/help/usethis.rdb
/usr/lib64/R/library/usethis/help/usethis.rdx
/usr/lib64/R/library/usethis/html/00Index.html
/usr/lib64/R/library/usethis/html/R.css
/usr/lib64/R/library/usethis/templates/CODE_OF_CONDUCT.md
/usr/lib64/R/library/usethis/templates/Jenkinsfile
/usr/lib64/R/library/usethis/templates/Makefile
/usr/lib64/R/library/usethis/templates/NEWS.md
/usr/lib64/R/library/usethis/templates/addins.dcf
/usr/lib64/R/library/usethis/templates/appveyor.yml
/usr/lib64/R/library/usethis/templates/article.Rmd
/usr/lib64/R/library/usethis/templates/circleci-config.yml
/usr/lib64/R/library/usethis/templates/citation-template.R
/usr/lib64/R/library/usethis/templates/code-cpp11.cpp
/usr/lib64/R/library/usethis/templates/code.c
/usr/lib64/R/library/usethis/templates/code.cpp
/usr/lib64/R/library/usethis/templates/codecov.yml
/usr/lib64/R/library/usethis/templates/cran-comments.md
/usr/lib64/R/library/usethis/templates/data-table.R
/usr/lib64/R/library/usethis/templates/gitlab-ci.yml
/usr/lib64/R/library/usethis/templates/junit-testthat.R
/usr/lib64/R/library/usethis/templates/license-AGPL-3.md
/usr/lib64/R/library/usethis/templates/license-GPL-2.md
/usr/lib64/R/library/usethis/templates/license-GPL-3.md
/usr/lib64/R/library/usethis/templates/license-LGPL-2.1.md
/usr/lib64/R/library/usethis/templates/license-LGPL-3.md
/usr/lib64/R/library/usethis/templates/license-apache-2.md
/usr/lib64/R/library/usethis/templates/license-cc0.md
/usr/lib64/R/library/usethis/templates/license-ccby-4.md
/usr/lib64/R/library/usethis/templates/license-mit.md
/usr/lib64/R/library/usethis/templates/license-proprietary.txt
/usr/lib64/R/library/usethis/templates/lifecycle-archived.svg
/usr/lib64/R/library/usethis/templates/lifecycle-defunct.svg
/usr/lib64/R/library/usethis/templates/lifecycle-deprecated.svg
/usr/lib64/R/library/usethis/templates/lifecycle-experimental.svg
/usr/lib64/R/library/usethis/templates/lifecycle-maturing.svg
/usr/lib64/R/library/usethis/templates/lifecycle-questioning.svg
/usr/lib64/R/library/usethis/templates/lifecycle-stable.svg
/usr/lib64/R/library/usethis/templates/lifecycle-superseded.svg
/usr/lib64/R/library/usethis/templates/package-README
/usr/lib64/R/library/usethis/templates/packagename-data-prep.R
/usr/lib64/R/library/usethis/templates/packagename-package.R
/usr/lib64/R/library/usethis/templates/pipe.R
/usr/lib64/R/library/usethis/templates/project-README
/usr/lib64/R/library/usethis/templates/readme-rmd-pre-commit.sh
/usr/lib64/R/library/usethis/templates/revdep-email.yml
/usr/lib64/R/library/usethis/templates/rmarkdown-template.Rmd
/usr/lib64/R/library/usethis/templates/rmarkdown-template.yml
/usr/lib64/R/library/usethis/templates/template.Rproj
/usr/lib64/R/library/usethis/templates/test-example-2.1.R
/usr/lib64/R/library/usethis/templates/testthat.R
/usr/lib64/R/library/usethis/templates/tidy-contributing.md
/usr/lib64/R/library/usethis/templates/tidy-eval.R
/usr/lib64/R/library/usethis/templates/tidy-issue.md
/usr/lib64/R/library/usethis/templates/tidy-support.md
/usr/lib64/R/library/usethis/templates/tidy-travis.yml
/usr/lib64/R/library/usethis/templates/travis.yml
/usr/lib64/R/library/usethis/templates/tutorial-template.Rmd
/usr/lib64/R/library/usethis/templates/vignette.Rmd
/usr/lib64/R/library/usethis/templates/year-copyright.txt
/usr/lib64/R/library/usethis/tests/spelling.R
/usr/lib64/R/library/usethis/tests/testthat.R
/usr/lib64/R/library/usethis/tests/testthat/_snaps/badge.md
/usr/lib64/R/library/usethis/tests/testthat/_snaps/course.md
/usr/lib64/R/library/usethis/tests/testthat/_snaps/pipe.md
/usr/lib64/R/library/usethis/tests/testthat/_snaps/release.md
/usr/lib64/R/library/usethis/tests/testthat/_snaps/tibble.md
/usr/lib64/R/library/usethis/tests/testthat/_snaps/ui.md
/usr/lib64/R/library/usethis/tests/testthat/_snaps/vignette.md
/usr/lib64/R/library/usethis/tests/testthat/helper.R
/usr/lib64/R/library/usethis/tests/testthat/ref/README.Rmd
/usr/lib64/R/library/usethis/tests/testthat/ref/README.md
/usr/lib64/R/library/usethis/tests/testthat/ref/foo-loose-dropbox.zip
/usr/lib64/R/library/usethis/tests/testthat/ref/foo-loose-regular.zip
/usr/lib64/R/library/usethis/tests/testthat/ref/foo-not-loose.zip
/usr/lib64/R/library/usethis/tests/testthat/ref/foo/file.txt
/usr/lib64/R/library/usethis/tests/testthat/ref/yo-loose-dropbox.zip
/usr/lib64/R/library/usethis/tests/testthat/ref/yo-loose-regular.zip
/usr/lib64/R/library/usethis/tests/testthat/ref/yo-not-loose.zip
/usr/lib64/R/library/usethis/tests/testthat/ref/yo/subdir1/file1.txt
/usr/lib64/R/library/usethis/tests/testthat/ref/yo/subdir2/file2.txt
/usr/lib64/R/library/usethis/tests/testthat/setup.R
/usr/lib64/R/library/usethis/tests/testthat/teardown.R
/usr/lib64/R/library/usethis/tests/testthat/test-addin.R
/usr/lib64/R/library/usethis/tests/testthat/test-badge.R
/usr/lib64/R/library/usethis/tests/testthat/test-browse.R
/usr/lib64/R/library/usethis/tests/testthat/test-ci.R
/usr/lib64/R/library/usethis/tests/testthat/test-code-of-conduct.R
/usr/lib64/R/library/usethis/tests/testthat/test-course.R
/usr/lib64/R/library/usethis/tests/testthat/test-cpp11.R
/usr/lib64/R/library/usethis/tests/testthat/test-cran.R
/usr/lib64/R/library/usethis/tests/testthat/test-create.R
/usr/lib64/R/library/usethis/tests/testthat/test-data-table.R
/usr/lib64/R/library/usethis/tests/testthat/test-data.R
/usr/lib64/R/library/usethis/tests/testthat/test-description.R
/usr/lib64/R/library/usethis/tests/testthat/test-directory.R
/usr/lib64/R/library/usethis/tests/testthat/test-documentation.R
/usr/lib64/R/library/usethis/tests/testthat/test-edit.R
/usr/lib64/R/library/usethis/tests/testthat/test-git.R
/usr/lib64/R/library/usethis/tests/testthat/test-github-actions.R
/usr/lib64/R/library/usethis/tests/testthat/test-github_token.R
/usr/lib64/R/library/usethis/tests/testthat/test-helpers.R
/usr/lib64/R/library/usethis/tests/testthat/test-ignore.R
/usr/lib64/R/library/usethis/tests/testthat/test-jenkins.R
/usr/lib64/R/library/usethis/tests/testthat/test-latest-dependencies.R
/usr/lib64/R/library/usethis/tests/testthat/test-license.R
/usr/lib64/R/library/usethis/tests/testthat/test-lifecycle.R
/usr/lib64/R/library/usethis/tests/testthat/test-line-ending.R
/usr/lib64/R/library/usethis/tests/testthat/test-logo.R
/usr/lib64/R/library/usethis/tests/testthat/test-make.R
/usr/lib64/R/library/usethis/tests/testthat/test-package.R
/usr/lib64/R/library/usethis/tests/testthat/test-pipe.R
/usr/lib64/R/library/usethis/tests/testthat/test-pkgdown.R
/usr/lib64/R/library/usethis/tests/testthat/test-proj.R
/usr/lib64/R/library/usethis/tests/testthat/test-r.R
/usr/lib64/R/library/usethis/tests/testthat/test-rcpp.R
/usr/lib64/R/library/usethis/tests/testthat/test-readme.R
/usr/lib64/R/library/usethis/tests/testthat/test-release.R
/usr/lib64/R/library/usethis/tests/testthat/test-revdep.R
/usr/lib64/R/library/usethis/tests/testthat/test-rmarkdown.R
/usr/lib64/R/library/usethis/tests/testthat/test-roxygen.R
/usr/lib64/R/library/usethis/tests/testthat/test-rstudio.R
/usr/lib64/R/library/usethis/tests/testthat/test-template.R
/usr/lib64/R/library/usethis/tests/testthat/test-test.R
/usr/lib64/R/library/usethis/tests/testthat/test-testthat.R
/usr/lib64/R/library/usethis/tests/testthat/test-tibble.R
/usr/lib64/R/library/usethis/tests/testthat/test-tidyverse.R
/usr/lib64/R/library/usethis/tests/testthat/test-tutorial.R
/usr/lib64/R/library/usethis/tests/testthat/test-ui.R
/usr/lib64/R/library/usethis/tests/testthat/test-utils-git.R
/usr/lib64/R/library/usethis/tests/testthat/test-utils-github.R
/usr/lib64/R/library/usethis/tests/testthat/test-utils-glue.R
/usr/lib64/R/library/usethis/tests/testthat/test-utils.R
/usr/lib64/R/library/usethis/tests/testthat/test-version.R
/usr/lib64/R/library/usethis/tests/testthat/test-vignette.R
/usr/lib64/R/library/usethis/tests/testthat/test-write.R
