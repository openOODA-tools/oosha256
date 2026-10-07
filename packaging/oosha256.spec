Name:           oosha256
Version:        0.1.0
Release:        1%{?dist}
Summary:        Hardware-accelerated SHA-256 cryptographic digest generator and verifier.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oosha256
Source0:        oosha256-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oosha256 is a sovereign, capability-bounded SHA256 HASHER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oosha256
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oosha256-uninstall

%files
/usr/bin/oosha256
/usr/bin/oosha256-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
