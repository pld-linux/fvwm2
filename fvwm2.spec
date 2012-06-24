Summary:	An improved version of the FVWM X-based window manager
Summary(de):	F(?) Virtual Window Manager
Summary(es):	Administrador de ventanas semejante al mwm
Summary(fr):	F(?) Virtual Window Manager
Summary(ja):	������ FVWM - X �ѥ�����ɥ��ޥ͡�����
Summary(tr):	Yayg�n bir pencere denetleyicisi
Summary(pt_BR):	Gerenciador de janelas semelhante ao mwm
Summary(ru):	����������� ������� �������� F(?)
Name:		fvwm2
Version:	2.4.3
Release:	2
License:	GPL
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fen�tres
Group(pl):	X11/Zarz�dcy Okien
URL:		http://www.fvwm.org/
Source0:	ftp://ftp.fvwm.org/pub/fvwm/version-2/fvwm-%{version}.tar.gz
Source1:	fvwm-2.0.46.icons.tar.gz
Source2:	%{name}.desktop
Source3:	%{name}-system.%{name}rc.tar.gz
Source4:	%{name}.RunWM
Source5:	%{name}.wm_style
Patch0:		%{name}-paths.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	fvwm2-icons
Requires:	wmconfig >= 0.9.10-6
Requires:	m4
Requires:	xinitrc >= 3.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	readline-devel >= 4.2
Obsoletes:	fvwm95

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/fvwm2
%define		_wmpropsdir	%{_datadir}/wm-properties

%description
FVWM2 (the F stands for whatever you want, but the VWM stands for
Virtual Window Manager) is an improved version of the FVWM window
manager for the X Window System and shares the same characteristics as
FVWM.

Install the fvwm2 package if you'd like to use the FVWM2 window
manager. If you install fvwm2, you'll also need to install
fvwm2-icons.

%description -l es
Fvwm2 es una versi�n del popular administrador de ventanas "Feeble
Virtual Window Manager".

%description -l ja
FVWM2 (F�Ϲ����ʤ褦�˲�ᤷ�Ƥ����������������� VWM �� Virtual Window
Manager ���ά������ΤǤ���)�� FVWM ��Ʊ����ħ����� ���˳�ĥ���줿 X
Window System �ѥ�����ɥ��ޥ͡�����Ǥ���

FVWM2 ������ɥ��ޥ͡��������Ѥ����硢 fvwm2
�ѥå������򥤥󥹥ȡ��� ���Ƥ��������� fvwm2
�ѥå������Υ��󥹥ȡ���ˤ� fvwm2-icons �ѥå����� ��ɬ�פǤ���

%description -l pl
FVWM (za F mo�na sobie podstawic co kto woli, lecz VWM pochodzi od
pierwszych liter "Virtual Window Manager", czyli wirtualnego mened�era
okien) to ulepszona wersja mened�era okien dla systemu X Window FVWM i
posiada te same cechy.

Nale�y zainstalowa� pakiet fvwm2 jesli chce si� uzywa� mened�era okien
FVWM2. Instaluj�c fvwm2 nalezy r�wniez zainstalowa� pakiet
fvwm2-icons.

%description -l pt_BR
Fvwm2 � uma vers�o do popular gerenciador de janelas "Feeble Virtual
Window Manager".

%description -l ru
fvwm2 - ��� ������ ����������� "Feeble Virtual Window Manager".

%package icons
Summary:	Graphic files used by the FVWM and FVWM2 window managers
Summary(de):	Symbole und Pixmaps f�r fvwm
Summary(fr):	Ic�nes et pixmaps pour fvwm
Summary(ru):	����������� � ��������� �������� ��� fvwm2
Summary(tr):	Fvwm i�in �e�itli minik g�r�nt� ve simgeler
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fen�tres
Group(pl):	X11/Zarz�dcy Okien
Obsoletes:	fvwm95-icons

%description icons
The fvwm2-icons package contains icons, bitmaps and pixmaps used by
the FVWM and FVWM2 X Window System window managers.

You'll need to install fvwm2-icons if you are installing fvwm and/or
fvwm2.

%description icons
This package contains icons, bitmaps and pixmaps for fvwm and fvwm2.

%description -l de icons
Dieses Paket enth�lt Symbole, Bitmaps und Pixmaps f�r fvwm und fvwm2.

%description -l fr icons
Ce package contient des icones, bitmaps et pixmaps pour fvwm et fvwm2.

%description icons -l ru
���� ����� �������� ����������� � ������ �������� ��� fvwm2.

%description -l tr icons
Fvwm i�in �e�itli minik g�r�nt� ve simgeler.

%prep
%setup -n fvwm-%{version} -q -a1 -a3
%patch0 -p1

%build
rm missing
aclocal
autoconf
automake -a -c
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions" \
%configure \
	--disable-package-subdirs \
	--disable-dmalloc \
	--disable-efence \
	--disable-debug-msgs \
	--disable-command-log \
	--enable-multibyte \
	--enable-shape \
	--enable-gnome \
	--enable-sm \
	--with-xpm-library \
	--with-rplay-library \
	--with-stroke-library \
	--with-readline-library \
	--with-ncurses-library \
	--with-gnome

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT{%{_sysconfdir}/{sysconfig/wmstyle,X11/fvwm2},%{_wmpropsdir}}
install -d $RPM_BUILD_ROOT{%{_sysconfdir},/etc/sysconfig/wmstyle}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install system.fvwm2rc $RPM_BUILD_ROOT%{_sysconfdir}
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

mv $RPM_BUILD_ROOT%{_datadir}/wm-properties{,_}
install -d $RPM_BUILD_ROOT%{_wmpropsdir}
mv $RPM_BUILD_ROOT{%{_datadir}/wm-properties_,%{_wmpropsdir}/fvwm2.desktop}

gzip -9fn README AUTHORS NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,AUTHORS,NEWS,ChangeLog}.gz
%doc docs
%dir /etc/X11/fvwm2
%config(noreplace) /etc/X11/fvwm2/*
%attr(755,root,root) /etc/sysconfig/wmstyle/*.sh
/etc/sysconfig/wmstyle/*.names
%attr(755,root,root) %{_libdir}/Fvwm*
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/fvwm
%{_datadir}/fvwm/*
%{_wmpropsdir}/fvwm2.desktop
%{_mandir}/man1/*

%files icons
%defattr(644,root,root,755)
%dir %{_datadir}/icons
%dir %{_datadir}/icons/mini
%{_datadir}/icons/*.xpm
%{_datadir}/icons/mini/*.xpm
