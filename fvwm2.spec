#
# TODO: more updates in system.fvwm2rc (see warnings on run)
#
# Conditional build:
%bcond_without	stroke		# without mouse strokes (gestures) support
%bcond_without	xft		# without Xft (1 or 2) support
%bcond_with	fribidi		# with bidirectional text support
%bcond_with	gnome		# with gnome-libs and wm-properties
%bcond_with	rplay		# with internal sound support (through rplay)
#
%include	/usr/lib/rpm/macros.perl
Summary:	An improved version of the FVWM X-based window manager
Summary(de.UTF-8):	F(?) Virtual Window Manager
Summary(es.UTF-8):	Administrador de ventanas semejante al mwm
Summary(fr.UTF-8):	F(?) Virtual Window Manager
Summary(ja.UTF-8):	改良版 FVWM - X 用ウィンドウマネージャ
Summary(pl.UTF-8):	Ulepszona wersja zarządcy okien FVWM
Summary(pt_BR.UTF-8):	Gerenciador de janelas semelhante ao mwm
Summary(ru.UTF-8):	Виртуальный оконный менеджер F(?)
Summary(tr.UTF-8):	Yaygın bir pencere denetleyicisi
Name:		fvwm2
Version:	2.5.28
Release:	7
License:	GPL
Group:		X11/Window Managers
Source0:	ftp://ftp.fvwm.org/pub/fvwm/version-2/fvwm-%{version}.tar.bz2
# Source0-md5:	8e11fa4f752c568b392973d13af993df
Source1:	fvwm-2.0.46.icons.tar.gz
# Source1-md5:	8d81420cf49442fca4bb2b61ae54eeb9
Source2:	%{name}-system.%{name}rc.tar.gz
# Source2-md5:	22c1f6c5ab4bd84376daa37debd3e889
Source3:	%{name}.RunWM
Source4:	%{name}-xsession.desktop
Source5:	%{name}.desktop
Source6:	mozilla.xpm
Patch0:		%{name}-paths.patch
Patch1:		FvwmPager.patch
Patch2:		%{name}-locale_names.patch
Patch3:		%{name}-varia.patch
Patch4:		%{name}-libpng14.patch
Patch5:		%{name}-xft2-link.patch
URL:		http://www.fvwm.org/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_fribidi:BuildRequires:	fribidi-devel}
%{?with_gnome:BuildRequires:	gnome-libs-devel}
BuildRequires:	gtk+-devel
BuildRequires:	libpng-devel >= 1.4
%{?with_stroke:BuildRequires:	libstroke-devel}
BuildRequires:	pkgconfig
BuildRequires:	readline-devel >= 4.2
%{?with_rplay:BuildRequires:	rplay-devel}
BuildRequires:	rpm-perlprov
%{?with_xft:BuildRequires:	xorg-lib-libXft-devel}
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXt-devel
Requires(post):	vfmg >= 0.9.95
Requires:	fvwm2-icons = %{version}-%{release}
Requires:	m4
Requires:	vfmg >= 0.9.18-2
Obsoletes:	fvwm95
Conflicts:	filesystem < 3.0-20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/fvwm2
%define		_wmpropsdir	/usr/share/gnome/wm-properties

%description
FVWM2 (the F stands for whatever you want, but the VWM stands for
Virtual Window Manager) is an improved version of the FVWM window
manager for the X Window System and shares the same characteristics as
FVWM.

%description -l es.UTF-8
Fvwm2 es una versión del popular administrador de ventanas "Feeble
Virtual Window Manager".

%description -l ja.UTF-8
FVWM2 (Fは好きなように解釈してください。ただし、 VWM は Virtual Window
Manager を省略したものです。)は FVWM と同じ特徴を持ち 更に拡張された X
Window System 用ウィンドウマネージャです。

%description -l pl.UTF-8
FVWM (za F można sobie podstawić co kto woli, lecz VWM pochodzi od
pierwszych liter "Virtual Window Manager", czyli wirtualny zarządca
okien) to ulepszona wersja zarządcy okien dla systemu X Window FVWM i
posiadająca te same cechy.

%description -l pt_BR.UTF-8
Fvwm2 é uma versão do popular gerenciador de janelas "Feeble Virtual
Window Manager".

%description -l ru.UTF-8
fvwm2 - это версия популярного "Feeble Virtual Window Manager".

%package icons
Summary:	Graphic files used by the FVWM and FVWM2 window managers
Summary(de.UTF-8):	Symbole und Pixmaps für fvwm
Summary(fr.UTF-8):	Icônes et pixmaps pour fvwm
Summary(pl.UTF-8):	Pliki graficzne używane przez zarządców okien FVWM i FVWM2
Summary(ru.UTF-8):	Пиктограммы и растровые картинки для fvwm2
Summary(tr.UTF-8):	Fvwm için çeşitli minik görüntü ve simgeler
Group:		X11/Window Managers
Obsoletes:	fvwm95-icons

%description icons
This package contains icons, bitmaps and pixmaps for fvwm and fvwm2.

%description icons -l de.UTF-8
Dieses Paket enthält Symbole, Bitmaps und Pixmaps für fvwm und fvwm2.

%description icons -l fr.UTF-8
Ce package contient des icones, bitmaps et pixmaps pour fvwm et fvwm2.

%description icons -l pl.UTF-8
Ten pakiet zawiera ikony, bitmapy i pixmapy dla fvwm i fvwm2.

%description icons -l ru.UTF-8
Этот пакет содержит пиктограммы и прочие картинки для fvwm2.

%description icons -l tr.UTF-8
Fvwm için çeşitli minik görüntü ve simgeler.

%package perl
Summary:	fvwm-perllib, FvwmPerl and dependent modules
Summary(pl.UTF-8):	fvwm-perllib, FvwmPerl i zależne moduły
Group:		X11/Window Managers/Tools
Requires:	%{name} = %{version}-%{release}

%description perl
fvwm-perllib, FvwmPerl and dependent modules.

%description perl -l pl.UTF-8
fvwm-perllib, FvwmPerl i zależne moduły.

%prep
%setup -n fvwm-%{version} -q -a1 -a2
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

mv -f po/FvwmScript.sv{_SE,}.po
mv -f po/FvwmTaskBar.sv{_SE,}.po
mv -f po/fvwm.sv{_SE,}.po

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-dmalloc \
	--disable-efence \
	--%{!?debug:dis}%{?debug:en}able-debug-msgs \
	--disable-command-log \
	%{!?with_fribidi:--disable-bidi} \
	%{!?with_xft:--disable-xft} \
	--enable-multibyte \
	--enable-shape \
	--enable-sm \
	%{?with_gnome:--with-gnome}%{!?with_gnome:--without-gnome} \
	--with-xpm-library \
	%{!?with_rplay:--without-rplay-library} \
	--with-stroke-library \
	--with-ncurses-library \
	--with-readline-library \
	--with-ncurses-library \
	--with-iconv-library=no \
	--without-termcap-library

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

install -d \
	$RPM_BUILD_ROOT{%{_sysconfdir},%{_wmpropsdir}} \
	$RPM_BUILD_ROOT{%{_datadir}/{locale,xsessions},%{_pixmapsdir}/mini}

install system.fvwm2rc $RPM_BUILD_ROOT%{_sysconfdir}/system.fvwm2rc
install fvwm2.menu.m4 $RPM_BUILD_ROOT%{_sysconfdir}

install icons/*.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

mv $RPM_BUILD_ROOT%{_pixmapsdir}/mini-*.xpm \
	$RPM_BUILD_ROOT%{_pixmapsdir}/mini

# Conflicts with wmmaker
mv $RPM_BUILD_ROOT%{_pixmapsdir}/xv{,-fvwm}.xpm

install %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/fvwm2-session
install %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop
%{?with_gnome:install %{SOURCE5} $RPM_BUILD_ROOT%{_wmpropsdir}}
install %{SOURCE6} $RPM_BUILD_ROOT%{_pixmapsdir}

touch $RPM_BUILD_ROOT%{_sysconfdir}/fvwm2.menu2

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/xpmroot.1
echo ".so fvwm-root.1" > $RPM_BUILD_ROOT%{_mandir}/man1/xpmroot.1

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
# generate initial menu
[ -f /etc/sysconfig/vfmg ] && . /etc/sysconfig/vfmg
[ "$FVWM2" = yes -o "$FVWM2" = 1 -o ! -f /etc/X11/fvwm2/fvwm2.menu2 ] && \
	vfmg fvwm2 >/etc/X11/fvwm2/fvwm2.menu2 2>/dev/null ||:

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS NEWS docs
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/fvwm2.menu.m4
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/system.fvwm2rc
%ghost %{_sysconfdir}/fvwm2.menu2
%attr(755,root,root) %{_bindir}/[!f]*
%attr(755,root,root) %{_bindir}/fvwm
%attr(755,root,root) %{_bindir}/fvwm-[!p]*
%attr(755,root,root) %{_bindir}/fvwm2
%attr(755,root,root) %{_bindir}/fvwm2-session
%dir %{_libdir}/fvwm
%attr(755,root,root) %{_libdir}/fvwm/Fvwm[!DGPWT]*
%attr(755,root,root) %{_libdir}/fvwm/FvwmD[!e]*
%attr(755,root,root) %{_libdir}/fvwm/FvwmGtk
%attr(755,root,root) %{_libdir}/fvwm/FvwmP[!e]*
%attr(755,root,root) %{_libdir}/fvwm/FvwmT[!a]*
%attr(755,root,root) %{_libdir}/fvwm/FvwmTaskBar
%attr(755,root,root) %{_libdir}/fvwm/FvwmW[!i]*
%attr(755,root,root) %{_libdir}/fvwm/FvwmWinList
%dir %{_datadir}/fvwm
%{_datadir}/fvwm/[!p]*
%{_datadir}/xsessions/%{name}.desktop
%{?with_gnome:%{_wmpropsdir}/fvwm2.desktop}
%{_mandir}/man1/[!Ff]*.1*
%{_mandir}/man1/Fvwm[!DGPW]*.1*
%{_mandir}/man1/FvwmD[!e]*.1*
%{_mandir}/man1/FvwmP[!e]*.1*
%{_mandir}/man1/FvwmW[!i]*.1*
%{_mandir}/man1/FvwmWinList.1*
%{_mandir}/man1/fvwm.1*
%{_mandir}/man1/fvwm-[!p]*.1*

%files icons
%defattr(644,root,root,755)
%{_pixmapsdir}/*.xpm
%dir %{_pixmapsdir}/mini
%{_pixmapsdir}/mini/*.xpm

%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fvwm-perllib
%attr(755,root,root) %{_libdir}/fvwm/FvwmDebug
%attr(755,root,root) %{_libdir}/fvwm/FvwmGtkDebug
%attr(755,root,root) %{_libdir}/fvwm/FvwmPerl
%attr(755,root,root) %{_libdir}/fvwm/FvwmTabs
%attr(755,root,root) %{_libdir}/fvwm/FvwmWindowMenu
%{_datadir}/fvwm/perllib
%{_mandir}/man1/fvwm-perllib.1*
%{_mandir}/man1/FvwmDebug.1*
%{_mandir}/man1/FvwmGtkDebug.1*
%{_mandir}/man1/FvwmPerl.1*
%{_mandir}/man1/FvwmWindowMenu.1*
