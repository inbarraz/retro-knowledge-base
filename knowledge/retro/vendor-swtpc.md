# Southwest Technical Products Corporation (SWTPC)

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| SWTPC 6800 | Desktop Computer Kit | [Diqea-ahnXE] |
| CT-1024 | Video Terminal Kit | [Diqea-ahnXE] |
| GT-6144 | Graphics Terminal Kit | [Diqea-ahnXE] |
| AC-30 | Cassette Interface | [Diqea-ahnXE] |
| PR-40 | Dot Matrix Printer Kit | [Diqea-ahnXE] |
| MPR | EPROM Programmer | [Diqea-ahnXE] |
| Newtech Model 68 Music Board | Sound Card | [h-dA24sfnSI] |
| MP-16 | 16K RAM Card | [h-dA24sfnSI] |

## Platform-Specific Knowledge

### SWTPC 6800 Computer System

#### Overview
- Kit computer released in 1975 - Source: [Diqea-ahnXE]
- Based in San Antonio, Texas - Source: [Diqea-ahnXE]
- Uses Motorola 6800 CPU (ancestor of 6502) - Source: [Diqea-ahnXE]
- 64KB address space like 6502 - Source: [Diqea-ahnXE]
- Everything was sold as a kit - you assembled it yourself - Source: [Diqea-ahnXE]
- Original price: $395 for base system - Source: [Diqea-ahnXE]
- 2K to 4K RAM upgrade was $45 extra - Source: [Diqea-ahnXE]
- Required terminal for operation (no front panel switches like Altair) - Source: [Diqea-ahnXE]

#### Architecture
- MPa = CPU card - Source: [Diqea-ahnXE]
- MPb = Motherboard - Source: [Diqea-ahnXE]
- SS30 = smaller expansion slots for add-on cards - Source: [Diqea-ahnXE]
- Bank switching possible with clever circuitry - Source: [Diqea-ahnXE]
- Standard 1MHz clock speed - Source: [Diqea-ahnXE]

#### ROM Monitor
- SWTPCbug was the original ROM monitor - Source: [Diqea-ahnXE]
- SmartBug was a third-party replacement with more features - Source: [Diqea-ahnXE]
- Tiny ROM allows basic assembly input, jumping to routines - Source: [Diqea-ahnXE]
- BASIC not in ROM - must be loaded from tape or disk - Source: [Diqea-ahnXE]

#### BASIC Versions
- 4K BASIC: Entire interpreter fits in 4KB RAM - Source: [Diqea-ahnXE]
- 8K BASIC: More features but uses more RAM - Source: [Diqea-ahnXE]
- 4K BASIC dated 1976, 8K BASIC 2.3 dated 1978 - Source: [Diqea-ahnXE]
- Larger BASIC = less RAM available for programs - Source: [Diqea-ahnXE]

#### Program Loading
- Uses Motorola S-record format - Source: [Diqea-ahnXE]
- Each line starts with "S1" followed by hex data and checksum - Source: [Diqea-ahnXE]
- Very inefficient: each byte becomes two ASCII hex characters - Source: [Diqea-ahnXE]
- Binary loader available to speed up loading (2x or faster) - Source: [Diqea-ahnXE]
- Binary loader: small program loads first, then accepts raw bytes - Source: [Diqea-ahnXE]

#### Historical Context
- Predecessor to pre-assembled computers - Source: [Diqea-ahnXE]
- Apple II, TRS-80 Model 1, PET 2001 came out in 1977 - Source: [Diqea-ahnXE]
- Those machines were pre-built, just plug in and turn on - Source: [Diqea-ahnXE]
- SWTPC required building every component yourself - Source: [Diqea-ahnXE]
- By 1987 very few people still using systems like this - Source: [Diqea-ahnXE]

### CT-1024 Terminal

#### Overview
- Video terminal kit for displaying text on television - Source: [Diqea-ahnXE]
- $275 additional to computer kit - Source: [Diqea-ahnXE]
- Required external television set - Source: [Diqea-ahnXE]
- Connects via serial interface to computer - Source: [Diqea-ahnXE]

#### Features
- Includes keyboard encoder - Source: [Diqea-ahnXE]
- Serial interface board required for computer communication - Source: [Diqea-ahnXE]
- Without serial board, just types text onto TV (no computer interface) - Source: [Diqea-ahnXE]

### GT-6144 Graphics Terminal

#### Overview
- Graphics terminal system for graphical display - Source: [Diqea-ahnXE]
- 64 x 96 pixel resolution - Source: [Diqea-ahnXE]
- Has own 6144-bit static RAM - Source: [Diqea-ahnXE]
- Works with any computer with 8-bit parallel interface - Source: [Diqea-ahnXE]
- Can combine with CT-1024 for text + graphics on same display - Source: [Diqea-ahnXE]

### AC-30 Cassette Interface

#### Overview
- $79 kit for tape storage - Source: [Diqea-ahnXE]
- Works like a modem: converts digital to audio and back - Source: [Diqea-ahnXE]
- 300 baud speed - Source: [Diqea-ahnXE]
- Connect to any cassette player/recorder - Source: [Diqea-ahnXE]

### PR-40 Printer

#### Overview
- Unusual looking - resembles telephone - Source: [Diqea-ahnXE]
- 5x7 dot matrix impact printer - Source: [Diqea-ahnXE]
- Similar to Centronics printers - Source: [Diqea-ahnXE]
- 64 character uppercase ASCII - Source: [Diqea-ahnXE]
- 40 characters per line - Source: [Diqea-ahnXE]
- 75 lines per minute - Source: [Diqea-ahnXE]
- Uses 3-7/8" adding machine paper rolls - Source: [Diqea-ahnXE]
- Kit form only - Source: [Diqea-ahnXE]

### MPR EPROM Programmer

#### Overview
- Plugs into SS30 expansion slot - Source: [Diqea-ahnXE]
- Programs 2716 EPROMs - Source: [Diqea-ahnXE]
- Uses ZIF socket for easy chip insertion - Source: [Diqea-ahnXE]
- Very simple design - Source: [Diqea-ahnXE]
- Can verify EPROMs after programming - Source: [Diqea-ahnXE]
- Requires software (typed in or loaded from tape) - Source: [Diqea-ahnXE]

### Smoke Signal Broadcasting

#### Overview
- Third-party add-on manufacturer - Source: [Diqea-ahnXE]
- Made disk system for SWTPC 6800 - Source: [Diqea-ahnXE]
- Made SmartBug ROM monitor replacement - Source: [Diqea-ahnXE]

#### Disk System Requirements
- 8" drives require minimum 1.65MHz clock - Source: [Diqea-ahnXE]
- Standard 6800 runs at 1MHz - too slow - Source: [Diqea-ahnXE]
- Chieftain accelerator card available (2MHz CPU card) - Source: [Diqea-ahnXE]
- MPA CPU board can be modified for 1.8MHz - Source: [Diqea-ahnXE]
- Modification: cut traces, add jumper - Source: [Diqea-ahnXE]
- Also requires capacitor change on MPA2 serial board - Source: [Diqea-ahnXE]

#### DOS68
- Operating system for disk-based SWTPC systems - Source: [Diqea-ahnXE]
- Sequential file access supported - Source: [Diqea-ahnXE]
- Programming guide available - Source: [Diqea-ahnXE]

### Assembly and Documentation

#### Kit Assembly
- Build every component yourself - Source: [Diqea-ahnXE]
- Check off components as installed - Source: [Diqea-ahnXE]
- Detailed circuit trace diagrams with front/back colors - Source: [Diqea-ahnXE]
- Full schematics provided for everything - Source: [Diqea-ahnXE]
- "Right to repair" assumed - you built it! - Source: [Diqea-ahnXE]

#### Software Distribution
- Games and utilities often distributed as typed listings - Source: [Diqea-ahnXE]
- Had to type in entire hex dump manually - Source: [Diqea-ahnXE]
- Multiple pages of hex codes for larger programs - Source: [Diqea-ahnXE]
- Once typed in, could save to tape for future use - Source: [Diqea-ahnXE]

### Available Software (Contemporary)
- Hangman, Acey-Deucy, Craps, Mastermind - games - Source: [Diqea-ahnXE]
- Space Voyage - Star Trek clone requiring 8K RAM - Source: [Diqea-ahnXE]
- Klingon Capture - smaller space game, only 2K RAM needed - Source: [Diqea-ahnXE]
- Floating Point Package - math capability - Source: [Diqea-ahnXE]
- Line Editor, Random Number Generator - utilities - Source: [Diqea-ahnXE]
- COREDIT Editor/Assembler - development tool - Source: [Diqea-ahnXE]
- Trace Disassembler - debugging tool - Source: [Diqea-ahnXE]

### Newtech Model 68 Music Board

#### Overview
- Sound card for SWTPC 6800 computer - Source: [h-dA24sfnSI]
- Original design from 1977, modern replica by Paul - Source: [h-dA24sfnSI]
- Based on 6-bit DAC resistor ladder network - Source: [h-dA24sfnSI]
- Similar to TRS-80 CoCo sound circuit design - Source: [h-dA24sfnSI]
- GitHub: github.com/CorshamTech/Music_Board (Rev 2 gerbers) - Source: [h-dA24sfnSI]

#### Technical Details
- Uses resistor ladder for digital-to-analog conversion - Source: [h-dA24sfnSI]
- Connected through VIA chip (like 6522) - Source: [h-dA24sfnSI]
- Software creates multi-channel audio with proper sine waves - Source: [h-dA24sfnSI]
- Not square wave beeps - sounds like real music - Source: [h-dA24sfnSI]
- Bit-banged audio requires CPU to do all the work - Source: [h-dA24sfnSI]
- CPU cannot multitask while playing music - Source: [h-dA24sfnSI]

#### Assembly
- Uses SS30 expansion slot (30-pin connector) - Source: [h-dA24sfnSI]
- Goes into I/O mapped slots on back of computer - Source: [h-dA24sfnSI]
- 74LS logic chips and LM op-amp - Source: [h-dA24sfnSI]
- Molex connectors for SS30 bus - Source: [h-dA24sfnSI]
- Kit is relatively straightforward to assemble - Source: [h-dA24sfnSI]

#### Software Caveat
- Original code is 6809-optimized (from TRS-80 CoCo) - Source: [h-dA24sfnSI]
- No 6800 native code currently available - Source: [h-dA24sfnSI]
- Needs adaptation from 6809 to 6800 instruction set - Source: [h-dA24sfnSI]

### MP-16 RAM Card (Prototype)

#### Overview
- 16K (or 32K) RAM expansion card - Source: [h-dA24sfnSI]
- Motorola Memory Systems manufacture - Source: [h-dA24sfnSI]
- Possible 1977 prototype with bodge wires - Source: [h-dA24sfnSI]
- Later released as MP-16A (documented version) - Source: [h-dA24sfnSI]

#### Identification
- Gold ceramic packages on RAM chips - Source: [h-dA24sfnSI]
- Date codes from 1977 - Source: [h-dA24sfnSI]
- Jumper for 16K/32K selection - Source: [h-dA24sfnSI]
- Extensive bodge wires and dead-bug chips - Source: [h-dA24sfnSI]
- Chips piggybacked onto other chips (literally attached) - Source: [h-dA24sfnSI]

#### Memory Limitations
- SWTPC 6800 can only address 48K total RAM - Source: [h-dA24sfnSI]
- Due to I/O address space and ROM mapping - Source: [h-dA24sfnSI]
- No bank switching on standard machine - Source: [h-dA24sfnSI]
- Bodge wires may enable bank switching for extra memory - Source: [h-dA24sfnSI]
