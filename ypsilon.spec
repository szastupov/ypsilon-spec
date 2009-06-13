Name:		ypsilon
Version:	0.9.6.update3
Release:	1%{?dist}
Summary:	R6RS Scheme implementation with concurrent garbage collector

Group:		Development/Languages
License:	BSD
URL:		http://code.google.com/p/ypsilon/
Source0:	http://ypsilon.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	make

%description
Ypsilon is an implementation of the Scheme programming language which conforms
to the latest standard R6RS. It achieves a remarkably short garbage collection
pause time and improved performance during parallel execution because it
implements mostly concurrent garbage collection, which is optimized for the
multi-core CPU system.

%prep
%setup -q


%build
make %{?_smp_mflags} PREFIX=/usr


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT PREFIX=/usr


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
%{_bindir}/*
%{_datadir}/%{name}/
%{_mandir}/man*/*

%changelog

