Summary:	Jabber/XMPP client library
Summary(pl.UTF-8):	Biblioteka klienta Jabber/XMPP
Name:		gloox
Version:	1.0
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://camaya.net/download/%{name}-%{version}.tar.bz2
# Source0-md5:	f8eacf1c6476e0a309b453fd04f90e31
URL:		http://camaya.net/gloox
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnutls-devel
BuildRequires:	iksemel-devel
BuildRequires:	libidn-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gloox is a full-featured Jabber/XMPP client without GUI, written in
C++ and implemented as a shared library.

%description -l pl.UTF-8
gloox jest pełnym clienten Jabbera/XMPP, bez interfejsu graficznego.
Napisany został w C++ i zaimplementowany jako biblioteka dzielona.

%package devel
Summary:	gloox header files
Summary(pl.UTF-8):	Pliki nagłówkowe gloox
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnutls-devel
Requires:	iksemel-devel
Requires:	libidn-devel
Requires:	zlib-devel

%description devel
Header files for gloox library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gloox.

%package static
Summary:	gloox static library
Summary(pl.UTF-8):	Statyczna biblioteka gloox
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
gloox static library.

%description static -l pl.UTF-8
Statyczna biblioteka gloox.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
%attr(755,root,root) %{_libdir}/libgloox.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgloox.so.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gloox-config
%attr(755,root,root) %{_libdir}/libgloox.so
%{_libdir}/libgloox.la
%{_includedir}/gloox
%{_pkgconfigdir}/gloox.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
