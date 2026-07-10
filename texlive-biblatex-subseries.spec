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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Some publishers organize book series with subseries. In this case, two
numbers are associated with one volume: the number inside the series and
the number inside the subseries. That is the case of the series Corpus
Scriptorium Christianorum Orientalium published by Peeters. This package
provides new fields to manage such system.

