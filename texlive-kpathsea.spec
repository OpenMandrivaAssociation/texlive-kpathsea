Name:		texlive-kpathsea
Version:	72376
Release:	1
Summary:	Path searching library for TeX-related files
Group:		Publishing
URL:		https://tug.org/texlive
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kpathsea.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kpathsea.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea.bin
Requires(postun):texlive-kpathsea.bin
%rename kpathsea

%description
Kpathsea is a library and utility programs which provide path
searching facilities for TeX file types, including the self-
locating feature required for movable installations, layered on
top of a general search mechanism. It is not distributed
separately, but rather is released and maintained as part of
the TeX live sources.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/web2c/amiga-pl.tcx
%{_texmfdistdir}/web2c/cp1250cs.tcx
%{_texmfdistdir}/web2c/cp1250pl.tcx
%{_texmfdistdir}/web2c/cp1250t1.tcx
%{_texmfdistdir}/web2c/cp227.tcx
%{_texmfdistdir}/web2c/cp852-cs.tcx
%{_texmfdistdir}/web2c/cp852-pl.tcx
%{_texmfdistdir}/web2c/cp8bit.tcx
%{_texmfdistdir}/web2c/empty.tcx
%config(noreplace) %{_texmfdistdir}/web2c/fmtutil.cnf
%{_texmfdistdir}/web2c/il1-t1.tcx
%{_texmfdistdir}/web2c/il2-cs.tcx
%{_texmfdistdir}/web2c/il2-pl.tcx
%{_texmfdistdir}/web2c/il2-t1.tcx
%{_texmfdistdir}/web2c/kam-cs.tcx
%{_texmfdistdir}/web2c/kam-t1.tcx
%{_texmfdistdir}/web2c/macce-pl.tcx
%{_texmfdistdir}/web2c/macce-t1.tcx
%{_texmfdistdir}/web2c/maz-pl.tcx
%{_texmfdistdir}/web2c/mktex.cnf
%{_texmfdistdir}/web2c/mktex.opt
%{_texmfdistdir}/web2c/mktexdir
%{_texmfdistdir}/web2c/mktexdir.opt
%{_texmfdistdir}/web2c/mktexnam
%{_texmfdistdir}/web2c/mktexnam.opt
%{_texmfdistdir}/web2c/mktexupd
%{_texmfdistdir}/web2c/natural.tcx
%{_texmfdistdir}/web2c/tcvn-t5.tcx
%{_texmfdistdir}/web2c/texmf.cnf
%{_texmfdistdir}/web2c/viscii-t5.tcx
%doc %{_texmfdistdir}/doc/info/dir
%doc %{_infodir}/kpathsea.info*
%doc %{_infodir}/web2c.info*
%doc %{_texmfdistdir}/doc/kpathsea
%doc %{_mandir}/man1/*.1*
%doc %{_texmfdistdir}/doc/man/man1/*
%doc %{_texmfdistdir}/doc/web2c/web2c.html
%doc %{_texmfdistdir}/doc/web2c/web2c.pdf
%doc %{_texmfdistdir}/doc/web2c/NEWS

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

perl -pi -e 's%^(TEXMFMAIN\s+= ).*%$1%{_texmfdistdir}%;'			  \
	 -e 's%^(TEXMFDIST\s+= ).*%$1%{_texmfdistdir}%;'		  \
	 -e 's%^(TEXMFLOCAL\s+= ).*%$1%{_texmflocaldir}%;'		  \
	 -e 's%^(TEXMFSYSVAR\s+= ).*%$1%{_texmfvardir}%;'		  \
	 -e 's%^(TEXMFSYSCONFIG\s+= ).*%$1%{_texmfconfdir}%;'		  \
	 -e 's%^(TEXMFHOME\s+= ).*%$1\$HOME/texmf%;'			  \
	 -e 's%^(TEXMFVAR\s+= ).*%$1\$HOME/.texlive2013/texmf-var%;'	  \
	 -e 's%^(TEXMFCONFIG\s+= ).*%$1\$HOME/.texlive2013/texmf-config%;'\
	 -e 's%^(TEXMFROOT\s+= ).*%$1\%{_datadir}%;'\
	 -e 's%^(OSFONTDIR\s+= ).*%$1%{_datadir}/fonts%;'		  \
	texmf-dist/web2c/texmf.cnf

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_infodir}
mv %{buildroot}%{_texmfdistdir}/doc/info/*.info %{buildroot}%{_infodir}
