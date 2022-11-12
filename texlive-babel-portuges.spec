Name:		texlive-babel-portuges
Version:	59883
Release:	1
Summary:	TeXLive babel-portuges package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-portuges.r59883.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-portuges.doc.r59883.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-portuges.source.r59883.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive babel-portuges package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-portuges
%doc %{_texmfdistdir}/doc/generic/babel-portuges
#- source
%doc %{_texmfdistdir}/source/generic/babel-portuges

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
