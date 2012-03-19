%define api 1.0
%define major 4
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d

Summary:	Object-oriented framework for creating UPnP devices and control points
Name:		gupnp
Version:	0.18.2
Release:	1
License:	GPLv2+
Group:		Development/Other
Url:		http://www.gupnp.org/sources/gupnp/
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.xz
Patch0: gupnp-0.18.2-fix-linking.patch
BuildRequires:	gssdp-devel >= 0.11.2
BuildRequires:	libuuid-devel
BuildRequires:	libsoup-devel >= 2.28.2
BuildRequires:	libxml2-devel
BuildRequires:	glib2-devel
BuildRequires:	gobject-introspection-devel

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
%apply_patches

autoreconf -fi

%build
%configure2_5x \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name '*.la' | xargs rm


%files -n %{libname}
%{_libdir}/*%{api}.so.%{major}*
%_libdir/girepository-1.0/GUPnP-1.0.typelib

%files -n %{develname}
%doc AUTHORS README NEWS
%{_libdir}/pkgconfig/gupnp*.pc
%{_includedir}/gupnp-1.0/lib%{name}/*.h
%{_libdir}/*.so
%{_datadir}/gtk-doc/html/*
%{_bindir}/gupnp-binding-tool
%_datadir/gir-1.0/GUPnP-1.0.gir

