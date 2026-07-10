%global tl_name biblatex-subseries
%global tl_revision 76790

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2.0
Release:	%{tl_revision}.1
Summary:	Manages subseries with BibLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-subseries
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-subseries.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-subseries.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Some publishers organize book series with subseries. In this case, two
numbers are associated with one volume: the number inside the series and
the number inside the subseries. That is the case of the series Corpus
Scriptorium Christianorum Orientalium published by Peeters. This package
provides new fields to manage such system.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-subseries
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-subseries
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-subseries/documentation
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-subseries/README
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-subseries/documentation/biblatex-subseries-example.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-subseries/documentation/biblatex-subseries-example.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-subseries/documentation/biblatex-subseries-example.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-subseries/documentation/biblatex-subseries.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-subseries/documentation/biblatex-subseries.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-subseries/documentation/makefile
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-subseries/makefile
%{_datadir}/texmf-dist/tex/latex/biblatex-subseries/subseries.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-subseries/subseries.dbx
