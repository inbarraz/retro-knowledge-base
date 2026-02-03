# Acorn

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| BBC Master 128 | Desktop Computer | [3JcUtkCjF-0], [KddR9KSRx4Y] |
| BBC Model B | Desktop Computer | [3JcUtkCjF-0], [KddR9KSRx4Y] |
| BBC Model B+ | Desktop Computer | [3JcUtkCjF-0] |
| Acorn Electron | Desktop Computer | [3JcUtkCjF-0] |
| Acorn Mouse | Peripheral | [KddR9KSRx4Y] |

## Platform-Specific Knowledge

### BBC Master 128

#### Machine Operating System (MOS) Versions
- MOS 3.2: Original Master ROM - Source: [3JcUtkCjF-0]
- MOS 3.5: Newest version with Y2K clock bug fix - Source: [3JcUtkCjF-0]
- MOS 2.0: From BBC Model B+ (64K variant) - Source: [3JcUtkCjF-0]
- OS 1.2: From original BBC Model B - Source: [3JcUtkCjF-0]
- Use `*HELP` command to see current MOS version - Source: [3JcUtkCjF-0]

#### Compatibility Issues
- Some older BBC games have corruption/issues on Master - Source: [3JcUtkCjF-0]
- Architectural differences between Model B and Master cause incompatibilities - Source: [3JcUtkCjF-0]
- Running older MOS ROMs may help with compatibility (unconfirmed) - Source: [3JcUtkCjF-0]

#### Internal Headers/Ports
- Modem port header: Can be repurposed for second user port - Source: [3JcUtkCjF-0]
- User port on bottom of machine: Standard peripheral connection - Source: [3JcUtkCjF-0]
- Tube interface: Allows co-processor expansion (Z80, ARM, etc.) - Source: [3JcUtkCjF-0]
- Econet networking capability - Source: [3JcUtkCjF-0]

#### ROM Sockets
- Multiple ROM sockets available for expansion - Source: [3JcUtkCjF-0]
- Can install switchable ROM boards with jumpers - Source: [3JcUtkCjF-0]
- `*UNPLUG` and `*INSERT` commands manage ROM activation - Source: [3JcUtkCjF-0]

### SD Card Solutions

#### Internal SD Card (Modem Port Adapter)
- Plugs into internal modem port header at address FE80 - Source: [3JcUtkCjF-0]
- Adds second user port plus SD card reader - Source: [3JcUtkCjF-0]
- Includes 6522 VIA chip for additional I/O - Source: [3JcUtkCjF-0]
- Frees external user port for other devices (AMX Mouse, BBC Turtle) - Source: [3JcUtkCjF-0]
- SD card slot can be mounted through case slot near power supply - Source: [3JcUtkCjF-0]
- Commands: `*CARD` to select card, `*.` for directory, Shift+Break to boot menu - Source: [3JcUtkCjF-0]

#### External SD Card (User Port)
- Simple solution using user port on bottom of machine - Source: [3JcUtkCjF-0]
- Can be hot-glued directly to user port connector - Source: [3JcUtkCjF-0]
- Uses MMFS ROM for file system support - Source: [3JcUtkCjF-0]

#### MMFS (Mass Memory File System)
- File system for SD cards on BBC machines - Source: [3JcUtkCjF-0]
- Original MMFS: Uses single .MMB file containing all disc images - Source: [3JcUtkCjF-0]
- MMFS2: Uses individual .SSD disc images - Source: [3JcUtkCjF-0]
- Only one MMFS ROM should be active at a time - Source: [3JcUtkCjF-0]

### Video Output

#### RGB Output
- Uses D-connector (not standard DE-9 CGA pinout) - Source: [3JcUtkCjF-0]
- TTL RGB levels (like CGA) - Source: [3JcUtkCjF-0]
- No intensity bit - ground the intensity pin - Source: [3JcUtkCjF-0]
- Composite sync instead of separate H/V sync - Source: [3JcUtkCjF-0]
- Same RGB pinout works with Acorn Electron - Source: [3JcUtkCjF-0]
- For RGB2HDMI: Wire sync to both H-sync and V-sync pins - Source: [3JcUtkCjF-0]
- Composite video output also available - Source: [3JcUtkCjF-0]

### Clock/Battery

#### NecroWare Clock Module
- Replacement for original clock chip and battery - Source: [3JcUtkCjF-0]
- Uses sealed lithium cell (10+ year life) - Source: [3JcUtkCjF-0]
- Eliminates leaky battery concerns - Source: [3JcUtkCjF-0]
- GitHub repo recommends 10K pull-up on Motorola pin for safety - Source: [3JcUtkCjF-0]

### Keyboard

#### Key Switch Issues
- Oxidized shafts inside key switches cause contact problems - Source: [3JcUtkCjF-0]
- Fix: Scratch and polish the shafts - Source: [3JcUtkCjF-0]
- Keyboard feel is excellent when working properly - Source: [3JcUtkCjF-0]

### Historical Notes

#### ARM Processor Development
- Original ARM (Acorn RISC Machine) developed on BBC Model B - Source: [3JcUtkCjF-0]
- Used Tube interface as co-processor during development - Source: [3JcUtkCjF-0]
- Same architecture now in phones and Apple Silicon Macs - Source: [3JcUtkCjF-0]

### Resources
- Stardot.org.uk forums: Main community for Acorn/BBC machines - Source: [3JcUtkCjF-0]

## Peripherals

### Acorn Mouse

#### Overview
- Official Acorn two-button mouse - Source: [KddR9KSRx4Y]
- Chunky design typical of 1980s computer mice - Source: [KddR9KSRx4Y]
- Uses ball mechanism (may need cleaning) - Source: [KddR9KSRx4Y]

#### Connection
- Uses multi-pin connector (not standard serial) - Source: [KddR9KSRx4Y]
- Probably connects to user port - Source: [KddR9KSRx4Y]
- Uses quadrature encoding (similar to Atari/Amiga/Mac mice) - Source: [KddR9KSRx4Y]

#### Software Compatibility
- BBC Master 512 (PC emulator card) supported mouse for DOS/GEM environments - Source: [KddR9KSRx4Y]
- Native BBC software with mouse support exists (paint programs, etc.) - Source: [KddR9KSRx4Y]
- May work with BBC Model B as well as Master 128 - Source: [KddR9KSRx4Y]

### Sideways RAM Expansion (Solid Disk Technology)

#### Overview
- RAM expansion board for BBC Model B - Source: [KddR9KSRx4Y]
- Adds up to 32KB of bank-switched RAM - Source: [KddR9KSRx4Y]
- Made by Solid Disk Technology Limited - Source: [KddR9KSRx4Y]
- Uses TMS4416 RAM chips - Source: [KddR9KSRx4Y]

#### How Sideways RAM Works
- BBC memory map: 32K RAM + 16K sideways ROM/RAM area + 16K MOS - Source: [KddR9KSRx4Y]
- Sideways ROM area bank-switches multiple ROMs/RAM into same address space - Source: [KddR9KSRx4Y]
- MOS controls up to 16 ROM/RAM sockets - Source: [KddR9KSRx4Y]
- Sideways RAM allows software to be loaded from disc into ROM address space - Source: [KddR9KSRx4Y]

#### Installation
- Base unit plugs into rightmost ROM socket on motherboard - Source: [KddR9KSRx4Y]
- Control wires connect to 6522 VIA chip for bank selection - Source: [KddR9KSRx4Y]
- Additional wires to 74LS163 and 6502 CPU - Source: [KddR9KSRx4Y]
- Wires push into IC sockets alongside existing IC pins - Source: [KddR9KSRx4Y]
- Manual available online (search for Solid Disk sideways RAM manual) - Source: [KddR9KSRx4Y]

#### Usage
- Can run "sideways software" from disc without burning EPROMs - Source: [KddR9KSRx4Y]
- Solid Disk provided disc caching utilities (100x faster disc access) - Source: [KddR9KSRx4Y]
- BBC Master 128 uses similar bank switching for its 128K RAM - Source: [KddR9KSRx4Y]

### Cheetah Sweet Talker (Speech Synthesizer)

#### Overview
- Speech synthesis module for BBC Model A and B - Source: [KddR9KSRx4Y]
- Made by Cheetah Marketing - Source: [KddR9KSRx4Y]
- Alternative to Acorn's official speech upgrade - Source: [KddR9KSRx4Y]
- Cost 25 pounds in 1980s (very affordable) - Source: [KddR9KSRx4Y]

#### Hardware
- Plugs into IC socket 99 on BBC Micro motherboard - Source: [KddR9KSRx4Y]
- Uses SPO256A-AL2 speech processor chip - Source: [KddR9KSRx4Y]
- Contains all 59 phonemes of English language - Source: [KddR9KSRx4Y]
- Five pause lengths available - Source: [KddR9KSRx4Y]

#### Software
- Comes with demonstration tape containing example programs - Source: [KddR9KSRx4Y]
- Phonemes are individually addressable - Source: [KddR9KSRx4Y]
- Example: "HH1 EH L L OW" produces "hello" - Source: [KddR9KSRx4Y]

### Vine Micros Replay (Freezer/Copy Utility)

#### Overview
- ROM-based utility for BBC Micro Model B and B+ - Source: [KddR9KSRx4Y]
- Transfers programs from tape to disc and disc to disc - Source: [KddR9KSRx4Y]
- Can freeze games mid-play for later replay - Source: [KddR9KSRx4Y]
- Released July 1985 - Source: [KddR9KSRx4Y]

#### Components
- ROM chip that installs in motherboard socket - Source: [KddR9KSRx4Y]
- External button for freezing programs - Source: [KddR9KSRx4Y]
- IC clips connect to chips on motherboard - Source: [KddR9KSRx4Y]

#### Features
- `*REPLAY` or `*REP` command accesses menu - Source: [KddR9KSRx4Y]
- Press freeze button once to pause game (keyboard LEDs flash) - Source: [KddR9KSRx4Y]
- Press F6 to restart frozen game - Source: [KddR9KSRx4Y]
- Can save screen state for printing with screen dump routine - Source: [KddR9KSRx4Y]

#### Variants
- Multiple versions exist (Mark 1, etc.) - Source: [KddR9KSRx4Y]
- Different hardware configurations for installation - Source: [KddR9KSRx4Y]
- Some use IC clips, others use IC sockets - Source: [KddR9KSRx4Y]

### BBC Master ROM Cartridges

#### Overview
- Cartridge slots on BBC Master for easy ROM installation - Source: [KddR9KSRx4Y]
- Machine has two cartridge slots - Source: [KddR9KSRx4Y]
- Alternative to internal ROM sockets for adding software - Source: [KddR9KSRx4Y]

#### Cartridge Types
- Accept 32K EPROMs or 128K EPROMs (27513 equivalent) - Source: [KddR9KSRx4Y]
- Each cartridge can hold two ROM chips - Source: [KddR9KSRx4Y]
- Notches must face correct direction when installing - Source: [KddR9KSRx4Y]

#### Usage
- Similar functionality to internal ROM sockets on Model B - Source: [KddR9KSRx4Y]
- Can hold games or utility ROMs - Source: [KddR9KSRx4Y]
- Example: Arkanoid game ROM - Source: [KddR9KSRx4Y]
