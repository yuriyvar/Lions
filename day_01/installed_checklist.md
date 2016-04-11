# Proxy Configuration for Windows
- Open a new *Command Prompt* window (a Windows terminal - you can
search for "Command Prompt")
- We need to set environment variables to direct traffic through the
proxy. For windows this is done through the `http_proxy` and
`https_proxy` environment variables. We will set both of these to the
same value.
- In the command prompt, please enter the following commands (replace
`ABC123` with your EID and `yourpassword` with, well, your password):
  ```
setx http_proxy "http://ABC123:yourpassword@10.37.135.39:8099/"
setx https_proxy "http://ABC123:yourpassword@10.37.135.39:8099/"
```
  With the output, your command prompt should look something like this:

```
C:\Users\Ryangosling1337>setx http_proxy "http://ryanGosling1337:OMGyolo@10.37.135.39:8099/"

SUCCESS: Specified value was saved.

C:\Users\Ryangosling1337>setx https_proxy "http://ryanGosling1337:OMGyolo@10.37.135.39:8099/"

SUCCESS: Specified value was saved.

C:\Users\Ryangosling1337> _
```
- You're set. Close the command prompt window.

<p style="page-break-after:always;"></p>

# Proxy Configuration for Mac OS X / Linux

- We need to set environment variables to direct traffic through the
proxy. For windows this is done through the `http_proxy` and
`https_proxy` environment variables. We will set both of these to the
same value.
- In your home directory (which follows the pattern
`/Users/<yourusername>` such as `/Users/ryanGosling1337` in OS X and `/home/<yourusername>` in Linux), create a new file called ".bashrc" (note the leading dot, no extension)
with the following content (replace `ABC123` with your EID and `yourpassword` with, well, your password):
```
export http_proxy="http://ABC123:yourpassword@10.37.135.39:8099/"
export https_proxy=$http_proxy
```
(Note: if you already have a `.bashrc` file, just add these two lines in there)

- This gets run every time you open a terminal, so these values will
be set from now on in all future terminals, but they are not run yet on this one. Either
  - quit the terminal and you're good for the future
  - or if you need proxy to work on this very terminal right now, type `source ~/.bashrc` to run this file we edited

<p style="page-break-after:always;"></p>

# Installation of Packages and Setup
- Version control: [Git](https://git-scm.com/)
  - When running the installer, the default settings are good - no
  need to monkey with them.
- Get an account at [GitHub.com](http://github.com)
- Text editor: [Atom](https://atom.io/)
- Python + libraries: Anaconda (version 2.2 or later)
  - **If you already have Anaconda installed** (for *Python I & II* courses or other reasons):
      - We need to update it to the latest version (and install the seaborn module)
      - Open up a terminal (*Anaconda Command Prompt* in Windows, *Terminal* in OS X/Linux)
      - Execute the following commands
      ```
conda update conda
conda update anaconda
conda install seaborn
      ```
      - If the proxy settings are correct, this should work without problems. If it doesn't, go back and check / redo the proxy configuration steps. If it still doesn't work and you cannot solve it, don't worry we will help you out and get it working on the first day of class.
  - **If you don't have Anaconda**
      - [Install it](http://continuum.io/downloads)
      - Open up a terminal (*Anaconda Command Prompt* in Windows, *Terminal* in OS X/Linux)
      - Execute the following command
      ```
conda install seaborn
      ```
      - If the proxy settings are correct, this should work without problems. If it doesn't, go back and check / redo the proxy configuration steps. If it still doesn't work and you cannot solve it, don't worry we will help you out and get it working on the first day of class.

