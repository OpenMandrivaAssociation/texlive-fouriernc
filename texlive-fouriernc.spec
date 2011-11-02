Name:		texlive-fouriernc
Version:	1.0
Release:	1
Summary:	Use New Century Schoolbook text with Fourier maths fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/fouriernc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fouriernc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fouriernc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package provides a LaTeX mathematics font setup for use
with New Century Schoolbook text. In order to use it you need
to have the Fourier-GUTenberg fonts installed.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

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
%{_texmfdistdir}/fonts/afm/public/fouriernc/fourier-mcl.afm
%{_texmfdistdir}/fonts/afm/public/fouriernc/fourier-ml.afm
%{_texmfdistdir}/fonts/afm/public/fouriernc/fourier-mlb.afm
%{_texmfdistdir}/fonts/afm/public/fouriernc/fourier-mlit.afm
%{_texmfdistdir}/fonts/afm/public/fouriernc/fourier-mlitb.afm
%{_texmfdistdir}/fonts/afm/public/fouriernc/fourier-ms.afm
%{_texmfdistdir}/fonts/afm/public/fouriernc/pncb8a.afm
%{_texmfdistdir}/fonts/afm/public/fouriernc/pncbi8a.afm
%{_texmfdistdir}/fonts/afm/public/fouriernc/pncr8a.afm
%{_texmfdistdir}/fonts/afm/public/fouriernc/pncri8a.afm
%{_texmfdistdir}/fonts/tfm/public/fouriernc/fncmi.tfm
%{_texmfdistdir}/fonts/tfm/public/fouriernc/fncmib.tfm
%{_texmfdistdir}/fonts/tfm/public/fouriernc/fncmii.tfm
%{_texmfdistdir}/fonts/tfm/public/fouriernc/fncmiib.tfm
%{_texmfdistdir}/fonts/tfm/public/fouriernc/fncsy.tfm
%{_texmfdistdir}/fonts/vf/public/fouriernc/fncmi.vf
%{_texmfdistdir}/fonts/vf/public/fouriernc/fncmib.vf
%{_texmfdistdir}/fonts/vf/public/fouriernc/fncmii.vf
%{_texmfdistdir}/fonts/vf/public/fouriernc/fncmiib.vf
%{_texmfdistdir}/fonts/vf/public/fouriernc/fncsy.vf
%{_texmfdistdir}/tex/latex/fouriernc/fmlfncm.fd
%{_texmfdistdir}/tex/latex/fouriernc/fmlfncmi.fd
%{_texmfdistdir}/tex/latex/fouriernc/fmsfncm.fd
%{_texmfdistdir}/tex/latex/fouriernc/fouriernc.sty
%{_texmfdistdir}/tex/latex/fouriernc/t1fnc.fd
%{_texmfdistdir}/tex/latex/fouriernc/ts1fnc.fd
%doc %{_texmfdistdir}/doc/fonts/fouriernc/README
%doc %{_texmfdistdir}/doc/fonts/fouriernc/build-fouriernc.tex
%doc %{_texmfdistdir}/doc/fonts/fouriernc/mathit.mtx
%doc %{_texmfdistdir}/doc/fonts/fouriernc/mathsy.mtx
%doc %{_texmfdistdir}/doc/fonts/fouriernc/omlgutop.etx
%doc %{_texmfdistdir}/doc/fonts/fouriernc/omsgutop.etx
%doc %{_texmfdistdir}/doc/fonts/fouriernc/setxheight.mtx
%doc %{_texmfdistdir}/doc/fonts/fouriernc/specialkernings.mtx
%doc %{_texmfdistdir}/doc/fonts/fouriernc/specialkerningsital.mtx
%doc %{_texmfdistdir}/doc/fonts/fouriernc/test_fouriernc.pdf
%doc %{_texmfdistdir}/doc/fonts/fouriernc/unset0.mtx
%doc %{_texmfdistdir}/doc/fonts/fouriernc/unset0A.mtx
%doc %{_texmfdistdir}/doc/fonts/fouriernc/unsetAlph.mtx
%doc %{_texmfdistdir}/doc/fonts/fouriernc/unsetUCgreek.mtx
%doc %{_texmfdistdir}/doc/fonts/fouriernc/unsetfontparams.mtx
%doc %{_texmfdistdir}/doc/fonts/fouriernc/unsetmu.mtx
%doc %{_texmfdistdir}/doc/fonts/fouriernc/unsetpar.mtx
%doc %{_texmfdistdir}/doc/fonts/fouriernc/zrmhax.mtx
%doc %{_texmfdistdir}/doc/fonts/fouriernc/zrykernx.mtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
