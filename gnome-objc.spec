Summary:	GNOME Objective C libraries
Summary(pl.UTF-8):	Biblioteki Objective C do GNOME
Name:		gnome-objc
Version:	1.0.40
Release:	8
License:	LGPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-objc/1.0/%{name}-%{version}.tar.gz
# Source0-md5:	5128635f4d8d143e5f9b4646456b3025
URL:		http://www.gnome.org/
BuildRequires:	automake
BuildRequires:	gcc-objc
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
Requires:	gtk+ >= 1.2.1
Obsoletes:	gnome
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Basic libraries you must have installed to use GNOME programs that are
built with Objective C.

GNOME is the GNU Network Object Model Environment. That's a fancy name
but really GNOME is a nice GUI desktop environment. It makes using
your computer easy, powerful, and easy to configure.

%description -l pl.UTF-8
Pakiet ten zawiera biblioteki Objective C do GNOME.

GNOME jest graficznym interfejsem użytkownika łatwym w konfiguracji.
Uczyni z twojego komputera maszynę łatwą i przyjemną w obsłudze.

%package devel
Summary:	Header filesc, etc to develop Objective C GNOME applications
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do Objective C GNOME
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gcc-objc

%description devel
Libraries, include files, etc you can use to develop Objective C GNOME
applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe itp. Jednym słowem wszystko czego potrzebujesz aby
samemu tworzyć aplikacje GNOME z użyciem Objective C.

%package static
Summary:	Static ibraries Objective C GNOME applications
Summary(pl.UTF-8):	Biblioteki statyczne do Objective C GNOME
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries to develop Objective C GNOME applications.

%description static -l pl.UTF-8
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
