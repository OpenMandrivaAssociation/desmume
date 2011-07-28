Name:			desmume
%define longname	DeSmuME
Version:		0.9.7
Release:		%mkrel 1

Summary:	A Nintendo DS emulator
License:	GPLv2+
Group:		Emulators
URL:		http://desmume.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source10:	%{name}-48.png

BuildRequires:	gtk2-devel
BuildRequires:	libglade2.0-devel
BuildRequires:	gtkglext-devel
BuildRequires:	wxgtku2.8-devel
BuildRequires:	agg-devel
BuildRequires:	pcap-devel
BuildRequires:	desktop-file-utils
BuildRequires:	recode
BuildRequires:	intltool
BuildRequires:	libSDL-devel
BuildRequires:	libz-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%package -n %{name}-glade
Summary:	A Nintendo DS emulator (Glade GUI version)
Group:		Applications/Emulators
License:	GPLv2+

%package -n %{name}-cli
Summary:	A Nintendo DS emulator (CLI version)
Group:		Applications/Emulators
License:	GPLv2+

%package -n wx%{name}
Summary:	A Nintendo DS emulator (wxWidgets GUI version)
Group:		Applications/Emulators
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
recode l1..u8 AUTHORS ChangeLog
perl -pi -e 's|\r\n|\n|g' AUTHORS ChangeLog
find src -name *.[ch]* -exec chmod 644 {} +

%build
./autogen.sh
%configure2_5x --enable-wifi --enable-wxwidgets
#--enable-openal --enable-osmesa
%make

%install
rm -rf %{buildroot}
%makeinstall

#glade files
install -d -m 755 %{buildroot}/%{_datadir}/%{name}
install -m 644 src/gtk-glade/glade/* %{buildroot}/%{_datadir}/%{name}

#icons
install -d -m 755 %{buildroot}/%{_iconsdir}
install -m 644 %{SOURCE10} %{buildroot}/%{_iconsdir}/%{name}.png
install -m 644 %{SOURCE10} %{buildroot}/%{_iconsdir}/%{name}-glade.png
install -m 644 %{SOURCE10} %{buildroot}/%{_iconsdir}/wx%{name}.png

#rm -rf %{buildroot}/%{_datadir}/pixmaps

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

%if %mdkversion<200900
%post
%{update_menus}

%post -n %{name}-glade
%{update_menus}

%post -n wx%{name}
%{update_menus}

%postun
%{clean_menus}

%postun -n %{name}-glade
%{clean_menus}

%postun -n wx%{name}
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README README.LIN
%attr(0755,root,root) %{_bindir}/%{name}
%{_iconsdir}/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/desmume.1.*
%{_datadir}/pixmaps/DeSmuME.xpm

%files -n %{name}-glade -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README README.LIN
%attr(0755,root,root) %{_bindir}/%{name}-glade
%{_datadir}/%{name}
%{_iconsdir}/%{name}-glade.png
%{_datadir}/applications/%{name}-glade.desktop
%{_mandir}/man1/desmume-glade.1.*

%files -n %{name}-cli
%defattr(-,root,root)
%doc AUTHORS ChangeLog README README.LIN
%attr(0755,root,root) %{_bindir}/%{name}-cli
%{_mandir}/man1/desmume-cli.1.*

%files -n wx%{name}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README README.LIN
%attr(0755,root,root) %{_bindir}/wx%{name}
%{_iconsdir}/wx%{name}.png
%{_datadir}/applications/wx%{name}.desktop


%clean
rm -rf %{buildroot}

