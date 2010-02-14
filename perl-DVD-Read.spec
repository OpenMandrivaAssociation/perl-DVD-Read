%define upstream_name    DVD-Read
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

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
