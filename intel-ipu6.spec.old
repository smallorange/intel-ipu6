Name:           intel-ipu6-kmod-common
Summary:        Binaries for Intel IPU6
Version:        0.0.1
Release:        2%{?dist}
License:        Proprietory

URL:            https://github.com/smallorange
Source0:        %{url}/ipu6-camera-bins/releases/download/%{version}/ipu6-camera-bins-%{version}.tar.xz
Source1:        %{url}/ivsc-firmware/releases/download/%{version}/ivsc-firmware-%{version}.tar.xz

BuildRequires:  systemd-rpm-macros
# For kmod package
Provides:       %{name}-kmod-common = %{version}-%{release}

BuildArch:      noarch

%description
This provides the necessary firmwares for Intel IPU6, including IPU6 itself
and iVSC.

This package contains the binary firmware for %{name}.

%prep

%setup -q -D -c -a 1

echo "xxx"
cp ivsc-firmware-%{version}/LICENSE ./

%build
# Nothing to build

%install
# IPU6 firmwares
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6/lib/firmware/intel/ipu6_fw.bin %{buildroot}%{_prefix}/lib/firmware/intel/ipu6_fw.bin
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6ep/lib/firmware/intel/ipu6ep_fw.bin %{buildroot}%{_prefix}/lib/firmware/intel/ipu6ep_fw.bin

#iVSC firmwares
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_pkg_ovti5678_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti5678_0_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_skucfg_ovti2740_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti2740_0_1_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_pkg_ovti9738_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti9738_0_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_pkg_ovti2740_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti2740_0_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_skucfg_ovti02c1_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti02c1_0_1_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_fw.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_fw_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_pkg_ovti01af_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti01af_0_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_skucfg_ovti01a0_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti01a0_0_1_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_skucfg_ovti9734_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti9734_0_1_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_skucfg_hi556_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_hi556_0_1_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_pkg_ovti01as_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti01as_0_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_skucfg_ovti9738_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti9738_0_1_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_skucfg_ovti5678_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti5678_0_1_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_pkg_ovti02c1_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti02c1_0_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_skucfg_ovti01as_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti01as_0_1_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_skucfg_ovti01af_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti01af_0_1_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_pkg_himx11b1_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_himx11b1_0_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_pkg_ovti9734_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti9734_0_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_pkg_hi556_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_hi556_0_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_pkg_ovti01a0_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti01a0_0_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_skucfg_himx11b1_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_himx11b1_0_1_a1_prod.bin

%files
%license LICENSE
# IPU6 firmware
%{_prefix}/lib/firmware/intel/ipu6_fw.bin
%{_prefix}/lib/firmware/intel/ipu6ep_fw.bin

#iVSC firmware
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti5678_0_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti2740_0_1_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti9738_0_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti2740_0_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti02c1_0_1_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_fw_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti01af_0_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti01a0_0_1_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti9734_0_1_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_hi556_0_1_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti01as_0_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti9738_0_1_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti5678_0_1_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti02c1_0_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti01as_0_1_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti01af_0_1_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_himx11b1_0_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti9734_0_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_hi556_0_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti01a0_0_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_himx11b1_0_1_a1_prod.bin


%changelog
* Tue Oct 25 2022 Kate Hsuan <hpa@redhat.com> - 0.0.1
- First commit
