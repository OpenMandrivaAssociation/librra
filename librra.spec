%define shortname	rra

%define major		0
%define libname		%mklibname %{shortname} %{major}
%define develname	%mklibname %{shortname} -d

Summary:	SynCE: Communication application
Name:		librra
Version:	0.11.1
Release:	%{mkrel 2}
License:	MIT
Group:		System/Libraries
Source0:	http://prdownloads.sourceforge.net/synce/%{name}-%{version}.tar.gz
Patch0:		synce-unused_var.patch
# From upstream SVN (rev 3466): fix using the word "type" as a
# variable name (breaks build) - AdamW 2008/06
Patch1:		librra-0.11.1-declarator.patch
URL:		http://synce.sourceforge.net/
Buildroot:	%{_tmppath}/%{name}-root
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
Obsoletes:	%{libname}-python < %{libname}-python-%{version}
Obsoletes:	python-%{mklibname rra 0} < %{version}-%{release}

%description -n python-%{name}
%{name} is part of the SynCE project.

%package -n %{develname}
Group:		Development/C
Summary:	SynCE: Communication application
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{libname}-devel < %{libname}-devel-%{version}
Obsoletes:	%{mklibname rra 0 -d}

%description -n %{develname}
%{name} is part of the SynCE project.

%prep
%setup -q
%patch0 -p1 -b .unused-var
%patch1 -p2 -b .declarator

perl -pi -e 's/-Werror//' lib/Makefile.in

%build
%configure2_5x --with-libsynce=%{_prefix} --includedir=%{_includedir}/rra
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

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_includedir}/rra
%{_libdir}/pkgconfig/librra.pc

%files -n python-%{name}
%{py_platsitedir}/pyrra.*

