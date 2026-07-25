# Installing mBlock

mBlock is the software used to write and run programs for the mBot. It is a block-based (Scratch-like) environment, so programs are built by dragging blocks rather than typing code.

There are two ways to use it, and either works for all our lesson plans:

- **Install it on the computer.** Available for Windows and Mac only.
- **Run it in a browser.** Works on Windows, Mac, Linux and Chromebooks, but needs a small helper program called mLink so the browser can talk to the robot.

These are the same editor, not two different products. The blocks, menus and screens are the same either way, so the instructions and screenshots in these materials apply whichever route you take, and a program saved in one opens in the other. The differences are practical rather than functional: the installed version keeps working when the internet does not, while the browser version needs mLink running alongside it.

To install mBlock, mLink, or both, download them from Makeblock's download page: [mblock.cc/pages/downloads](https://mblock.cc/pages/downloads). Everything below starts there.

## Which should I use?

| Your computers | Use |
| --- | --- |
| Windows | Either. Installing is a little more reliable. |
| Mac | Either. Take care to pick the right version — see below. |
| Chromebook | Browser only |
| Linux | Browser only |

If you are running a class on mixed hardware, the browser route keeps everyone using the same software.

Some school computers are locked down and will not allow either the mBlock installer or mLink to be installed. If that happens, you will need your school's IT staff to install it for you. It is worth checking this well before the first lesson.

## Option A: Install mBlock on the computer

### Windows

1. Go to [mblock.cc/pages/downloads](https://mblock.cc/pages/downloads).
2. Find the **mBlock PC version** section and download the Windows version. An `.exe` installer and an `.msi` package are both offered; the `.exe` is the normal choice, and the `.msi` is there for IT departments that deploy software centrally.
3. Run the downloaded installer and follow the prompts.
4. Near the end, the installer offers to install a **device driver**. This is what lets the computer talk to the robot, so click `Install`. If you see `Driver Install Failure`, the driver is most likely already present from an earlier installation — click `Uninstall`, then `Install` again.
5. Click `Finish`.

**Windows requirement:** mBlock needs **64-bit** Windows 7 or Windows 10. It will not install on a 32-bit machine. Older school laptops are worth checking before the lesson.

### Mac

1. Go to [mblock.cc/pages/downloads](https://mblock.cc/pages/downloads).
2. Find the **mBlock PC version** section. There are **two** Mac downloads, and picking the wrong one is the most common problem on Mac:
    - **For Apple M1/M2 chips** — use this on any Mac with Apple Silicon, which means essentially every Mac sold since late 2020.
    - The standard Mac download — for older Intel Macs.

    If you are unsure which you have, open the Apple menu and choose `About This Mac`. A chip named "Apple M1", "M2", "M3" or similar means Apple Silicon.

3. Run the downloaded installer and follow the prompts.

**Mac requirement:** macOS 10.12 or later.

### Mac: getting past the security warnings

macOS may refuse to open the installer or the installed app because it was not downloaded from the App Store. Two different warnings, two different fixes:

- **The installer will not start.** Right-click the installer package and choose `Open`, then click `Open` in the dialog that appears.
- **The installed app will not open** ("cannot be opened because Apple cannot check it for malicious software"). Find mBlock in the Finder — not in Launchpad, which will not offer the option. Control-click its icon, choose `Open`, then click `Open`. macOS remembers this, so you only do it once.

## Option B: Run mBlock in a browser

The browser version of mBlock cannot reach the robot on its own. A small program called **mLink** runs on the computer and bridges between the two. So this route is two steps: install mLink, then open the editor.

> Use **Chrome**. The online editor is most reliable there, and on Linux mLink only works with Chrome and Chromium — not with other Chrome-based browsers.

### Step 1: Install mLink

Go to [mblock.cc/pages/downloads](https://mblock.cc/pages/downloads) and scroll to the **mLink** downloads. Versions are offered for Windows, Mac, Linux and Chromebook.

**Windows** — download and run the installer. As with mBlock itself, it will offer to install a device driver at the end: click `Install`, and if you get `Driver Install Failure`, choose `Uninstall` then `Install` again. Windows 7 or 10, 64-bit.

**Mac** — download and run the installer. macOS 10.12 or later. If macOS blocks it, use the same two fixes as above.

**Linux** — two packages are offered: `.deb` for Debian and Ubuntu-based systems, `.rpm` for Fedora and Red Hat-based ones. Install whichever matches your distribution.

**Chromebook** — open the downloads page in Chrome, find the Chromebook version of mLink, click `Download`, and follow the prompts Chrome shows to add it.

### Step 2: Start mLink

mLink has to be running before the browser can find the robot.

- **Windows** — start mLink from the Start menu. It opens a small window confirming it is running. **Leave that window open.** The first time, Windows may ask about the firewall: click `Allow Access`, or the browser will not be able to reach mLink.
- **Mac** — start mLink from Applications. It opens a small window confirming it is running. Leave it open.
- **Linux** — start it from a terminal with `mblock-mlink start`.
- **Chromebook** — nothing to start; Chrome handles it once mLink is added.

### Step 3: Open the editor

Go to [ide.mblock.cc](https://ide.mblock.cc). That is the block-based editor used throughout our lesson plans.

(Makeblock also publishes a Python editor at [python.mblock.cc](https://python.mblock.cc). We do not use it.)

## What we do not use

A few other things appear on Makeblock's download page. For clarity, none of them are used in our lesson plans:

- **mBlock 3** — an older, discontinued version. Our programs will not open in it.
- **The mobile app** (Android and iOS) — programming on a phone screen is impractical in class, and it connects over Bluetooth in a way that makes it hard to tell which robot you have reached.
- **The Python editor** — our lesson plans are entirely block-based.

## Next step

Once mBlock is working, continue with [Getting started with the robot](#getting-started-with-the-robot), which covers pairing the Bluetooth dongle, connecting, Live and Upload mode, and running your first program.
