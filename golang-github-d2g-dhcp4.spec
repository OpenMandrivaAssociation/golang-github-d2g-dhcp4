# http://github.com/d2g/dhcp4
%global goipath         github.com/d2g/dhcp4
%global commit          a1d1b6c41b1ce8a71a5121a9cee31809c4707d9c

%gometa

Name:           %{goname}
Version:        0
Release:        0.10%{?dist}
Summary:        DHCP4 library written in Go
# Detected licences
# - BSD (3 clause) at 'LICENSE'
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup
cp %{SOURCE1} %{SOURCE2} .

%install
%goinstall glide.lock glide.yaml

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Thu Nov 15 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.10.20181115gita1d1b6c
- Bump to commit a1d1b6c41b1ce8a71a5121a9cee31809c4707d9c

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.9.20150413gitf0e4d29
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitf0e4d29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.7.20150413gitf0e4d29
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.6.20150413gitf0e4d29
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gitf0e4d29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitf0e4d29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitf0e4d29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitf0e4d29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.1.gitf0e4d29
- First package for Fedora
  resolves: #1410390
