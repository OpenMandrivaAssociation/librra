%define shortname	rra

%define major		0
%define libname		%mklibname %{shortname} %{major}
%define develname	%mklibname %{shortname} -d

Summary:	SynCE: Communication application
Name:		librra
Version:	0.14
Release:	3
License:	MIT
Group:		System/Libraries
Source0:	http://prdownloads.sourceforge.net/synce/%{name}-%{version}.tar.gz
URL:		http://synce.sourceforge.net/
BuildRequires:	libmimedir-devel
BuildRequires:	librapi-devel >= %{version}
BuildRequires:	automake
BuildRequires:	python-devel
BuildRequires:	python-pyrex
Obsoletes:	synce-%{shortname} < %{version}-%{release}

%description
%{name} is part of the SynCE project. 

%package -n %{libname}
Group:		System/Libraries
Summary:	SynCE: Communication application
Obsoletes:	%libname < %{libname}-%{version}

%description -n %{libname}
%{name} is part of the SynCE project.

%package -n python-%{name}
Group:		System/Libraries
Summary:	SynCE: Communication application
Obsoletes:	python-%{mklibname rra 0} < %{version}-%{release}

%description -n python-%{name}
%{name} is part of the SynCE project.

%package -n %{develname}
Group:		Development/C
Summary:	SynCE: Communication application
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{mklibname rra 0 -d}

%description -n %{develname}
%{name} is part of the SynCE project.

%prep
%setup -q

perl -pi -e 's/-Werror//' lib/Makefile.in

%build
%configure2_5x --with-libsynce=%{_prefix} --includedir=%{_includedir}/rra
%make includedir=%{buildroot}%{_includedir}/rra

%install
rm -rf %{buildroot}
%makeinstall includedir=%{buildroot}%{_includedir}/rra

%files
%defattr(-,root,root)
%doc README TODO
%{_bindir}/*
%{_mandir}/man?/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/rra
%{_libdir}/pkgconfig/librra.pc

%files -n python-%{name}
%{py_platsitedir}/pyrra.*



%changelog
* Sun Nov 21 2010 Funda Wang <fwang@mandriva.org> 0.14-2mdv2011.0
+ Revision: 599411
- rebuild for p2.7

* Thu Jul 23 2009 Frederik Himpe <fhimpe@mandriva.org> 0.14-1mdv2010.0
+ Revision: 399058
- Update to new version 0.14
- Drop useless patch

* Wed Jan 14 2009 Adam Williamson <awilliamson@mandriva.org> 0.13-1mdv2009.1
+ Revision: 329254
- new release 0.13

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 0.12-2mdv2009.1
+ Revision: 319652
- rebuild with python 2.6

* Thu Jul 17 2008 Adam Williamson <awilliamson@mandriva.org> 0.12-1mdv2009.0
+ Revision: 237689
- drop declarator.patch (merged upstream)
- new release 0.12

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Jun 03 2008 Adam Williamson <awilliamson@mandriva.org> 0.11.1-2mdv2009.0
+ Revision: 214749
- add declarator.patch from upstream SVN to fix a build error
- rebuild against fixed libmimedir

* Wed Apr 16 2008 Adam Williamson <awilliamson@mandriva.org> 0.11.1-1mdv2009.0
+ Revision: 194661
- python package should be python-%%name, not python-%%libname
- new devel policy
- version obsoletes and provides
- clean spec
- new release 0.11.1

* Thu Jan 17 2008 Emmanuel Andry <eandry@mandriva.org> 0.11-6mdv2008.1
+ Revision: 154432
+ rebuild (emptylog)

* Sun Jan 13 2008 Emmanuel Andry <eandry@mandriva.org> 0.11-5mdv2008.1
+ Revision: 150901
- fix provides

* Sat Jan 12 2008 Emmanuel Andry <eandry@mandriva.org> 0.11-4mdv2008.1
+ Revision: 149805
- fix obsoletes
- split binaries and libs

* Fri Jan 11 2008 Emmanuel Andry <eandry@mandriva.org> 0.11-2mdv2008.1
+ Revision: 148843
- fix build
- import librra


