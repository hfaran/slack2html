### This project is a wrapper on top of [`slack-export-viewer`](https://github.com/hfaran/slack-export-viewer)

# `slack2html`

Export and view your entire team's Slack history (even on a free plan)
as HTML (in channels)!
![Preview](screenshot.png)

## Usage

### 1) Grab your Slack team's export

* Visit [https://yourslackteam.slack.com/services/export]
(https://yourslackteam.slack.com/services/export) (*yourslackteam* should obviously be replaced with your **actual** Slack team)
* Create an export
* Wait for it to complete
* Refresh the page and download the export (.zip file) into whatever directory

### 2) Point `slack2html` to it

Point slack2html to the .zip file and let it do its magic

```bash
./slack2html.py -z /path/to/export/zip -o /path/to/output/dir
```

If everything went well, your archive will have been extracted, processed, and browser window will have opened showing your *#general* channel from the export.
