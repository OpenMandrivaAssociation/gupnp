%define api 1.0
%define major 3
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d

Summary:	Object-oriented framework for creating UPnP devices and control points
Name:		gupnp
Version:	0.16.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Development/Other
Url:		http://www.gupnp.org/sources/gupnp/
Source0:	http://www.gupnp.org/sources/gupnp/%{name}-%{version}.tar.gz
BuildRequires:	gssdp-devel >= 0.9.2
BuildRequires:	libuuid-devel
BuildRequires:	libsoup-devel >= 2.28.2
BuildRequires:	libxml2-devel
BuildRequires:	glib2-devel
BuildRequires:	gobject-introspection-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
GUPnP is an object-oriented open source framework for creating UPnP 
devices and control points.

%package -n %{libname}

Summary:	Main library for gupnp
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{_lib}gupnp3 < 0.16.0
Conflicts: gir-repository < 0.6.5-11

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with gupnp.

%package -n %{develname}
Summary:	Headers for developing programs that will use gupnp
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts: gir-repository < 0.6.5-11

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use gupnp

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*%{api}.so.%{major}*
%_libdir/girepository-1.0/GUPnP-1.0.typelib

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS README NEWS
%{_libdir}/pkgconfig/gupnp*.pc
%{_includedir}/gupnp-1.0/lib%{name}/*.h
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_datadir}/gtk-doc/html/*
%{_bindir}/gupnp-binding-tool
%_datadir/gir-1.0/GUPnP-1.0.gir

