# avi502 profile — setup

## 1. Publish
    # repo must be named exactly: avi502  (public)
    git init && git add . && git commit -m "feat: animated terminal profile"
    git branch -M main
    git remote add origin https://github.com/avi502/avi502.git
    git push -u origin main --force      # --force replaces the existing README

## 2. Enable the daily heatmap refresh
Repo -> Settings -> Actions -> General -> Workflow permissions -> **Read and write** -> Save.
Then Actions -> "Update profile art" -> Run workflow.
(`assets/contrib-heatmap.svg` is an empty placeholder; the first run fills it with your real data.)

## 3. Optional: ASCII portrait (needs your photo)
    pip install -r scripts/requirements-local.txt -r scripts/requirements.txt
    python scripts/prep_photo.py photo.jpg source-prepped.png
    python scripts/make_ascii_svg.py source-prepped.png assets/avi-ascii.svg
    # preview final frame: STATIC=1 python scripts/make_ascii_svg.py ...
Then swap the portrait table in README.md (instructions are in the comment at the top).

## Regenerate the wordmark
    WORDMARK_TEXT=AVISEKH python scripts/make_wordmark_svg.py --mode rock --out assets/wordmark.svg
(Set WORDMARK_FONT to a bold .ttf if the default font isn't found on your OS.)
