%define upstream_name    DVD-Read
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:    Access to DVD IFO file using libdvdread
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DVD/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: libdvdread-devel
BuildRequires: perl-devel

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provide way to query video DVD using libdvdread.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README sample/*
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.40.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.40.0-2
+ Revision: 681368
- mass rebuild

* Tue Apr 06 2010 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.1
+ Revision: 532140
- update to 0.04

* Sun Feb 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.1
+ Revision: 505724
- rebuild using %%perl_convert_version

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.03-2mdv2010.0
+ Revision: 440553
- rebuild

* Tue Nov 25 2008 Olivier Thauvin <nanardon@mandriva.org> 0.03-1mdv2009.1
+ Revision: 306493
- import perl-DVD-Read


