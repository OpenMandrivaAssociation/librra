%define shortname rra

%define major 0
%define libname %mklibname %{shortname} %{major}
%define devname %mklibname %{shortname} -d

Summary:	SynCE: Communication application
Name:		librra
Version:	0.14
Release:	5
License:	MIT
Group:		System/Libraries
Url:		http://synce.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/synce/%{name}-%{version}.tar.gz
BuildRequires:	python-pyrex
BuildRequires:	libmimedir-devel
BuildRequires:	pkgconfig(librapi2) >= %{version}
BuildRequires:	pkgconfig(python)

%description
%{name} is part of the SynCE project.

%files
%doc README TODO
%{_bindir}/*
%{_mandir}/man?/*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	SynCE: Communication application
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
%{name} is part of the SynCE project.

%files -n %{devname}
%{_libdir}/*.so
%{_includedir}/rra
%{_libdir}/pkgconfig/librra.pc

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	SynCE: Communication application
Group:		System/Libraries

%description -n %{libname}
%{name} is part of the SynCE project.

%files -n %{libname}
%{_libdir}/librra.so.%{major}*

#----------------------------------------------------------------------------

%package -n python-%{name}
Summary:	SynCE: Communication application
Group:		System/Libraries

%description -n python-%{name}
%{name} is part of the SynCE project.

%files -n python-%{name}
%{py_platsitedir}/pyrra.*

#----------------------------------------------------------------------------

%prep
%setup -q
perl -pi -e 's/-Werror//' lib/Makefile.in

%build
%configure2_5x --with-libsynce=%{_prefix} --includedir=%{_includedir}/rra
%make includedir=%{buildroot}%{_includedir}/rra

%install
%makeinstall includedir=%{buildroot}%{_includedir}/rra

