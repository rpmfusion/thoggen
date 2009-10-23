Summary: DVD backup utility
Name: thoggen
Version: 0.7.1
Release: 4%{?dist}
License: GPLv2+
Group: Applications/Multimedia
URL: http://thoggen.net/
Source: http://downloads.sf.net/thoggen/thoggen-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: gstreamer-plugins-good
Requires: gstreamer-plugins-ugly
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: perl(XML::Parser)
BuildRequires: gtk2-devel
BuildRequires: libglade2-devel
BuildRequires: gstreamer-devel >= 0.10.14
BuildRequires: gstreamer-plugins-base-devel >= 0.10.14
BuildRequires: hal-devel >= 0.5.7
BuildRequires: dbus-glib-devel >= 0.71
BuildRequires: libdvdread-devel
# The videobox plugin is here
BuildRequires: gstreamer-plugins-good
# The mpeg2dec plugin is here
BuildRequires: gstreamer-plugins-ugly

%description
Thoggen is a DVD backup utility ('DVD ripper') for Linux, based on GStreamer
and Gtk+.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}
# Extra gettext files...
%find_lang thoggen_iso_639
%{__cat} thoggen_iso_639.lang >> %{name}.lang
# Remove installed docs which we include as %%doc here
%{__rm} -rf %{buildroot}%{_docdir}/thoggen/
desktop-file-install --vendor="" \
  --add-category="X-AudioVideoImport" \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/thoggen.desktop

%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/thoggen
%{_datadir}/applications/thoggen.desktop
%{_datadir}/pixmaps/thoggen.png
%{_datadir}/thoggen/
%{_mandir}/man1/thoggen.1*


%changelog
* Fri Oct 23 2009 Orcan Ogetbil <oged[DOT]fedora[AT]gmail[DOT]com> - 0.7.1-4
- Update desktop file according to F-12 FedoraStudio feature

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.7.1-3
- rebuild for new F11 features

* Sat Oct 18 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.7.1-2
- rebuild for RPM Fusion

* Tue Jul  1 2008 Matthias Saou <http://freshrpms.net/> 0.7.1-1
- Update to 0.7.1.

* Sun May 18 2008 Matthias Saou <http://freshrpms.net/> 0.7.0-1
- Initial RPM release.

