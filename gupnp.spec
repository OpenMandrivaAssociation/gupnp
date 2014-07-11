%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api	1.0
%define major	4
%define libname %mklibname %{name} %{api} %{major}
%define girname %mklibname %{name}-gir %{api}
%define devname %mklibname %{name} -d

Summary:	Object-oriented framework for creating UPnP devices and control points
Name:		gupnp
Version:	0.20.5
Release:	7
License:	GPLv2+
Group:		Development/Other
Url:		http://www.gupnp.org/sources/gupnp/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gupnp/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(gssdp-1.0) >= 0.11.2
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(libsoup-2.4) >= 2.28.2
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(uuid)
BuildRequires:  vala-tools

%description
GUPnP is an object-oriented open source framework for creating UPnP 
devices and control points.

%package -n %{libname}
Summary:	Main library for gupnp
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with gupnp.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Conflicts:	%{libname} < 0.18.4-2

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	Headers for developing programs that will use gupnp
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
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
%makeinstall_std

%files -n %{libname}
%{_libdir}/*%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GUPnP-%{api}.typelib

%files -n %{devname}
%doc AUTHORS README NEWS
%{_libdir}/pkgconfig/gupnp*.pc
%{_includedir}/gupnp-1.0/lib%{name}/*.h
%{_libdir}/*.so
%{_datadir}/gtk-doc/html/*
%{_bindir}/gupnp-binding-tool
%{_datadir}/gir-1.0/GUPnP-1.0.gir
%{_datadir}/vala/vapi/*

