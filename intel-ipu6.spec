Name:           intel-ipu6-kmod-common
Summary:        Metadata package for IPU6 camera support
Version:        0.0
Release:        2%{?dist}
License:        Proprietary
URL:            https://github.com/intel/ipu6-drivers

BuildRequires:  systemd-rpm-macros

Requires:       kernel(x86-64) > 5.19.17-200
Requires:       icamerasrc
Requires:       akmod-intel-ipu6

BuildArch:      noarch

%description
This is the metadata package for IPU6 camera support.

%files

%changelog
* Tue Feb 7 2023 Kate Hsuan <hpa@redhat.com> - 0.0-2
- Update dependency

* Tue Oct 25 2022 Kate Hsuan <hpa@redhat.com> - 0.0.1
- First commit
