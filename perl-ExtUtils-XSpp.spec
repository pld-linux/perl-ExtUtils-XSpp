#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	ExtUtils
%define	pnam	XSpp
Summary:	ExtUtils::XSpp - XS for C++
Summary(pl.UTF-8):	ExtUtils::XSpp - XS dla C++
Name:		perl-ExtUtils-XSpp
Version:	0.18
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c44ad3281df81319d02833a4e42282ac
URL:		http://search.cpan.org/dist/ExtUtils-XSpp/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Base
BuildRequires:	perl-Test-Differences
%endif
Requires:	perl-Digest-MD5 >= 2.0
Requires:	perl-ExtUtils-ParseXS >= 3.07
Requires:	perl(ExtUtils::Typemaps) >= 1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XS++ is just a thin layer over plain XS.

%description -l pl.UTF-8
XS++ to niewielka warstwa nad zwykłym XS.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	config="optimize='%{rpmcflags}'" \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/ExtUtils/XSpp.pod \
	$RPM_BUILD_ROOT%{perl_vendorlib}/ExtUtils/XSpp/Plugin.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/xspp
%{perl_vendorlib}/ExtUtils/XSpp.pm
%dir %{perl_vendorlib}/ExtUtils/XSpp
%{perl_vendorlib}/ExtUtils/XSpp/*.pm
%{perl_vendorlib}/ExtUtils/XSpp/Exception
%{perl_vendorlib}/ExtUtils/XSpp/Node
%dir %{perl_vendorlib}/ExtUtils/XSpp/Plugin
%dir %{perl_vendorlib}/ExtUtils/XSpp/Plugin/feature
%{perl_vendorlib}/ExtUtils/XSpp/Plugin/feature/default_xs_typemap.pm
%{perl_vendorlib}/ExtUtils/XSpp/Typemap
%{_mandir}/man1/xspp.1p*
%{_mandir}/man3/ExtUtils::XSpp*.3pm*
%{_examplesdir}/%{name}-%{version}
