#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : qt-creator
Version  : 1
Release  : 1
URL      : file:///insilications/build/git-clr/qt-creator-clr.tar.gz
Source0  : file:///insilications/build/git-clr/qt-creator-clr.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.1
BuildRequires : ImageMagick-dev
BuildRequires : SDL2
BuildRequires : SDL2-dev
BuildRequires : Sphinx
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : Z3-dev
BuildRequires : Z3-staticdev
BuildRequires : acl
BuildRequires : acl-dev
BuildRequires : acl-staticdev
BuildRequires : alsa-lib-dev
BuildRequires : alsa-lib-lib
BuildRequires : alsa-tools
BuildRequires : binutils
BuildRequires : binutils-dev
BuildRequires : binutils-staticdev
BuildRequires : brotli
BuildRequires : brotli-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-meson
BuildRequires : buildreq-qmake
BuildRequires : bzip2
BuildRequires : bzip2-dev
BuildRequires : bzip2-staticdev
BuildRequires : ca-certs
BuildRequires : ca-certs-static
BuildRequires : cairo
BuildRequires : cairo-dev
BuildRequires : cairo-lib
BuildRequires : ccache
BuildRequires : clazy
BuildRequires : cmake
BuildRequires : cppcheck
BuildRequires : curl-dev
BuildRequires : dbus
BuildRequires : dbus-broker
BuildRequires : dbus-dev
BuildRequires : dbus-glib
BuildRequires : dbus-glib-dev
BuildRequires : dbus-python
BuildRequires : doxygen
BuildRequires : e2fsprogs-dev
BuildRequires : elfutils-dev
BuildRequires : evtest
BuildRequires : expat-dev
BuildRequires : expat-dev32
BuildRequires : expat-staticdev
BuildRequires : findutils
BuildRequires : fontconfig-data
BuildRequires : fontconfig-dev
BuildRequires : fontconfig-lib
BuildRequires : freetype-dev
BuildRequires : freetype-lib
BuildRequires : fribidi-dev
BuildRequires : gcc
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : gdb
BuildRequires : gdb-dev
BuildRequires : gettext
BuildRequires : glib
BuildRequires : glib-bin
BuildRequires : glib-data
BuildRequires : glib-dev
BuildRequires : glib-lib
BuildRequires : glibc
BuildRequires : glibc-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-lib-avx2
BuildRequires : glibc-libc32
BuildRequires : glibc-staticdev
BuildRequires : gmp
BuildRequires : gmp-dev
BuildRequires : gmp-staticdev
BuildRequires : gnutls
BuildRequires : gnutls-dev
BuildRequires : googletest
BuildRequires : googletest-dev
BuildRequires : graphite
BuildRequires : graphite-dev
BuildRequires : gsm-dev
BuildRequires : gtk+-data
BuildRequires : gtk+-lib
BuildRequires : gtk3-lib
BuildRequires : harfbuzz-dev
BuildRequires : harfbuzz-lib
BuildRequires : icu4c-lib
BuildRequires : jsoncpp
BuildRequires : jsoncpp-dev
BuildRequires : jsoncpp-lib
BuildRequires : keyutils
BuildRequires : keyutils-dev
BuildRequires : krb5
BuildRequires : krb5-dev
BuildRequires : libX11-data
BuildRequires : libX11-dev
BuildRequires : libX11-lib
BuildRequires : libXScrnSaver
BuildRequires : libXScrnSaver-dev
BuildRequires : libXScrnSaver-lib
BuildRequires : libXau-dev
BuildRequires : libXau-lib
BuildRequires : libXcursor-dev
BuildRequires : libXcursor-lib
BuildRequires : libXdamage-dev
BuildRequires : libXdamage-lib
BuildRequires : libXdmcp-dev
BuildRequires : libXdmcp-lib
BuildRequires : libXext-dev
BuildRequires : libXext-lib
BuildRequires : libXfont2-dev
BuildRequires : libXft-dev
BuildRequires : libXft-lib
BuildRequires : libXi-dev
BuildRequires : libXi-lib
BuildRequires : libXrender-dev
BuildRequires : libXrender-lib
BuildRequires : libXtst-dev
BuildRequires : libXtst-lib
BuildRequires : libXxf86vm-dev
BuildRequires : libXxf86vm-lib
BuildRequires : libarchive
BuildRequires : libarchive-dev
BuildRequires : libarchive-staticdev
BuildRequires : libatomic_ops-dev
BuildRequires : libatomic_ops-staticdev
BuildRequires : libcap
BuildRequires : libcap-dev
BuildRequires : libcap-ng-dev
BuildRequires : libconfig-dev
BuildRequires : libdrm
BuildRequires : libdrm-dev
BuildRequires : libdrm-lib
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libepoxy
BuildRequires : libepoxy-dev
BuildRequires : libffi
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libgcc1
BuildRequires : libgcrypt
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error
BuildRequires : libgpg-error-dev
BuildRequires : libidn2
BuildRequires : libidn2-dev
BuildRequires : libinput-data
BuildRequires : libinput-lib
BuildRequires : libinput-libexec
BuildRequires : libjpeg-turbo-dev
BuildRequires : libogg
BuildRequires : libogg-dev
BuildRequires : libpciaccess
BuildRequires : libpciaccess-dev
BuildRequires : libplacebo
BuildRequires : libplacebo-dev
BuildRequires : libpng-dev
BuildRequires : libpng-lib
BuildRequires : libstdc++
BuildRequires : libstdc++-dev
BuildRequires : libtasn1-dev
BuildRequires : libunistring-dev
BuildRequires : libunwind
BuildRequires : libunwind-dev
BuildRequires : libusb
BuildRequires : libusb-dev
BuildRequires : libva
BuildRequires : libva-dev
BuildRequires : libva-lib
BuildRequires : libvdpau
BuildRequires : libvdpau-dev
BuildRequires : libvorbis
BuildRequires : libvorbis-dev
BuildRequires : libwebp-dev
BuildRequires : libxcb-dev
BuildRequires : libxcb-lib
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : libxslt-bin
BuildRequires : llvm
BuildRequires : llvm-abi
BuildRequires : llvm-bin
BuildRequires : llvm-data
BuildRequires : llvm-dev
BuildRequires : llvm-lib
BuildRequires : llvm-libexec
BuildRequires : llvm-man
BuildRequires : llvm-staticdev
BuildRequires : lz4
BuildRequires : lz4-dev
BuildRequires : lz4-staticdev
BuildRequires : lzo
BuildRequires : lzo-dev
BuildRequires : lzo-staticdev
BuildRequires : md4c
BuildRequires : md4c-dev
BuildRequires : mediasdk-dev
BuildRequires : mesa
BuildRequires : mesa-dev
BuildRequires : mesa-lib
BuildRequires : mm-common-dev
BuildRequires : nasm
BuildRequires : nasm-bin
BuildRequires : ncurses-dev
BuildRequires : nettle
BuildRequires : nettle-dev
BuildRequires : ninja
BuildRequires : not-ffmpeg
BuildRequires : not-ffmpeg-dev
BuildRequires : numlockx
BuildRequires : nvidia
BuildRequires : nvidia-dev
BuildRequires : nvidia-lib
BuildRequires : opencl-headers
BuildRequires : opencl-headers-dev
BuildRequires : openjpeg-dev
BuildRequires : openssl
BuildRequires : openssl-dev
BuildRequires : openssl-lib
BuildRequires : openssl-staticdev
BuildRequires : orc-dev
BuildRequires : orc-staticdev
BuildRequires : p11-kit
BuildRequires : p11-kit-dev
BuildRequires : pacrunner
BuildRequires : pacrunner-dev
BuildRequires : pango-lib
BuildRequires : pcre-dev
BuildRequires : pcre-staticdev
BuildRequires : perl
BuildRequires : perl(XML::Parser)
BuildRequires : perl-Config-General
BuildRequires : perl-Config-Tiny
BuildRequires : perl-Crypt-SSLeay
BuildRequires : perl-DBI
BuildRequires : perl-DateTime-TimeZone
BuildRequires : perl-Encode-Locale
BuildRequires : perl-Error
BuildRequires : perl-File-Listing
BuildRequires : perl-HTML-Parser
BuildRequires : perl-HTML-Tagset
BuildRequires : perl-HTTP-Cookies
BuildRequires : perl-HTTP-Date
BuildRequires : perl-HTTP-Message
BuildRequires : perl-HTTP-Negotiate
BuildRequires : perl-IO-HTML
BuildRequires : perl-LWP-MediaTypes
BuildRequires : perl-LWP-Protocol-https
BuildRequires : perl-Params-Validate
BuildRequires : perl-Test-Simple
BuildRequires : perl-Try-Tiny
BuildRequires : perl-URI
BuildRequires : perl-XML-NamespaceSupport
BuildRequires : perl-XML-Parser
BuildRequires : perl-libwww-perl
BuildRequires : perl-man
BuildRequires : pixman
BuildRequires : pixman-dev
BuildRequires : pixman-lib
BuildRequires : pixman-staticdev
BuildRequires : pkg-config
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(32expat)
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(32ice)
BuildRequires : pkgconfig(32libsystemd)
BuildRequires : pkgconfig(32sm)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(Qt5Concurrent)
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5DBus)
BuildRequires : pkgconfig(Qt5Designer)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Help)
BuildRequires : pkgconfig(Qt5Location)
BuildRequires : pkgconfig(Qt5Multimedia)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5OpenGL)
BuildRequires : pkgconfig(Qt5Pdf)
BuildRequires : pkgconfig(Qt5PdfWidgets)
BuildRequires : pkgconfig(Qt5PrintSupport)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5QuickControls2)
BuildRequires : pkgconfig(Qt5QuickTest)
BuildRequires : pkgconfig(Qt5QuickWidgets)
BuildRequires : pkgconfig(Qt5Script)
BuildRequires : pkgconfig(Qt5Sensors)
BuildRequires : pkgconfig(Qt5SerialPort)
BuildRequires : pkgconfig(Qt5Sql)
BuildRequires : pkgconfig(Qt5Svg)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5WebChannel)
BuildRequires : pkgconfig(Qt5WebEngine)
BuildRequires : pkgconfig(Qt5WebEngineCore)
BuildRequires : pkgconfig(Qt5WebEngineWidgets)
BuildRequires : pkgconfig(Qt5WebSockets)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : pkgconfig(Qt5X11Extras)
BuildRequires : pkgconfig(Qt5Xml)
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(alsa-topology)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(dri)
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(expat)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(glesv1_cm)
BuildRequires : pkgconfig(glesv2)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmock)
BuildRequires : pkgconfig(gmock_main)
BuildRequires : pkgconfig(gtest)
BuildRequires : pkgconfig(gtest_main)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libpulse-simple)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(libunwind)
BuildRequires : pkgconfig(libunwind-coredump)
BuildRequires : pkgconfig(libunwind-generic)
BuildRequires : pkgconfig(libunwind-ptrace)
BuildRequires : pkgconfig(libunwind-setjmp)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : pkgconfig(osmesa)
BuildRequires : pkgconfig(samplerate)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(vulkan)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xatracker)
BuildRequires : pkgconfig(xcursor)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xinerama)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(xrandr)
BuildRequires : pkgconfig(xscrnsaver)
BuildRequires : pkgconfig(zlib)
BuildRequires : pulseaudio
BuildRequires : pulseaudio-dev
BuildRequires : python3
BuildRequires : python3-core
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : qca-qt5
BuildRequires : qca-qt5-dev
BuildRequires : qt3d
BuildRequires : qt3d-dev
BuildRequires : qt5ct
BuildRequires : qtbase
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtbase-extras
BuildRequires : qtcanvas3d
BuildRequires : qtcharts
BuildRequires : qtcharts-dev
BuildRequires : qtconnectivity
BuildRequires : qtconnectivity-dev
BuildRequires : qtdatavis3d
BuildRequires : qtdatavis3d-dev
BuildRequires : qtdeclarative
BuildRequires : qtdeclarative-dev
BuildRequires : qtgamepad
BuildRequires : qtgamepad-dev
BuildRequires : qtgraphicaleffects
BuildRequires : qtimageformats
BuildRequires : qtlocation
BuildRequires : qtlocation-dev
BuildRequires : qtmqtt
BuildRequires : qtmqtt-dev
BuildRequires : qtmultimedia
BuildRequires : qtmultimedia-dev
BuildRequires : qtnetworkauth
BuildRequires : qtnetworkauth-dev
BuildRequires : qtquickcontrols
BuildRequires : qtquickcontrols2
BuildRequires : qtquickcontrols2-dev
BuildRequires : qtremoteobjects-dev
BuildRequires : qtscript
BuildRequires : qtscript-dev
BuildRequires : qtscript-extras
BuildRequires : qtscxml
BuildRequires : qtscxml-dev
BuildRequires : qtsensors
BuildRequires : qtsensors-dev
BuildRequires : qtserialbus
BuildRequires : qtserialbus-dev
BuildRequires : qtserialport
BuildRequires : qtserialport-dev
BuildRequires : qtspeech
BuildRequires : qtspeech-dev
BuildRequires : qtsvg
BuildRequires : qtsvg-dev
BuildRequires : qttools
BuildRequires : qttools-dev
BuildRequires : qttranslations
BuildRequires : qtvirtualkeyboard
BuildRequires : qtvirtualkeyboard-dev
BuildRequires : qtwayland
BuildRequires : qtwayland-dev
BuildRequires : qtwebchannel
BuildRequires : qtwebchannel-dev
BuildRequires : qtwebengine
BuildRequires : qtwebengine-dev
BuildRequires : qtwebsockets
BuildRequires : qtwebsockets-dev
BuildRequires : qtx11extras
BuildRequires : qtx11extras-dev
BuildRequires : qtxmlpatterns
BuildRequires : qtxmlpatterns-dev
BuildRequires : setxkbmap
BuildRequires : shared-mime-info
BuildRequires : snappy-dev
BuildRequires : sqlite-autoconf
BuildRequires : sqlite-autoconf-dev
BuildRequires : syntax-highlighting
BuildRequires : syntax-highlighting-data
BuildRequires : syntax-highlighting-dev
BuildRequires : syntax-highlighting-lib
BuildRequires : systemd
BuildRequires : systemd-dev
BuildRequires : texinfo
BuildRequires : util-linux
BuildRequires : util-linux-dev
BuildRequires : valgrind
BuildRequires : valgrind-dev
BuildRequires : wayland
BuildRequires : weston
BuildRequires : wmctrl
BuildRequires : xauth
BuildRequires : xclip
BuildRequires : xdg-dbus-proxy
BuildRequires : xdg-desktop-portal
BuildRequires : xdg-desktop-portal-dev
BuildRequires : xdg-desktop-portal-gtk
BuildRequires : xdg-desktop-portal-kde
BuildRequires : xdg-user-dirs
BuildRequires : xdg-user-dirs-gtk
BuildRequires : xdg-utils
BuildRequires : xdotool
BuildRequires : xdpyinfo
BuildRequires : xf86-input-libinput
BuildRequires : xf86-video-amdgpu
BuildRequires : xf86-video-ati
BuildRequires : xf86-video-fbdev
BuildRequires : xf86-video-nouveau
BuildRequires : xf86-video-qxl
BuildRequires : xf86-video-vboxvideo
BuildRequires : xf86-video-vesa
BuildRequires : xf86-video-vmware
BuildRequires : xfontsel
BuildRequires : xhost
BuildRequires : xinit
BuildRequires : xinput
BuildRequires : xkbcomp
BuildRequires : xkeyboard-config
BuildRequires : xkill
BuildRequires : xmodmap
BuildRequires : xorg-server
BuildRequires : xorg-server-dev
BuildRequires : xorgproto
BuildRequires : xorgproto-dev
BuildRequires : xprop
BuildRequires : xrandr
BuildRequires : xrdb
BuildRequires : xrdp
BuildRequires : xrestop
BuildRequires : xscreensaver
BuildRequires : xsel
BuildRequires : xset
BuildRequires : xsetroot
BuildRequires : xvfb-run
BuildRequires : xwd
BuildRequires : xwininfo
BuildRequires : xz
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : yaml-cpp
BuildRequires : yaml-cpp-dev
BuildRequires : zlib
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
BuildRequires : zstd-dev
BuildRequires : zstd-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Qt is provided with a powerful embedded scripting environment through the Qt Script
classes.

%prep
%setup -q -n qt-creator-clr
cd %{_builddir}/qt-creator-clr

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1620544176
unset LD_AS_NEEDED
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export FCFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export FFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export CXXFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export LDFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fPIC -Wl,-z,max-page-size=0x1000 -fvisibility=hidden -flto-partition=none
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FCFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export CXXFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export LDFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread $PGO_USE"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export DISPLAY=:0
export __GL_ALLOW_UNOFFICIAL_PROTOCOL=1
export __GL_SYNC_TO_VBLANK=0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH=/usr/share/defaults/fonts
## altflags_pgo end
if [ ! -f statuspgo ]; then
echo PGO Phase 1
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
%cmake .. -G Ninja \
-DCMAKE_JOB_POOLS:STRING="compile=16;link=6" \
-DCMAKE_JOB_POOL_COMPILE:STRING="compile" \
-DCMAKE_JOB_POOL_LINK:STRING="link" \
-DCMAKE_NM=/usr/bin/gcc-nm \
-DCMAKE_RANLIB=/usr/bin/gcc-ranlib \
-DCMAKE_AR=/usr/bin/gcc-ar \
-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
-DCMAKE_INSTALL_BINDIR=bin \
-DCMAKE_INSTALL_LIBDIR=lib64 \
-DCMAKE_INSTALL_LIBEXECDIR=libexec \
-DCMAKE_PREFIX_PATH=/usr \
-DCMAKE_BUILD_TYPE=Release \
-DCMAKE_C_COMPILER=gcc \
-DCMAKE_CXX_COMPILER=g++ \
-DQT_BUILD_EXAMPLES:BOOL=OFF \
-DCLANGTOOLING_LINK_CLANG_DYLIB:BOOL=OFF \
-DBUILD_CPLUSPLUS_TOOLS:BOOL=ON \
-DSHOW_BUILD_DATE:BOOL=ON \
-DWITH_DOCS:BOOL=OFF \
-DLITEHTML_UTF8:BOOL=OFF \
-DWITH_TESTS:BOOL=ON \
-DWITH_UNIT_TESTS:BOOL=ON \
-DBUILD_TESTING:BOOL=ON \
-DBUILD_QBS:BOOL=OFF \
-DBUILD_LIBRARY_QLITEHTML:BOOL=OFF \
-DENABLE_SVG_SUPPORT:BOOL=ON \
-DENABLE_BUILD_QBS:BOOL=OFF \
-DPYTHON_EXECUTABLE:FILEPATH=/usr/bin/python3 \
-DPython3_EXECUTABLE="/usr/bin/python3" \
-DClang_DIR=/usr/lib64/cmake/clang \
-DLLVM_DIR=/usr/lib64/cmake/llvm
ninja --verbose -j16
#make -j16 V=1 VERBOSE=1
## ccache stats
ccache -s
## ccache stats

export DISPLAY=:0
export __GL_ALLOW_UNOFFICIAL_PROTOCOL=1
export __GL_SYNC_TO_VBLANK=0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH=/usr/share/defaults/fonts
export LD_LIBRARY_PATH="/builddir/build/BUILD/qt-creator-clr/clr-build/lib64:/builddir/build/BUILD/qt-creator-clr/clr-build/lib64/qtcreator:/builddir/build/BUILD/qt-creator-clr/clr-build/lib64/qtcreator/plugins:/usr/cuda/lib64:/usr/cuda/targets/x86_64-linux/lib:/usr/nvidia/lib64:/usr/nvidia/lib:/usr/nvidia/lib/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/lib64/dri:/usr/lib64/haswell:/usr/lib64:/usr/lib:/usr/share"
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:../"
export PATH="/builddir/build/BUILD/qt-creator-clr/clr-build/bin:/builddir/build/BUILD/qt-creator-clr/clr-build/libexec/qtcreator:/opt/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
export $(dbus-launch)
ctest --parallel 16 -V --progress --timeout 200 || :
#/builddir/build/BUILD/qt-creator-clr/clr-build/bin/qtcreator -temporarycleansettings -settingspath /builddir/ -installsettingspath /builddir/ -pluginpath /builddir/build/BUILD/qt-creator-clr/clr-build/lib64/qtcreator/plugins -noload ClangCodeModel ClangFormat
#/builddir/build/BUILD/qt-creator-clr/clr-build/bin/qtcreator -settingspath /builddir/ -installsettingspath /builddir/ -pluginpath /builddir/build/BUILD/qt-creator-clr/clr-build/lib64/qtcreator/plugins -noload ClangCodeModel ClangFormat
/builddir/build/BUILD/qt-creator-clr/clr-build/bin/qtcreator -noload Help
find . -type f,l -not -name '*.gcno' -not -name 'statuspgo*' -delete -print
echo USED > statuspgo
fi
if [ -f statuspgo ]; then
echo PGO Phase 2
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%cmake .. -G Ninja \
-DCMAKE_JOB_POOLS:STRING="compile=16;link=6" \
-DCMAKE_JOB_POOL_COMPILE:STRING="compile" \
-DCMAKE_JOB_POOL_LINK:STRING="link" \
-DCMAKE_NM=/usr/bin/gcc-nm \
-DCMAKE_RANLIB=/usr/bin/gcc-ranlib \
-DCMAKE_AR=/usr/bin/gcc-ar \
-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
-DCMAKE_INSTALL_BINDIR=bin \
-DCMAKE_INSTALL_LIBDIR=lib64 \
-DCMAKE_INSTALL_LIBEXECDIR=libexec \
-DCMAKE_PREFIX_PATH=/usr \
-DCMAKE_BUILD_TYPE=Release \
-DCMAKE_C_COMPILER=gcc \
-DCMAKE_CXX_COMPILER=g++ \
-DQT_BUILD_EXAMPLES:BOOL=OFF \
-DCLANGTOOLING_LINK_CLANG_DYLIB:BOOL=OFF \
-DBUILD_CPLUSPLUS_TOOLS:BOOL=ON \
-DSHOW_BUILD_DATE:BOOL=ON \
-DWITH_DOCS:BOOL=OFF \
-DLITEHTML_UTF8:BOOL=OFF \
-DWITH_TESTS:BOOL=OFF \
-DWITH_UNIT_TESTS:BOOL=OFF \
-DBUILD_TESTING:BOOL=OFF \
-DBUILD_QBS:BOOL=OFF \
-DBUILD_LIBRARY_QLITEHTML:BOOL=OFF \
-DENABLE_SVG_SUPPORT:BOOL=ON \
-DENABLE_BUILD_QBS:BOOL=OFF \
-DPYTHON_EXECUTABLE:FILEPATH=/usr/bin/python3 \
-DPython3_EXECUTABLE="/usr/bin/python3" \
-DClang_DIR=/usr/lib64/cmake/clang \
-DLLVM_DIR=/usr/lib64/cmake/llvm
ninja --verbose -j16
#make -j16 V=1 VERBOSE=1
## ccache stats
ccache -s
## ccache stats
fi
popd

%install
export SOURCE_DATE_EPOCH=1620544176
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
