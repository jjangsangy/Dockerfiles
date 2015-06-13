install_anaconda() {

    local pkg=${1} dest=${2}
    bash "${pkg}" -b -p "${dest}"
}

check_installer() {

    if [ -r "./src/${INSTALLER}" ]; then
        printf "Found Installer: %s\n" "./src/${INSTALLER}"
        mv ./src/${INSTALLER} .
    else
        printf "Downloading Installer: %s\n" "${LINK}"
        curl -O "${LINK}"
    fi

}

main() {
    check_installer
    install_anaconda "${INSTALLER}" "/opt/conda"
    rm "${INSTALLER}"
}


main
