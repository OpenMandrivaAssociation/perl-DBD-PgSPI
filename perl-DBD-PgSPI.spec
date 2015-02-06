%define upstream_name DBD-PgSPI
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	8

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


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.20.0-6
+ Revision: 774153
- use perl() deps for buildrequires
- cleanout spec
- add some missing variables for printfs.. (P3)
- fix build against recent postgresql (P2)
- mass rebuild of perl extensions against perl 5.14.2

  + Funda Wang <fwang@mandriva.org>
    - mass rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Jérôme Quelin <jquelin@mandriva.org>
    - force rebuild
    - rebuild using %%perl_convert_version

* Mon Sep 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.02-11mdv2009.0
+ Revision: 289453
- fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.02-8mdv2008.1
+ Revision: 152055
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Oct 27 2007 Olivier Thauvin <nanardon@mandriva.org> 0.02-7mdv2008.1
+ Revision: 102500
- Patch1: fix compilation against latest DBI driver


* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/06/06 22:58:41 (53723)
- rebuild

* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/06/06 22:57:36 (53722)
Import perl-DBD-PgSPI

* Sun Apr 30 2006 Olivier Thauvin <nanardon@mandriva.org> 0.02-4mdk
- rebuild

* Sun Apr 17 2005 Olivier Thauvin <nanardon@mandrake.org> 0.02-3mdk
- rebuild against latest postgres

* Sun Mar 13 2005 Olivier Thauvin <nanardon@mandrake.org> 0.02-2mdk
- BuildRequires

* Sat Mar 12 2005 Olivier Thauvin <nanardon@mandrake.org> 0.02-1mdk
- make a specfile

