Name:       rocksdb
Version:    5.7.3
Release:    2%{?dist}
Summary:    A Persistent Key-Value Store for Flash and RAM Storage

License:    BSD
URL:        https://github.com/facebook/rocksdb.git

BuildRequires:    gtest-devel

Source0:    https://github.com/facebook/rocksdb/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:     rocksdb-5.2.1-install_path.patch

%description
Rocksdb is a library that forms the core building block for a fast key value
server, especially suited for storing data on flash drives. It has a
Log-Structured-Merge-Database (LSM) design with flexible trade offs between
Write-Amplification-Factor (WAF), Read-Amplification-Factor (RAF) and
Space-Amplification-Factor (SAF). It has multithreaded compaction, making it
specially suitable for storing multiple terabytes of data in a single database.

%package devel
Summary: Development files for rocksdb
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for rocksdb


%prep
%setup -q

%patch0 -p1 -b .install_path

rm -rf third-party/gtest-1.7.0
rm java/benchmark/src/main/java/org/rocksdb/benchmark/DbBenchmark.java
rm build_tools/gnu_parallel


%build
export CFLAGS="%{optflags}"
export EXTRA_CXXFLAGS=" -std=c++11 %{optflags}"
make %{?_smp_mflags} shared_lib

%install
make install-shared \
         INSTALL_PREFIX=%{buildroot}\
         LIB_INSTALL_DIR=%{_libdir}\
         INCLUDE_INSTALL_DIR=%{_includedir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%{_libdir}/librocksdb.so.5
%{_libdir}/librocksdb.so.5.7
%{_libdir}/librocksdb.so.5.7.3
%license COPYING


%files devel
%{_libdir}/librocksdb.so
%{_includedir}/*

%changelog
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 26 2017 Matej Mužila <mmuzila@redhat.com> - 5.7.3-1
- Update to version 5.7.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jan 24 2017 Matej Muzila <mmuzila@redhat.com> 5.2.1-1
- Packaged rocksdb

