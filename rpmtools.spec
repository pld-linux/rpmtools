#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define rpm_version %(rpm -q --queryformat '%{version}-%{release}' rpm)
Name:		rpmtools
Summary:	Contains various rpm command-line tools
Version:	5.0.20
Release:	0.1
# get the source from mdk cvs repository (see http://www.linuxmandrake.com/en/cvs.php3)
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-no-MDK.patch
License:	GPL
Group:		Base/Utilities
URL:		http://cvs.mandrakesoft.com/cgi-bin/cvsweb.cgi/soft/rpmtools
BuildRequires:	rpm-devel >= 4.0.3
BuildRequires:	bzip2-devel
BuildRequires:	perl-devel
BuildRequires:	perl-Compress-Zlib
Requires:	rpm >= %{rpm_version}
Requires:	bzip2 >= 1.0
Requires:	perl-URPM >= 0.94
Conflicts:	rpmtools-compat <= 2.0
Conflicts:	rpmtools-devel <= 2.0
Conflicts:	packdrake < 5.0.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# perl-Compress-Zlib is only "suggested"
%define		_noautoreq	'perl(Compress::Zlib)'

%description
Various tools needed by urpmi and drakxtools for handling rpm files.

%package -n packdrake
Summary:	A simple Archive Extractor/Builder
Group:		Base/Utilities
Conflicts:	rpmtools <= 5.0.0
Provides:	perl(packdrake)

%description -n packdrake
Packdrake is a simple indexed archive builder and extractor using
standard compression methods.

Packadrakeng is a from scratch rewrite of the original packdrake. Its
format is fully compatible with old packdrake.

%prep
%setup -q
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
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
