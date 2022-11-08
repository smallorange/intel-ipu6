Name:           intel-ipu6-kmod-common
Summary:        Binaries for Intel IPU6
Version:        0.0.1
Release:        2%{?dist}
License:        Proprietory

URL:            https://github.com/smallorage
Source0:        %{url}/ipu6-drivers/releases/download/%{version}/ipu6-drivers-%{version}.tar.xz
Source1:        modules-load-d-intel-ipu6.conf

BuildRequires:  systemd-rpm-macros
# For kmod package
Provides:       %{name} = %{version}-%{release}

Requires:       kernel(x86-64) <= 5.19.17-200

BuildArch:      noarch

%description
This provides the module loading configurations for Intel IPU6.

This package contains the module configurations for %{name}.

%prep

%setup -q -D -c

%build
# Nothing to build

%install
install -D -m 0644 %{SOURCE1} %{buildroot}%{_modulesloaddir}/intel-ipu6.conf

%files
%{_modulesloaddir}/intel-ipu6.conf


%changelog
* Tue Oct 25 2022 Kate Hsuan <hpa@redhat.com> - 0.0.1
- First commit
