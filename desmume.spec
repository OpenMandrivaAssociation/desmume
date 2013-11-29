%define		longname	DeSmuME

Summary:	A Nintendo DS emulator
Name:		desmume
Version:	0.9.10
Release:	1
License:	GPLv2+
Group:		Emulators
Url:		http://desmume.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source10:	%{name}-48.png
Patch0:		desmume-0.9.10-no-return-for-void.patch
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	recode
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtkglext-1.0)
BuildRequires:	pkgconfig(libagg)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pcap-devel
Obsoletes:	wx%{name} < 0.9.10

%description
DeSmuME is a Nintendo DS emulator running homebrew demos and commercial 
games... For the latter ones, you should own the games corresponding the 
roms you play with.

You can find a compatibility list here : http://desmume.org/?page_id=15

In this package is the GTK GUI version.

%files
%doc AUTHORS ChangeLog README README.LIN
%attr(0755,root,root) %{_bindir}/%{name}
%{_iconsdir}/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/desmume.1.*
%{_datadir}/pixmaps/DeSmuME.xpm

#----------------------------------------------------------------------------

%package -n %{name}-glade
Summary:	A Nintendo DS emulator (Glade GUI version)
Group:		Emulators

%description -n %{name}-glade
DeSmuME is a Nintendo DS emulator running homebrew demos and commercial 
games... For the latter ones, you should own the games corresponding the 
roms you play with.

You can find a compatibility list here : http://desmume.org/?page_id=15

In this package is the GTK/Glade version, which includes a translation.

%files -n %{name}-glade -f %{name}.lang
%doc AUTHORS ChangeLog README README.LIN
%attr(0755,root,root) %{_bindir}/%{name}-glade
%{_datadir}/%{name}
%{_iconsdir}/%{name}-glade.png
%{_datadir}/applications/%{name}-glade.desktop
%{_mandir}/man1/desmume-glade.1.*

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
%doc AUTHORS ChangeLog README README.LIN
%attr(0755,root,root) %{_bindir}/%{name}-cli
%{_mandir}/man1/desmume-cli.1.*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
recode l1..u8 AUTHORS ChangeLog
perl -pi -e 's|\r\n|\n|g' AUTHORS ChangeLog
find src -name *.[ch]* -exec chmod 644 {} +

%build
./autogen.sh
%configure2_5x \
	--enable-wifi \
	--enable-glade
%make

%install
%makeinstall_std

#glade files
install -d -m 755 %{buildroot}/%{_datadir}/%{name}
install -m 644 src/gtk-glade/glade/* %{buildroot}/%{_datadir}/%{name}

#icons
install -d -m 755 %{buildroot}/%{_iconsdir}
install -m 644 %{SOURCE10} %{buildroot}/%{_iconsdir}/%{name}.png
install -m 644 %{SOURCE10} %{buildroot}/%{_iconsdir}/%{name}-glade.png

#xdg menus
desktop-file-install --vendor="" \
 --remove-category="Application" \
 --remove-key="Version" \
 --add-category="X-MandrivaLinux-MoreApplications-Emulators" \
 --add-category="Emulator" \
 --dir=%{buildroot}%{_datadir}/applications \
 %{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-install --vendor="" \
 --remove-category="Application" \
 --remove-key="Version" \
 --add-category="X-MandrivaLinux-MoreApplications-Emulators" \
 --add-category="Emulator" \
 --dir=%{buildroot}%{_datadir}/applications \
 %{buildroot}%{_datadir}/applications/%{name}-glade.desktop

%find_lang %{name}

