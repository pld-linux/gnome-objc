Summary:     GNOME Objective C libraries
Name:        gnome-objc
Version:     0.27
Release:     1
Copyright:   LGPL
Group:       X11/gnome
Source:      ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
Requires:    gnome-libs >= %{version}
URL:         http://www.gnome.org/
BuildRoot:   /tmp/%{name}-%{version}-root

%description
Basic libraries you must have installed to use GNOME programs
that are built with Objective C.

GNOME is the GNU Network Object Model Environment.  That's a fancy
name but really GNOME is a nice GUI desktop environment.  It makes
using your computer easy, powerful, and easy to configure.

%package devel
Summary:     Header filesc, etc to develop Objective C GNOME applications
Group:       X11/gnome
Requires:    %{name} = %{version}

%description devel
Libraries, include files, etc you can use to develop Objective C
GNOME applications.

%package static
Summary:     Static ibraries Objective C GNOME applications
Group:       X11/gnome
Requires:    %{name}-devel = %{version}

%description static
Static libraries to develop Objective C GNOME applications.

%prep
%setup -q

%build
# Needed for snapshot releases.
if [ ! -f configure ]; then
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh --prefix=/usr
else
  CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
fi

make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr install

strip $RPM_BUILD_ROOT/usr/lib/lib*.so.*.*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog NEWS README
%attr(755, root, root) /usr/lib/lib*.so.*.*
%lang(es) /usr/share/locale/es/LC_MESSAGES/gnome-objc.mo
%lang(fr) /usr/share/locale/fr/LC_MESSAGES/gnome-objc.mo
%lang(it) /usr/share/locale/it/LC_MESSAGES/gnome-objc.mo
%lang(no) /usr/share/locale/no/LC_MESSAGES/gnome-objc.mo
%lang(pt) /usr/share/locale/pt/LC_MESSAGES/gnome-objc.mo

%files devel
%defattr(644, root, root, 755)
/usr/lib/lib*.so
/usr/lib/*.sh
/usr/include/*

%files static
/usr/lib/lib*.a

%changelog
* Mon Aug 24 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.27-1]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- added "Requires: gnome-libs >= %%{version}" to main package,
- changeded dependences to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- added %lang macros for .mo foles,
- added striping shared libraries,
- added %attr and %defattr macros in %files (allow build package from
  non-root account).

* Fri Mar 13 1998 Marc Ewing <marc@redhat.com>
- Integrate into gnome-objc source tree
