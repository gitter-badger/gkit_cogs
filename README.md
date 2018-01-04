[![PyPI](https://img.shields.io/badge/Python-3.5-blue.svg)](https://www.python.org/downloads/) 
[![Red Bot](https://img.shields.io/badge/Red-V3-red.svg)](https://github.com/Twentysix26/Red-DiscordBot)
[![Cogs.Red](https://img.shields.io/badge/Cogs.Red-gkit__cogs-red.svg)](https://cogs.red/cogs/gannon93/gkit_cogs/)

# Gannon Toolkit Library - Cogs (gkit_cogs)

Shoot me a discord message: **Gannon#0851**

---

## DESCRIPTION

This repository is a collection of cogs written for [Twentysix's](https://github.com/Twentysix26) [Red-DiscordBot](https://github.com/Cog-Creators/Red-DiscordBot).  

> Red is a fully modular bot – meaning all features and commands can be enabled/disabled to your liking, making it completely customizable.

Much of my cogs started as dog trash "generate a random number and say a random meme from a pre-defined dictionary of phrases", but the repo is slowly gaining actual utilization. Check out VapeNaysh and ArkAdvisor (when it's released) for some non-garbage cogs.

---

## [:book:](https://github.com/gannon93/gkit_cogs/wiki/Cogs) [:mute:](https://cogs.red/cogs/gannon93/gkit_cogs/) COGS

The following is a list of my available cogs.  

  - Click :book: to go to the GitHub Wiki page.
  - Click :mute: to go the the [Cogs.Red](https://cogs.red) page.

---

## QUALITY 10/10 WOULD DOWNLOAD AGAIN COGS

[:book:](https://github.com/gannon93/gkit_cogs/wiki/ArkAdvisor) [:mute:](https://cogs.red/cogs/gannon93/gkit_cogs/arkadvisor/) **[ALPHA]** _**ArkAdvisor**_ (`arkadvisor`)
  - All of your _**ARK: Survival Evolved**_ needs at your fingertips.
  - Requires:
    - [BeautifulSoup4](https://pypi.python.org/pypi/beautifulsoup4) (`pip install beautifulsoup4`)
  - Commands:
    - `ark`

      | Sub-Command | Options | Description |
      | ----------- | ------- | ----------- |
      | _tame_ | - `dino_name` (String) or `dino_id` (Integer) | Lookup taming info for a dino (kibble & method so far) |
      | _give_ | - `mod_name` (String) or `mod_id` (Integer) or None (None),<br />- `item_name` (String) or `item_id` (Integer),<br />- `amount` (Integer),<br />- `quality` (Integer) | Builds cheat command to give the player items |
      | _spawn_ | - `dino_name` (String) or `dino_id` (Integer),<br />- `do_tame` (Boolean) | Builds cheat command to spawn a dino, which can be tamed or wild

---

[:book:](https://github.com/gannon93/gkit_cogs/wiki/VapeNaysh) [:mute:](https://cogs.red/cogs/gannon93/gkit_cogs/vapenaysh/) **[NEW]** _**VapeNaysh**_ (`vapenaysh`)
  - Vape Naysh yall `\//\`
  - Requires:
    - [BeautifulSoup4](https://pypi.python.org/pypi/beautifulsoup4) (`pip install beautifulsoup4`)
  - Commands:
    - `vape`

      | Sub-Command | Options | Description |
      | ----------- | ------- | ----------- |
      | _bdv_ | - `flavor`| Search for a flavor on Blue Dot Vapors |
      | _wlj_ | - `flavor`| Search for a flavor on White Label Juice Co. |

---

## GARBAGE COGS

[:book:](https://github.com/gannon93/gkit_cogs/wiki/BASTA!) [:mute:](https://cogs.red/cogs/gannon93/gkit_cogs/basta/) _**BASTA!**_ (`basta`)
  - And so the lord said to me, _**BASTA!**_
  - Commands:
    - `basta`

      | Sub-Command | Options | Description |
      | ----------- | ------- | ----------- |
      | _santa_ | | |
      | _satan_ | | |
      | _user_ | - `user` | |

---

[:book:](https://github.com/gannon93/gkit_cogs/wiki/FlavorSavor) [:mute:](https://cogs.red/cogs/gannon93/gkit_cogs/flavorsavor/) _**FlavorSavor**_ (`flavorsavor`)
  - Savor that Fieri flavor!
  - Commands:
    - `savor`

      | Sub-Command | Options | Description |
      | ----------- | ------- | ----------- |
      | _gusto_ | | |
      | _juicy_ | | |
      | _spicy_ | | |

    - `taste`

      | Sub-Command | Options | Description |
      | ----------- | ------- | ----------- |
      | _bitter_ | | |
      | _salty_ | | |
      | _sour_ | | |
      | _sweet_ | | |
      | _umami_ | | |

---

[:book:](https://github.com/gannon93/gkit_cogs/wiki/PEP20) [:mute:](https://cogs.red/cogs/gannon93/gkit_cogs/pep20/) _**PEP20**_ (`pep20`)
  - The word of the BDFL is law.
  - Commands:
    - `bdlf`

      | Sub-Command | Options | Description |
      | ----------- | ------- | ----------- |
      | _assimilate_ | | |
      | _pontificate_ | | |
      | _preach_ | | |

---

[:book:](https://github.com/gannon93/gkit_cogs/wiki/WannaCookie) [:mute:](https://cogs.red/cogs/gannon93/gkit_cogs/wannacookie/) _**WannaCookie**_ (`wannacookie`)
  - What, do you want a... ?
  - Commands:
    - `wanna`

      | Sub-Command | Options | Description |
      | ----------- | ------- | ----------- |
      | _cookie_ | - `user` | |
      | _goldstar_ | - `user` | |

---

## SUSPENDED COGS

[:book:](https://github.com/gannon93/gkit_cogs/wiki/SaltyDebt) [:mute:](https://cogs.red/cogs/gannon93/gkit_cogs/saltydebt/) **[SUSPENDED]** _**SaltyDebt**_ (`saltydebt`)
  - Feed your Salty Bet gambling addiction.
  - Commands:
    - `salty`

      | Sub-Command | Options | Description |
      | ----------- | ------- | ----------- |
      | _balance_ | | |
      | _bet_ | | |
      | _cashout_ | | |

---

## INSTALLATION

These cogs are in _**very**_ early development, but can be downloaded through Red's distributor and [Cogs.Red](https://cogs.red/cogs/gannon93/gkit_cogs/):  

  - `[p]cog repo add gkit_cogs https://github.com/gannon93/gkit_cogs`
  - `[p]cog install gkit_cogs <cog>`
    - Available `<cog>` options: `arkadvisor`, `basta`, `flavorsavor`, `pep20`, `vapenaysh`, `wannacookie`

---

## CONTRIBUTION

Found a bug or thinking of a way to add some extra spice to my cogs?  
Boy oh boy, you better add an issue and a PR if you can fix the bug or add the enhancement yourself.  

Follow these 5 easy steps for a successful contribution (by [@Redjumpman](https://github.com/Redjumpman)):

  1. Fork it!
  2. Develop your feature branch
  3. Commit your changes
  4. Push to the main branch
  5. Submit a pull request

---

## LICENSE

The project is licensed under [MIT](https://github.com/gannon93/gkit_cogs/blob/master/LICENSE). Feel free to alter this project anyway you see fit, as long as I am credited for the original work.

---

## CREDITS and THANKS

  - [@Twentysix26](https://github.com/Twentysix26), for making a great Python subcommunity and finally providing me with a platform to exercise my Python/Gaming/Internet passion. 
  - [@Redjumpman](https://github.com/Redjumpman) and [@irdumbs](https://github.com/irdumbs), for unknowingly being my Cog Creator senseis. 
  - [@Orels1](https://github.com/orels1), for creating the swanky Red-Portal cog registry at [Cogs.Red](http://cogs.red).
  - The Red community, for constantly coming up with bigger and better ideas for cogs.
