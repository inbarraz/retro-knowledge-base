# Texas Instruments

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| TI-99/4A | Home Computer | [ANbiQW-Ppt4], [eFatlDatjZM] |

## Platform-Specific Knowledge

### TI-99/4A Cartridge System

#### GROM Chips
- GROM = Graphics ROM (proprietary TI chip format) - Source: [ANbiQW-Ppt4]
- Small packages holding ~4KB each - Source: [ANbiQW-Ppt4]
- Addressable independently - Source: [ANbiQW-Ppt4]
- Can be stacked (traces run parallel between them) - Source: [ANbiQW-Ppt4]
- Not replaceable with standard EPROMs - Source: [ANbiQW-Ppt4]

#### TI Extended Basic Cartridge
- Required for disk drive use (built-in BASIC too limited) - Source: [ANbiQW-Ppt4]
- Faster than built-in BASIC - Source: [ANbiQW-Ppt4]
- Allows access to extended memory (up to 32KB) - Source: [ANbiQW-Ppt4]
- Contains DOS-like commands for disk operations - Source: [ANbiQW-Ppt4]
- Has both GROM chips and mask ROM chips - Source: [ANbiQW-Ppt4]
- 74LS74 and 74LS00 TTL for bank switching - Source: [ANbiQW-Ppt4]
- Stacked GROMs on PCB (4 GROMs in stack configuration) - Source: [ANbiQW-Ppt4]
- Different colored cartridge shells (yellow variant exists) - Source: [ANbiQW-Ppt4]

#### Extended Basic Internals
- 4 XB GROMs (stacked, don't mind being stacked) - Source: [ANbiQW-Ppt4]
- 2 ROM chips with 12KB programming data - Source: [ANbiQW-Ppt4]
- Bank switching logic in center (74LS74 and 74LS00) - Source: [ANbiQW-Ppt4]
- Upper 4KB bank-switched, lower portion always present - Source: [ANbiQW-Ppt4]

#### Disk Manager 2 Cartridge
- Used for disk formatting and management - Source: [ANbiQW-Ppt4]
- Catalog/directory viewing - Source: [ANbiQW-Ppt4]
- Disk backup - Source: [ANbiQW-Ppt4]
- Disk initialization (formatting) - Source: [ANbiQW-Ppt4]
- Complements Extended Basic for disk operations - Source: [ANbiQW-Ppt4]

#### Cartridge Contact Cleaning
- Contacts are solder-coated, not gold - Source: [ANbiQW-Ppt4]
- DeoxIT + magic eraser effective for cleaning - Source: [ANbiQW-Ppt4]
- Pencil eraser also works - Source: [ANbiQW-Ppt4]
- Magic eraser mildly abrasive, good with DeoxIT - Source: [ANbiQW-Ppt4]

#### Cartridge Troubleshooting
- Shows on startup menu but hangs = likely GROM or ROM failure - Source: [ANbiQW-Ppt4]
- If TTL bank switching fails, may cause same symptoms - Source: [ANbiQW-Ppt4]
- GROM failures not easily repairable (proprietary chips) - Source: [ANbiQW-Ppt4]
- Mask ROM failures potentially repairable with EPROM replacement - Source: [ANbiQW-Ppt4]

### TI-99/4A Software

#### Micro Surgeon
- Medical-themed arcade game - Source: [ANbiQW-Ppt4]
- Player navigates inside human body - Source: [ANbiQW-Ppt4]
- Ported to many platforms (ColecoVision, PC Jr) - Source: [ANbiQW-Ppt4]
- Supports TI Speech Synthesizer - Source: [ANbiQW-Ppt4]
- Cartridge survived severe rust damage and still works - Source: [ANbiQW-Ppt4]

### TI-99/4A Expansion

#### Peripheral Expansion Box (PEB)

##### Overview
- Contains disk drive controller - Source: [ANbiQW-Ppt4]
- Requires Extended Basic cartridge for full functionality - Source: [ANbiQW-Ppt4]
- Can hold extended memory cards - Source: [ANbiQW-Ppt4]
- Extremely heavy - possibly one of heaviest home computer peripherals - Source: [fIR3sitVPP8]
- Metal case with die-cast card enclosures - Source: [fIR3sitVPP8]
- Noisy internal fan - Source: [fIR3sitVPP8]

##### Connection to Computer
- Uses "Fire Hose" cable - long thick ribbon cable - Source: [fIR3sitVPP8]
- Peripheral Interface Card goes in PEB slot 1 - Source: [fIR3sitVPP8]
- Flex cable interface plugs into side expansion port on TI-99 - Source: [fIR3sitVPP8]
- Does NOT use cartridge slot - goes to side port - Source: [fIR3sitVPP8]
- Cable long enough to position computer away from PEB - Source: [fIR3sitVPP8]

##### Power Supply Architecture
- Provides +8V, +16V, -16V to expansion cards - Source: [fIR3sitVPP8]
- Cards have local voltage regulation (7805 for 5V) - Source: [fIR3sitVPP8]
- Similar to S-100 bus power distribution approach - Source: [fIR3sitVPP8]
- Internal floppy drive has its own regulation from main rails - Source: [fIR3sitVPP8]

##### Card Slot LEDs
- LED indicators on each card slot - Source: [fIR3sitVPP8]
- Light pipes in front panel pick up LEDs from cards - Source: [fIR3sitVPP8]
- Disk controller LED blinks during disk access - Source: [fIR3sitVPP8]
- Memory card LED may blink on access - Source: [fIR3sitVPP8]

##### Die-Cast Card Cases
- Expansion cards have heavy die-cast metal enclosures - Source: [fIR3sitVPP8]
- Provides RF shielding (in addition to metal case) - Source: [fIR3sitVPP8]
- Contributes significantly to overall weight - Source: [fIR3sitVPP8]
- Cards feel ridiculously heavy compared to modern cards - Source: [fIR3sitVPP8]

##### Basic TI-99/4A Disk Operations
- Stock BASIC only supports OLD (load) and SAVE commands - Source: [fIR3sitVPP8]
- Syntax: OLD DSK1.filename or SAVE DSK1.filename - Source: [fIR3sitVPP8]
- No directory command without Extended Basic or Disk Manager - Source: [fIR3sitVPP8]
- Extended Basic programs won't run properly in stock BASIC - Source: [fIR3sitVPP8]

##### Testing the PEB
- Turn on PEB first, then computer - Source: [fIR3sitVPP8]
- Activity LED on peripheral interface card indicates connection - Source: [fIR3sitVPP8]
- Disk controller LED should blink on computer startup - Source: [fIR3sitVPP8]
- Extended Basic or Disk Manager cartridge needed for real testing - Source: [fIR3sitVPP8]
- Final ROM or Final GROM multicart can substitute - Source: [fIR3sitVPP8]

#### Memory Expansion
- Up to 32KB expansion memory - Source: [ANbiQW-Ppt4]
- Available in PEB or side-mount module - Source: [ANbiQW-Ppt4]
- Extended Basic required to access expansion memory - Source: [ANbiQW-Ppt4]
- 32x8 memory expansion card common in PEB - Source: [fIR3sitVPP8]

#### CorComp Triple Tech Card

##### Overview
- Third-party expansion card combining multiple functions - Source: [fIR3sitVPP8]
- Three-in-one card for TI-99/4A PEB - Source: [fIR3sitVPP8]
- Manufacturer: CorComp Incorporated, Laguna Hills, California - Source: [fIR3sitVPP8]
- Reference: ninerpedia.org/wiki/Triple_Tech - Source: [fIR3sitVPP8]

##### Functions
- Real-time clock/calendar (battery-backed CR2032) - Source: [fIR3sitVPP8]
- 64K print buffer with Z80 processor - Source: [fIR3sitVPP8]
- Speech synthesizer adapter (accepts TI Speech module board) - Source: [fIR3sitVPP8]

##### Speech Adapter Feature
- Accepts circuit board from TI Speech Synthesizer - Source: [fIR3sitVPP8]
- Plugs into card inside PEB instead of side expansion port - Source: [fIR3sitVPP8]
- Frees up side port for other expansion - Source: [fIR3sitVPP8]
- Audio presumably fed back through cable to computer - Source: [fIR3sitVPP8]

##### Print Buffer Details
- Uses Z80 processor for buffer management - Source: [fIR3sitVPP8]
- 64K RAM for print buffer storage - Source: [fIR3sitVPP8]
- Copy button: Sends buffer contents again (reprints) - Source: [fIR3sitVPP8]
- Clear button: Resets print buffer - Source: [fIR3sitVPP8]
- Buttons can be relocated to external case - Source: [fIR3sitVPP8]

##### Real-Time Clock
- Accessible via BASIC with OPEN and PRINT commands - Source: [fIR3sitVPP8]
- CR2032 battery maintains time when powered off - Source: [fIR3sitVPP8]
- Date codes on ICs from 1986 - Source: [fIR3sitVPP8]

##### Z80 Note
- Z80 only used for print buffer functionality - Source: [fIR3sitVPP8]
- Does NOT enable CP/M capability - Source: [fIR3sitVPP8]
- Manual has no mention of alternative Z80 use - Source: [fIR3sitVPP8]

#### CorComp RS-232 Card

##### Overview
- Serial interface card for TI-99/4A PEB - Source: [fIR3sitVPP8]
- Manufacturer: CorComp Incorporated, Laguna Hills, California - Source: [fIR3sitVPP8]
- Die-cast enclosure like standard TI cards - Source: [fIR3sitVPP8]

##### Features
- RS-232 serial port connector on card - Source: [fIR3sitVPP8]
- Ribbon cable connection to Triple Tech for parallel I/O - Source: [fIR3sitVPP8]
- PIO (Parallel I/O) functionality - Source: [fIR3sitVPP8]

#### Tippy PEB (Raspberry Pi Expansion)
- Raspberry Pi interface card for TI-99/4A Peripheral Expansion Box - Source: [cQGWcHCzZmU]
- Provides networking support - Source: [cQGWcHCzZmU]
- Provides floppy drive emulation - Source: [cQGWcHCzZmU]
- Uses Xilinx CPLD/FPGA for interface - Source: [cQGWcHCzZmU]
- Pi connects via expansion header to card - Source: [cQGWcHCzZmU]
- Open source project by JediMatt - Source: [cQGWcHCzZmU]
- Also available as "Tippy" side-car version (no PEB required) - Source: [cQGWcHCzZmU]

### TMS9918 Video Chip

#### Overview
- TMS9918 is the video chip used in TI-99/4A - Source: [eFatlDatjZM]
- TMS9929 is the PAL variant - Source: [eFatlDatjZM]
- Same chip used in many other computers (not just TI) - Source: [eFatlDatjZM]

#### Compatible Systems
- TI-99/4A - Source: [eFatlDatjZM]
- ColecoVision - Source: [eFatlDatjZM]
- Adam computer - Source: [eFatlDatjZM]
- Early MSX computers - Source: [eFatlDatjZM]
- Sega SG-1000 and SD-3000 - Source: [eFatlDatjZM]
- VTech CreatiVision - Source: [eFatlDatjZM]
- Dick Smith Wizard - Source: [eFatlDatjZM]
- NABU - Source: [eFatlDatjZM]

#### Pico9918 Replacement

##### Overview
- TMS9918/9929 replacement using Raspberry Pi Pico RP2040 - Source: [eFatlDatjZM]
- Designed by Troy Schrapel (Australia) - Source: [eFatlDatjZM]
- Open source project on GitHub - Source: [eFatlDatjZM]
- github.com/visrealm/pico9918 - Source: [eFatlDatjZM]

##### Versions
- Original version: Separate PCB + Raspberry Pi Pico module on top - Source: [eFatlDatjZM]
- Newer version 0.3: All-in-one with built-in RP2040 - Source: [eFatlDatjZM]
- All-in-one version has external VGA connector - Source: [eFatlDatjZM]

##### Features
- Pixel-perfect VGA output (not relying on junky composite) - Source: [eFatlDatjZM]
- Level shifters for chip compatibility - Source: [eFatlDatjZM]
- F18A compatibility mode - Source: [eFatlDatjZM]
- 80 column text mode (not standard on original TMS9918) - Source: [eFatlDatjZM]
- Enhanced sprite modes - Source: [eFatlDatjZM]
- More colors available in enhanced modes - Source: [eFatlDatjZM]
- Parallax scrolling demos (SNES-style graphics possible) - Source: [eFatlDatjZM]

##### F18A Compatibility
- F18A is another TMS9918 replacement project - Source: [eFatlDatjZM]
- Pico9918 supports F18A demo programs - Source: [eFatlDatjZM]
- F18A demos show much better graphics than original chip - Source: [eFatlDatjZM]

##### Installation
- Requires USB-C Raspberry Pi Pico variant (not micro USB) - Source: [eFatlDatjZM]
- Older version requires separate Pico module installation - Source: [eFatlDatjZM]
- Plugs into TMS9918 socket in compatible computer - Source: [eFatlDatjZM]

##### Why It's Impressive
- RP2040 microcontroller only costs a few dollars - Source: [eFatlDatjZM]
- Replaces entire graphics chip functionality - Source: [eFatlDatjZM]
- Adds VGA output plus enhanced capabilities - Source: [eFatlDatjZM]
- Example of RP2040's incredible versatility - Source: [eFatlDatjZM]
