Summary:	GNOME Objective C libraries
Summary(pl):	Biblioteki Objective C do GNOME
Name:		gnome-objc
Version:	1.0.40
Release:	8
License:	LGPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-objc/1.0/%{name}-%{version}.tar.gz
Icon:		gnome-objc.gif
URL:		http://www.gnome.org/
Requires:	gtk+ >= 1.2.1
BuildRequires:	automake
BuildRequires:	gcc-objc
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome

%define		_prefix		/usr/X11R6

%description
Basic libraries you must have installed to use GNOME programs that are
built with Objective C.

GNOME is the GNU Network Object Model Environment. That's a fancy name
but really GNOME is a nice GUI desktop environment. It makes using
your computer easy, powerful, and easy to configure.

%description -l pl
Pakiet ten zawiera biblioteki Objective C do GNOME.

GNOME jest graficznym inferfejsem u¿ytkownika ³atwym wkonfiguracji.
Uczyni z twojego komputera maszynê ³atw± i przyjemn± w obs³udze.

%package devel
Summary:	Header filesc, etc to develop Objective C GNOME applications
Summary(pl):	Pliki nag³ówkowe i dokumentacja do Objective C GNOME
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	gcc-objc

%description devel
Libraries, include files, etc you can use to develop Objective C GNOME
applications.

%description devel -l pl
Pliki nag³ówkowe itp. Jednym s³owem wszystko czego potrzebujesz aby
samemu tworzyæ aplikacje GNOME z u¿yciem Objective C.

%package static
Summary:	Static ibraries Objective C GNOME applications
Summary(pl):	Biblioteki statyczne do Objective C GNOME
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries to develop Objective C GNOME applications.

%description static -l pl
Biblioteki statyczne do Objective C GNOME.

%prep
%setup -q

%build
OBJC="%{__cc}"; export OBJC
install /usr/share/automake/config.* .
%{__gettextize}
%{__aclocal} -I macros
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/obgnome-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
