#!C:/Users/XBBNQVM/miniconda3/envs/compapp\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'wxPython==4.0.2','console_scripts','helpviewer'
__requires__ = 'wxPython==4.0.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('wxPython==4.0.2', 'console_scripts', 'helpviewer')()
    )
