set(VCPKG_POLICY_SKIP_COPYRIGHT_CHECK enabled)

vcpkg_download_distfile(ARCHIVE
    URLS "http://127.0.0.1:8000/vcpkg-wtoe-registry/examples/dists/libcppexample-${VERSION}.7z"
    FILENAME "libcppexample-${VERSION}.7z"
    SHA512 7A5F4B4CC51090DE08436E54425598818724930E56CF0CE6AB18E6216D097FB75225D082309A4B6CFCA9738EA2249B219FEC4FAB90C79E86D8F74299AF9A837F
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


