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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the language definition file for support of
Portuguese and Brazilian Portuguese in babel. Some shortcuts are
defined, as well as translations to Portuguese of standard "LaTeX
names".

%prep
%setup -q -c -a1 -a2
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
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/source/generic
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/doc/generic/babel-portuges
%dir %{_datadir}/texmf-dist/source/generic/babel-portuges
%dir %{_datadir}/texmf-dist/tex/generic/babel-portuges
%doc %{_datadir}/texmf-dist/doc/generic/babel-portuges/README.md
%doc %{_datadir}/texmf-dist/doc/generic/babel-portuges/portuges.pdf
%doc %{_datadir}/texmf-dist/source/generic/babel-portuges/portuges.dtx
%doc %{_datadir}/texmf-dist/source/generic/babel-portuges/portuges.ins
%{_datadir}/texmf-dist/tex/generic/babel-portuges/brazil.ldf
%{_datadir}/texmf-dist/tex/generic/babel-portuges/brazilian.ldf
%{_datadir}/texmf-dist/tex/generic/babel-portuges/portuges.ldf
%{_datadir}/texmf-dist/tex/generic/babel-portuges/portuguese.ldf
