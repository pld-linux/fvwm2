Summary:	An improved version of the FVWM X-based window manager.
Name:		fvwm2
Version:	2.2
Release:	6
Source0:	ftp://ftp.fvwm.org/pub/fvwm/version-2/fvwm-2.2.tar.gz
Source1:	fvwm-2.0.46.icons.tar.gz
Patch0:		fvwm-2.2-redhat.patch
Copyright:	GPL
Group:		User Interface/Desktops
Buildroot:	/tmp/%{name}-%{version}-root
Requires:	fvwm2-icons
Url:		http://fvwm.math.uh.edu/
Obsoletes:	fvwm95

%define		_prefix	/usr/X11R6
%define		_mandir	/usr/X11R6/man

%description
FVWM2 (the F stands for whatever you want, but the VWM stands for
Virtual Window Manager) is an improved version of the FVWM window
manager for the X Window System and shares the same characteristics as
FVWM.  

Install the fvwm2 package if you'd like to use the FVWM2 window manager.
If you install fvwm2, you'll also need to install fvwm2-icons.

%package icons
Summary:	Graphic files used by the FVWM and FVWM2 window managers.
Group:		User Interface/Desktops
Obsoletes:	fvwm95-icons

%description icons
The fvwm2-icons package contains icons, bitmaps and pixmaps used by
the FVWM and FVWM2 X Window System window managers.  

You'll need to install fvwm2-icons if you are installing fvwm and/or
fvwm2.

%prep
%setup -n fvwm-%{version} -q
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=%{_prefix} \
	--enable-extras \
	--libexecdir=\${prefix}/lib/X11/fvwm2	\
	--sysconfdir=/etc/X11/fvwm2 \
	--mandir=%{_mandir}
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/fvwm2

make install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	sysconfdir=$RPM_BUILD_ROOT/etc/X11/fvwm2 \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	INSTALL_PROGRAM="/usr/bin/install -c -s"

install -m 644 sample.fvwmrc/system.fvwm2rc $RPM_BUILD_ROOT/etc/X11/fvwm2
rm -rf $RPM_BUILD_ROOT/usr/share/icons
install -d $RPM_BUILD_ROOT%{_datadir}/icons/mini

install icons/*.xpm $RPM_BUILD_ROOT%{_datadir}/icons
mv $RPM_BUILD_ROOT%{_datadir}/icons/mini.*.xpm $RPM_BUILD_ROOT%{_datadir}/icons/mini

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
%dir %{_libdir}/X11/fvwm2
%attr(755,root,root) %{_libdir}/X11/fvwm2/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files icons
%defattr(644,root,root,755)
%dir %{_datadir}/icons
%dir %{_datadir}/icons/mini
%{_datadir}/icons/*.xpm
%{_datadir}/icons/mini/*.xpm
