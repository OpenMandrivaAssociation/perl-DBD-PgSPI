%define upstream_name DBD-PgSPI
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	PL/Perl PostgreSQL database driver for the DBI module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBD/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		perl-%{upstream_name}.includedir.patch
Patch1:		DBI2.patch
Patch2:		DBD-PgSPI-0.02-postgresql9.patch
Patch3:		DBD-PgSPI-0.02-add-missing-string-format-variables.patch

BuildRequires:	perl-devel 
BuildRequires:	perl(DBI)
BuildRequires:	postgresql-devel

%description
DBD::PgSPI is a Perl module which works with the DBI module to provide access
to PostgreSQL database from within pl/perl functions inside the database.

If you are looking for a way to access postgresql database from a perl script
running outside of your database, look at DBD::Pg, you cannot use this module.
This module is only intended for use by stored procedures written in 'plperl'
programming language running inside PostgreSQL.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p0 -b .includedir
%patch1 -p0 -b .dbi2
%patch2 -p1 -b .postgresql9~
%patch3 -p1 -b .str_fmt~

%build
export POSTGRES_HOME=%{_includedir}/postgresql

perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# Skipping make test, because it try to connect to a local DB
# make test

%install
%makeinstall_std

%files
%doc README 
%{_mandir}/man*/*
%{perl_vendorlib}/*
