set(VCPKG_POLICY_SKIP_COPYRIGHT_CHECK enabled)
set(VCPKG_POLICY_EMPTY_INCLUDE_FOLDER enabled)
set(VCPKG_POLICY_ALLOW_EXES_IN_BIN enabled)
set(VCPKG_POLICY_DLLS_IN_STATIC_LIBRARY enabled)

vcpkg_download_distfile(ARCHIVE
    URLS "http://127.0.0.1:8000/vcpkg-wtoe-registry/examples/archives/testexample-${VERSION}.7z"
    FILENAME "testexample-${VERSION}.7z"
    SHA512 A19031F542EBAFEE574CB39D56359AF213C3BFE7F1DE99D2628C1F9BA1B5404E68F9243E571A95E904E00B74EFB49FE81BD550DE3AABA2A184F49ABB0E5C9B7A
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


