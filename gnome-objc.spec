Summary:	GNOME Objective C libraries
Summary(pl):	Biblioteki Objective C do GNOME
Name:		gnome-objc
Version:	1.0.2
Release:	1
Copyright:	LGPL
Group:		X11/GNOME
Group(pl):	X11/GNOME
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/gnome-objc/%{name}-%{version}.tar.gz
Patch0:		gnome-objc-DESTDIR.patch
Icon:		gnome-objc.gif
URL:		http://www.gnome.org/
Requires:	gtk+ = 1.2.1
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	gnome

%description
Basic libraries you must have installed to use GNOME programs
that are built with Objective C.

GNOME is the GNU Network Object Model Environment. That's a fancy
name but really GNOME is a nice GUI desktop environment.  It makes
using your computer easy, powerful, and easy to configure.

%description -l pl
Pakiet ten zawiera biblioteki Objective C do GNOME.

GNOME jest graficznym inferfejsem u¿ytkownika ³atwym wkonfiguracji.
Uczyni z twojego komputera maszynê ³atw± i przyjemn± w obs³udze.

%package devel
Summary:	Header filesc, etc to develop Objective C GNOME applications
Summary(pl):	Pliki nag³ówkowe i dokumentacja do Objective C GNOME
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Libraries, include files, etc you can use to develop Objective C
GNOME applications.

%description -l pl devel
Pliki nag³ówkowe itp. Jednym s³owem wszystko czego potrzebujesz
aby samemu tworzyæ aplikacje GNOME z u¿yciem Objective C.

%package static
Summary:	Static ibraries Objective C GNOME applications
Summary(pl):	Biblioteki statyczne do Objective C GNOME
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libraries to develop Objective C GNOME applications.

%description -l pl static
Biblioteki statyczne do Objective C GNOME.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr/X11R6
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*.*

gzip -9nf AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/lib/lib*.so.*.*

%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/gnome-objc.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/gnome-objc.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/gnome-objc.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/gnome-objc.mo
%lang(pt) /usr/X11R6/share/locale/pt/LC_MESSAGES/gnome-objc.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/gnome-objc.mo

%files devel
%doc *gz
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/obgnome-config
%attr(755,root,root) /usr/X11R6/lib/lib*.so
%attr(755,root,root) /usr/X11R6/lib/*.sh
/usr/X11R6/include/*

%files static
%attr(644,root,root) /usr/X11R6/lib/lib*.a

%changelog
* Mon Mar 29 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0.2-1]
- added ru locale,
- added pl translation,
- gzipping %doc,
- %doc moved to devel.

* Wed Jan 06 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.99.1-1]
- added LDFLAGS="-s" to ./configure enviroment,
- dome updates in %files.

* Fri Sep 18 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.27-2]
- added package Icon,
- changed prefix to /usr/X11R6.

* Mon Aug 24 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.27-1]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- added "Requires: gnome-libs >= %%{version}" to main package,
- changed dependencies to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- added %lang macros for .mo foles,
- added stripping shared libraries,
- added %attr and %defattr macros in %files (allows build package from
  non-root account).

* Fri Mar 13 1998 Marc Ewing <marc@redhat.com>
- Integrate into gnome-objc source tree
