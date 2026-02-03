# Modern Solutions for Retro Systems

> Part of the retro knowledge base. See also: tech-*.md files for other categories.

## Contents
- [LCD Monitor Selection for Retro Use](#lcd-monitor-selection-for-retro-use)
- [Early LCD Displays for Retro Use](#early-lcd-displays-for-retro-use)
- [Modern Retro Hardware](#modern-retro-hardware)
- [WiFi/Network Storage Solutions](#wifinetwork-storage-solutions)
- [XT-IDE (8-bit IDE)](#xt-ide-8-bit-ide)
- [ISA Sound Cards (Modern)](#isa-sound-cards-modern)
- [3D Printed Motherboard Trays/Standoffs](#3d-printed-motherboard-traysstandoffs)

## LCD Monitor Selection for Retro Use

### 240p Handling
- Most 8-bit computers output 240p (progressive scan, 60Hz) - Source: [CluzXuInAqU]
- Cheap LCD monitors often treat 240p as interlaced - Source: [CluzXuInAqU]
- Forced interlace causes visible jitter/shaking on screen - Source: [CluzXuInAqU]
- PAL systems (25fps) show more noticeable jitter than NTSC (30fps) - Source: [CluzXuInAqU]
- Some monitors handle 240p correctly (Sony KLV-S19A10) - Source: [A6kfCOJHs2U]
- Test with Commodore 64 or Apple II before purchasing - Source: [CluzXuInAqU]

### Sync-on-Green Support
- Some systems output video sync embedded in green channel - Source: [CluzXuInAqU]
- Systems using sync-on-green: Mac IIci, Silicon Graphics, Sun workstations - Source: [CluzXuInAqU]
- Most consumer LCD monitors do NOT support sync-on-green - Source: [CluzXuInAqU]
- Monitor shows black/no signal without explicit sync-on-green support - Source: [CluzXuInAqU]
- Professional monitors (Asus, some others) more likely to support it - Source: [CluzXuInAqU]

### VGA Non-Standard Resolution Support
- DOS computers use 640x400@70Hz (not 640x480) - Source: [CluzXuInAqU]
- EGA uses 640x350@70Hz - Source: [CluzXuInAqU]
- Many LCD monitors only support 640x480 and above - Source: [CluzXuInAqU]
- Test with DOS machine before purchasing for vintage PC use - Source: [CluzXuInAqU]
- Good monitors auto-calibrate and remember multiple VGA modes - Source: [CluzXuInAqU]

### Panel Type Considerations
- IPS panels: Better viewing angles, colors stable off-axis - Source: [CluzXuInAqU]
- TN panels: Poor viewing angles, brightness drops off-axis - Source: [CluzXuInAqU]
- Some monitors marketed as IPS are actually TN - Source: [CluzXuInAqU]
- Test viewing angle before purchase if possible - Source: [CluzXuInAqU]
- TN panels problematic for filming/camera capture - Source: [CluzXuInAqU]

### Composite Video Quality
- Consumer LCDs often keep chroma filter active even for monochrome - Source: [A6kfCOJHs2U]
- Results in soft/blurry 80-column text - Source: [A6kfCOJHs2U]
- Apple IIe/IIc dedicated monitors are exception (auto-disable filter) - Source: [A6kfCOJHs2U]
- No sharpness control on some monitors limits adjustment - Source: [CluzXuInAqU]

### HDMI Input Caveats
- Some monitors force overscan on HDMI - Source: [A6kfCOJHs2U]
- Some monitors use DAC conversion (HDMI to analog internally) - Source: [A6kfCOJHs2U]
- Test with RetroTink or similar upscaler for best results - Source: [CluzXuInAqU]
- Pass-through mode (480i) may not work on monitors expecting line-doubled - Source: [CluzXuInAqU]

### PAL Support
- North American consumer LCDs (Sony, Samsung, LG) typically NTSC only - Source: [A6kfCOJHs2U]
- Chinese/Taiwan import brands more likely to support PAL - Source: [A6kfCOJHs2U]
- Test PAL source before relying on monitor for European systems - Source: [CluzXuInAqU]

## Early LCD Displays for Retro Use

### Overview
- Early 2000s 4:3 LCD TVs useful for retro computers - Source: [EjjJWY01jRQ]
- Hybrid sets: LCD panel with analog inputs only - Source: [EjjJWY01jRQ]
- Lighter and thinner than CRTs, easier to find - Source: [EjjJWY01jRQ]
- Look for 4:3 aspect ratio models specifically - Source: [EjjJWY01jRQ]

### Sharp LC-15S4U-S
- 15" EDTV LCD, 12V DC center positive - Source: [EjjJWY01jRQ]
- Inputs: Composite, S-Video, Component, RF - Source: [EjjJWY01jRQ]
- No VGA or digital inputs - Source: [EjjJWY01jRQ]
- Manual PAL/NTSC/SECAM selection required (not auto) - Source: [EjjJWY01jRQ]
- Supports 240p through component but not perfect - Source: [EjjJWY01jRQ]
- Better 240p processing than Magnavox - Source: [EjjJWY01jRQ]
- Less input lag than Magnavox - Source: [EjjJWY01jRQ]
- VESA mount with carry handle - Source: [EjjJWY01jRQ]
- Full control buttons on top (no remote needed) - Source: [EjjJWY01jRQ]

### Magnavox 15MF605T/17 (Philips)
- 15" LCD, 16V DC center positive - Source: [EjjJWY01jRQ]
- Inputs: Composite, S-Video, Component, VGA, RF - Source: [EjjJWY01jRQ]
- VGA input useful for PC connection - Source: [EjjJWY01jRQ]
- Auto PAL/NTSC switching - Source: [EjjJWY01jRQ]
- VGA supports 480p, 720p, 1080i (not 1080p) - Source: [EjjJWY01jRQ]
- VGA does NOT support 15kHz (240p/480i) - Source: [EjjJWY01jRQ]
- Component only supports 480i (not 240p) - Source: [EjjJWY01jRQ]
- More input lag than Sharp - Source: [EjjJWY01jRQ]
- Picture-in-picture feature (remote has button) - Source: [EjjJWY01jRQ]
- Stores settings per resolution (useful) - Source: [EjjJWY01jRQ]

### 240p Handling
- Neither monitor handles 240p natively/perfectly - Source: [EjjJWY01jRQ]
- Artifacts visible in fast-moving games - Source: [EjjJWY01jRQ]
- Interlacing artifacts visible even in 240p mode - Source: [EjjJWY01jRQ]
- CRT always better for 240p content - Source: [EjjJWY01jRQ]

### Composite Video Sharpness Trick
- Connect composite to green component jack (Luma only) - Source: [EjjJWY01jRQ]
- No analog filtering on component input vs composite input - Source: [EjjJWY01jRQ]
- Gives sharper text than standard composite jack - Source: [EjjJWY01jRQ]
- Same technique works on Commodore 1084 S-Video input - Source: [EjjJWY01jRQ]
- Loses color (monochrome only) - Source: [EjjJWY01jRQ]

### Finding These Monitors
- Check thrift stores regularly (Goodwill, etc.) - Source: [EjjJWY01jRQ]
- Often priced $10-20 at thrift stores - Source: [EjjJWY01jRQ]
- eBay prices inflated due to retro gaming demand - Source: [EjjJWY01jRQ]
- Staff often don't recognize value of analog inputs - Source: [EjjJWY01jRQ]

## Modern Retro Hardware

### WeeCee Miniature DOS PC

#### Overview
- Miniature DOS gaming PC in very small form factor - Source: [eyV7kaEMcfs]
- Solid metal case - Source: [eyV7kaEMcfs]
- Now manufactured in USA (Seattle) - Source: [eyV7kaEMcfs]
- Originally designed by Rasteriser (UK) - Source: [eyV7kaEMcfs]
- Hand-assembled, limited production - Source: [eyV7kaEMcfs]

#### Hardware Specifications
- Modern 486 processor (not original vintage 486) - Source: [eyV7kaEMcfs]
- Speed range: 25MHz to 800MHz (equivalent to Pentium 2) - Source: [eyV7kaEMcfs]
- VGA output (no 3D acceleration - software rendering only) - Source: [eyV7kaEMcfs]
- Cirrus Logic audio chip (Sound Blaster-ish, not full compatible) - Source: [eyV7kaEMcfs]
- Windows 95/98 and DOS support - Source: [eyV7kaEMcfs]

#### Connectivity
- VGA output - Source: [eyV7kaEMcfs]
- Ethernet - Source: [eyV7kaEMcfs]
- USB - Source: [eyV7kaEMcfs]
- Micro USB for power - Source: [eyV7kaEMcfs]
- Game port for joysticks - Source: [eyV7kaEMcfs]
- PS/2 input - Source: [eyV7kaEMcfs]
- Micro SD for storage - Source: [eyV7kaEMcfs]

#### Optional Audio Upgrades
- Dream Blaster S2 can be included - Source: [eyV7kaEMcfs]
- Provides General MIDI sound - Source: [eyV7kaEMcfs]
- Better audio quality than FM synthesis - Source: [eyV7kaEMcfs]

#### Pricing and Availability
- Starting bid ~$500 on eBay - Source: [eyV7kaEMcfs]
- Can go up to $800+ for complete units - Source: [eyV7kaEMcfs]
- Limited production, hand-assembled - Source: [eyV7kaEMcfs]

#### Use Case
- Run DOS games on actual hardware without emulation - Source: [eyV7kaEMcfs]
- Avoid unreliable vintage hardware that can fail - Source: [eyV7kaEMcfs]
- Compact size vs. full vintage PC setup - Source: [eyV7kaEMcfs]
- Can use power bank (micro USB power) - Source: [eyV7kaEMcfs]

### Magic Wand Word Processor

#### Overview
- CP/M-based word processor software from early 1980s - Source: [eyV7kaEMcfs]
- Publisher: Small Business Applications, Houston, Texas - Source: [eyV7kaEMcfs]
- Retail price: $400 in 1984 (early 1980s dollars - ~$1200 adjusted) - Source: [eyV7kaEMcfs]

#### Platform Support
- Runs on CP/M computers - Source: [eyV7kaEMcfs]
- Available on 8-inch soft sector disks - Source: [eyV7kaEMcfs]
- Available on 5.25" North Star or Micropolis (hard sector) - Source: [eyV7kaEMcfs]
- Available on 5.25" soft sector disks - Source: [eyV7kaEMcfs]

#### Terminal Support
- Required specific terminal emulation support - Source: [eyV7kaEMcfs]
- Supported terminals: Lear Siegler, Intertech, Microterm, Act Five - Source: [eyV7kaEMcfs]
- Also: Parker Elmer, Soroc, VDM1, Televideo, TRS-80 Model 2 - Source: [eyV7kaEMcfs]
- Also: Vector Graphics, others - Source: [eyV7kaEMcfs]
- DMA terminal support (video boards with memory-mapped display) - Source: [eyV7kaEMcfs]

#### System Requirements
- Minimum 16KB RAM, 32KB recommended - Source: [eyV7kaEMcfs]
- Spell checker included - Source: [eyV7kaEMcfs]
- Brochure available at archive.org - Source: [eyV7kaEMcfs]

#### Disk Format Notes
- 8-inch disks could be used by many systems - Source: [eyV7kaEMcfs]
- Company would provide disks formatted for your specific system - Source: [eyV7kaEMcfs]
- Disk format varied by disk controller even on same computer type - Source: [eyV7kaEMcfs]
- Customer told company their system and controller type - Source: [eyV7kaEMcfs]

## WiFi/Network Storage Solutions

### FujiNet Ecosystem

#### Overview
- ESP32-based network/storage devices for retro computers - Source: [rDAv6K2i2tk]
- Originally for Atari 8-bit line (SIO bus) - Source: [rDAv6K2i2tk]
- Name comes from Atari logo (Mount Fuji shape) - Source: [rDAv6K2i2tk]
- Now ported to multiple platforms - Source: [rDAv6K2i2tk]

#### Supported Platforms
- Atari 8-bit (800, XL, XE) via SIO bus - Source: [rDAv6K2i2tk]
- Apple II via SmartPort - Source: [rDAv6K2i2tk]
- Commodore (via Meatloaf device) - Source: [rDAv6K2i2tk]
- Coleco Adam - Source: [rDAv6K2i2tk]

#### Features
- Emulates disk drives and cartridges - Source: [rDAv6K2i2tk]
- Load software from built-in memory or SD card - Source: [rDAv6K2i2tk]
- Load software directly from internet (no local storage needed) - Source: [rDAv6K2i2tk]
- Telnet BBS access - Source: [rDAv6K2i2tk]
- Multiplayer games (poker, etc.) - Source: [rDAv6K2i2tk]
- Real-time ISS position tracker - Source: [rDAv6K2i2tk]
- CP/M emulation (runs inside ESP32, uses host keyboard/screen) - Source: [rDAv6K2i2tk]
- Uses undocumented Apple SmartPort features that Apple specified but nobody used - Source: [rDAv6K2i2tk]

#### Coleco Adam Version
- PCB available with ESP32 module - Source: [rDAv6K2i2tk]
- Works with Adam tape drive interface - Source: [rDAv6K2i2tk]
- Adam tape drives (Digital Data Pack) are indexed, seek like floppy drives - Source: [rDAv6K2i2tk]
- Much faster than standard linear cassette tape - Source: [rDAv6K2i2tk]

### Meatloaf (WiFi IEC Device for Commodore)

#### Overview
- WiFi-enabled device that connects to Commodore IEC bus - Source: [PsA0TKVZBR8]
- Developed by same team as FujiNet - Source: [PsA0TKVZBR8]
- Allows loading software directly from internet - Source: [PsA0TKVZBR8]
- Compatible with C64, C128, VIC-20, Plus/4 (any IEC-equipped Commodore) - Source: [PsA0TKVZBR8]

#### Features
- Emulates 1541 disk drive over IEC - Source: [PsA0TKVZBR8]
- Connects to WiFi network - Source: [PsA0TKVZBR8]
- Can browse and load software from internet archives - Source: [PsA0TKVZBR8]
- SD card for local storage of disk images - Source: [PsA0TKVZBR8]
- Web interface for configuration - Source: [PsA0TKVZBR8]

#### Hardware
- ESP32-based design - Source: [PsA0TKVZBR8]
- Standard IEC connector (6-pin DIN) - Source: [PsA0TKVZBR8]
- MicroSD card slot - Source: [PsA0TKVZBR8]
- USB for power and firmware updates - Source: [PsA0TKVZBR8]

### ZiModem (WiFi Serial Modem)

#### Overview
- ESP8266-based WiFi modem for serial devices - Source: [RneTw_LThzQ]
- Provides internet access for vintage terminals and computers - Source: [RneTw_LThzQ]
- Hayes-compatible AT command set - Source: [RneTw_LThzQ]
- Connects via RS-232 serial port - Source: [RneTw_LThzQ]

#### Compatible Devices
- DEC terminals (VT-100, VT-220, etc.) - Source: [RneTw_LThzQ]
- Any device with RS-232 serial port and terminal software - Source: [RneTw_LThzQ]
- Vintage computers with serial ports - Source: [RneTw_LThzQ]
- BBSes designed for modem connections - Source: [RneTw_LThzQ]

#### Features
- Telnet client mode - connect to remote hosts - Source: [RneTw_LThzQ]
- Configurable baud rates (9600, 19200 common) - Source: [RneTw_LThzQ]
- Hayes AT command compatible - Source: [RneTw_LThzQ]
- Connect to modern BBSes and telnet hosts - Source: [RneTw_LThzQ]
- Bridge between vintage serial and modern TCP/IP - Source: [RneTw_LThzQ]

#### Connection
- Requires null modem cable for terminal connection - Source: [RneTw_LThzQ]
- Match baud rate settings between modem and terminal - Source: [RneTw_LThzQ]
- USB power supply - Source: [RneTw_LThzQ]
- Configure WiFi credentials via AT commands - Source: [RneTw_LThzQ]

### Badger6502Pico (Complete 6502 on Raspberry Pi Pico)

#### Overview
- Full 6502 computer emulated on Raspberry Pi Pico microcontroller - Source: [PsA0TKVZBR8]
- VGA output, PS/2 keyboard input, SD card storage - Source: [PsA0TKVZBR8]
- All peripherals directly connected to Pico - Source: [PsA0TKVZBR8]
- No separate CPU chip - entire system emulated - Source: [PsA0TKVZBR8]

#### Features
- Runs 6502 software (BASIC, games, etc.) - Source: [PsA0TKVZBR8]
- VGA output for modern monitors - Source: [PsA0TKVZBR8]
- PS/2 keyboard support - Source: [PsA0TKVZBR8]
- SD card for program storage - Source: [PsA0TKVZBR8]
- Very low cost compared to vintage hardware - Source: [PsA0TKVZBR8]

#### Limitations
- Emulation, not real 6502 hardware - Source: [PsA0TKVZBR8]
- Can't use physical 6502 expansion cards - Source: [PsA0TKVZBR8]
- Software compatibility depends on emulation accuracy - Source: [PsA0TKVZBR8]

### TRS-80 Model 1 Reproduction Parts (RetroStack)

#### Overview
- Open source reproduction parts for TRS-80 Model 1 - Source: [PsA0TKVZBR8]
- Project by RetroStack - Source: [PsA0TKVZBR8]
- Allows building complete working TRS-80 Model 1 from new parts - Source: [PsA0TKVZBR8]
- All designs published on GitHub - Source: [PsA0TKVZBR8]

#### Available Components
- Motherboard reproduction - Source: [PsA0TKVZBR8]
- Keyboard reproduction - Source: [PsA0TKVZBR8]
- Power supply board - Source: [PsA0TKVZBR8]
- Expansion interface reproductions - Source: [PsA0TKVZBR8]

#### Project Resources
- GitHub: github.com/RetroStack - Source: [PsA0TKVZBR8]
- All designs open source - Source: [PsA0TKVZBR8]
- Can order PCBs from PCBWay, JLCPCB, etc. - Source: [PsA0TKVZBR8]
- Community-driven development - Source: [PsA0TKVZBR8]

## XT-IDE (8-bit IDE)

### Overview
- 8-bit version of IDE, NOT standard 40-pin IDE - Source: [3DbmGtHJ-Wc]
- Used on some embedded systems like Zenith Eazy PC - Source: [3DbmGtHJ-Wc]
- Western Digital drives had XT-IDE variants - Source: [3DbmGtHJ-Wc]
- 40-pin connector looks like IDE but incompatible with standard IDE drives - Source: [3DbmGtHJ-Wc]
- Did not gain much traction outside specific systems - Source: [3DbmGtHJ-Wc]

## ISA Sound Cards (Modern)

### PicoGUS

#### Overview
- Open source software-defined ISA sound card - Source: [QljsIIPl-SE]
- Based on Raspberry Pi Pico (RP2040) microcontroller - Source: [QljsIIPl-SE]
- Replaces need for expensive Gravis Ultrasound cards - Source: [QljsIIPl-SE]
- Works in 8-bit ISA slots (compatible with XT machines) - Source: [QljsIIPl-SE]
- Version 2.0 has all components integrated on PCB - Source: [QljsIIPl-SE]
- Price approximately $45-70 - Source: [QljsIIPl-SE]

#### Emulation Modes
- Gravis Ultrasound (GUS) - primary mode - Source: [QljsIIPl-SE]
- Sound Blaster 2.0 (mono 8-bit) - Source: [QljsIIPl-SE]
- AdLib (OPL2 FM synthesis) - Source: [QljsIIPl-SE]
- Creative Music System (CMS) - 22 channel square wave - Source: [QljsIIPl-SE]
- Tandy 3-voice audio - Source: [QljsIIPl-SE]
- MPU-401 MIDI interface - Source: [QljsIIPl-SE]
- Mode switched via DOS command, firmware flash - Source: [QljsIIPl-SE]

#### Features
- USB port for Xbox 360 controller as joystick - Source: [QljsIIPl-SE]
- Wave table header for external MIDI modules - Source: [QljsIIPl-SE]
- High-quality DAC (24-bit, 96kHz) - very low noise - Source: [QljsIIPl-SE]
- Much better audio quality than original Sound Blaster cards - Source: [QljsIIPl-SE]
- ENIG gold plating on edge connector (version 2.0) - Source: [QljsIIPl-SE]

#### Hardware Versions
- Version 1.0: Separate modules soldered together - Source: [QljsIIPl-SE]
- Version 2.0: All components integrated on single PCB - Source: [QljsIIPl-SE]
- Version for hand386 portable computer available - Source: [QljsIIPl-SE]
- Book 8088 compatible version available - Source: [QljsIIPl-SE]

#### Limitations
- No OPL3 emulation yet (code not optimized for RP2040) - Source: [QljsIIPl-SE]
- No Sound Blaster 16 emulation - Source: [QljsIIPl-SE]
- Sound Blaster Pro 1.0 support in development - Source: [QljsIIPl-SE]

#### Project Resources
- Website: polpo.org/picogus - Source: [QljsIIPl-SE]
- GitHub: github.com/polpo/picogus - Source: [QljsIIPl-SE]
- Tindie store for assembled units - Source: [QljsIIPl-SE]
- Joe's Computer Museum also distributes in North America - Source: [QljsIIPl-SE]
- Fully open source hardware and software - Source: [QljsIIPl-SE]

## USB MIDI Host Adapters

### DoreMidi UMH10 USB MIDI Host

#### Overview
- Converts USB MIDI devices to standard 5-pin MIDI - Source: [sUgM0k-Exyg]
- Allows USB-only MIDI keyboards to work with vintage sound modules - Source: [sUgM0k-Exyg]
- Useful for connecting modern USB keyboards to Sound Canvas and similar - Source: [sUgM0k-Exyg]

#### Connections
- USB Host port for USB MIDI devices - Source: [sUgM0k-Exyg]
- MIDI In 5-pin DIN - Source: [sUgM0k-Exyg]
- MIDI Out 5-pin DIN - Source: [sUgM0k-Exyg]
- USB port for power input only - Source: [sUgM0k-Exyg]

#### Specifications
- 16 channel standard MIDI - Source: [sUgM0k-Exyg]
- Full speed USB MIDI host interface - Source: [sUgM0k-Exyg]
- Minimal internal circuitry - dedicated IC handles conversion - Source: [sUgM0k-Exyg]

#### Availability
- Website: doremidi.cn - Source: [sUgM0k-Exyg]

## 3D Printed Motherboard Trays/Standoffs

### AT/Baby-AT Motherboard Standoffs
- Printables model 1043675 (Baby-AT), 1043698 (ATX) - Source: [4uxKHjXGXnU]
- Raises motherboard so expansion card brackets don't hit desk - Source: [4uxKHjXGXnU]
- Has locating pins for initial alignment - Source: [4uxKHjXGXnU]
- Five studs have holes for screws (coarse thread works best) - Source: [4uxKHjXGXnU]
- Small bump indicates keyboard connector corner location - Source: [4uxKHjXGXnU]
- Holes for wall mounting if desired - Source: [4uxKHjXGXnU]
- Works with most AT motherboards, XT may need variant - Source: [4uxKHjXGXnU]
- Requires larger print bed than Ender 3 - Source: [4uxKHjXGXnU]
