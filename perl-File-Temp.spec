%{?scl:%scl_package perl-File-Temp}

%global cpan_version 0.2309
Name:           %{?scl_prefix}perl-File-Temp
Epoch:          1
# Normalized version, compete with perl.spec
Version:        0.230.900
Release:        451%{?dist}
Summary:        Return name and handle of a temporary file safely
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/File-Temp
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/File-Temp-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl(:VERSION) >= 5.6
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
# Keep Carp::Heavy optional
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(Errno)
BuildRequires:  %{?scl_prefix}perl(Exporter) >= 5.57
BuildRequires:  %{?scl_prefix}perl(Fcntl) >= 1.03
BuildRequires:  %{?scl_prefix}perl(File::Path) >= 2.06
BuildRequires:  %{?scl_prefix}perl(File::Spec) >= 0.8
BuildRequires:  %{?scl_prefix}perl(IO::Handle)
BuildRequires:  %{?scl_prefix}perl(IO::Seekable)
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(parent) >= 0.221
BuildRequires:  %{?scl_prefix}perl(POSIX)
BuildRequires:  %{?scl_prefix}perl(Scalar::Util)
# Symbol not needed
# VMS::Stdio not needed
# Tests:
BuildRequires:  %{?scl_prefix}perl(FileHandle)
# Symbol not needed
BuildRequires:  %{?scl_prefix}perl(Test::More)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(POSIX)

# Filter unused dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(Symbol|VMS::Stdio\\)

%description
File::Temp can be used to create and open temporary files in a safe way.
There is both a function interface and an object-oriented interface. The
File::Temp constructor or the tempfile() function can be used to return the
name and the open file handle of a temporary file. The tempdir() function
can be used to create a temporary directory.

%prep
%setup -q -n File-Temp-%{cpan_version}
chmod -x misc/benchmark.pl
%{?scl:scl enable %{scl} '}perl -MConfig -p -i -e %{?scl:'"}'%{?scl:"'}s|\A#!/usr/local/bin/perl\b|$Config{startperl}|%{?scl:'"}'%{?scl:"'} misc/benchmark.pl%{?scl:'}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc LICENSE
# Omit CONTRIBUTING (first half is not relevant to a binary package, second
# half is already presented in POD)
%doc Changes misc README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Dec 20 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.230.900-451
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.230.900-439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.230.900-438
- Increase release to favour standalone package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.230.900-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Petr Pisar <ppisar@redhat.com> - 1:0.230.900-1
- 0.2309 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.230.800-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Petr Pisar <ppisar@redhat.com> - 1:0.230.800-1
- 0.2308 bump

* Tue Jun 26 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.230.600-2
- Perl 5.28 rebuild

* Mon Jun 25 2018 Petr Pisar <ppisar@redhat.com> - 0.230.600-1
- 0.2306 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.230.400-396
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 15 2017 Petr Pisar <ppisar@redhat.com> - 0.230.400-395
- Remove duplicate dependencies

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.230.400-394
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.230.400-393
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.230.400-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Petr Pisar <ppisar@redhat.com> - 0.230.400-1
- Normalize package version to dotted decimal format

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.23.04-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.04-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.04-346
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.23.04-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.23.04-311
- Perl 5.22 rebuild

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.23.04-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.23.04-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Oct 14 2013 Petr Pisar <ppisar@redhat.com> - 0.23.04-1
- 0.2304 bump

* Thu Oct 10 2013 Petr Pisar <ppisar@redhat.com> - 0.23.03-1
- 0.2303 bump

* Tue Oct 01 2013 Petr Pisar <ppisar@redhat.com> - 0.23.02-1
- 0.2302 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 29 2013 Petr Pisar <ppisar@redhat.com> - 0.23.01-3
- Specify all dependencies

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 0.23.01-2
- Link minimal build-root packages against libperl.so explicitly

* Mon Apr 15 2013 Petr Pisar <ppisar@redhat.com> - 0.23.01-1
- 0.2301 bump

* Fri Mar 22 2013 Petr Pisar <ppisar@redhat.com> 0.23-1
- Specfile autogenerated by cpanspec 1.78.
