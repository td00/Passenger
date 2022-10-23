name="passenger-pm-diy-git"
version=1.0
release=1
desc="DIY (Do It Yourself) password manager keeps password multi layer encoded"
architectures=("all")
homepage="https://github.com/Elagoht/Passenger"
license=("GPLv3")
maintainer="Furkan Baytekin (Elagoht)"
provides="passenger-pm"
sources="git+https://github.com/Elagoht/Passenger/"
checksums="SKIP"
version() {
    cd "$srcdir/Passenger"
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}
prepare() {
    # Get custom endecode.py
    printf "\e[32m==> Write here your endecode.py files directory:\e[0m "
    while true; do
        read -r endedir
        if [ -f $endedir ]; then
            break
        fi
        printf "\e[31m==> Please enter a valid directory:\e[0m "
    done
    # Create build environment
    python3 -m venv builder
    source builder/bin/activate
    # Recieve dependencies
    pip install pyqt5 pyqtdarktheme pyperclip pyinstaller
    cp -v "$endedir" "$srcdir/Passenger/endecode.py"
}
build() {
    # Build app
    python3 -m PyInstaller --onefile --noconsole "$srcdir/Passenger/passenger.py" --name=passenger.app
    # Clean build junks
    rm -rf "$srcdir/builder/"
}
package() {
    # Create app files
    install -d "$pkgdir/usr/share/passenger-pm/"
    mv "$srcdir/Passenger/passenger-pm/assets" "$pkgdir/usr/share/passenger-pm"   
    install -Dm755 "$srcdir/dist/passenger.app" -t "$pkgdir/usr/share/passenger-pm/"
    # Create shortcut
    install -d "$pkgdir/usr/share/applications/"
    install -Dm644 "Passenger/Passenger.desktop" -t "$pkgdir/usr/share/applications/"
    # Create bin file
    install -d "$pkgdir/usr/bin/"
    ln -s "/usr/share/passenger-pm/passenger.app" "$pkgdir/usr/bin/passenger-pm"
    # Clean environment
    rm -rf $srcdir/*
}
