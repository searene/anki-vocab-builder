#!/bin/bash

# This script is used to deploy the add-on to Anki

PACKAGE_DIR=/tmp/word_fellow
ANKI_ADDON_DIR=$HOME/AppData/Roaming/Anki2/addons21

./package.sh "${PACKAGE_DIR}"

rm -rf "${ANKI_ADDON_DIR}/word_fellow"
unzip "${PACKAGE_DIR}/word_fellow.ankiaddon" -d "${ANKI_ADDON_DIR}/word_fellow"