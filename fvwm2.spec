Summary:	An improved version of the FVWM X-based window manager.
Name:		fvwm2
Version:	2.2.4
Release:	7
License:	GPL
Group:		X11/Window Managers
Group(pl):	X11/Zarz±dcy Okien
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
URL:		http://www.fvwm.org/
Source0:	ftp://ftp.fvwm.org/pub/fvwm/version-2/fvwm-%{version}.tar.gz
Source1:	fvwm-2.0.46.icons.tar.gz
Source2:	fvwm2.desktop
Source3:	fvwm2-system.fvwm2rc.tar.gz
Source4:	%{name}.RunWM
Source5:	%{name}.wm_style
Patch0:		fvwm2-paths.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	fvwm2-icons
Requires:	wmconfig >= 0.9.9-5
Requires:	m4
Requires:	xinitrc >= 3.0
Obsoletes:	fvwm95

%define		_prefix	/usr/X11R6
%define		_mandir	/usr/X11R6/man

%description
FVWM2 (the F stands for whatever you want, but the VWM stands for
Virtual Window Manager) is an improved version of the FVWM window
manager for the X Window System and shares the same characteristics as
FVWM.

Install the fvwm2 package if you'd like to use the FVWM2 window
manager. If you install fvwm2, you'll also need to install
fvwm2-icons.

%description -l pl
FVWM (za F mo¿na sobie podstawic co kto woli, lecz VWM pochodzi od
pierwszych liter "Virtual Window Manager", czyli wirtualnego mened¿era
okien) to ulepszona wersja mened¿era okien dla systemu X Window FVWM i
posiada te same cechy.

Nale¿y zainstalowaæ pakiet fvwm2 jesli chce siê uzywaæ mened¿era okien
FVWM2. Instaluj±c fvwm2 nalezy równiez zainstalowaæ pakiet
fvwm2-icons.

%package icons
Summary:	Graphic files used by the FVWM and FVWM2 window managers
Group:		X11/Window Managers
Group(pl):	X11/Zarz±dcy Okien
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Obsoletes:	fvwm95-icons

%description icons
The fvwm2-icons package contains icons, bitmaps and pixmaps used by
the FVWM and FVWM2 X Window System window managers.

You'll need to install fvwm2-icons if you are installing fvwm and/or
fvwm2.

%prep
%setup -n fvwm-%{version} -q -a1 -a3
%patch0 -p1

%build
CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions" \
CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=%{_prefix} \
	--enable-extras \
	--libexecdir=\${prefix}/lib/X11/fvwm2	\
	--sysconfdir=%{_sysconfdir}/X11/fvwm2 \
	--mandir=%{_mandir}
%{__make} \
	CFLAGS="$RPM_OPT_FLAGS" \
	CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{sysconfig/wmstyle,X11/fvwm2} \
	$RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir}/X11/fvwm2 \
	mandir=$RPM_BUILD_ROOT%{_mandir}

install system.fvwm2rc $RPM_BUILD_ROOT%{_sysconfdir}/X11/fvwm2
install fvwm2.menu.m4 $RPM_BUILD_ROOT%{_sysconfdir}/X11/fvwm2

rm -rf $RPM_BUILD_ROOT%{_datadir}/icons
install -d $RPM_BUILD_ROOT%{_datadir}/icons/mini

install icons/*.xpm $RPM_BUILD_ROOT%{_datadir}/icons
mv $RPM_BUILD_ROOT%{_datadir}/icons/mini.*.xpm $RPM_BUILD_ROOT%{_datadir}/icons/mini

install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties

install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/%{name}.sh
install %{SOURCE5} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/%{name}.names

# consflicts with gimp
rm -f $RPM_BUILD_ROOT/usr/X11R6/share/icons/{folder,question}.xpm

strip --strip-unneeded $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/X11/fvwm2}/* || :

gzip -9nf README AUTHORS NEWS ChangeLog \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,AUTHORS,NEWS,ChangeLog}.gz
%doc docs
%dir /etc/X11/fvwm2
%config /etc/X11/fvwm2/*
%attr(755,root,root) /etc/sysconfig/wmstyle/*.sh
/etc/sysconfig/wmstyle/*.names
%dir %{_libdir}/X11/fvwm2
%attr(755,root,root) %{_libdir}/X11/fvwm2/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gnome/wm-properties/fvwm2.desktop
%{_mandir}/man1/*

%files icons
%defattr(644,root,root,755)
%dir %{_datadir}/icons
%dir %{_datadir}/icons/mini
%{_datadir}/icons/*.xpm
%{_datadir}/icons/mini/*.xpm
