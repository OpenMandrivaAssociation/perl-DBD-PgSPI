%define module  DBD-PgSPI
%define	name	perl-%{module}
%define	version	0.02
%define	release	%mkrel 7
%define	pdir	DBD-PgSPI

Summary:	PL/Perl PostgreSQL database driver for the DBI module
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{module}-%{version}.tar.bz2
Patch0:		perl-%{module}.includedir.patch
Patch1:     DBI2.patch
Url:		http://search.cpan.org/search?dist=%{module}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel 
BuildRequires:  perl-DBI
BuildRequires:  postgresql-devel

%description
DBD::PgSPI is a Perl module which works with the DBI module to provide access
to PostgreSQL database from within pl/perl functions inside the database.

If you are looking for a way to access postgresql database from a perl script
running outside of your database, look at DBD::Pg, you cannot use this module.
This module is only intended for use by stored procedures written in 'plperl'
programming language running inside PostgreSQL.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0 -b .includedir
%patch1 -p0 -b .dbi2

%build
export POSTGRES_HOME=%_includedir/pgsql
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# Skipping make test, because it try to connect to a local DB
# make test

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README 
%{_mandir}/man*/*
%{perl_vendorlib}/*
