# CookieCrasher c.1 firmware and solutions

Two firmware versions are provided, the "standard" challenge firmware plus a "sidechannel" version that alternates a pin on every RSA mod-pow loop iteration.

Furthermore, solution.txt already provides the solution expected by the flagservice.

cookieserver/ contains the full server side code

## Build instructions

- Build micropython from master source according to docs
- apply micropython.patch to the master source
- create symlink ports/rp2/boards/powerslot pointing to ./board/
- Build with `make BOARD=powerslot PICO_BOARD_HEADER_DIRS=path/to/./board/ FROZEN_MANIFEST=path/to/./manifest-...`
