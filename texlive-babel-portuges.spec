%global tl_name babel-portuges
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2u
Release:	%{tl_revision}.1
Summary:	Babel support for Portuges
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/portuges
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-portuges.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-portuges.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-portuges.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the language definition file for support of
Portuguese and Brazilian Portuguese in babel. Some shortcuts are
defined, as well as translations to Portuguese of standard "LaTeX
names".

