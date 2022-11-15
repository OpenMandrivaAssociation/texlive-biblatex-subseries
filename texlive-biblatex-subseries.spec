Name:		texlive-biblatex-subseries
Version:	43330
Release:	1
Summary:	Manages subseries with BibLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-subseries
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-subseries.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-subseries.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Some publishers organize book series with subseries. In this
case, two numbers are associated with one volume: the number
inside the series and the number inside the subseries. That is
the case of the series Corpus Scriptorium Christianorum
Orientalium published by Peeters. This package provides new
fields to manage such system.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/biblatex-subseries
%doc %{_texmfdistdir}/doc/latex/biblatex-subseries

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
