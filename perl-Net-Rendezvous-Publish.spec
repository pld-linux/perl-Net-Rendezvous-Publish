#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Net
%define	pnam	Rendezvous-Publish
Summary:	Net::Rendezvous::Publish - publish Rendezvous services
Name:		perl-Net-Rendezvous-Publish
Version:	0.04
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	abd07bd91853f5536d6e3434c67918c3
URL:		http://search.cpan.org/dist/Net-Bonjour/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Accessor-Lvalue
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Rendezvous::Publish - publish Rendezvous services

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorlib}/Net/Rendezvous/Publish
%dir %{perl_vendorlib}/Net/Rendezvous/Publish/Backend
%{perl_vendorlib}/Net/Rendezvous/Publish.pm
%{perl_vendorlib}/Net/Rendezvous/Publish/Service.pm
%{perl_vendorlib}/Net/Rendezvous/Publish/Backend/Null.pm
%{_mandir}/man3/*
