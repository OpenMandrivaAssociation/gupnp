%define api 1.0
%define major 4
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d

Summary:	Object-oriented framework for creating UPnP devices and control points
Name:		gupnp
Version:	0.18.4
Release:	1
License:	GPLv2+
Group:		Development/Other
Url:		http://www.gupnp.org/sources/gupnp/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.xz
Patch0:		gupnp-0.18.2-fix-linking.patch
BuildRequires:	pkgconfig(gssdp-1.0) >= 0.11.2
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(libsoup-2.4) >= 2.28.2
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)

%description
GUPnP is an object-oriented open source framework for creating UPnP 
devices and control points.

%package -n %{libname}
Summary:	Main library for gupnp
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{_lib}gupnp3 < 0.16.0
Conflicts:	gir-repository < 0.6.5-11

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with gupnp.

%package -n %{develname}
Summary:	Headers for developing programs that will use gupnp
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	gir-repository < 0.6.5-11

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

%files -n %{libname}
%{_libdir}/*%{api}.so.%{major}*
%{_libdir}/girepository-1.0/GUPnP-1.0.typelib

%files -n %{develname}
%doc AUTHORS README NEWS
%{_libdir}/pkgconfig/gupnp*.pc
%{_includedir}/gupnp-1.0/lib%{name}/*.h
%{_libdir}/*.so
%{_datadir}/gtk-doc/html/*
%{_bindir}/gupnp-binding-tool
%{_datadir}/gir-1.0/GUPnP-1.0.gir



%changelog
* Mon Aug 20 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.18.4-1
+ Revision: 815393
- update to new version 0.18.4

* Fri May 04 2012 Götz Waschk <waschk@mandriva.org> 0.18.3-1
+ Revision: 795835
- update to new version 0.18.3

* Mon Mar 19 2012 Götz Waschk <waschk@mandriva.org> 0.18.2-1
+ Revision: 785548
- fix linking
- new version

* Sun Dec 11 2011 Götz Waschk <waschk@mandriva.org> 0.18.1-1
+ Revision: 740253
- update to new version 0.18.1

* Fri Dec 09 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.18.0-2
+ Revision: 739261
- rebuild
- removed .la files
- disabled static build
- removed mkrel, BuildRoot, clean section, defattr
- removed pre 200900 scriptlets
- cleaned up spec

* Tue Aug 30 2011 Götz Waschk <waschk@mandriva.org> 0.18.0-1
+ Revision: 697459
- new version
- bump gssdp dep
- new major

* Thu May 26 2011 Götz Waschk <waschk@mandriva.org> 0.16.1-1
+ Revision: 679166
- new version
- new source URL

* Fri Apr 15 2011 Funda Wang <fwang@mandriva.org> 0.16.0-1
+ Revision: 653169
- new version 0.16.0

* Wed Apr 06 2011 Funda Wang <fwang@mandriva.org> 0.13.5-4
+ Revision: 651063
- rebuild
- rebuild for updated libsoup libtool archive

* Mon Sep 13 2010 Götz Waschk <waschk@mandriva.org> 0.13.5-2mdv2011.0
+ Revision: 577977
- rebuild for new g-i

* Tue Aug 17 2010 Emmanuel Andry <eandry@mandriva.org> 0.13.5-1mdv2011.0
+ Revision: 570981
- New version 0.13.5

* Fri Jul 30 2010 Funda Wang <fwang@mandriva.org> 0.13.4-2mdv2011.0
+ Revision: 563770
- rebuild for new gobject-introspection

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 0.13.4-1mdv2011.0
+ Revision: 550674
- new version

* Mon Apr 12 2010 Götz Waschk <waschk@mandriva.org> 0.13.3-1mdv2010.1
+ Revision: 533734
- update build deps
- new version
- add introspection support

* Sat Dec 05 2009 Götz Waschk <waschk@mandriva.org> 0.13.2-1mdv2010.1
+ Revision: 473841
- new version

* Sat Nov 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.13.1-1mdv2010.1
+ Revision: 462239
- update to new version 0.13.1

* Sun Sep 20 2009 Frederik Himpe <fhimpe@mandriva.org> 0.13.0-1mdv2010.0
+ Revision: 445420
- Update to new version 0.13.0 (new major)

* Tue Aug 04 2009 Eugeni Dodonov <eugeni@mandriva.com> 0.12.8-2mdv2010.0
+ Revision: 409182
- Updated buildrequires for libuuid.

* Wed Jun 03 2009 Götz Waschk <waschk@mandriva.org> 0.12.8-1mdv2010.0
+ Revision: 382413
- update to new version 0.12.8

* Mon Apr 27 2009 Götz Waschk <waschk@mandriva.org> 0.12.7-1mdv2010.0
+ Revision: 369062
- update to new version 0.12.7

* Thu Mar 05 2009 Emmanuel Andry <eandry@mandriva.org> 0.12.6-1mdv2009.1
+ Revision: 349313
- New version 0.12.6

* Sun Jan 18 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.12.5-1mdv2009.1
+ Revision: 331044
- update to new version 0.12.5

* Tue Dec 02 2008 Götz Waschk <waschk@mandriva.org> 0.12.4-2mdv2009.1
+ Revision: 309215
- rebuild to get rid of libtasn1 dep

* Sun Nov 30 2008 Emmanuel Andry <eandry@mandriva.org> 0.12.4-1mdv2009.1
+ Revision: 308521
- New version

* Wed Nov 19 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.12.3-1mdv2009.1
+ Revision: 304513
- add buildrequires libtasn1-devel
- update to new version 0.12.3

* Mon Sep 01 2008 Frederik Himpe <fhimpe@mandriva.org> 0.12.2-1mdv2009.0
+ Revision: 278645
- New version (new major)
- Add gupnp-binding-tool file, only used for development
- Don't package ChangeLog

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun May 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.10.1-1mdv2009.0
+ Revision: 211075
- bump major
- new version
- do not re-define stuff
- update buildrequires
- spec file clean

* Mon Feb 25 2008 Thierry Vignaud <tv@mandriva.org> 0.6-2mdv2008.1
+ Revision: 174698
- fix summary

* Mon Feb 25 2008 Erwan Velu <erwan@mandriva.org> 0.6-1mdv2008.1
+ Revision: 174660
- Adding more BuildRequires
- import gupnp


