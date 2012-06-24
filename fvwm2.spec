#
# TODO: more updates in system.fvwm2rc (see warnings on run)
#
# Conditional build:
%bcond_without	stroke		# without mouse strokes (gestures) support
%bcond_without	xft		# without Xft (1 or 2) support
%bcond_with	fribidi		# with bidirectional text support
%bcond_with	gnome		# with gnome-libs
%bcond_with	rplay		# with internal sound support (through rplay)
#
%include	/usr/lib/rpm/macros.perl
Summary:	An improved version of the FVWM X-based window manager
Summary(de):	F(?) Virtual Window Manager
Summary(es):	Administrador de ventanas semejante al mwm
Summary(fr):	F(?) Virtual Window Manager
Summary(ja):	������ FVWM - X �ѥ�����ɥ��ޥ͡�����
Summary(pl):	Ulepszona wersja zarz�dcy okien FVWM
Summary(pt_BR):	Gerenciador de janelas semelhante ao mwm
Summary(ru):	����������� ������� �������� F(?)
Summary(tr):	Yayg�n bir pencere denetleyicisi
Name:		fvwm2
Version:	2.5.16
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	ftp://ftp.fvwm.org/pub/fvwm/version-2/fvwm-%{version}.tar.bz2
# Source0-md5:	78eb609bd913868f659034173292b9bd
Source1:	fvwm-2.0.46.icons.tar.gz
# Source1-md5:	8d81420cf49442fca4bb2b61ae54eeb9
Source2:	%{name}.desktop
Source3:	%{name}-system.%{name}rc.tar.gz
# Source3-md5:	22c1f6c5ab4bd84376daa37debd3e889
Source4:	%{name}.RunWM
Source5:	mozilla.xpm
Source6:	%{name}-xsession.desktop
Patch0:		%{name}-paths.patch
Patch1:		FvwmPager.patch
Patch2:		%{name}-locale_names.patch
Patch3:		%{name}-varia.patch
URL:		http://www.fvwm.org/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_fribidi:BuildRequires:	fribidi-devel}
%{?with_gnome:BuildRequires:	gnome-libs-devel}
BuildRequires:	gtk+-devel
BuildRequires:	libpng-devel
%{?with_stroke:BuildRequires:	libstroke-devel}
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/fvwm2
%define		_wmpropsdir	/usr/share/wm-properties

%description
FVWM2 (the F stands for whatever you want, but the VWM stands for
Virtual Window Manager) is an improved version of the FVWM window
manager for the X Window System and shares the same characteristics as
FVWM.

%description -l es
Fvwm2 es una versi�n del popular administrador de ventanas "Feeble
Virtual Window Manager".

%description -l ja
FVWM2 (F�Ϲ����ʤ褦�˲�ᤷ�Ƥ����������������� VWM �� Virtual Window
Manager ���ά������ΤǤ���)�� FVWM ��Ʊ����ħ����� ���˳�ĥ���줿 X
Window System �ѥ�����ɥ��ޥ͡�����Ǥ���

%description -l pl
FVWM (za F mo�na sobie podstawi� co kto woli, lecz VWM pochodzi od
pierwszych liter "Virtual Window Manager", czyli wirtualny zarz�dca
okien) to ulepszona wersja zarz�dcy okien dla systemu X Window FVWM i
posiadaj�ca te same cechy.

%description -l pt_BR
Fvwm2 � uma vers�o do popular gerenciador de janelas "Feeble Virtual
Window Manager".

%description -l ru
fvwm2 - ��� ������ ����������� "Feeble Virtual Window Manager".

%package icons
Summary:	Graphic files used by the FVWM and FVWM2 window managers
Summary(de):	Symbole und Pixmaps f�r fvwm
Summary(fr):	Ic�nes et pixmaps pour fvwm
Summary(pl):	Pliki graficzne u�ywane przez zarz�dc�w okien FVWM i FVWM2
Summary(ru):	����������� � ��������� �������� ��� fvwm2
Summary(tr):	Fvwm i�in �e�itli minik g�r�nt� ve simgeler
Group:		X11/Window Managers
Obsoletes:	fvwm95-icons

%description icons
This package contains icons, bitmaps and pixmaps for fvwm and fvwm2.

%description icons -l de
Dieses Paket enth�lt Symbole, Bitmaps und Pixmaps f�r fvwm und fvwm2.

%description icons -l fr
Ce package contient des icones, bitmaps et pixmaps pour fvwm et fvwm2.

%description icons -l pl
Ten pakiet zawiera ikony, bitmapy i pixmapy dla fvwm i fvwm2.

%description icons -l ru
���� ����� �������� ����������� � ������ �������� ��� fvwm2.

%description icons -l tr
Fvwm i�in �e�itli minik g�r�nt� ve simgeler.

%package perl
Summary:	fvwm-perllib, FvwmPerl and dependent modules
Summary(pl):	fvwm-perllib, FvwmPerl i zale�ne modu�y
Group:		X11/Window Managers/Tools
Requires:	%{name} = %{version}-%{release}

%description perl
fvwm-perllib, FvwmPerl and dependent modules.

%description perl -l pl
fvwm-perllib, FvwmPerl i zale�ne modu�y.

%prep
%setup -n fvwm-%{version} -q -a1 -a3
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

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

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d \
	$RPM_BUILD_ROOT{%{_sysconfdir},/etc/sysconfig/wmstyle,%{_wmpropsdir}} \
	$RPM_BUILD_ROOT{%{_datadir}/{locale,xsessions},%{_pixmapsdir}/mini}

install system.fvwm2rc $RPM_BUILD_ROOT%{_sysconfdir}/system.fvwm2rc
install fvwm2.menu.m4 $RPM_BUILD_ROOT%{_sysconfdir}

install icons/*.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

mv $RPM_BUILD_ROOT%{_pixmapsdir}/mini-*.xpm \
	$RPM_BUILD_ROOT%{_pixmapsdir}/mini

# Conflicts with wmmaker
mv $RPM_BUILD_ROOT%{_pixmapsdir}/xv{,-fvwm}.xpm

install %{SOURCE2} $RPM_BUILD_ROOT%{_wmpropsdir}
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/%{name}.sh
install %{SOURCE5} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop
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
%attr(755,root,root) /etc/sysconfig/wmstyle/*.sh
%attr(755,root,root) %{_bindir}/[!f]*
%attr(755,root,root) %{_bindir}/fvwm
%attr(755,root,root) %{_bindir}/fvwm2
%attr(755,root,root) %{_bindir}/fvwm-[!p]*
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
%{_wmpropsdir}/fvwm2.desktop
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
