%define name     librra
%define shortname rra
%define release  %mkrel 6
%define version  0.11

%define major 0

%define libname %mklibname %shortname %major

Summary: SynCE: Communication application
Name: %{name}
Version: %{version}
Release: %{release}
License: MIT
Group: System/Libraries
Source: %{name}-%{version}.tar.bz2
Patch0: synce-unused_var.patch
URL: http://synce.sourceforge.net/
Buildroot: %{_tmppath}/%name-root
BuildRequires: libmimedir-devel
BuildRequires: librapi-devel >= %{version}
BuildRequires: automake
BuildRequires: python-devel
BuildRequires: python-pyrex
Obsoletes: synce-%shortname


%description
%{shortname} is part of the SynCE project

%package -n %libname
Group: System/Libraries
Summary: SynCE: Communication application
Provides: lib%{shortname} = %{version}-%{release}
Provides: %{shortname} = %{version}-%{release}
Obsoletes: %libname < %libname-%{version}


%description -n %libname
%{name} is part of the SynCE project


%package -n python-%libname
Group: System/Libraries
Summary: SynCE: Communication application
Provides: lib%{shortname}-python = %{version}-%{release}
Provides: python-%{name} = %{version}-%{release}
Obsoletes: %libname-python < %libname-python-%{version}

%description -n python-%libname
%{shortname} is part of the SynCE project


%package -n %libname-devel
Group: System/Libraries
Summary: SynCE: Communication application
Provides: lib%{shortname}-devel = %{version}-%{release}
Requires: %{libname} = %{version}-%{release}
Obsoletes: %libname-devel < %libname-devel-%{version}

%description -n %libname-devel
%{shortname} is part of the SynCE project

%prep
%setup -q
%patch0 -p1 -b .unused-var

perl -pi -e 's/-Werror//' lib/Makefile.in

%build
%configure --with-libsynce=%{_prefix} --includedir=%{_includedir}/rra
%make includedir=%{buildroot}%{_includedir}/rra

%install
rm -rf %{buildroot}
%makeinstall includedir=%{buildroot}%{_includedir}/rra

%post -n %{name} -p /sbin/ldconfig
%postun -n %{name} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README TODO
%{_bindir}/*
%{_mandir}/man?/*

%files -n %libname
%defattr(-,root,root)
%_libdir/*.so.%{major}
%_libdir/*.so.%{major}.*

%files -n %{libname}-devel
%defattr(-,root,root)
%_libdir/*.so
%_libdir/*.la
%_libdir/*.a
%_includedir/rra
%_libdir/pkgconfig/librra.pc

%files -n python-%{libname}
%py_platsitedir/pyrra.*
