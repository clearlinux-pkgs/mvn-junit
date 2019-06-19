#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-junit
Version  : 3.8.1
Release  : 2
URL      : https://repo1.maven.org/maven2/junit/junit/3.8.1/junit-3.8.1.jar
Source0  : https://repo1.maven.org/maven2/junit/junit/3.8.1/junit-3.8.1.jar
Source1  : https://repo1.maven.org/maven2/junit/junit/3.8.1/junit-3.8.1.pom
Source2  : https://repo1.maven.org/maven2/junit/junit/3.8.2/junit-3.8.2.pom
Source3  : https://repo1.maven.org/maven2/junit/junit/4.11/junit-4.11.jar
Source4  : https://repo1.maven.org/maven2/junit/junit/4.11/junit-4.11.pom
Source5  : https://repo1.maven.org/maven2/junit/junit/4.12/junit-4.12.jar
Source6  : https://repo1.maven.org/maven2/junit/junit/4.12/junit-4.12.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : CPL-1.0
Requires: mvn-junit-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-junit package.
Group: Data

%description data
data components for the mvn-junit package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/junit/t/3.8.1
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/junit/t/3.8.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/junit/t/3.8.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/junit/t/3.8.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/junit/t/3.8.2
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/junit/t/3.8.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/junit/t/4.11
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/junit/t/4.11

mkdir -p %{buildroot}/usr/share/java/.m2/repository/junit/t/4.11
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/junit/t/4.11

mkdir -p %{buildroot}/usr/share/java/.m2/repository/junit/t/4.12
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/junit/t/4.12

mkdir -p %{buildroot}/usr/share/java/.m2/repository/junit/t/4.12
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/junit/t/4.12


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/junit/t/3.8.1/junit-3.8.1.jar
/usr/share/java/.m2/repository/junit/t/3.8.1/junit-3.8.1.pom
/usr/share/java/.m2/repository/junit/t/3.8.2/junit-3.8.2.pom
/usr/share/java/.m2/repository/junit/t/4.11/junit-4.11.jar
/usr/share/java/.m2/repository/junit/t/4.11/junit-4.11.pom
/usr/share/java/.m2/repository/junit/t/4.12/junit-4.12.jar
/usr/share/java/.m2/repository/junit/t/4.12/junit-4.12.pom
