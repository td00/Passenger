# Passenger Password Manager

TL;DR just show me [how to install.](#5)

## Table of Content

1. [What is Passenger?](#0)
    * [How It Works?](#1)
2. [Privacy](#2)
    * [But Passwords Stores in a Local File?](#3)
3. [Why is It Not Open Source?](#4)
4. [Installation](#5)
5. [Updates](#6)
6. [Planning Updates](#7)
7. [FAQ](#8)
8. [Screenshots](#9)

<h2 id="0">What is Passenger</h2>
Passenger is a password manager. I programmed it to keep my password safe. I know there is lots of password manager and also they have an online interface and online databases.

The word **online** is not enough safe. If an hacker attacks to a big database that you store your password in, you are in danger. Not surprisingly, it happened to me. After that I started to program that software.

<h3 id="1">How It Works</h3>
On first run, Passenger prompts you to create a password to register the app. Your password is going to encode and save into database. You will need that password to login to program next times.

Passwords you add, will encode and save into databese. When you want to get that password you can click ***Copy*** button next to password info.

It writes all data into a file as multi-encryped format. On every action, it differently re-encrypted. 

<h2 id="2">Privacy</h2>
Passenger can not reach to internet. You can test it via measuring network activity. So me, the developer cannot get your passwords. Only you can get your passwords after logging in and pressing copy buttons.

A person who watches or records your screen, cannot see your passwords because you will get your passwords via clicking a button and, you will paste this password into a password area that censors your passwords.

Copying passwords also protects you from lots of keylogger viruses. If they cannot read your clipboard, they will never get your passwords becaoyse you will never write your passwords.

<h3 id="3">But Passwords Stores in a Local File?</h3>

Briefly, There is 4 layers of security:
1. Encoding algorithm encoded, and encoded code stored in source code in different ways.
2. When an hacker breaks to the lowest layer, it will meet only a computer-readable object.
3. The database object that encrypted encrypted with another encryption method.
4. Finally, that multy encrypted database encrypted with another method that I develop.
5. Bonus layer: After login, your passwords will stay encryped format until you press the copy button.

<h2 id="4">Why is It Not Open Source?</h2>
I would like to make it FOSS. But then a hacker would be able to break my encoding-decoding algorithm easily. We never want that. But as I say in privacy section, you can test this application anyway.

<h2 id="5">How to Install</h2>
If you using Windows, delete it and install Linux. We talking about privacy.

*Just kiddin'. There is a Windows version. But I highly recommend you to try Linux.*

On linux:

   1. Download zip and extract it. Then open directory in terminal (You can use **cd** command)
   2. Type the command below:
   > sudo ./install.sh
   1. Well, You are done.

On windows:

I prepared a Winrar SFX to install it. Just run it or install manually with given archive.

<h2 id="6">Updates</h2>

* Username cells changed with buttons so you can copy them via one click.
* You can add constants to use shortcuts to access the same username/email. In example if you add a constant like " Email " and set it's value to " somebody@somemail.com " and add an entry with " $Email ". On button you will see " $Email " and you will know you will copy "somebody@somemail.com".
* Now, you can export your data to a csv file as _**unencrypted format!**_ So do not show anyone this file. U can use this file to use "import from csv file." feature on web browsers excluding firefox and firefox based ones. Because firefox needs platforms' url that other browsers does not require. 
* Encryption algorithm changed. In some cases, old algorithm were create a situation that user will lost that specific password. I had to develop a seed-generated algorithm instead of a dynamically-generated one. **But the program still uses 3 layers of encryption.
* Now passwords in database, stores as encrypted format. So, this means when program read and encrypt the data base, your data will still stay encrypted format on ram. When you hit the copy button, it will be decrypted and presented to you.

<h2 id="7">Planning Updates</h2>

* For extra security, I will add an security number between 1 and 100. It will require to login and play a seed role to encrypt your passwords.
* I will add an option to read external databases. This will make the program portable.
* The feature that excites me the most. There will be an **github integration** to backup your passwords in your own private repository.

<h2 id="8">FAQ</h2>

* When we get a Mac version?

> When I get a Mac to compile it on or when I decided to install a macintosh in Virtual Machine.

* When will we get Safari import option?

> Probably never. Export to csv and import the exported csv into a chromium based browser. Then open safari, import from other browser.

<h2 id="9">Screenshots</h2>

![Login Screen](https://raw.githubusercontent.com/Elagoht/Passenger/main/screenshots/passenger-login.png)

![Query Screen](https://raw.githubusercontent.com/Elagoht/Passenger/main/screenshots/passenger-passwords.png)

![Edit Screen](https://raw.githubusercontent.com/Elagoht/Passenger/main/screenshots/passenger-edit.png)

![Reset Screen](https://raw.githubusercontent.com/Elagoht/Passenger/main/screenshots/passenger-resetpassword.png)

![Import Screen](https://raw.githubusercontent.com/Elagoht/Passenger/main/screenshots/passenger-import.png)

![Export Screen](https://raw.githubusercontent.com/Elagoht/Passenger/main/screenshots/passenger-export.png)