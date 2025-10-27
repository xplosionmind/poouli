<div align=center>
	<h1>🗃️ Pöuli 🐙</h1>
	<p>Synchronize local files with MediaWiki instances.</p>
</div>

## ℹ️ About

This tool was originally conceived by [Tommi](https://pzwiki.wdka.nl/mediadesign/User:Tommi 'User:Tommi on the XPUB Wiki') to upload a subset of their personal knowledge repository, [*the Jam*](https://tommi.space/jam/), with their Personal Reader, [*PaJamas*](https://pzwiki.wdka.nl/mediadesign/User:Tommi/PaJamas 'PaJamas Homepage on the XPUB Wiki'). Hopefully, it can flourish beyond this specific use-case, and be helpful for other XPUB students or wiki adventurers.

## ✨ Meaning

The name “Pöuli” (equivalent of PoOuli) stands for:

- Practically Often Used Lovely Interface
- Petty yet Outstanding Utility Leading to Integration
- Phenomenal Optimistic Useful Lovely Idea
- Paradoxically Obscure but Unstoppable Link Ignitor

It is the anagram of [Oulipo](https://en.wikipedia.org/wiki/Oulipo 'Oulipo on Wikipedia'), an eclectic, mad, and maddening collective of artists formed in the ’60s.

+++ IDEA: Writing machine name generator

## ⏬ Installation

The installation instructions assume you are using [uv](https://docs.astral.sh/uv/ 'uv’s documentation homepage').

+++ TODO

## ⚙️ Configuration

The initial configuration requires to follow the following steps.

1. Generate a Bot Password in MediaWiki:
	1. Visit <https://pzwiki.wdka.nl/mediadesign/Special:BotPasswords>
	1. Generate a bot
	1. Save the chosen bot name and its generated password
1. Run `pwb generate_family_file` to tell the script that you want to use the XPUB’s wiki as the reference wiki
1. Run `pwb generate_user_files` to provide the login credentials retrieved while generating a Bot Password
1. Run `pwb login` to establish the connection and to check if everything is working nominally
1. Create a YAML configuration file in the config directory or in the script’s directory, with the following data:
	- **`local_directory`**: path of the directory for the local files
	- **`wiki_base_path`**: the path of the main page within which the local files should be synchronized (can be overwritten by `permalink_wiki` in each note’s front matter)
	- `banner` (optional): path to an HTML file to include at the end of all wiki pages published via Pöuli, unless `wiki_banner` is `False` in the frontmatter.
	- `styling` (optional): path to an HTML file to include at the end of all wiki pages published via Pöuli, *if and only if* `wiki_styling` is `True` in the frontmatter.

## 📡 Usage

+++ TODO

## 🤔 To-do list

An unsorted list of things to do. Everything will be moved to proper issue tracking after the first release.

- Handle images
- Get configuration settings from command line arguments, overriding config file instructions
- Links management and testing
	- local → local private
	- local → local public (on tommi.space)
	- local → local synchronized
	- local → Wiki (as a regular https link)
	- Wiki → Jam (as a regular https link to tommi.space)
	- Wiki → Wiki (not part of Pajamas)
	- Wiki → Wiki
	- Anchor links
		- same page
		- another page
- Deal with Categories (see below)
- Note metadata
	- `aliases`
	- `updated`
	- `wiki_categories`
- Move the Wiki information and credentials to the YAML configuration file. Ideally, no scripts or commands should be required to run before the main one.
- test on Windows
- Get wiki pages that are in the specified subpage but are not found locally
- Transclusion
	- transform `<includeonly>` (and similar) to `<div id=includeonly>` in Markdown
	- How to transform anchor transclusions in MediaWiki? It’s not supported
- Exclude JSON and YAML files from the source directory
- Test how references and foonotes work
- Add `dict` and instructions about how the script works

## ♻️ License

Everything inside this repository is licensed under the [European Union Public License](https://eupl.eu 'EUPL [European Union Public Licence]').
