%define shortname	rra

%define major		0
%define libname		%mklibname %{shortname} %{major}
%define develname	%mklibname %{shortname} -d

Summary:	SynCE: Communication application
Name:		librra
Version:	0.16
Release:	1
License:	MIT
Group:		System/Libraries
Source0:	http://prdownloads.sourceforge.net/synce/%{name}-%{version}.tar.gz
URL:		http://synce.sourceforge.net/
BuildRequires:	libmimedir-devel
#BuildRequires:	librapi-devel >= %{version}
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
%configure2_5x --with-libsynce=%{_prefix} --includedir=%{_includedir}/rra --disable-static
%make includedir=%{buildroot}%{_includedir}/rra

%install
%makeinstall includedir=%{buildroot}%{_includedir}/rra

%files
%doc README TODO
%{_bindir}/*
%{_mandir}/man?/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/rra
%{_libdir}/pkgconfig/librra.pc

%files -n python-%{name}
%{py_platsitedir}/pyrra.*

