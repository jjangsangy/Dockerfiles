#!/bin/bash
# If you place an anaconda installer in the src directory
# Docker will default to using your versionn of Anaconda
#
# This can be utilizes to cache installations so that
# and not require going over the wire evry time

check_installer() {

    if ! [ -r "${INSTALLER}" ]; then
        printf "Downloading Installer: %s\n" "${LINK}"
        curl -O "${LINK}"
    fi
}

check_installer && bash "${INSTALLER}" -b -p "/opt/conda" && rm "${INSTALLER}"
