
%define		org_name	imms

Summary:	Intelligent playlist plug-in for XMMS
Summary(pl):	Inteligenta wtyczka listy odtwarzania dla XMMS-a
Name:		xmms-%{org_name}
Version:	0.9.9
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/%{org_name}/%{org_name}-%{version}.tar.bz2
# Source0-md5:	729930cac26a8155415fa208cbe2f723
URL:		http://www.luminal.org/phpwiki/index.php/IMMS
BuildRequires:	autoconf
BuildRequires:	id3lib-devel >= 3.8.0
BuildRequires:	pcre-devel
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	sqlite-devel
BuildRequires:	xmms-devel >= 1.2.0
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IMMS is an intelligent playlist plug-in for XMMS that tracks your
listening patterns and adapts itself to your taste.

%description -l pl
IMMS to inteligentna wtyczka listy odtwarzania dla XMMS-a, �ledz�ca
przes�uchiwane pliki, a nast�pnie adaptuj�ca si� do gustu s�uchacza.

%prep
%setup -q -n %{org_name}-%{version}

%build
%{__autoconf}
%{__autoheader}

%configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{xmms_general_plugindir}

install libimms.so $RPM_BUILD_ROOT%{xmms_general_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{xmms_general_plugindir}/*.so
