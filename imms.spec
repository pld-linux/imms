
%define		org_name	imms

Summary:	Intelligent playlist plug-in for XMMS
Summary(pl):	Inteligenta wtyczka listy odtwarzania dla XMMS-a
Name:		xmms-%{org_name}
Version:	0.7.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/%{org_name}/%{org_name}-%{version}.tar.bz2
# Source0-md5:	e939204eda6b815f6386c6d44e2422a8
URL:		http://www.luminal.org/phpwiki/index.php/IMMS
BuildRequires:	id3lib-devel >= 3.8.0
BuildRequires:	xmms-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		xmmsplugindir	%(xmms-config --general-plugin-dir)

%description
IMMS is an intelligent playlist plug-in for XMMS that tracks your
listening patterns and adapts itself to your taste.

%description -l pl
IMMS to inteligentna wtyczka listy odtwarzania dla XMMS-a, ¶ledz±ca
przes³uchiwane pliki, a nastêpnie adaptuj±ca siê do gustu s³uchacza.

%prep
%setup -q -n %{org_name}-%{version}a

%build
%{__make} \
	CFLAGS="%{rpmcflags} `xmms-config --cflags` -MMD -ansi -Wall -pedantic -D_GNU_SOURCE"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{xmmsplugindir}

install libimms.so $RPM_BUILD_ROOT%{xmmsplugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{xmmsplugindir}/*.so
