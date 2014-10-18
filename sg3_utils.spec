Summary:	Utilities and test programs for the Linux sg version 3 device driver
Name:		sg3_utils
Version:	1.39
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://sg.danny.cz/sg/p/%{name}-%{version}.tgz
# Source0-md5:	cab917b6406ef0337b499a4fce8a38f8
URL:		http://sg.danny.cz/sg/
Requires:	%{name} = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains some utilities and test programs for the Linux
sg (version 3) device driver. This driver is found in the Linux 2.4+
kernels.

%package libs
Summary:	sgutils2 library
License:	BSD
Group:		Libraries

%description libs
sgutils2 library.

%package devel
Summary:	Header files for sgutils2 library
License:	BSD
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for sgutils2 library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING COVERAGE CREDITS ChangeLog README README.sg_start
%attr(755,root,root) %{_bindir}/s*
%{_mandir}/man8/s*.8*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libsgutils2.so.?
%attr(755,root,root) %{_libdir}/libsgutils2.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsgutils2.so
%{_libdir}/libsgutils2.la
%{_includedir}/scsi/sg_*.h

