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
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/MB/MBARBON/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8a039891dbf2deeebe8940bc805e0660
URL:		http://search.cpan.org/dist/ExtUtils-XSpp/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Base
BuildRequires:	perl-Test-Differences
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Anything that does not look like a XS++ directive or a class
declaration is passed verbatim to XS. If you want XS++ to ignore code
that looks like a XS++ directive or class declaration, simply surround
it with a raw block delimiter like this:

%{ XS++ won't interpret this %}

See under Classes.

# %description -l pl.UTF-8
# TODO

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/xspp
%{perl_vendorlib}/ExtUtils/*.pm
%dir %{perl_vendorlib}/ExtUtils/XSpp
%{perl_vendorlib}/ExtUtils/XSpp/*.pm
%{_mandir}/man?/*
%{_examplesdir}/%{name}-%{version}
