# Spoti-Term
**ONLY WORKS ON MAC SINCE IT USES APPLESCRIPT!!**
Simple script to show basic information about the current playing song on Spotify in terminal. It prints a ASCII version of the album cover, the song name, the artist and the album name.
## How to use
After cloning the repository, you can run the following command to install the dependencies:
```bash
chmod a+x install.sh
chmod a+x spoti-term.sh
./install.sh
```
Then just execute `run_app.sh` whenever you want to see the current playing song on Spotify.

### Clickable Executable
In case you want to have a clickable executable on MacOS, just right click on `run_app.sh` and select `Open with > Other...`, then select `Terminal` (to do so you need to change from `Recommended Applications` to `All Applications`). Finally, check the box `Always Open With` and click `Open`.

## General Issues and To-Do's
- The cover is not centered, but that should be an easy (?) fix
- Pretty sure it could be optimized to run only when the key for new song is clicked, instead of constantly checking
