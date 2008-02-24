%define name gupnp
%define version 0.6
%define release %mkrel 1
%define major 0
%define libname %mklibname %{name}  %{major}
%define develname %mklibname %{name} -d

Summary: GUPnP is an object-oriented open source framework for creating UPnP devices and control points
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Development/Other
Url: http://www.gupnp.org/sources/gupnp/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gssdp-devel

%description
GUPnP is an object-oriented open source framework for creating UPnP devices and control points

%package -n %{libname}

Summary:        Main library for gupnp
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with gupnp.

%package -n     %{develname}
Summary:        Headers for developing programs that will use gupnp
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use gupnp

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%prep
%setup -q
%configure

%build
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/pkgconfig/gupnp*.pc
%{_includedir}/gupnp-1.0/lib%{name}/*.h
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_datadir}/gtk-doc/html/*

