Summary:	An improved version of the FVWM X-based window manager
Summary(de):	F(?) Virtual Window Manager
Summary(es):	Administrador de ventanas semejante al mwm
Summary(fr):	F(?) Virtual Window Manager
Summary(ja):	≤˛Œ…»« FVWM - X Õ—•¶•£•Û•…•¶•ﬁ•Õ°º•∏•„
Summary(tr):	Yayg˝n bir pencere denetleyicisi
Summary(pl):	Ulepszona wersja zarz±dcy okien FVWM
Summary(pt_BR):	Gerenciador de janelas semelhante ao mwm
Summary(ru):	˜…“‘’¡ÃÿŒŸ  œÀœŒŒŸ  Õ≈Œ≈ƒ÷≈“ F(?)
Name:		fvwm2
Version:	2.5.0
Release:	2
License:	GPL
Group:		X11/Window Managers
Source0:	ftp://ftp.fvwm.org/pub/fvwm/version-2/fvwm-%{version}.tar.bz2
Source1:	fvwm-2.0.46.icons.tar.gz
Source2:	%{name}.desktop
Source3:	%{name}-system.%{name}rc.tar.gz
Source4:	%{name}.RunWM
Source5:	%{name}.wm_style
Patch0:		%{name}-paths.patch
Patch1:		%{name}-ac.patch
URL:		http://www.fvwm.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	fvwm2-icons
Requires:	wmconfig >= 0.9.10-6
Requires:	m4
Requires:	xinitrc >= 3.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	readline-devel >= 4.2
Obsoletes:	fvwm95

%define		_sysconfdir	/etc/X11/fvwm2
%define		_wmpropsdir	%{_datadir}/wm-properties

%description
FVWM2 (the F stands for whatever you want, but the VWM stands for
Virtual Window Manager) is an improved version of the FVWM window
manager for the X Window System and shares the same characteristics as
FVWM.

%description -l es
Fvwm2 es una versiÛn del popular administrador de ventanas "Feeble
Virtual Window Manager".

%description -l ja
FVWM2 (F§œπ•§≠§ §Ë§¶§À≤Úº·§∑§∆§Ø§¿§µ§§°£§ø§¿§∑°¢ VWM §œ Virtual Window
Manager §Úæ Œ¨§∑§ø§‚§Œ§«§π°£)§œ FVWM §»∆±§∏∆√ƒß§Úª˝§¡ ππ§À≥»ƒ•§µ§Ï§ø X
Window System Õ—•¶•£•Û•…•¶•ﬁ•Õ°º•∏•„§«§π°£

%description -l pl
FVWM (za F moøna sobie podstawic co kto woli, lecz VWM pochodzi od
pierwszych liter "Virtual Window Manager", czyli wirtualny zarz±dca
okien) to ulepszona wersja zarz±dcy okien dla systemu X Window FVWM i
posiadaj±ca te same cechy.

%description -l pt_BR
Fvwm2 È uma vers„o do popular gerenciador de janelas "Feeble Virtual
Window Manager".

%description -l ru
fvwm2 - ‹‘œ ◊≈“”…— –œ–’Ã—“Œœ«œ "Feeble Virtual Window Manager".

%package icons
Summary:	Graphic files used by the FVWM and FVWM2 window managers
Summary(de):	Symbole und Pixmaps f¸r fvwm
Summary(fr):	IcÙnes et pixmaps pour fvwm
Summary(pl):	Pliki graficzne uøywane przez zarz±dcÛw okien FVWM i FVWM2
Summary(ru):	…À‘œ«“¡ÕÕŸ … “¡”‘“œ◊Ÿ≈ À¡“‘…ŒÀ… ƒÃ— fvwm2
Summary(tr):	Fvwm iÁin Áe˛itli minik gˆr¸nt¸ ve simgeler
Group:		X11/Window Managers
Obsoletes:	fvwm95-icons

%description icons
This package contains icons, bitmaps and pixmaps for fvwm and fvwm2.

%description icons -l de
Dieses Paket enth‰lt Symbole, Bitmaps und Pixmaps f¸r fvwm und fvwm2.

%description icons -l fr
Ce package contient des icones, bitmaps et pixmaps pour fvwm et fvwm2.

%description icons -l pl
Ten pakiet zawiera ikony, bitmapy i pixmapy dla fvwm i fvwm2.

%description icons -l ru
¸‘œ‘ –¡À≈‘ ”œƒ≈“÷…‘ –…À‘œ«“¡ÕÕŸ … –“œﬁ…≈ À¡“‘…ŒÀ… ƒÃ— fvwm2.

%description icons -l tr
Fvwm iÁin Áe˛itli minik gˆr¸nt¸ ve simgeler.

%prep
%setup -n fvwm-%{version} -q -a1 -a3
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__automake}
%{__autoconf}
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions" \
%configure \
	--disable-package-subdirs \
	--disable-dmalloc \
	--disable-efence \
	--disable-debug-msgs \
	--disable-command-log \
	--enable-multibyte \
	--enable-shape \
	--disable-gnome \
	--enable-sm \
	--disable-xinerama \
	--with-xpm-library \
	--with-rplay-library \
	--with-stroke-library \
	--with-ncurses-library \
	--with-readline-library \
	--with-ncurses-library \
	--with-gnome

touch *
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

mv -f $RPM_BUILD_ROOT%{_datadir}/wm-properties{,_}
install -d $RPM_BUILD_ROOT%{_wmpropsdir}
mv -f $RPM_BUILD_ROOT{%{_datadir}/wm-properties_,%{_wmpropsdir}/fvwm2.desktop}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS NEWS
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
