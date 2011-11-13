# revision 24417
# category TLCore
# catalog-ctan undef
# catalog-date 2010-05-03 20:19:11 +0200
# catalog-license lgpl
# catalog-version undef
Name:		texlive-kpathsea
Version:	20100503
Release:	2
Summary:	Path searching library for TeX-related files
Group:		Publishing
URL:		http://tug.org/texlive
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kpathsea.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kpathsea.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea.bin
%rename kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Kpathsea is a library and utility programs which provide path
searching facilities for TeX file types, including the self-
locating feature required for movable installations, layered on
top of a general search mechanism. It is not distributed
separately, but rather is released and maintained as part of
the TeX-live sources.

%pre
    %_texmf_updmap_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post
    %_texmf_updmap_pre

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdir}/web2c/amiga-pl.tcx
%{_texmfdir}/web2c/cp1250cs.tcx
%{_texmfdir}/web2c/cp1250pl.tcx
%{_texmfdir}/web2c/cp1250t1.tcx
%{_texmfdir}/web2c/cp227.tcx
%{_texmfdir}/web2c/cp852-cs.tcx
%{_texmfdir}/web2c/cp852-pl.tcx
%{_texmfdir}/web2c/cp8bit.tcx
%{_texmfdir}/web2c/empty.tcx
%config(noreplace) %{_texmfdir}/web2c/fmtutil.cnf
%{_texmfdir}/web2c/il1-t1.tcx
%{_texmfdir}/web2c/il2-cs.tcx
%{_texmfdir}/web2c/il2-pl.tcx
%{_texmfdir}/web2c/il2-t1.tcx
%{_texmfdir}/web2c/kam-cs.tcx
%{_texmfdir}/web2c/kam-t1.tcx
%{_texmfdir}/web2c/macce-pl.tcx
%{_texmfdir}/web2c/macce-t1.tcx
%{_texmfdir}/web2c/maz-pl.tcx
%{_texmfdir}/web2c/mktex.cnf
%{_texmfdir}/web2c/mktex.opt
%{_texmfdir}/web2c/mktexdir
%{_texmfdir}/web2c/mktexdir.opt
%{_texmfdir}/web2c/mktexnam
%{_texmfdir}/web2c/mktexnam.opt
%{_texmfdir}/web2c/mktexupd
%{_texmfdir}/web2c/natural.tcx
%{_texmfdir}/web2c/tcvn-t5.tcx
%{_texmfdir}/web2c/texmf.cnf
%{_texmfdir}/web2c/viscii-t5.tcx
%doc %{_texmfdir}/doc/info/dir
%doc %{_infodir}/kpathsea.info*
%doc %{_infodir}/tds.info*
%doc %{_infodir}/web2c.info*
%doc %{_texmfdir}/doc/kpathsea/kpathsea.html
%doc %{_texmfdir}/doc/kpathsea/kpathsea.pdf
%doc %{_mandir}/man1/kpseaccess.1*
%doc %{_texmfdir}/doc/man/man1/kpseaccess.man1.pdf
%doc %{_mandir}/man1/kpsepath.1*
%doc %{_texmfdir}/doc/man/man1/kpsepath.man1.pdf
%doc %{_mandir}/man1/kpsereadlink.1*
%doc %{_texmfdir}/doc/man/man1/kpsereadlink.man1.pdf
%doc %{_mandir}/man1/kpsestat.1*
%doc %{_texmfdir}/doc/man/man1/kpsestat.man1.pdf
%doc %{_mandir}/man1/kpsetool.1*
%doc %{_texmfdir}/doc/man/man1/kpsetool.man1.pdf
%doc %{_mandir}/man1/kpsewhere.1*
%doc %{_texmfdir}/doc/man/man1/kpsewhere.man1.pdf
%doc %{_mandir}/man1/kpsewhich.1*
%doc %{_texmfdir}/doc/man/man1/kpsewhich.man1.pdf
%doc %{_mandir}/man1/kpsexpand.1*
%doc %{_texmfdir}/doc/man/man1/kpsexpand.man1.pdf
%doc %{_mandir}/man1/mkocp.1*
%doc %{_texmfdir}/doc/man/man1/mkocp.man1.pdf
%doc %{_mandir}/man1/mkofm.1*
%doc %{_texmfdir}/doc/man/man1/mkofm.man1.pdf
%doc %{_mandir}/man1/mktexfmt.1*
%doc %{_texmfdir}/doc/man/man1/mktexfmt.man1.pdf
%doc %{_mandir}/man1/mktexlsr.1*
%doc %{_texmfdir}/doc/man/man1/mktexlsr.man1.pdf
%doc %{_mandir}/man1/mktexmf.1*
%doc %{_texmfdir}/doc/man/man1/mktexmf.man1.pdf
%doc %{_mandir}/man1/mktexpk.1*
%doc %{_texmfdir}/doc/man/man1/mktexpk.man1.pdf
%doc %{_mandir}/man1/mktextfm.1*
%doc %{_texmfdir}/doc/man/man1/mktextfm.man1.pdf
%doc %{_mandir}/man1/texhash.1*
%doc %{_texmfdir}/doc/man/man1/texhash.man1.pdf
%doc %{_texmfdir}/doc/web2c/web2c.html
%doc %{_texmfdir}/doc/web2c/web2c.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

perl -pi -e 's%^(TEXMFMAIN\s+= ).*%$1%{_texmfdir}%;'			  \
	 -e 's%^(TEXMFDIST\s+= ).*%$1%{_texmfdistdir}%;'		  \
	 -e 's%^(TEXMFLOCAL\s+= ).*%$1%{_texmflocaldir}%;'		  \
	 -e 's%^(TEXMFSYSVAR\s+= ).*%$1%{_texmfvardir}%;'		  \
	 -e 's%^(TEXMFSYSCONFIG\s+= ).*%$1%{_texmfconfdir}%;'		  \
	 -e 's%^(TEXMFHOME\s+= ).*%$1\$HOME/texmf%;'			  \
	 -e 's%^(TEXMFVAR\s+= ).*%$1\$HOME/.texlive2011/texmf-var%;'	  \
	 -e 's%^(TEXMFCONFIG\s+= ).*%$1\$HOME/.texlive2011/texmf-config%;'\
	 -e 's%^(OSFONTDIR\s+= ).*%$1%{_datadir}/fonts%;'		  \
	texmf/web2c/texmf.cnf

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_infodir}
mv %{buildroot}%{_texmfdir}/doc/info/*.info %{buildroot}%{_infodir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
