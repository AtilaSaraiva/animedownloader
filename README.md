# Anime Downloader

Anime Downloader is a simple command-line tool to search for anime torrents on Anime Tosho and download them using qBittorrent.

## Features

- Search for anime torrents on Anime Tosho using a given search term
- Specify an episode number to narrow down the search
- Provide a list of blacklisted terms to avoid certain releases
- Provide a list of preferred terms to prioritize specific releases
- Automatically download the torrent using qBittorrent

## Installation

1. Clone this repository:

> $ git clone https://github.com/AtilaSaraiva/anime-downloader.git

    Change into the cloned directory:

> $ cd anime-downloader

    Install the package:


> $ pip install -e .

## Usage


> $ anime-downloader "search_term" --episode <episode_number> --blacklist <blacklist_terms> --preferred <preferred_terms>

### Example


> $ anime-downloader "onmyouji" --episode 12 --blacklist dub --preferred 720p

This will search for the 12th episode of "Onmyouji", avoiding "dub" releases and preferring "720p" torrents. It will then download the torrent using qBittorrent.

## Requirements

    Python 3.6+
    qBittorrent

## Dependencies

    requests
    beautifulsoup4
    argparse

This tool is for educational purposes only. Please support the creators and distributors of the anime by purchasing their releases or subscribing to legal streaming services.
