Summary:	GNU Find Utilities (find, xargs)
Name:		findutils
Version:	4.4.2
Release:	4
Epoch:		1
License:	GPL
Group:		Applications/File
# development versions at ftp://alpha.gnu.org/gnu/findutils/
Source0:	ftp://ftp.gnu.org/gnu/findutils/%{name}-%{version}.tar.gz
# Source0-md5:	351cc4adb07d54877fa15f75fb77d39f
URL:		http://www.gnu.org/software/findutils/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The findutils package contains programs which will help you locate
files on your system. The find utility searches through a hierarchy of
directories looking for files which match a certain set of criteria
(such as a filename pattern). The locate utility searches a database
(create by updatedb) to quickly find a file matching a given pattern.
The xargs utility builds and executes command lines from standard
input arguments (usually lists of file names generated by the find
command).

%prep
%setup -q

%build
%{__aclocal} -I gnulib/m4 -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# unpackaged locate
rm -f $RPM_BUILD_ROOT%{_bindir}/{locate,updatedb} \
	$RPM_BUILD_ROOT%{_libdir}/{bigram,code,frcode} \
	$RPM_BUILD_ROOT%{_mandir}/{,*/}man?/{locate.1,updatedb.1,locatedb.5}*

rm -f $RPM_BUILD_ROOT{%{_infodir}/dir,%{_mandir}/README.findutils-non-english-man-pages}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README TODO ChangeLog
%attr(755,root,root) %{_bindir}/find
%attr(755,root,root) %{_bindir}/xargs
%{_mandir}/man1/[fx]*
%{_infodir}/find.info*

