Summary:	GNOME Objective C libraries
Summary(pl):	Biblioteki Objective C do GNOME
Name:		gnome-objc
Version:	1.0.40
Release:	7
License:	LGPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-objc/%{name}-%{version}.tar.gz
Icon:		gnome-objc.gif
URL:		http://www.gnome.org/
Requires:	gtk+ >= 1.2.1
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
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	gcc-objc

%description devel
Libraries, include files, etc you can use to develop Objective C GNOME
applications.

%description -l pl devel
Pliki nag³ówkowe itp. Jednym s³owem wszystko czego potrzebujesz aby
samemu tworzyæ aplikacje GNOME z u¿yciem Objective C.

%package static
Summary:	Static ibraries Objective C GNOME applications
Summary(pl):	Biblioteki statyczne do Objective C GNOME
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libraries to develop Objective C GNOME applications.

%description -l pl static
Biblioteki statyczne do Objective C GNOME.

%prep
%setup -q

%build
OBJC="%{__cc}"; export OBJC
gettextize --copy --force
aclocal -I macros
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

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
%doc *gz
%attr(755,root,root) %{_bindir}/obgnome-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
