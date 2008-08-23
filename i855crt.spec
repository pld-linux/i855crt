Summary:	intel 855GM crt video out driver
Name:		i855crt
Version:	0.4
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/sourceforge/i855crt/%{name}-%{version}.tar.gz
Patch0:		%{name}-Makefile.patch
# Source0-md5:	6522fa9b261be53c366ba153876fcc83
URL:		http://i855crt.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
i855crt is an userspace driver for linux that can enable the crt out (port
for external monitor) on i855GM based laptop.

%prep
%setup -q
%patch0 -p1
# clean binaries:
%{__make} clean

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	OPTLDFLAGS="-lX11 -lXv -lXext"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}}

install i855crt $RPM_BUILD_ROOT%{_bindir}
install i855crt.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG README TODO
%attr(644,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/i855crt.conf
%attr(755,root,root) %{_bindir}/i855crt
