%{?scl:%scl_package perl-File-Temp}

%global cpan_version 0.2304
Name:           %{?scl_prefix}perl-File-Temp
# Keep 2-digit version to align with future versions
Version:        %(echo '%{cpan_version}' | sed 's/\(\...\)\(.\)/\1.\2/')
Release:        366%{?dist}
Summary:        Return name and handle of a temporary file safely
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/File-Temp/
Source0:        http://www.cpan.org/authors/id/D/DA/DAGOLDEN/File-Temp-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.17
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
BuildRequires:  %{?scl_prefix}perl(vars)
# VMS::Stdio not needed
# Tests:
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(File::Spec::Functions)
BuildRequires:  %{?scl_prefix}perl(FileHandle)
BuildRequires:  %{?scl_prefix}perl(List::Util)
# Symbol not needed
BuildRequires:  %{?scl_prefix}perl(Test::More)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(IO::Handle)
Requires:       %{?scl_prefix}perl(parent) >= 0.221
Requires:       %{?scl_prefix}perl(POSIX)

%if 0%{?rhel} < 7
# RPM 4.8 style
%{?filter_setup:
# Filter unused dependencies
%filter_from_requires /^%{?scl_prefix}perl(Symbol)/d
%filter_from_requires /^%{?scl_prefix}perl(VMS::Stdio)/d
# Filter under-specified dependencies
%filter_from_requires /^%{?scl_prefix}perl(parent)$/d
%?perl_default_filter
}
%else
# RPM 4.9 style
# Filter unused dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(Symbol|VMS::Stdio\\)
# Filter under-specified dependencies
%global __requires_exclude %{__requires_exclude}|^%{?scl_prefix}perl\\(parent\\)$
%endif

%description
File::Temp can be used to create and open temporary files in a safe way.
There is both a function interface and an object-oriented interface. The
File::Temp constructor or the tempfile() function can be used to return the
name and the open file handle of a temporary file. The tempdir() function
can be used to create a temporary directory.

%prep
%setup -q -n File-Temp-%{cpan_version}
chmod -x misc/benchmark.pl
%{?scl:scl enable %{scl} '}perl -MExtUtils::MakeMaker -e "ExtUtils::MM_Unix->fixin(q{misc/benchmark.pl})"%{?scl:'}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes LICENSE misc README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jul 11 2016 Petr Pisar <ppisar@redhat.com> - 0.23.04-366
- SCL

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
