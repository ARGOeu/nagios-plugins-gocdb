%define dir /usr/libexec/argo-monitoring/probes/fedcloud

Summary: Nagios plugins for EGI GOCDB
Name: nagios-plugins-gocdb
Version: 1.0.0
Release: 2%{?dist}
License: ASL 2.0
Group: Network/Monitoring
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install --directory ${RPM_BUILD_ROOT}%{dir}
install --mode 755 src/*  ${RPM_BUILD_ROOT}%{dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{dir}

%changelog
* Fri Feb 10 2017 Emir Imamagic <eimamagi@srce.hr> - 1.0.0-2%{?dist}
- Probes location aligned with guidelines
* Fri Sep 18 2015 Emir Imamagic <eimamagi@srce.hr> - 1.0.0-1%{?dist}
- Initial version based on nagios-gocdb-downtime
