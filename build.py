#!/usr/bin/env python3

import os
import sys
import shutil

from glob import glob
from debian import deb822
from xml.dom.minidom import Document

def main(dir):
    num = 0

    doc = Document()
    events = doc.createElement('data')
    doc.appendChild(events)

    for filename in glob(os.path.join(dir, '*')):
        print(f"Reading events from {filename}", file=sys.stderr)
        with open(filename, encoding='utf-8') as f:
            input_lines = f.read().split('\n')

        for para in deb822.Deb822.iter_paragraphs(input_lines, use_apt_pkg=False):
            events.appendChild(create_event(doc, para))
            sys.stderr.write('.')
            num += 1
        print(file=sys.stderr)

    print(f"Writing {num} events", file=sys.stderr)

    print(f'<!-- Generated from {dir}/* - do not edit -->')
    print(events.toprettyxml(indent='  '))

def create_event(doc, para):
    entry = doc.createElement('entry')
    entry.setAttribute('title', para['Title'])

    if 'Start-Date' in para:
        entry.setAttribute('isDuration', 'true')
        entry.setAttribute('start', para['Start-Date'])
        entry.setAttribute('end', para['End-Date'])
    else:
        entry.setAttribute('start', para['Date'])

    if 'Source' in para:
        text = doc.createTextNode(f'<a href="{para["Source"]}">Source</a>')
        entry.appendChild(text)

    return entry

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
