name="passenger-pm-bin"
version=1.0
release=1
desc="Password manager keeps password multi layer encoded"
architectures=("amd64")
homepage="https://github.com/Elagoht/Passenger"
license=("GPLv3")
maintainer="Furkan Baytekin (Elagoht)"
provides="passenger-pm"
sources_amd64="https://github.com/Elagoht/Passenger/releases/download/v$version/PassengerLinuxInstaller.tar.gz?~archive=false"
checksums_amd64="610f1cc3adbbf6ef68d510ac719eaeb0d3a2a685ae951752865fb323b21cd0c2"
version() {
    printf "%s" $version
}
package() {
    tar -xf "$srcdir/PassengerLinuxInstaller.tar.gz"
    install -d "$pkgdir/usr/bin/"
    echo "/usr/share/Passenger/Passenger.app" > passenger
    install -Dm755 "passenger" -t "$pkgdir/usr/bin/"
    install -d "$pkgdir/usr/share/Passenger/"
    mv "Passenger/" "$pkgdir/usr/share/"
    install -Dm755 "Passenger.app" -t "$pkgdir/usr/share/Passenger/"
    install -d "$pkgdir/usr/share/applications/"
    install -Dm644 "Passenger.desktop" -t "$pkgdir/usr/share/applications/"
}
