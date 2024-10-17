%define name xd3d
%define version 8.3.1
%define release 7
# Don't support by g95
%define _ssp_cflags %nil
%define Werror_cflags %nil
# kept g95 option even if the compilation is made with gfortran
%define g95flags %( echo %optflags | sed 's/-mtune=[^ ]*//' )

Summary: A simple scientific visualization tool
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: GPL
Group: Sciences/Other
Url: https://www.cmap.polytechnique.fr/~jouve/xd3d/
BuildRequires: gcc-gfortran
BuildRequires: libxpm-devel
Buildrequires: pkgconfig(x11)
BuildRequires: pkgconfig(zlib)

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
perl -pi -e 's!^COMPILF =.*!COMPILF = gfortran!' RULES
perl -pi -e 's!\$\(COMPILF\) \$\(OPTF\) -o!\$(COMPILF) \$(OPTF) %ldflags -o!' RULES

%build
make

%install
mkdir -p %buildroot%_bindir

make install INSTALL_DIR=%buildroot%_bindir

%files
%doc CHANGELOG BUGS FORMATS README
%doc Examples Manuals
%_bindir/*
