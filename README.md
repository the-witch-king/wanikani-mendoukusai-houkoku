# wanikani-mendoukusai-houkoku

Generates a report of troublesome items in your WaniKani account. These are items that are older than 12 months (1 year!) which means they are items that have given you some trobule in keeping them locked in your brain.

Toss this CSV into any ol' spreadsheet software to get a nice overview.

Each item will contain:

- Characters
- Type (Radical | Kanji | Vocabulary)
- Date seen (first time you learned it)
- Level Encountered
- Link to the WaniKani page for said item

How you go about improving your retention of these items is entirely up to you from this point. My plan is to write them out by hand, but if you have another strategy, please let me know.

## Installing Dependancies

If you don't want to install global dependancies, use [Poetry](https://python-poetry.org/)!

Once you've installed Poetry, change into the directory where you cloned this repo and run:

```
poetry install
```

Your dependancies are now installed. すごい！

## Get your WaniKani API Key

In order to use this tool, you must provide your WaniKani API key. When running the script, you will be prompted for it (and it will be saved to a `.env` file).

To get your key, sign in to WaniKani and go to the [Settings/API Tokens](https://www.wanikani.com/settings/personal_access_tokens) page. Your key will be there.

## Running the Report

Generating the report is pretty simple.

```
# Used Poetry
poetry run python main.py

# Unpoetic (this was only tested with Python 3.9)
python main.py
```

The report will be saved to a file called `report.csv` by default.

There are some command line arguments you can use as well:

```
-h, --help  Get Help
-m, --months Set amount of minimum amount of months since encountering item to include in report (default is 12)
-o, --out Path to save the CSV to
```
