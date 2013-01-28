import os.path
from subprocess import check_call

def compile(module, source_folder, target_folder, locale=None, locale_all=False):
    cdir = os.path.abspath(os.path.dirname(__file__))
    gcin = os.path.join(cdir, 'gcin/bin/createjs')
    cmd = [
        gcin,
        '-n', module,
        '-d', source_folder,
        '-o', target_folder
    ]
    if locale:
        cmd.append('--po=' + locale)

    if locale_all:
        cmd.append('-s')

    print "Running gcin: ", ' '.join(cmd)
    check_call(cmd)
    print "Done"

