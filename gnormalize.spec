%define version	0.53
%define release	%mkrel 1

Name: 		gnormalize
Summary:	A ripper, an encoder and an audio converter
Version:	%{version}
Release:	%{release}
Group:		Sound
License:	GPL
URL:		http://gnormalize.sourceforge.net
Source0:	%{name}-%{version}.tar.bz2
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


%post
%{update_menus}

%postun
%{clean_menus}

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


