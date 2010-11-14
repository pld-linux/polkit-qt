%define		qtver	4.6.0

Summary:	Convenience library for using PolicyKit with Qt-styled API
Summary(pl.UTF-8):	Biblioteka ułatwiająca używanie biblioteki PolicyKit poprzez API w stylu Qt
Name:		polkit-qt
Version:	0.9.4
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	ftp://ftp.kde.org/pub/kde/stable/apps/KDE4.x/admin/%{name}-%{version}.tar.bz2
# Source0-md5:	70c41208716098793c7f946a67c21902
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
Requires:	QtCore >= %{qtver}
Requires:	QtDBus >= %{qtver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polkit-qt is a library that lets developers use the PolicyKit API
through a nice Qt-styled API. It is mainly a wrapper around QAction
and QAbstractButton that lets you integrate those two component easily
with PolicyKit.

%description -l pl.UTF-8
Polkit-qt to biblioteka pozwalająca programistom używać API biblioteki
PolicyKit za pośrednictwem API w stylu Qt. Jest głównie obudowaniem
QAction i QAbstractButton pozwalającym integrować te komponenty przy
użyciu PolicyKita.

%package devel
Summary:	Polkit-qt header files
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Polkit-qt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= %{qtver}

%description devel
Polkit-qt header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Polkit-qt.

%package gui
Summary:	Polkit-qt GUI library
Summary(pl.UTF-8):	Biblioteka Polkit-qt GUI
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtGui >= %{qtver}

%description gui
Polkit-qt GUI library.

%description gui -l pl.UTF-8
Biblioteka Polkit-qt GUI.

%package gui-devel
Summary:	Header files for Polkit-qt GUI library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Polkit-qt GUI
Group:		Development/Libraires
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gui = %{version}-%{release}
Requires:	QtGui-devel >= %{qtver}

%description gui-devel
Header files for Polkit-qt GUI library.

%description gui-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Polkit-qt GUI.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_CXX_FLAGS_RELEASE="-DNDEBUG" \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	-DLIB_INSTALL_DIR=%{_libdir} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	-DQT_QMAKE_EXECUTABLE=/usr/bin/qmake-qt4

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	gui -p /sbin/ldconfig
%postun	gui -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libpolkit-qt-core.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpolkit-qt-core.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpolkit-qt-core.so
%dir %{_includedir}/PolicyKit/polkit-qt
%{_includedir}/PolicyKit/polkit-qt/Context
%{_includedir}/PolicyKit/polkit-qt/context.h
%{_includedir}/PolicyKit/polkit-qt/export.h
%{_includedir}/PolicyKit/polkit-qt/polkitqtversion.h
%{_pkgconfigdir}/polkit-qt-core.pc

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpolkit-qt-gui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpolkit-qt-gui.so.0

%files gui-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpolkit-qt-gui.so
%{_includedir}/PolicyKit/polkit-qt/Action*
%{_includedir}/PolicyKit/polkit-qt/Auth
%{_includedir}/PolicyKit/polkit-qt/action*.h
%{_includedir}/PolicyKit/polkit-qt/auth.h
%{_pkgconfigdir}/polkit-qt-gui.pc
%{_pkgconfigdir}/polkit-qt.pc
