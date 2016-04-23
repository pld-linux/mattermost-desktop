# TODO
# - based on atom-electron, build our own?
# - lang tag locales

Summary:	Mattermost Desktop application
Name:		mattermost-desktop
Version:	1.1.1
Release:	0.1
License:	MIT
Group:		X11/Applications
# Source0Download: https://github.com/mattermost/desktop/releases
Source0:	https://github.com/mattermost/desktop/releases/download/v%{version}/%{name}-%{version}-linux-x64.tar.gz
# Source0-md5:	1d01e6b7b5dc40e8ffbcd07667576f39
URL:		https://github.com/mattermost/desktop
BuildRequires:	rpmbuild(macros) >= 1.596
ExclusiveArch:	%{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_prefix}/lib/%{name}

%description
Native desktop application for Mattermost

%prep
%setup -q -n mattermost-desktop-%{version}-linux-x64

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_appdir},%{_desktopdir},%{_pixmapsdir}}

cp -a . $RPM_BUILD_ROOT%{_appdir}
%{__rm} $RPM_BUILD_ROOT%{_appdir}/{LICENSE,LICENSES.chromium.html}

ln -s %{_appdir}/Mattermost $RPM_BUILD_ROOT%{_bindir}/mattermost

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE LICENSES.chromium.html
%attr(755,root,root) %{_bindir}/mattermost
%dir %{_appdir}
%{_appdir}/version
%{_appdir}/*.bin
%{_appdir}/content_shell.pak
%{_appdir}/icudtl.dat
%attr(755,root,root) %{_appdir}/Mattermost
%attr(755,root,root) %{_appdir}/libgcrypt.so.11
%attr(755,root,root) %{_appdir}/libnode.so
%attr(755,root,root) %{_appdir}/libffmpeg.so

%{_appdir}/locales

%dir %{_appdir}/resources
%{_appdir}/resources/app
%{_appdir}/resources/atom.asar
