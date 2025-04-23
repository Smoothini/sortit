# sortit 👌

Small utility to sort one of those very messy folders (like my download folder). Reads the yaml configuration, based on which it will create or use sub folders in the new root location upon running. Logs everything.


I wanted to initially add support for moving folders if there's an archive or a html file or such, but combinations were too many so for now it just skips over em.


## How to

Change the yaml config to your liking.

``` yaml
---
include:
  music:
    - mp3
    - flac
  docs:
    - docx
    - pdf
exclude:
  files:
    - sort.py
    - somefancyscript.sh
```

Based on the above example, upon scanning the root directory it will place all the mp3 and flac files into a subfolder called music, and also all the docx and pdf's into a docs folder, while making sure to ignore the 2 files, sort.py and somefancescript.py.
Make sure the `root`, `new_root`, `config_location` and `log_location` are setup before running, and enjoy having a sorted life I guess.
