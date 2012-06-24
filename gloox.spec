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
BuildRequires:	libidn-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gloox is a full-featured Jabber/XMPP client without GUI, written in
C++ and implemented as a shared library.

%description -l pl
gloox jest pe�nym clienten Jabbera/XMPP, bez interfejsu graficznego.
Napisany zosta� w C++ i zaimplementowany jako biblioteka dzielona.

%package devel
Summary:	gloox header files
Summary(pl):	Pliki nag��wkowe gloox
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnutls-devel
Requires:	iksemel-devel
Requires:	libidn-devel
Requires:	zlib-devel

%description devel
Header files for gloox library.

%description devel -l pl
Pliki nag��wkowe biblioteki gloox.

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
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
