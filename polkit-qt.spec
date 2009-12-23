%define		qtver	4.6.0

Summary:	Polkit-qt use the PolicyKit API through Qt-styled API
Name:		polkit-qt
Version:	0.9.3
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	ftp://ftp.kde.org/pub/kde/stable/apps/KDE4.x/admin/%{name}-%{version}.tar.bz2
# Source0-md5:	8be0205f8cb91161fdaf527f7cb6852d
URL:		http://www.kde.org/
BuildRequires:	PolicyKit-devel
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polkit-qt is a library that lets developers use the PolicyKit API
through a nice Qt-styled API. It is mainly a wrapper around QAction
and QAbstractButton that lets you integrate those two component easily
with PolicyKit.

%package devel
Summary:	Polkit-qt use the PolicyKit API through Qt-styled API
License:	GPL v2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-gui = %{version}-%{release}

%description devel
Polkit-qt is a library that lets developers use the PolicyKit API
through a nice Qt-styled API. It is mainly a wrapper around QAction
and QAbstractButton that lets you integrate those two component easily
with PolicyKit.

%package gui
Summary:	Polkit-qt use the PolicyKit API through Qt-styled API
License:	GPL v2
Group:		Libraries

%description gui
Polkit-qt is a library that lets developers use the PolicyKit API
through a nice Qt-styled API. It is mainly a wrapper around QAction
and QAbstractButton that lets you integrate those two component easily
with PolicyKit.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-LCMS_DIR=%{_libdir} \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DCMAKE_BUILD_TYPE=%{!?debug:release}%{?debug:debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libpolkit-qt-core.so.?
%attr(755,root,root) %{_libdir}/libpolkit-qt-core.so.*.*.*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libpolkit-qt-gui.so.?
%attr(755,root,root) %{_libdir}/libpolkit-qt-gui.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpolkit-qt-core.so
%attr(755,root,root) %{_libdir}/libpolkit-qt-gui.so
%{_includedir}/PolicyKit/polkit-qt
%{_libdir}/pkgconfig/*.pc
