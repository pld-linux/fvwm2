Summary: An improved version of the FVWM X-based window manager.
Name: fvwm2
Version: 2.2
Release: 5
Source0: ftp://ftp.fvwm.org/pub/fvwm/version-2/fvwm-2.2.tar.gz
Source1: fvwm-2.0.46.icons.tar.gz
Source2: compat-icons.tar.gz
Patch0: fvwm-2.2-redhat.patch
Copyright: GPL
Group: User Interface/Desktops
Buildroot: /var/tmp/fvwm2-root
Requires: fvwm2-icons
Url: http://fvwm.math.uh.edu/
Obsoletes: fvwm95

%description
FVWM2 (the F stands for whatever you want, but the VWM stands for
Virtual Window Manager) is an improved version of the FVWM window
manager for the X Window System and shares the same characteristics as
FVWM.  

Install the fvwm2 package if you'd like to use the FVWM2 window manager.
If you install fvwm2, you'll also need to install fvwm2-icons.

%package icons
Summary: Graphic files used by the FVWM and FVWM2 window managers.
Group: User Interface/Desktops
Obsoletes: fvwm95-icons

%description icons
The fvwm2-icons package contains icons, bitmaps and pixmaps used by
the FVWM and FVWM2 X Window System window managers.  

You'll need to install fvwm2-icons if you are installing fvwm and/or
fvwm2.

%prep
%setup -n fvwm-%{version} -q
%patch0 -p1 -b .redhat

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=/usr/X11R6 --enable-extras \
	--libexecdir=\${prefix}/lib/X11/fvwm2	\
	--sysconfdir=/etc/X11/fvwm2
make 

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr/X11R6 \
	sysconfdir=$RPM_BUILD_ROOT/etc/X11/fvwm2 \
	INSTALL_PROGRAM="/usr/bin/install -c -s"
mkdir -p $RPM_BUILD_ROOT/etc/X11/fvwm2
install -m 644 sample.fvwmrc/system.fvwm2rc $RPM_BUILD_ROOT/etc/X11/fvwm2
rm -rf $RPM_BUILD_ROOT/usr/share/icons
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/mini
install -m 644 icons/*.xpm $RPM_BUILD_ROOT/usr/share/icons
mv $RPM_BUILD_ROOT/usr/share/icons/mini.*.xpm $RPM_BUILD_ROOT/usr/share/icons/mini
# install compatibility icons
tar xvzf $RPM_SOURCE_DIR/compat-icons.tar.gz -C $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc INSTALL README AUTHORS INSTALL.fvwm NEWS ChangeLog
%doc docs
/usr/X11R6/lib/X11/fvwm2
/usr/X11R6/man/man1/*
/usr/X11R6/bin/*
%dir /etc/X11/fvwm2
%config /etc/X11/fvwm2/*

%files icons
%defattr(-,root,root)
%dir /usr/share/icons
%dir /usr/share/icons/mini
/usr/share/icons/*.xpm
/usr/share/icons/mini/*.xpm

%clean
rm -rf $RPM_BUILD_ROOT
