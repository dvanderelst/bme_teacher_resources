# Installing mBlock

mBlock is the block-based software used to program the mBot. Programs are built by dragging blocks rather than typing code.

There are two ways to use it; both work with all our lesson plans:

- **Install it on the computer.** Available for Windows and Mac only.
- **Run it in a browser.** Works on Windows, Mac, Linux, and Chromebooks. Chrome communicates directly with the robot; other browsers require mLink, a helper program.

Both options use the same editor. The blocks, menus, and screens are identical, so the instructions and screenshots in these materials apply to either choice. Programs saved in one version open in the other.

The differences are practical rather than functional: the installed version works offline, while the browser version needs a network connection — but, in Chrome, nothing installed at all.

To install mBlock, mLink, or both, download them from Makeblock's download page: [mblock.cc/pages/downloads](https://mblock.cc/pages/downloads). Everything below starts there.

## Which should I use?

| Your computers | Use |
| --- | --- |
| Windows | Either. Installing is slightly more reliable. |
| Mac | Either. Take care to select the correct version — see below. |
| Chromebook | Browser only |
| Linux | Browser only, using Chrome or Chromium and direct connection. mLink is not usable — see the note under [Step 1: Install mLink](#step-1-install-mlink). |

If your class uses mixed hardware, the browser version ensures everyone uses identical software.

Some school computers restrict software installation, blocking either the mBlock installer or mLink. If so, contact your IT staff to install it well before the first lesson.

## Option A: Install mBlock on the computer

### Windows

1. Go to [mblock.cc/pages/downloads](https://mblock.cc/pages/downloads).
2. Find the **mBlock PC version** section and download the Windows version. Both `.exe` and `.msi` packages are available. Use the `.exe` installer normally; the `.msi` is for IT departments deploying software centrally.
3. Run the downloaded installer and follow the prompts. There is nothing to configure and nothing to choose; it takes a minute or two.

    ![The mBlock installer running, here version 5.6.0.](images/installing-mblock-installer.png)

4. Click `Finish`.

    ![The end of the installation. Version 5.6.0 does not offer to launch mBlock afterwards; start it from the Start menu.](images/installing-mblock-finish.png)

> **Note**
>
> Older versions of mBlock installed a **device driver** as part of setup — the CH340 USB-to-serial driver. Version 5.6.0 does not: on a Windows 11 machine that had never had Makeblock software on it, the installer ran start to finish with no driver step at all.
>
> It matters when a connection that ought to work does not. Both the robot's USB port and the Bluetooth dongle present themselves to Windows as serial ports, and without the driver neither may appear. The symptom is an empty port list in the `Connect` dialog, or a browser that offers nothing to connect to.
>
> The fix is to install the driver, which the **mLink** installer still does — see [Step 1: Install mLink](#step-1-install-mlink) below. Installing mLink purely for its driver is harmless: you can go on using the installed mBlock and ignore mLink entirely.

**Windows requirement:** mBlock requires **64-bit** Windows 7 or 10 and will not install on 32-bit systems. Verify older school laptops meet this requirement before the lesson. It also runs on Windows 11, which is what we tested on.

### Mac

1. Go to [mblock.cc/pages/downloads](https://mblock.cc/pages/downloads).
2. Find the **mBlock PC version** section. There are **two** Mac downloads; selecting the wrong one is the most common issue on Mac:
    - **For Apple M1/M2 chips** — use this on any Mac with Apple Silicon (essentially every Mac sold since late 2020).
    - The standard Mac download — for older Intel Macs.

    To check your Mac's chip: open the Apple menu and select `About This Mac`. If the chip is named "Apple M1", "M2", "M3", or similar, you have Apple Silicon.

3. Run the downloaded installer and follow the prompts.

**Mac requirement:** macOS 10.12 or later.

### Mac: getting past the security warnings

macOS may block the installer or the installed app because it was not downloaded from the App Store. Two different warnings require two different solutions:

- **The installer will not start.** Right-click the installer package, choose `Open`, then click `Open` in the dialog.
- **The installed app will not open** ("cannot be opened because Apple cannot check it for malicious software"). Find mBlock in Finder — not Launchpad, which does not offer this option. Control-click its icon, choose `Open`, then click `Open`. macOS remembers this choice, so you only need to do it once.

## Option B: Run mBlock in a browser

Chrome can communicate directly with the robot via serial port, which our instructions use (see [Direct connection or mLink?](#direct-connection-or-mlink)). On Chrome, you can proceed directly to opening the editor. This is important for locked-down school computers, as the browser route requires **no installation at all**.

For non-Chrome browsers, install **mLink** first, then open the editor.

> **Use Chrome or Chromium itself**, not merely a browser built on Chromium. Direct connection relies on the browser's own serial-port support, and that is where the differences between Chromium-based browsers show up: in our tests, Vivaldi on Windows failed to connect over direct connection, while Chromium on Linux connected without trouble. If direct connection fails in a browser that is *nearly* Chrome, try actual Chrome before concluding the robot or the dongle is at fault.

### Step 1: Install mLink

Download mLink from [mblock.cc/pages/downloads](https://mblock.cc/pages/downloads). The page lists five downloads: Windows, Mac, `linux.deb`, `linux.rpm`, and Chromebook.

**Windows** — download and run the installer. Near the end it opens a separate window offering to install a **device driver**, the one described in the note above. Click `INSTALL`; if you see `Driver Install Failure`, click `UNINSTALL`, then `INSTALL` again. Requires Windows 7 or 10, 64-bit; Windows 11 works.

![The mLink installer. Note that the program calls itself mLink2, which is the same as the download page's mLink.](images/installing-mblock-mlink-installer.png)

![The driver window, which appears separately from the installer. `CH341SER.INF` should appear in the box; click `INSTALL`. Use `UNINSTALL` first if the install fails.](images/installing-mblock-driver-setup.png)

![Confirmation that the driver installed. Click `OK`, then close the driver window behind it.](images/installing-mblock-driver-installed.png)

![The end of the mLink installation. `Run mLink2` is selected by default, so it starts immediately.](images/installing-mblock-mlink-finish.png)

**Mac** — download and run the installer. Requires macOS 10.12 or later. If macOS blocks the installer, use the same workarounds described earlier.

**Linux** — two packages are available: `.deb` for Debian and Ubuntu-based systems, `.rpm` for Fedora and Red Hat-based systems.

> **Note**
>
> **On Linux, do not bother with mLink.** The `.deb` is mLink **1.2.0** — several major versions behind the 2.1.1 that Windows gets — and although it installs without complaint on Linux Mint 22.3, it then registers nothing: no menu entry, no command on the path, no way we could find to start it.
>
> Use the browser's direct connection instead, in Chrome or Chromium. We connected, ran a program in Live mode, uploaded, and reset the firmware that way, with nothing installed. See [Direct connection or mLink?](#direct-connection-or-mlink).

**Chromebook** — open the downloads page in Chrome, find the Chromebook version of mLink, click `Download`, and follow Chrome's prompts to add it.

### Step 2: Start mLink

mLink must be running before the browser can detect the robot.

- **Windows** — start mLink from the Start menu. It opens a window confirming it is running. **Leave this window open.** The first time, Windows displays a firewall prompt. Click `Allow Access`; otherwise, the browser cannot communicate with mLink. mLink also puts an icon in the notification area, which is where it hides once the window is closed.
- **Mac** — start mLink from Applications. It opens a window confirming it is running. Leave it open.
- **Linux** — not available in practice; use direct connection instead, as described above.
- **Chromebook** — nothing to start; Chrome handles it once mLink is added.

With mLink running, the browser will ask permission to hand over to it the first time you connect. Answer `Open mLink2`.

![The Windows firewall prompt, which appears the first time mLink runs. Select `Private networks`, since mLink and the browser are on the same machine. Click `Allow access`.](images/installing-mblock-firewall.png)

![mLink running. This window must remain open; closing it prevents the browser from detecting the robot. It is a launcher, so `Create now` under **mBlock block-based editor** opens the same editor as the next step.](images/installing-mblock-mlink-running.png)

![The browser asking to hand over to mLink. Click `Open mLink2`. Ticking the box stops it asking again on this computer.](images/installing-mblock-mlink-open-prompt.png)

### Step 3: Open the editor

Open the block-based editor at [ide.mblock.cc](https://ide.mblock.cc), which is used throughout our lesson plans.

(Makeblock also offers a Python editor at [python.mblock.cc](https://python.mblock.cc), which we do not use.)

## What we do not use

A few other items appear on Makeblock's download page. For clarity, none are used in our lesson plans:

- **mBlock 3** — an older, discontinued version. Our programs will not open in it.
- **The mobile app** (Android and iOS) — programming on a phone is impractical in class, and Bluetooth connections make it difficult to identify which robot you are controlling.
- **The Python editor** — our lesson plans use only block-based programming.

## Next step

Once mBlock is working, proceed to [Getting started with the robot](#getting-started-with-the-robot), which covers Bluetooth dongle pairing, connecting, Live and Upload modes, and running your first program.
