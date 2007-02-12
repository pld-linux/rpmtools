#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
Summary:	Contains various rpm command-line tools
Summary(pl.UTF-8):	Różne narzędzia linii poleceń dla rpm-a
Name:		rpmtools
Version:	5.0.24
Release:	1
License:	GPL
Group:		Base/Utilities
# ftp://ftp.aso.ee/pub/Mandrake/official/current/SRPMS/main/rpmtools-5.0.20-1mdk.src.rpm
# ftp://ftp.aso.ee/pub/Mandrake/devel/cooker/SRPMS/main/rpmtools-5.0.24-1mdk.src.rpm
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	a3f57fe905a0bc5b476238313e01a4a1
Patch0:		%{name}-no-MDK.patch
URL:		http://cvs.mandriva.com/cgi-bin/cvsweb.cgi/soft/rpmtools/
BuildRequires:	bzip2-devel
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-devel
BuildRequires:	rpm-devel >= 4.0.3
Requires:	bzip2 >= 1.0
Requires:	perl-URPM >= 0.94
Conflicts:	packdrake < 5.0.10
Conflicts:	rpmtools-compat <= 2.0
Conflicts:	rpmtools-devel <= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# perl-Compress-Zlib is only "suggested"
%define		_noautoreq	'perl(Compress::Zlib)'

%description
Various tools needed by urpmi and drakxtools for handling rpm files.

%description -l pl.UTF-8
Różne narzędzia wymagane przez urpmi i drakxtools do obsługi plików
rpm.

%package -n packdrake
Summary:	A simple Archive Extractor/Builder
Summary(pl.UTF-8):	Proste narzędzie do rozpakowywania i tworzenia archiwów
Group:		Base/Utilities
Provides:	perl(packdrake)
Conflicts:	rpmtools <= 5.0.0

%description -n packdrake
Packdrake is a simple indexed archive builder and extractor using
standard compression methods.

Packadrakeng is a from scratch rewrite of the original packdrake. Its
format is fully compatible with old packdrake.

%description -n packdrake -l pl.UTF-8
Packdrake to proste narzędzie do tworzenia i rozpakowywania
indeksowanych archiwów przy użyciu standardowych metod kompresji.

Packadrakeng to przepisanie od nowa oryginalnego packdrake'a. Jego
format jest w pełni kompatybilny ze starym packdrake'iem.

%prep
%setup -q
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/parsehdlist
%attr(755,root,root) %{_bindir}/rpm2header
%attr(755,root,root) %{_bindir}/gendistrib
%attr(755,root,root) %{_bindir}/genhdlist
%attr(755,root,root) %{_bindir}/rpm2cpio.pl
%attr(755,root,root) %{_bindir}/dumpdistribconf
%{perl_vendorlib}/Distribconf*
%{_mandir}/man1/*
%{_mandir}/man3/Distribconf*

%files -n packdrake
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/packdrake
%{perl_vendorlib}/packdrake.pm
%{perl_vendorlib}/Packdrakeng.pm
%{perl_vendorlib}/Packdrakeng/zlib.pm
%{_mandir}/man3/[pP]ackdrake*
