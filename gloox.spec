Summary:	Jabber/XMPP client library
Summary(pl):	Biblioteka klienta Jabber/XMPP
Name:		gloox
Version:	0.8
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://camaya.net/download/%{name}-%{version}.tar.bz2
# Source0-md5:	fc595ff8d468d2f4ebd73139494ea32c
URL:		http://camaya.net/gloox
BuildRequires:	gnutls-devel
BuildRequires:	iksemel-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gloox is a full-featured Jabber/XMPP client without GUI, written in
C++ and implemented as a shared library.

%package devel
Summary:	gloox header files
Summary(pl):	Pliki nag³ówkowe gloox
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for gloox library.

%description devel -l pl
Pliki nag³ówkowe biblioteki gloox.

%package static
Summary:	gloox static library
Summary(pl):	Statyczna biblioteka gloox
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
gloox static library.

%description static -l pl
Statyczna biblioteka gloox.

%prep
%setup -q

%build
#cp -f /usr/share/automake/config.* .
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_pkgconfigdir}/*
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_bindir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
