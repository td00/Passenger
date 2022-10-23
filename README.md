# Passenger Password Manager

![Passenger Windows](https://raw.githubusercontent.com/Elagoht/Passenger/main/repo-assets/passenger-windows.png)

Passenger is a fully browser compatible password manager originally made for
Linux, and also works on Windows. Why there is an application like this when we
have keepass apps?

## Explaning What Passenger Is (With English Subtitles)

[![Youtube Banner](https://i.ytimg.com/vi/KjZ4DAojTew/hqdefault.jpg)](https://www.youtube.com/watch?v=KjZ4DAojTew)

Watch this video on YouTube.

# Why To Use Passenger?

## Make It Your Own

Passenger is an open source project and it has a killer featue. Passenger
allows you to develop your own encrypt/decrypt algorithm. Passenger is actually
a GUI that manage your passwords. It keeps passwords in a local files, so you should backup these files.

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

You can import the data exported from browsers. The program will guide you how to install.

## Constants

You may not want to write exact same email adress to create a new entry. You can use constants that will make your job easy. You can also import and export your constants.

# How to Install?

Passenger is a GUI app but you can install a an executable with an closed
source algorithm I wrote for people who don't know how to create an
encrypt/decrypt algorithm.

Alternatively you can install source code version to use your own algorithm.
After that, if you want to you can compile to use in a more secure way.

## Install Executable Version (Easy Way)

On releases section, download the package for your operating system and follow instructions below:

### On Linux

There's an install script. Open folder in terminal and execute it via command below:

```sh
sudo ./install.sh
```

This script will guide you to install the version you want to install. To uninstall you can use same script. The closed source version will re-encrypt your data in a different way after every action.

### On Windows

There's a Winrar SFX file that makes install easy. It only installs closed source version. If you want to make your own, you can download and edit source code. You must install dependencies which are python, pyperclip, pyqt5, squirrel.

**Note:** Windows has limitations that I do not like. Exact same algorithm can run on Linux but Windows does not execute that. So propriety version *currently* have open source algorithm which means not safe.

# Mobile Phone Support

There will be a mobile application bu not soon. I have to learn a language to make it possible to run on mobile envrionments. Instead of this, I'll make an CLI application to run in termianal, and this will allows you to use it on terminal emulators, both desktop and mobile (search for termux and iShell).

# Conclusion

This is a secure, open source project you can safely use. You may want to help me to improve application.
