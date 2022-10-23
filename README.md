# Passenger Password Manager

![Passenger Windows](https://raw.githubusercontent.com/Elagoht/Passenger/main/repo-assets/passenger-windows.png)

Passenger is a fully browser compatible password manager originally made for
Linux, and also works on Windows. Why there is an application like this when we
have keepass apps?

# Why To Use Passenger?

## Make It Your Own

Passenger is an open source project and it has a killer featue. Passenger
allows you to develop your own encrypt/decrypt algorithm. Passenger is actually
a GUI that manage your passwords. It keeps passwords in a local files, so you
should backup these files.

Local files are located in

```
~/.passenger/
```

on Linux and

```
%appdata%/.passenger
```

on Windows.

## Easy Import and Export

You can import the data exported from browsers. The program will guide you how
to install.

## Constants

You may not want to write exact same email adress to create a new entry. You
can use constants that will make your job easy. You can also import and export
your constants.

# How to Install?

Passenger is a GUI app but you can install a an executable with an closed
source algorithm I wrote for people who don't know how to create an
encrypt/decrypt algorithm.

Alternatively you can install source code version to use your own algorithm.
After that, if you want to you can compile to use in a more secure way.

### On Linux

#### Pre-Built Version (Closed Source Algorithm)

Go to release and select the corret file for your distro and install the
pre-built closed source version.

#### Open Source Version (Need A Custom Algorithm)

Create an algorithm and use the lure.sh file with LURE. The installation
process will prompt you to write your endecode.py file's location. Then you
should be able to create your own DIY Passenger app.

### On Windows

There's a Winrar SFX file that makes install easy. It only installs closed
source version. If you want to make your own, you can download and edit source
code. You must install dependencies which are python, pyperclip, pyqt5,
squirrel.

**Note:** *Windows has limitations* that I do not like. Exact same algorithm can
run on Linux but Windows does not execute that. So propriety version
*currently* have open source algorithm **which means not safe.**

# Mobile Phone Support

There will be a mobile application bu not soon. I have to learn a language to
make it possible to run on mobile envrionments. Instead of this, I'll make an
CLI application to run in termianal, and this will allows you to use it on
terminal emulators, both desktop and mobile (search for termux and iShell).

# Conclusion

This is a secure, open source project you can safely use. You may want to help
me to improve application.
