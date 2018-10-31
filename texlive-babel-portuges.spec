# revision 30284
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-babel-portuges
Version:	1.2q
Release:	2
Summary:	TeXLive babel-portuges package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-portuges.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-portuges.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-portuges.source.tar.xz
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
%{_texmfdistdir}/tex/generic/babel-portuges/portuges.ldf
%doc %{_texmfdistdir}/doc/generic/babel-portuges/portuges.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-portuges/portuges.dtx
%doc %{_texmfdistdir}/source/generic/babel-portuges/portuges.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
