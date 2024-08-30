#### How to add a new port from git named libdvdcss from scratch

- 1. add ports/libdvdcss/portfile.cmake (for example [ports/libdvdcss/portfile.cmake](https://github.com/MediaPorts/vcpkg-media-registry/blob/main/ports/libdvdcss/portfile.cmake))
- 2. add ports/libdvdcss/vcpkg.json (for example [ports/libdvdcss/vcpkg.json](https://github.com/MediaPorts/vcpkg-media-registry/blob/main/ports/libdvdcss/vcpkg.json))
- 3. add other files if necessary (for example [ports/libdvdcss/portfile.cmake](https://github.com/MediaPorts/vcpkg-media-registry/blob/main/ports/libdvdcss/libdvdcss-config.cmake.in))
- 4. git add ports/libdvdcss/*
- 5. git commit -m "[libdvdcss] add libdvdcss 1.4.2 (d0b6a291) from videolan with cmake and uwp support"
- 6. git rev-parse HEAD:ports/libdvdcss
- 7. update versions/l-/libdvdcss.json with git-parse result (git-tree)
- 8. vcpkg search libdvdcss
- 9. vcpkg install libdvdcss
- 10. update versions/baseline.json (or vcpkg x-add-version libdvdcss)
- 11. git add versions/l-/libdvdcss.json versions/baseline.json versions/l-/libdvdcss.json
- 12. git commit -m "[libdvdcss] add 1.4.2 (d0b6a291) to versions"
- 13. git push
