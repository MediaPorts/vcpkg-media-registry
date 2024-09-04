set(VCPKG_POLICY_SKIP_COPYRIGHT_CHECK enabled)
set(VCPKG_POLICY_EMPTY_INCLUDE_FOLDER enabled)
set(VCPKG_POLICY_ALLOW_EXES_IN_BIN enabled)
set(VCPKG_POLICY_DLLS_IN_STATIC_LIBRARY enabled)

vcpkg_download_distfile(ARCHIVE
    URLS "http://127.0.0.1:8000/vcpkg-wtoe-registry/examples/dists/testexample-${VERSION}.7z"
    FILENAME "testexample-${VERSION}.7z"
    SHA512 0CEB2C1EC8176EDEF3B3BB60F640F03FD0D09E5F85BA4975E54E0514BBC2698EAA50576F085B4F2323B3C9CEED764F53819656C37B0731C7C555E63C9485039D
)

vcpkg_extract_source_archive(
    SOURCE_PATH
    ARCHIVE "${ARCHIVE}"
)

vcpkg_cmake_configure(
    SOURCE_PATH ${SOURCE_PATH}
)

vcpkg_cmake_install()
vcpkg_copy_pdbs()


