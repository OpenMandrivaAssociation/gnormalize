%define version	0.63
%define release	%mkrel 3

Name: 		gnormalize
Summary:	A ripper, an encoder and an audio converter
Version:	%{version}
Release:	%{release}
Group:		Sound
License:	GPLv2+
URL:		http://gnormalize.sourceforge.net
Source0:	http://kent.dl.sourceforge.net/sourceforge/gnormalize/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch
Requires:	normalize, cdparanoia
Requires:	vorbis-tools

%description
gnormalize is a front end to normalize, a ripper, an encoder and
an audio converter. It uses gtk2-perl.

gnormalize decodes the MP3/MPC/OGG/APE/FLAC file to WAV,
then normalizes the WAV to a targeted volume level and re-encodes it.
gnormalize can also rip, encode, convert audio format between MP3,
MPC, OGG, APE and FLAC, change the encoding and ID3 tag properties of
final normalized files.


%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

# We don't need to install Audio-CD*.tar.gz and CDDB_get*.tar.gz.
# Because mdk has the rpm packages: perl-CDDB_get, perl-Audio-CD.

# Install gnormalize
mkdir -p %{buildroot}%{_bindir}
	cp -vf gnormalize %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%name/animations
	cp -vf animations/*.gif %{buildroot}%{_datadir}/%name/animations/
	cp -vf README %{buildroot}%{_datadir}/%name/


# menu entrie

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Gnormalize
Comment=A ripper, an encoder and an audio converter
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;Audio;AudioVideoEditing;
EOF

mkdir -p %{buildroot}%{_iconsdir} %{buildroot}%{_miconsdir} %{buildroot}%{_liconsdir}
install -m 644 icons/%{name}-48.png  $RPM_BUILD_ROOT/%{_liconsdir}/%{name}.png
install -m 644 icons/%{name}-32.png  $RPM_BUILD_ROOT/%{_iconsdir}/%{name}.png
install -m 644 icons/%{name}-16.png  $RPM_BUILD_ROOT/%{_miconsdir}/%{name}.png


%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc README
%{_bindir}/*
%{_datadir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%name.png
%{_iconsdir}/%name.png
%{_liconsdir}/%name.png




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.63-3mdv2011.0
+ Revision: 619183
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.63-2mdv2010.0
+ Revision: 429264
- rebuild

* Sun Jul 13 2008 Funda Wang <fwang@mandriva.org> 0.63-1mdv2009.0
+ Revision: 234334
- update to new version 0.63

* Wed Jun 25 2008 Funda Wang <fwang@mandriva.org> 0.62-1mdv2009.0
+ Revision: 228840
- update to new version 0.62

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed May 28 2008 Funda Wang <fwang@mandriva.org> 0.61-1mdv2009.0
+ Revision: 212513
- New version 0.61

* Sat May 03 2008 Funda Wang <fwang@mandriva.org> 0.60-1mdv2009.0
+ Revision: 200619
- New version 0.60

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 05 2007 Jérôme Soyer <saispo@mandriva.org> 0.53-1mdv2008.1
+ Revision: 115738
- New release 0.53


* Tue Dec 05 2006 Lenny Cartier <lenny@mandriva.com> 0.52-1mdv2007.0
+ Revision: 90779
- Update to 0.52
- Import gnormalize

