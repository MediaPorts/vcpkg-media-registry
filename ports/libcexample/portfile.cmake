set(VCPKG_POLICY_SKIP_COPYRIGHT_CHECK enabled)

vcpkg_download_distfile(ARCHIVE
    URLS "http://127.0.0.1:8000/vcpkg-wtoe-registry/examples/dists/libcexample-${VERSION}.7z"
    FILENAME "libcexample-${VERSION}.7z"
    SHA512 E93AE5743F15ACBAD66A25D64E7665599028A37C8A01FB815D1BE204D4C29CA4A5313E809EBA2C8769551B3C88E6EB0D56F9B92FEF73231443E00FB27790545C
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


