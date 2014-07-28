Name:           ros-hydro-korg-nanokontrol
Version:        0.1.2
Release:        0%{?dist}
Summary:        ROS korg_nanokontrol package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/korg_nanokontrol
Source0:        %{name}-%{version}.tar.gz

Requires:       pygame-devel
Requires:       ros-hydro-rospy
Requires:       ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-catkin

%description
ROS driver to use the Kork NanoKontrol MIDI device as a joystick.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon Jul 28 2014 Austin Hendrix <namniart@gmail.com> - 0.1.2-0
- Autogenerated by Bloom

