#
# TODO: more updates in system.fvwm2rc (see warnings on run)
#
# Conditional build:
# _with_fribidi		- with bidirectional text support
# _with_gnome		- with gnome-libs
# _with_rplay		- with internal sound support (through rplay)
# _without_stroke	- without mouse strokes (gestures) support
# _without_xft		- without Xft (1 or 2) support
#
%include	/usr/lib/rpm/macros.perl
Summary:	An improved version of the FVWM X-based window manager
Summary(de):	F(?) Virtual Window Manager
Summary(es):	Administrador de ventanas semejante al mwm
Summary(fr):	F(?) Virtual Window Manager
Summary(ja):	²þÎÉÈÇ FVWM - X ÍÑ¥¦¥£¥ó¥É¥¦¥Þ¥Í¡¼¥¸¥ã
Summary(tr):	Yaygýn bir pencere denetleyicisi
Summary(pl):	Ulepszona wersja zarz±dcy okien FVWM
Summary(pt_BR):	Gerenciador de janelas semelhante ao mwm
Summary(ru):	÷ÉÒÔÕÁÌØÎÙÊ ÏËÏÎÎÙÊ ÍÅÎÅÄÖÅÒ F(?)
Name:		fvwm2
Version:	2.5.5
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	ftp://ftp.fvwm.org/pub/fvwm/version-2/fvwm-%{version}.tar.bz2
Source1:	fvwm-2.0.46.icons.tar.gz
Source2:	%{name}.desktop
Source3:	%{name}-system.%{name}rc.tar.gz
Source4:	%{name}.RunWM
Source5:	%{name}.wm_style
Patch0:		%{name}-paths.patch
URL:		http://www.fvwm.org/
%{!?_without_xft:BuildRequires:	Xft-devel}
BuildRequires:	autoconf
BuildRequires:	automake
%{?_with_fribidi:BuildRequires:	fribidi-devel}
%{?_with_gnome:BuildRequires:	gnome-libs-devel}
BuildRequires:	gtk+-devel
BuildRequires:	libpng-devel
%{!?_without_stroke:BuildRequires:	libstroke-devel}
BuildRequires:	readline-devel >= 4.2
%{?_with_rplay:BuildRequires:	rplay-devel}
BuildRequires:	rpm-perlprov
Requires:	fvwm2-icons
Requires:	wmconfig >= 0.9.10-6
Requires:	m4
Requires:	xinitrc >= 3.0
Obsoletes:	fvwm95
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/fvwm2
%define		_wmpropsdir	/usr/share/wm-properties

%description
FVWM2 (the F stands for whatever you want, but the VWM stands for
Virtual Window Manager) is an improved version of the FVWM window
manager for the X Window System and shares the same characteristics as
FVWM.

%description -l es
Fvwm2 es una versión del popular administrador de ventanas "Feeble
Virtual Window Manager".

%description -l ja
FVWM2 (F¤Ï¹¥¤­¤Ê¤è¤¦¤Ë²ò¼á¤·¤Æ¤¯¤À¤µ¤¤¡£¤¿¤À¤·¡¢ VWM ¤Ï Virtual Window
Manager ¤ò¾ÊÎ¬¤·¤¿¤â¤Î¤Ç¤¹¡£)¤Ï FVWM ¤ÈÆ±¤¸ÆÃÄ§¤ò»ý¤Á ¹¹¤Ë³ÈÄ¥¤µ¤ì¤¿ X
Window System ÍÑ¥¦¥£¥ó¥É¥¦¥Þ¥Í¡¼¥¸¥ã¤Ç¤¹¡£

%description -l pl
FVWM (za F mo¿na sobie podstawic co kto woli, lecz VWM pochodzi od
pierwszych liter "Virtual Window Manager", czyli wirtualny zarz±dca
okien) to ulepszona wersja zarz±dcy okien dla systemu X Window FVWM i
posiadaj±ca te same cechy.

%description -l pt_BR
Fvwm2 é uma versão do popular gerenciador de janelas "Feeble Virtual
Window Manager".

%description -l ru
fvwm2 - ÜÔÏ ×ÅÒÓÉÑ ÐÏÐÕÌÑÒÎÏÇÏ "Feeble Virtual Window Manager".

%package icons
Summary:	Graphic files used by the FVWM and FVWM2 window managers
Summary(de):	Symbole und Pixmaps für fvwm
Summary(fr):	Icônes et pixmaps pour fvwm
Summary(pl):	Pliki graficzne u¿ywane przez zarz±dców okien FVWM i FVWM2
Summary(ru):	ðÉËÔÏÇÒÁÍÍÙ É ÒÁÓÔÒÏ×ÙÅ ËÁÒÔÉÎËÉ ÄÌÑ fvwm2
Summary(tr):	Fvwm için çeþitli minik görüntü ve simgeler
Group:		X11/Window Managers
Obsoletes:	fvwm95-icons

%description icons
This package contains icons, bitmaps and pixmaps for fvwm and fvwm2.

%description icons -l de
Dieses Paket enthält Symbole, Bitmaps und Pixmaps für fvwm und fvwm2.

%description icons -l fr
Ce package contient des icones, bitmaps et pixmaps pour fvwm et fvwm2.

%description icons -l pl
Ten pakiet zawiera ikony, bitmapy i pixmapy dla fvwm i fvwm2.

%description icons -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÐÉËÔÏÇÒÁÍÍÙ É ÐÒÏÞÉÅ ËÁÒÔÉÎËÉ ÄÌÑ fvwm2.

%description icons -l tr
Fvwm için çeþitli minik görüntü ve simgeler.

%package perl
Summary:	fvwm-perllib, FvwmPerl and dependent modules
Summary(pl):	fvwm-perllib, FvwmPerl i zale¿ne modu³y
Group:		X11/Window Managers/Tools
Requires:	%{name} = %{version}

%description perl
fvwm-perllib, FvwmPerl and dependent modules.

%description perl -l pl
fvwm-perllib, FvwmPerl i zale¿ne modu³y.

%prep
%setup -n fvwm-%{version} -q -a1 -a3
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-dmalloc \
	--disable-efence \
	--disable-debug-msgs \
	--disable-command-log \
	%{!?_with_fribidi:--disable-bidi} \
	%{?_without_xft:--disable-xft} \
	--enable-multibyte \
	--enable-shape \
	--enable-sm \
	%{?_with_gnome:--with-gnome}%{!?_with_gnome:--without-gnome} \
	--with-xpm-library \
	%{!?_with_rplay:--without-rplay-library} \
	--with-stroke-library \
	--with-ncurses-library \
	--with-readline-library \
	--with-ncurses-library \
	--without-termcap-library

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},/etc/sysconfig/wmstyle,%{_wmpropsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

sed -e 's@^ModulePath.*@ModulePath /usr/lib/fvwm:/usr/share/fvwm@;s@^PixmapPath.*@@' \
	-e 's@^IconPath.*@ImagePath /usr/share/pixmaps:/usr/X11R6/share/pixmaps:/usr/X11R6/include/X11/pixmaps:/usr/X11R6/include/X11/bitmaps:/usr/share/icons:/usr/share/icons/mini@' \
	system.fvwm2rc > $RPM_BUILD_ROOT%{_sysconfdir}/system.fvwm2rc
install fvwm2.menu.m4 $RPM_BUILD_ROOT%{_sysconfdir}

rm -rf $RPM_BUILD_ROOT%{_datadir}/icons
install -d $RPM_BUILD_ROOT%{_datadir}/icons/mini

install icons/*.xpm $RPM_BUILD_ROOT%{_datadir}/icons
mv -f $RPM_BUILD_ROOT%{_datadir}/icons/mini-*.xpm $RPM_BUILD_ROOT%{_datadir}/icons/mini

install %{SOURCE2} $RPM_BUILD_ROOT%{_wmpropsdir}

install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/%{name}.sh
install %{SOURCE5} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/%{name}.names

# conflicts with gimp
rm -f $RPM_BUILD_ROOT%{_datadir}/icons/{folder,question}.xpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS NEWS docs
%dir /etc/X11/fvwm2
%config(noreplace) %verify(not size mtime md5) /etc/X11/fvwm2/*
%attr(755,root,root) /etc/sysconfig/wmstyle/*.sh
/etc/sysconfig/wmstyle/*.names
%attr(755,root,root) %{_bindir}/[!f]*
%attr(755,root,root) %{_bindir}/fvwm
%attr(755,root,root) %{_bindir}/fvwm2
%attr(755,root,root) %{_bindir}/fvwm-[!p]*
%dir %{_libdir}/fvwm
%attr(755,root,root) %{_libdir}/fvwm/Fvwm[!DGPW]*
%attr(755,root,root) %{_libdir}/fvwm/FvwmD[!e]*
%attr(755,root,root) %{_libdir}/fvwm/FvwmGtk
%attr(755,root,root) %{_libdir}/fvwm/FvwmP[!e]*
%attr(755,root,root) %{_libdir}/fvwm/FvwmW[!i]*
%attr(755,root,root) %{_libdir}/fvwm/FvwmWinList
%dir %{_datadir}/fvwm
%{_datadir}/fvwm/[!p]*
%{_wmpropsdir}/fvwm2.desktop
%{_mandir}/man1/[!Ff]*.1*
%{_mandir}/man1/Fvwm[!DGPW]*.1*
%{_mandir}/man1/FvwmD[!e]*.1*
%{_mandir}/man1/FvwmGtk.1*
%{_mandir}/man1/FvwmP[!e]*.1*
%{_mandir}/man1/FvwmW[!i]*.1*
%{_mandir}/man1/FvwmWinList.1*
%{_mandir}/man1/fvwm.1*
%{_mandir}/man1/fvwm-[!p]*.1*

%files icons
%defattr(644,root,root,755)
%dir %{_datadir}/icons
%dir %{_datadir}/icons/mini
%{_datadir}/icons/*.xpm
%{_datadir}/icons/mini/*.xpm

%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fvwm-perllib
%attr(755,root,root) %{_libdir}/fvwm/FvwmDebug
%attr(755,root,root) %{_libdir}/fvwm/FvwmGtkDebug
%attr(755,root,root) %{_libdir}/fvwm/FvwmPerl
%attr(755,root,root) %{_libdir}/fvwm/FvwmWindowLister
%{_datadir}/fvwm/perllib
%{_mandir}/man1/fvwm-perllib.1*
%{_mandir}/man1/FvwmDebug.1*
%{_mandir}/man1/FvwmGtkDebug.1*
%{_mandir}/man1/FvwmPerl.1*
%{_mandir}/man1/FvwmWindowLister.1*
