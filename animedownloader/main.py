import requests
from bs4 import BeautifulSoup
import argparse
import os
import subprocess

def download_with_qbittorrent(magnet_link, save_path, category):
    cmd = [
        "qbittorrent",
        magnet_link,
        f"--save-path={save_path}",
        f"--category={category}",
        "--skip-dialog=true"
    ]
    try:
        subprocess.run(cmd, check=True)
        print("Download started with qbittorrent.")
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        print("Failed to start download with qbittorrent.")

def search_anime_tosho(query, episode_number=None, blacklist=None, preferred_terms=None):
    if blacklist is None:
        blacklist = []

    if preferred_terms is None:
        preferred_terms = []

    url = "https://animetosho.org/search"
    params = {
        "q": query
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        entries = soup.find_all(class_="home_list_entry")

        best_match = None
        best_match_weight = -1

        for entry in entries:
            title = entry.find(class_="link").text.lower()
            if any(bl_term.lower() in title for bl_term in blacklist):
                continue

            if episode_number is not None:
                episode_str = str(episode_number)
                if episode_str not in title:
                    continue

            weight = sum(pref_term.lower() in title for pref_term in preferred_terms)
            if weight > best_match_weight:
                magnet_link = entry.find(href=lambda href: href and "magnet:?" in href)
                if magnet_link:
                    best_match = magnet_link["href"]
                    best_match_weight = weight

        return best_match

    return None

def main():
    parser = argparse.ArgumentParser(description="Search Anime Tosho for magnet links.")
    parser.add_argument("search_term", type=str, help="The search term (name of the anime).")
    parser.add_argument("--episode", "-e", type=int, default=None, help="The episode number.")
    parser.add_argument("--blacklist", "-b", nargs="*", default=[], help="List of blacklisted terms.")
    parser.add_argument("--preferred", "-p", nargs="*", default=[], help="List of preferred terms.")
    parser.add_argument("--category", "-c", type=str, default="tv-sonarr", help="The torrent category")

    args = parser.parse_args()

    magnet_link = search_anime_tosho(args.search_term, args.episode, args.blacklist, args.preferred)
    if magnet_link:
        print("Magnet link found:", magnet_link)
        download_with_qbittorrent(magnet_link, "/mnt/storage/Downloads", args.category)
    else:
        print("No magnet link found for the given search term and blacklist.")

# Call the main function when the script is run as the main program
if __name__ == "__main__":
    main()
