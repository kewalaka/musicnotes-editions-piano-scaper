# MusicNotes Editions Piano Scaper

> [!NOTE]
> This is not official, nor in any way endorsed by MusicNotes

This scrapes the contents of the MusicNotes website for metadata about piano scores, from the "Musicnotes Editions", i.e. the list that is offered for each month of a [MusicNotes Pro subscription](https://www.musicnotes.com/pro)

It was created because the official location only lets you see 30 scores per page, and there's a lot of pages.

## Usage

Inside this repository is a [CSV file](https://raw.githubusercontent.com/kewalaka/musicnotes-editions-piano-scaper/main/music-notes-output.csv) that you can import into your favourite spreadsheet, and filter and search to your hearts content.

The CSV export was created in Dec 2023.

## Information collected

Information exported includes:
- title
- artist
- scoring (e.g. "Piano/Vocal")
- instruments (including vocal range if provided)
- key
- url
- rating (sometimes, see known issues).

The list is taken from the official [location](https://www.musicnotes.com/search/go?p=Q&lbc=musicnotes&w=*&isort=score&method=and&view=list&af=producttype:lilnotemned&intcmp=HomePage:Position1:FreeMNE), which is provided the [MusicNotes search FAQ](https://help.musicnotes.com/hc/en-us/articles/360055349572-Searching-for-music), and filtered by Piano.

## Known issues

The information comes from the public website, using information embedded in a data block.  Some scores don't have the rating available in this tabular location, which is why it can be empty even if there is a rating when you click on the score.

## Fixes, suggestions

...are welcome, though I'm not planning to keep this up to date.
