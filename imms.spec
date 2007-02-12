Summary:        Intelligent playlist plugin for XMMS and BMP
Summary(pl.UTF-8):   Inteligenta wtyczka listy odtwarzania dla XMMS-a i BMP
Name:		imms
Version:	2.1.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/imms/%{name}-%{version}.tar.bz2
# Source0-md5:	e5423b073974daafd051cecf1b6d9472
URL:		http://www.luminal.org/phpwiki/index.php/IMMS
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bmp-devel >= 0.7
BuildRequires:	id3lib-devel >= 3.8.0
BuildRequires:	libtool
BuildRequires:	pcre-devel
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	sqlite3-devel >= 3.0
BuildRequires:	xmms-devel >= 1.2.0
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
IMMS is an intelligent playlist plug-in for XMMS and BMP that tracks
your listening patterns and adapts itself to your taste.

%description -l pl.UTF-8
IMMS to inteligentna wtyczka listy odtwarzania dla XMMS-a i BMP,
śledząca przesłuchiwane pliki, a następnie adaptująca się do gustu
słuchacza.

%package -n bmp-%{name}
Summary:	Intelligent playlist plugin for BMP
Summary(pl.UTF-8):   Inteligenta wtyczka listy odtwarzania dla BMP
Group:		X11/Applications/Multimedia
Requires:	bmp

%description -n bmp-%{name}
IMMS is an intelligent playlist plug-in for BMP that tracks your
listening patterns and adapts itself to your taste.

%description -n bmp-%{name} -l pl.UTF-8
IMMS to inteligentna wtyczka listy odtwarzania dla BMP, śledząca
przesłuchiwane pliki, a następnie adaptująca się do gustu słuchacza.

%package -n xmms-%{name}
Summary:	Intelligent playlist plugin for XMMS
Summary(pl.UTF-8):   Inteligenta wtyczka listy odtwarzania dla XMMS-a
Group:		X11/Applications/Multimedia
Requires:	xmms

%description -n xmms-%{name}
IMMS is an intelligent playlist plug-in for XMMS that tracks your
listening patterns and adapts itself to your taste.

%description -n xmms-%{name} -l pl.UTF-8
IMMS to inteligentna wtyczka listy odtwarzania dla XMMS-a, śledząca
przesłuchiwane pliki, a następnie adaptująca się do gustu słuchacza.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{xmms_general_plugindir} \
	$RPM_BUILD_ROOT%{_libdir}/bmp/General

install build/libxmmsimms.so $RPM_BUILD_ROOT%{xmms_general_plugindir}
install build/libbmpimms.so $RPM_BUILD_ROOT%{_libdir}/bmp/General

%clean
rm -rf $RPM_BUILD_ROOT

%files -n xmms-%{name}
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{xmms_general_plugindir}/*.so

%files -n bmp-%{name}
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/bmp/General/*.so
