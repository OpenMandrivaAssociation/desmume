%define		date		20211027
%define		longname	DeSmuME

Summary:	A Nintendo DS emulator
Name:		desmume
%if 0%{?date}
Version:	0.9.12
Release:	0.%{date}.1
%else
Version:	0.9.11
Release:	1
%endif
License:	GPLv2+
Group:		Emulators
Url:		http://desmume.org/
# Upstream recommends not using stable releases - see http://desmume.org/download/
Source0:	https://github.com/TASVideos/desmume/archive/refs/heads/master.tar.gz
Source10:	%{name}-48.png
Patch0:		desmume-formatstring.patch
#Patch1:		desmume-compile.patch
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	recode
BuildRequires:	meson
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(libpcap)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(soundtouch)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtkglext-1.0)
BuildRequires:	pkgconfig(libagg)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gl)
%rename %{name}-glade

%description
DeSmuME is a Nintendo DS emulator running homebrew demos and commercial 
games... For the latter ones, you should own the games corresponding the 
roms you play with.

You can find a compatibility list here : http://desmume.org/?page_id=15

In this package is the GUI version.

%files
%doc desmume/AUTHORS desmume/ChangeLog desmume/README desmume/README.LIN
%attr(0755,root,root) %{_bindir}/%{name}
%{_datadir}/icons/*/*/*/org.desmume.DeSmuME.svg
%{_datadir}/metainfo/org.desmume.DeSmuME.metainfo.xml
%{_datadir}/applications/*.desktop
%{_mandir}/man1/desmume.1*

#----------------------------------------------------------------------------

%package -n %{name}-cli
Summary:	A Nintendo DS emulator (CLI version)
Group:		Emulators

%description -n %{name}-cli
DeSmuME is a Nintendo DS emulator running homebrew demos and commercial 
games... For the latter ones, you should own the games corresponding the 
roms you play with.

You can find a compatibility list here : http://desmume.org/?page_id=15

In this package is the CLI version (without a GUI).

%files -n %{name}-cli
%doc desmume/AUTHORS desmume/ChangeLog desmume/README desmume/README.LIN
%attr(0755,root,root) %{_bindir}/%{name}-cli
%{_mandir}/man1/desmume-cli.1*

#----------------------------------------------------------------------------

%prep
%if 0%{?date}
%autosetup -p0 -n %{name}-master
%else
%autosetup -p1
%endif
recode l1..u8 %{name}/AUTHORS %{name}/ChangeLog
perl -pi -e 's|\r\n|\n|g' %{name}/AUTHORS %{name}/ChangeLog
find . -name *.[ch]* -exec chmod 644 {} +

# FIXME as of 2021/10/27, crashes on startup when
# built with clang
export CC=gcc
export CXX=g++

cd desmume/src/frontend/posix
%meson \
	-Dopenal=true \
	-Dfrontend-gtk=true \
	-Dfrontend-cli=true \
	-Dwifi=true \
	-Dgdb-stub=true

%build
%ninja_build -v -C desmume/src/frontend/posix/build

%install
%ninja_install -C desmume/src/frontend/posix/build
