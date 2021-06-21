#    AccGenBot
#    Copyright © 2021 SoulHackz

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    See < https://github.com/SoulHackz/AccGenBot/blob/master/LICENSE > 
#    for the license.

import glob
from pathlib import Path
from AccGenBot.utils import load_plugins
import logging
from . import AccGenBot

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "AccGenBot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
    
print("Successfully deployed AccountGenerator Bot!")

if __name__ == "__main__":
    AccGenBot.run_until_disconnected()
