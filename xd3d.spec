%define name xd3d
%define version 8.3.1
%define release %mkrel 6
# Don't support by g95
%define _ssp_cflags %nil
%define Werror_cflags %nil
%define g95flags %( echo %optflags | sed 's/-mtune=[^ ]*//' )

Summary: A simple scientific visualization tool
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: GPL
Group: Sciences/Other
Url: http://www.cmap.polytechnique.fr/~jouve/xd3d/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: g95
BuildRequires: libxpm-devel
Buildrequires: libx11-devel
BuildRequires: zlib-devel

%description
Xd3d is a simple scientific visualization tool designed to be easy to learn.
It can plot 2d and 3d meshes, with shadowing, contour plots, vector fields,
iso-contour (3d), as well as 3d surfaces z=f(x,y) defined by an algebraic
expression or a cloud of points. It generates high quality vector PostScript
files for scientific publications and still or animated bitmap images. It
includes the graph plotter xgraphic.

%prep
%setup -q

perl -pi -e "s!^XD3D_DIR =.*!XD3D_DIR = `pwd`!" RULES
perl -pi -e 's!^INSTALL_DIR =.*!INSTALL_DIR = %_bindir!' RULES
perl -pi -e 's!^OPTC =.*!OPTC = %g95flags!' RULES
perl -pi -e 's!^OPTF =.*!OPTF = %g95flags!' RULES
perl -pi -e 's!^LIBX11 =.*!LIBX11 = %_libdir!' RULES
perl -pi -e 's!^COMPILF =.*!COMPILF = g95!' RULES
perl -pi -e 's!\$\(COMPILF\) \$\(OPTF\) -o!\$(COMPILF) \$(OPTF) %ldflags -o!' RULES

%build
make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p %buildroot%_bindir

make install INSTALL_DIR=%buildroot%_bindir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGELOG BUGS FORMATS README
%doc Examples Manuals
%_bindir/*

