import subprocess as sp

def unpack7z(file, outputDir = '.'):
    sp.call(['7z', 'x', file, '-y', '-o%s' % outputDir])
