set(VCPKG_POLICY_SKIP_COPYRIGHT_CHECK enabled)

vcpkg_download_distfile(ARCHIVE
    URLS "http://127.0.0.1:8000/vcpkg-wtoe-registry/examples/archives/libcppexample-${VERSION}.7z"
    FILENAME "libcppexample-${VERSION}.7z"
    SHA512 5CD7250183F81D4FA76A31E42088F6E3D2837CFD0A3A97C14E5A0B5DB1A3CAA415F9B46BC209FA2065B6AD76293C5B4EA6C14DC5D44C680625548C1ED0020882
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


