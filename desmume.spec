%define		longname	DeSmuME

Name:		desmume
Version:	0.9.8
Release:	%mkrel 1
Summary:	A Nintendo DS emulator
License:	GPLv2+
Group:		Emulators
URL:		http://desmume.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source10:	%{name}-48.png
# Add missing in .tar.gz sources in patch
Patch0:		desmume-0.9.8-missing.patch
BuildRequires:	gtk2-devel
BuildRequires:	libglade2.0-devel
BuildRequires:	gtkglext-devel
BuildRequires:	wxgtku2.8-devel
BuildRequires:	agg-devel
BuildRequires:	pcap-devel
BuildRequires:	desktop-file-utils
BuildRequires:	recode
BuildRequires:	intltool
BuildRequires:	SDL-devel
BuildRequires:	zlib-devel

%package -n %{name}-glade
Summary:	A Nintendo DS emulator (Glade GUI version)
Group:		Emulators
License:	GPLv2+

%package -n %{name}-cli
Summary:	A Nintendo DS emulator (CLI version)
Group:		Emulators
License:	GPLv2+

%package -n wx%{name}
Summary:	A Nintendo DS emulator (wxWidgets GUI version)
Group:		Emulators
License:	GPLv2+

%description
DeSmuME is a Nintendo DS emulator running homebrew demos and commercial 
games... For the latter ones, you should own the games corresponding the 
roms you play with.

You can find a compatibility list here : http://desmume.org/?page_id=15

In this package is the GTK GUI version.

%description -n %{name}-glade
DeSmuME is a Nintendo DS emulator running homebrew demos and commercial 
games... For the latter ones, you should own the games corresponding the 
roms you play with.

You can find a compatibility list here : http://desmume.org/?page_id=15

In this package is the GTK/Glade version, which includes a translation.

%description -n %{name}-cli
DeSmuME is a Nintendo DS emulator running homebrew demos and commercial 
games... For the latter ones, you should own the games corresponding the 
roms you play with.

You can find a compatibility list here : http://desmume.org/?page_id=15

In this package is the CLI version (without a GUI).

%description -n wx%{name}
DeSmuME is a Nintendo DS emulator running homebrew demos and commercial
games... For the latter ones, you should own the games corresponding the
roms you play with.

You can find a compatibility list here : http://desmume.org/?page_id=15

In this package is the wxWidgets version.

%prep
%setup -q
%patch0 -p1
recode l1..u8 AUTHORS ChangeLog
%__perl -pi -e 's|\r\n|\n|g' AUTHORS ChangeLog
find src -name *.[ch]* -exec %__chmod 644 {} +

%build
./autogen.sh
%configure2_5x --enable-wifi --enable-wxwidgets
#--enable-openal --enable-osmesa
%make

%install
%__rm -rf %{buildroot}
%makeinstall

#glade files
%__install -d -m 755 %{buildroot}/%{_datadir}/%{name}
%__install -m 644 src/gtk-glade/glade/* %{buildroot}/%{_datadir}/%{name}

#icons
%__install -d -m 755 %{buildroot}/%{_iconsdir}
%__install -m 644 %{SOURCE10} %{buildroot}/%{_iconsdir}/%{name}.png
%__install -m 644 %{SOURCE10} %{buildroot}/%{_iconsdir}/%{name}-glade.png
%__install -m 644 %{SOURCE10} %{buildroot}/%{_iconsdir}/wx%{name}.png

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

desktop-file-install --vendor="" \
 --remove-category="Application" \
 --remove-key="Version" \
 --add-category="X-MandrivaLinux-MoreApplications-Emulators" \
 --add-category="Emulator" \
 --dir=%{buildroot}%{_datadir}/applications \
 %{buildroot}%{_datadir}/applications/wx%{name}.desktop

%find_lang %{name}

%clean
%__rm -rf %{buildroot}

%files
%doc AUTHORS ChangeLog README README.LIN
%attr(0755,root,root) %{_bindir}/%{name}
%{_iconsdir}/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/desmume.1.*
%{_datadir}/pixmaps/DeSmuME.xpm

%files -n %{name}-glade -f %{name}.lang
%doc AUTHORS ChangeLog README README.LIN
%attr(0755,root,root) %{_bindir}/%{name}-glade
%{_datadir}/%{name}
%{_iconsdir}/%{name}-glade.png
%{_datadir}/applications/%{name}-glade.desktop
%{_mandir}/man1/desmume-glade.1.*

%files -n %{name}-cli
%doc AUTHORS ChangeLog README README.LIN
%attr(0755,root,root) %{_bindir}/%{name}-cli
%{_mandir}/man1/desmume-cli.1.*

%files -n wx%{name}
%doc AUTHORS ChangeLog README README.LIN
%attr(0755,root,root) %{_bindir}/wx%{name}
%{_iconsdir}/wx%{name}.png
%{_datadir}/applications/wx%{name}.desktop



%changelog
* Tue Apr 10 2012 Andrey Bondrov <abondrov@mandriva.org> 0.9.8-1
+ Revision: 790269
- New version 0.9.8

* Fri Jul 29 2011 Andrey Bondrov <abondrov@mandriva.org> 0.9.7-1
+ Revision: 692166
- Fix group
- Fix man pages compression issue
- imported package desmume


* Thu Jul 21 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 0.9.7-1mdv2011.0
- New version 0.9.7

* Tue May 25 2010 Guillaume Bedot <littletux@zarb.org> 0.9.6-2plf2010.1
- build also wx gui

* Thu May 20 2010 Guillaume Bedot <littletux@zarb.org> 0.9.6-1plf2010.1
- 0.9.6

* Sat Sep  5 2009 Guillaume Bedot <littletux@zarb.org> 0.9.4-1plf2010.0
- 0.9.4

* Mon May 18 2009 Guillaume Bedot <littletux@zarb.org> 0.9.2-2plf2010.0
- fix buildrequires

* Mon May 18 2009 Guillaume Bedot <littletux@zarb.org> 0.9.2-1plf2009.1
- 0.9.2-1

* Mon Jan  5 2009 Guillaume Bedot <littletux@zarb.org> 0.9-1plf2009.1
- 0.9

* Wed Apr 23 2008 Guillaume Bedot <littletux@zarb.org> 0.8-1plf2009.0
- 0.8

* Tue Aug 14 2007 Guillaume Bedot <littletux@zarb.org> 0.7.3-1plf2008.0
- Release 0.7.3, with a french translation for desmume-glade

* Thu Jul 11 2007 Guillaume Bedot <littletux@zarb.org> 0.7.2-1plf2008.0
- RMLL release

* Thu Jun 21 2007 Guillaume Bedot <littletux@zarb.org> 0.7.1-1plf2008.0
- Release 0.7.1

* Mon May 14 2007 Guillaume Bedot <littletux@zarb.org> 0.7.0-1plf2008.0
- Release 0.7.0
- New menu item
- Aiglx / Gui warning

* Wed Mar 21 2007 Guillaume Bedot <littletux@zarb.org> 0.6.0-2plf2007.1
- Fix all glade paths

* Wed Mar 21 2007 Guillaume Bedot <littletux@zarb.org> 0.6.0-1plf2007.1
- First PLF package

