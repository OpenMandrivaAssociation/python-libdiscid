%global debug_package %{nil}

# set to nil when packaging a release, 
# or the long commit tag for the specific git branch
%global commit_tag %{nil}

# set with the commit date only if commit_tag not nil 
# git version (i.e. master) in format date +Ymd
%if "%{commit_tag}" != "%{nil}"
%global commit_date %(git show -s --date=format:'%Y%m%d' %{commit_tag})
%endif

# repack non-release git branches as .xz with the commit date
# in the following format <name>-<version>-<commit_date>.xz

Name:           python-libdiscid
Version:        2.0.3
Release:        %{?commit_date:~0.%{commit_date}.}2
Summary:        cython based Python bindings for libdiscid
Group:          Multimedia
License:        MIT
URL:            https://github.com/sebastinas/python-libdiscid

# change the source URL depending on if the package is a release version or a git version
%if "%{commit_tag}" != "%{nil}"
Source0:        https://github.com/<org_name>/<project_name>/archive/%{commit_tag}.tar.gz#/%{name}-%{version}.xz
%else
Source0:        %url/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif

BuildSystem:    python
BuildRequires:  python-cython
BuildRequires:  pkgconfig(libdiscid)
BuildRequires:  pkgconfig(python)

%description
Python-discid implements Python bindings for MusicBrainz Libdiscid. 

%files
%license LICENSE
%doc README.md
%{python_sitearch}/libdiscid
%{python_sitearch}/python_libdiscid-%version.dist-info

