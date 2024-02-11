# see m4/${libname}.m4 />= for required version of particular library
%define		libbfio_ver		20201125
%define		libcdata_ver		20220115
%define		libcerror_ver		20120425
%define		libcfile_ver		20160409
%define		libclocale_ver		20120425
%define		libcnotify_ver		20120425
%define		libcpath_ver		20180716
%define		libcsplit_ver		20120701
%define		libcthreads_ver		20160404
%define		libfcache_ver		20191109
%define		libfdata_ver		20201129
%define		libfvalue_ver		20200711
%define		libuna_ver		20210801
Summary:	Python 2 bindings for libvmdk library
Summary(pl.UTF-8):	Wiązania Pythona 2 do biblioteki libvmdk
Name:		python-pyvmdk
Version:	20221124
Release:	1
License:	LGPL v3+
Group:		Libraries/Python
#Source0Download: https://github.com/libyal/libvmdk/releases
Source0:	https://github.com/libyal/libvmdk/releases/download/%{version}/libvmdk-alpha-%{version}.tar.gz
# Source0-md5:	c61f05d917f4634a40c92613ce1de7f8
URL:		https://github.com/libyal/libvmdk/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.21
BuildRequires:	libbfio-devel >= %{libbfio_ver}
BuildRequires:	libcdata-devel >= %{libcdata_ver}
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libcfile-devel >= %{libcfile_ver}
BuildRequires:	libclocale-devel >= %{libclocale_ver}
BuildRequires:	libcnotify-devel >= %{libcnotify_ver}
BuildRequires:	libcpath-devel >= %{libcpath_ver}
BuildRequires:	libcsplit-devel >= %{libcsplit_ver}
BuildRequires:	libcthreads-devel >= %{libcthreads_ver}
BuildRequires:	libfcache-devel >= %{libfcache_ver}
BuildRequires:	libfdata-devel >= %{libfdata_ver}
BuildRequires:	libfvalue-devel >= %{libfvalue_ver}
BuildRequires:	libfuse-devel >= 2.6
BuildRequires:	libuna-devel >= %{libuna_ver}
BuildRequires:	libtool >= 2:2
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	zlib-devel >= 1.2.5
Requires:	libbfio >= %{libbfio_ver}
Requires:	libcerror >= %{libcerror_ver}
Requires:	libvmdk >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 bindings for libvmdk library.

%description -l pl.UTF-8
Wiązania Pythona 2 do biblioteki libvmdk.

%prep
%setup -q -n libvmdk-%{version}

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-python2 \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# keep only python2 module
%{__rm} $RPM_BUILD_ROOT%{_bindir}/vmdk*
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/libvmdk*
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvmdk.*
%{__rm} $RPM_BUILD_ROOT%{_pkgconfigdir}/libvmdk.pc
%{__rm} -r $RPM_BUILD_ROOT%{_mandir}/man[13]

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/pyvmdk.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{py_sitedir}/pyvmdk.so
