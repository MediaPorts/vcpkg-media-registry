set(VCPKG_POLICY_SKIP_COPYRIGHT_CHECK enabled)

vcpkg_download_distfile(ARCHIVE
    URLS "http://127.0.0.1:8000/vcpkg-wtoe-registry/examples/archives/libcexample-${VERSION}.7z"
    FILENAME "libcexample-${VERSION}.7z"
    SHA512 1222FD38C1BDD2F1EA40D3ADD28F818511F873B68921CFE6DE30F2FA72D038DA7A5F99A35C435A23D493FDDD981830C4F73B13897303BD26DBB018CC0B32F5FE
)

vcpkg_extract_source_archive(
    SOURCE_PATH
    ARCHIVE "${ARCHIVE}"
)

vcpkg_cmake_configure(
    SOURCE_PATH ${SOURCE_PATH}
)

vcpkg_cmake_install()
vcpkg_cmake_config_fixup()
vcpkg_copy_pdbs()
vcpkg_fixup_pkgconfig()


file(REMOVE_RECURSE
    "${CURRENT_PACKAGES_DIR}/debug/include"
    "${CURRENT_PACKAGES_DIR}/debug/share"
)


