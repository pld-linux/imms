
%define		org_name	imms

Summary:	Intelligent playlist plug-in for XMMS
Summary(pl):	Inteligenta wtyczka listy odtwarzania dla XMMS-a
Name:		xmms-%{org_name}
Version:	0.7
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/%{org_name}/%{org_name}-%{version}.tar.gz
URL:		http://www.luminal.org/phpwiki/index.php/IMMS
BuildRequires:	id3lib-devel >= 3.8.0
BuildRequires:	xmms-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IMMS is an intelligent playlist plug-in for XMMS that tracks your
listening patterns and adapts itself to your taste.

%description -l pl
IMMS to inteligentna wtyczka listy odtwarzania dla XMMS-a, ¶ledz±ca
przes³uchiwane pliki, a nastêpnie adaptuj±ca siê do gustu s³uchacza.

%prep
%setup -q -n %{org_name}-%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/xmms/General

install libimms.so $RPM_BUILD_ROOT%{_libdir}/xmms/General

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/xmms/General/*.so
