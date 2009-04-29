#
%define		rev	r960796

Summary:	Polkit-qt use the PolicyKit API through Qt-styled API
Name:		polkit-qt
Version:	0.9.2
Release:	0.%{rev}.1
License:	GPL v2
Group:		Libraries
URL:		http://www.kde.org/
BuildRequires:	PolicyKit-devel
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	pkgconfig
# svn co svn://anonsvn.kde.org/home/kde/trunk/kdesupport/polkit-qt
Source0:	%{name}-%{rev}.tar.bz2
# Source0-md5:	a2656d4d16c72e398ad2a19bc0d98b8f
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
%setup -q -n %{name}

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
%attr(755,root,root) %_libdir/libpolkit-qt-core.so.0
%attr(755,root,root) %_libdir/libpolkit-qt-core.so.0.9.2

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %_libdir/libpolkit-qt-gui.so.0
%attr(755,root,root) %_libdir/libpolkit-qt-gui.so.0.9.2

%files devel
%defattr(644,root,root,755)
%dir %_includedir/PolicyKit/polkit-qt
%_includedir/PolicyKit/polkit-qt
%_libdir/*.so
%_libdir/pkgconfig/*.pc
