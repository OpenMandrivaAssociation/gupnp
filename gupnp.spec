%define major 2
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Object-oriented framework for creating UPnP devices and control points
Name:		gupnp
Version:	0.12.3
Release:	%mkrel 1
License:	GPLv2+
Group:		Development/Other
Url:		http://www.gupnp.org/sources/gupnp/
Source0:	http://www.gupnp.org/sources/gupnp/%{name}-%{version}.tar.gz
BuildRequires:	gssdp-devel >= 0.6.1
BuildRequires:	ext2fs-devel
BuildRequires:	libsoup-devel
BuildRequires:	libxml2-devel
BuildRequires:	glib2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%package -n %{develname}
Summary:	Headers for developing programs that will use gupnp
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use gupnp

%prep
%setup -q
%configure2_5x

%build
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
%{_libdir}/*.so.%{major}*

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
