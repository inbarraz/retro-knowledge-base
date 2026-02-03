# Miscellaneous Techniques

> Part of the retro knowledge base. See also: tech-*.md files for other categories.

## Contents
- [Safety](#safety)
- [Bus Compatibility](#bus-compatibility)
- [Game Console Cartridge Issues](#game-console-cartridge-issues)
- [Famicom/NES Clone Systems](#famicomnes-clone-systems)
- [ROM/Firmware Preservation](#romfirmware-preservation)
- [Apple II User Group Archives](#apple-ii-user-group-archives)
- [X10 Home Automation](#x10-home-automation)
- [Digital Storage Scope Add-Ons](#digital-storage-scope-add-ons)
- [Tools Reference](#tools-reference)

## Safety

### Hot Chassis Television Safety
- Many 13-inch and smaller TVs are "hot chassis" designs - Source: [hPGWOAgkSXs]
- Hot chassis means B+ derived from mains without isolation transformer - Source: [hPGWOAgkSXs]
- Chassis ground can be at mains potential if plug reversed - Source: [hPGWOAgkSXs]
- NEVER add composite video mod to hot chassis TV without isolation - Source: [hPGWOAgkSXs]
- RCA cable ground would become live at 120V/240V - Source: [hPGWOAgkSXs]
- Hot chassis TVs use polarized plugs as only safety measure - Source: [hPGWOAgkSXs]
- All plastic construction = hot chassis indicator - Source: [hPGWOAgkSXs]
- Headphone jacks isolated via transformer on hot chassis sets - Source: [hPGWOAgkSXs]
- RF inputs isolated via matching transformer - Source: [hPGWOAgkSXs]
- Use isolation transformer when servicing hot chassis equipment - Source: [hPGWOAgkSXs]

### CRT Color Balance Adjustment (TV Sets)
- Grayscale test pattern: gray bars should be neutral, not tinted - Source: [hPGWOAgkSXs]
- Yellowish gray = blue too weak, adjust blue bias up - Source: [hPGWOAgkSXs]
- Bias controls on neck board affect black level per color - Source: [hPGWOAgkSXs]
- Drive controls affect white level per color - Source: [hPGWOAgkSXs]
- Some sets have only two drive pots (red fixed with resistor) - Source: [hPGWOAgkSXs]
- Adjust bias first, then drive - Source: [hPGWOAgkSXs]

### CRT Wear Indicators
- Brown striations visible through clear glass = cathode wear - Source: [hPGWOAgkSXs]
- Emissive material burns off cathode and deposits on glass - Source: [hPGWOAgkSXs]
- Worn CRTs may brighten up after warm-up period - Source: [hPGWOAgkSXs]

### Other Safety Notes
- Use gloves when handling extremely dirty/filthy equipment - Source: [_0XGFz67DIc]
- Be aware of sketchy wiring in modified equipment, especially mains AC distribution - Source: [_0XGFz67DIc]
- CRT DAG (conductive coating) ground connections should be verified - Source: [_0XGFz67DIc]
- NEVER open a CRT monitor or power supply unless you know how to do so safely - Source: [_MljEAIpQ8g]
- Mains voltage input carries lethal voltages, especially in 220V countries - Source: [_MljEAIpQ8g]
- High voltage anode cable: Do not bend or manipulate brittle cables - Source: [_MljEAIpQ8g]

## Bus Compatibility

### ISA and EISA Compatibility
- ISA cards can plug into EISA motherboards - Source: [3llXvhYbryY]
- EISA slot is deeper than ISA - extra contacts on lower row - Source: [3llXvhYbryY]
- EISA adds 32-bit width with more speed - Source: [3llXvhYbryY]
- EISA cards cannot plug into ISA slots (center notch different) - Source: [3llXvhYbryY]
- ISA cards compatible with EISA because notch alignment works one-way - Source: [3llXvhYbryY]
- EISA motherboard doesn't require case redesign - same card depth - Source: [3llXvhYbryY]

### Bus Extender Cards
- Plug into motherboard slot to work on cards externally - Source: [3llXvhYbryY]
- Extended pins allow easy test lead attachment - Source: [3llXvhYbryY]
- Available for ISA, EISA, PCI bus types - Source: [3llXvhYbryY]
- Companies: Vector Electric, JDR Micro Devices, Twin Industries - Source: [3llXvhYbryY]
- Often found with bodge wires from prototype work - Source: [3llXvhYbryY]

## Game Console Cartridge Issues

### Atari 2600 Tight/Swollen Cartridges
- Some cartridges swell over time, becoming very tight in console - Source: [eFatlDatjZM]
- Can lift entire console by cartridge when trying to remove - Source: [eFatlDatjZM]
- Affects official Atari cartridges, not just third-party - Source: [eFatlDatjZM]
- Problem appears to be date/manufacturing batch related - Source: [eFatlDatjZM]
- Same console may accept some cartridges easily and others not at all - Source: [eFatlDatjZM]

### Lock-On 2600 Adapter
- Adapter by Chris Cool Creations (aquietalcove.com) - Source: [eFatlDatjZM]
- Plugs into console easily, then accepts cartridge - Source: [eFatlDatjZM]
- Eliminates need to force tight cartridges into console - Source: [eFatlDatjZM]
- Works with both 2600 and 7800 consoles - Source: [eFatlDatjZM]
- ~$35 from maker's website - Source: [eFatlDatjZM]

## Famicom/NES Clone Systems

### PowerJoy PJ-800 (Famicom Clone)
- Famicom-on-a-chip in Nintendo 64 style controller form factor - Source: [eFatlDatjZM]
- Built-in light gun with trigger on controller - Source: [eFatlDatjZM]
- Battery powered (takes AA batteries) - Source: [eFatlDatjZM]
- Analog stick works as D-pad (digital, not true analog) - Source: [eFatlDatjZM]
- 9V center-negative power input for AC adapter - Source: [eFatlDatjZM]
- Very low power draw (~60mA at 9V) - Source: [eFatlDatjZM]
- Video quality has interference patterns (typical for blob-on-board clones) - Source: [eFatlDatjZM]
- Missing capacitor on 7805 regulator contributes to video interference - Source: [eFatlDatjZM]

### Construction Quality
- Three blobs inside (CPU, PPU, controller shift register) - Source: [eFatlDatjZM]
- Surprisingly has RF shielding (unusual for clone) - Source: [eFatlDatjZM]
- Gold-coated button contacts - Source: [eFatlDatjZM]
- Light gun is bent LED with heat shrink (crude but functional) - Source: [eFatlDatjZM]
- 12 screws hold case together (more than expected) - Source: [eFatlDatjZM]

### Cartridge Compatibility
- Multicart is standard Famicom pinout - Source: [eFatlDatjZM]
- PowerJoy multicart works in real Famicom/Famicone - Source: [eFatlDatjZM]
- Video quality much better on real Famicom than PowerJoy - Source: [eFatlDatjZM]
- Button mapping may be reversed vs. real NES - Source: [eFatlDatjZM]
- Licensed Nintendo games removed from multicart (copyright avoidance) - Source: [eFatlDatjZM]

### Multicart Internals
- Blob-on-carrier construction for ROM chips - Source: [eFatlDatjZM]
- Gold-plated edge connector - Source: [eFatlDatjZM]
- PCB opens easily (clip mechanism) - Source: [eFatlDatjZM]
- Not keyed for correct orientation - easy to install backwards - Source: [eFatlDatjZM]
- Date code suggests 2003 manufacture - Source: [eFatlDatjZM]

## ROM/Firmware Preservation

### Why Preserve Firmware
- Companies go out of business, firmware becomes unavailable - Source: [mRqsGytvSP8]
- Archived firmware allows others to upgrade/repair equipment - Source: [mRqsGytvSP8]
- Archive.org and GitHub are good preservation destinations - Source: [mRqsGytvSP8]
- Even partial dumps help future preservation efforts - Source: [mRqsGytvSP8]

### Dumping Multi-ROM Systems (Odd/Even)
- 16-bit systems often use two 8-bit ROMs (odd and even bytes) - Source: [mRqsGytvSP8]
- Must combine ROMs to get usable firmware image - Source: [mRqsGytvSP8]
- Mark chips as "odd" and "even" before removal - Source: [mRqsGytvSP8]
- ROMWAC utility combines odd/even byte ROMs - Source: [mRqsGytvSP8]
- GitHub: github.com/Freemac/romwac - Source: [mRqsGytvSP8]
- Run combination both ways to determine correct byte order - Source: [mRqsGytvSP8]
- Correct order shows readable ASCII strings - Source: [mRqsGytvSP8]

### Flash ROM Chips
- SST 39SF020 is common 256KB flash ROM - Source: [mRqsGytvSP8]
- Can be read with standard EPROM programmers - Source: [mRqsGytvSP8]
- TL866II Plus (MiniPro) supports most common flash chips - Source: [mRqsGytvSP8]

### PAL/GAL Dumping Challenges
- PALs/GALs often security protected (read-protected) - Source: [mRqsGytvSP8]
- Data IO 2900 programmer can attempt reads - Source: [mRqsGytvSP8]
- Protected chip reads all zeros/blank - Source: [mRqsGytvSP8]
- ICT 18CV8 common protected PAL - Source: [mRqsGytvSP8]
- Brute force possible for combinational logic but difficult for state machines - Source: [mRqsGytvSP8]
- Scraped-off chip markings = manufacturer knew they'd be protected - Source: [mRqsGytvSP8]

### PAL 16L8 Dumping and Recreation
- PAL 16L8 is simpler combinational logic chip (no registered outputs) - Source: [Rgt9ZWYsMTE]
- Can be reverse-engineered by probing all input/output combinations - Source: [Rgt9ZWYsMTE]

#### palrvs Tool (PAL Reverse Engineering)
- Command-line tool for PAL chip reverse engineering - Source: [Rgt9ZWYsMTE]
- GitHub: github.com/Kreeblah/palrvs - Source: [Rgt9ZWYsMTE]
- Generates truth table from brute force probing of all input states - Source: [Rgt9ZWYsMTE]
- Reads chip using EPROM programmer adapter (not standard programmer) - Source: [Rgt9ZWYsMTE]
- Outputs JEDEC file compatible with GAL programmers - Source: [Rgt9ZWYsMTE]

#### EPROM Programmer Adapter Method
- Standard EPROM programmers (TL866) cannot read PALs directly - Source: [Rgt9ZWYsMTE]
- Adapter PCB converts PAL 16L8 pinout to 28-pin EPROM socket - Source: [Rgt9ZWYsMTE]
- Uses shift registers to step through all 2^n input combinations - Source: [Rgt9ZWYsMTE]
- Programmer reads outputs as if reading EPROM addresses - Source: [Rgt9ZWYsMTE]
- Full probe of 16L8 takes seconds (relatively few input combinations) - Source: [Rgt9ZWYsMTE]

#### Logic Friday Software
- Free Windows software for logic equation manipulation - Source: [Rgt9ZWYsMTE]
- Downloads from: sontrak.com (original) or archive sites - Source: [Rgt9ZWYsMTE]
- Can import truth tables and generate minimized Boolean equations - Source: [Rgt9ZWYsMTE]
- Karnaugh map visualization shows logic reduction - Source: [Rgt9ZWYsMTE]
- Export to various PLD formats including JEDEC - Source: [Rgt9ZWYsMTE]
- Useful for optimizing equations to fit in smaller GAL chip - Source: [Rgt9ZWYsMTE]

#### PAL to GAL Conversion
- GAL 16V8 can replace most PAL 16L8 chips - Source: [Rgt9ZWYsMTE]
- GAL chips are electrically erasable and reprogrammable - Source: [Rgt9ZWYsMTE]
- May need to configure GAL mode bits for PAL compatibility - Source: [Rgt9ZWYsMTE]
- TL866II Plus can program GAL 16V8 chips directly - Source: [Rgt9ZWYsMTE]
- Verify output polarity matches original PAL (active high vs low) - Source: [Rgt9ZWYsMTE]

### RAMCheck DRAM Tester Specifics
- Innoventions Inc. RAMCheck - Source: [mRqsGytvSP8]
- Uses 486DX-40 processor internally - Source: [mRqsGytvSP8]
- Firmware archive: archive.org/details/ramcheck-firmware-2.35-merged - Source: [mRqsGytvSP8]
- Andrew's blog on firmware upgrade: linuxjedi.co.uk/upgrading-the-ram-detective-a-firmware-adventure-with-ramcheck/ - Source: [mRqsGytvSP8]
- Hardware revision differences may require PAL upgrade - Source: [mRqsGytvSP8]
- Serial port allows firmware updates (when company existed) - Source: [mRqsGytvSP8]

### Documentation to Archive
- Photograph PCBs, especially chip markings - Source: [mRqsGytvSP8]
- Note jumper configurations - Source: [mRqsGytvSP8]
- Save calibration data if visible on stickers - Source: [mRqsGytvSP8]
- Document hardware revisions - Source: [mRqsGytvSP8]
- Include photos of known-working units for comparison - Source: [mRqsGytvSP8]

## Apple II User Group Archives

### Apple Core Examiners Newsletter (January 1984)

#### Context
- Bay City, Michigan Apple II user group - Source: [F-Cw1f4WOTY]
- Monthly meeting format with newsletter distribution - Source: [F-Cw1f4WOTY]
- Dues: Cost club $6-7/month for newsletter distribution - Source: [F-Cw1f4WOTY]
- Members received ID cards for library access - Source: [F-Cw1f4WOTY]

#### Featured Hardware: Gibson LPS2 Light Pen
- Light pen package from Gibson - Source: [F-Cw1f4WOTY]
- Price: $350 in 1984 (equivalent to entire Commodore 64) - Source: [F-Cw1f4WOTY]
- Compared to "mini Lisa computer" experience - Source: [F-Cw1f4WOTY]
- Light pen requires software support (limited availability) - Source: [F-Cw1f4WOTY]
- Ergonomically challenging (arm fatigue from holding against screen) - Source: [F-Cw1f4WOTY]

#### Newsletter Format
- Printed on computer (unusual for 1984) - Source: [F-Cw1f4WOTY]
- Included type-in BASIC programs - Source: [F-Cw1f4WOTY]
- Corrections for previous month's program listings - Source: [F-Cw1f4WOTY]
- Mailed as folded newsletter with 20-cent stamp - Source: [F-Cw1f4WOTY]

#### Historical Context
- User groups were primary way to share software and knowledge - Source: [F-Cw1f4WOTY]
- Program libraries maintained for checkout by members - Source: [F-Cw1f4WOTY]
- Hardware demonstrations at monthly meetings - Source: [F-Cw1f4WOTY]
- Parallels to modern retrocomputing community meetups and VCF events - Source: [F-Cw1f4WOTY]

## X10 Home Automation

### Overview
- X10 is a home automation system from the late 1970s - Source: [yFQoVGVKAQE]
- Remained popular into the 2000s before Zigbee, Z-Wave, and Matter - Source: [yFQoVGVKAQE]
- Communicates over existing power lines (AC line carrier) - Source: [yFQoVGVKAQE]
- Uses BSR modules for lamps and appliances - Source: [yFQoVGVKAQE]

### Module Types
- Lamp modules: Plug lamp into module, plug module into wall - Source: [yFQoVGVKAQE]
- Appliance modules: Have relay inside for on/off control of any device - Source: [yFQoVGVKAQE]
- Wall switch modules: Replace light switches, powered parasitically through incandescent bulbs - Source: [yFQoVGVKAQE]
- 220V appliance modules available for dryers, etc. - Source: [yFQoVGVKAQE]
- Thermostat controller: Emits heat under thermostat to trick HVAC system - Source: [yFQoVGVKAQE]

### Control Methods
- Ultrasonic remote controls (BSR) with tone generator - Source: [yFQoVGVKAQE]
- Command modules receive ultrasonic tones, transmit over power line - Source: [yFQoVGVKAQE]
- Wired controllers with buttons for each device - Source: [yFQoVGVKAQE]
- Timer modules for scheduling - Source: [yFQoVGVKAQE]
- Telephone responder for remote control via phone - Source: [yFQoVGVKAQE]

### Addressing System
- House codes (A-P) and unit codes (1-16) - Source: [yFQoVGVKAQE]
- Selectable via dials/switches on each module - Source: [yFQoVGVKAQE]
- Groups possible by setting multiple modules to same code - Source: [yFQoVGVKAQE]
- Dimming supported on lamp modules - Source: [yFQoVGVKAQE]

### CP290 Computer Interface
- RS232 serial interface for computer control - Source: [yFQoVGVKAQE]
- Contains real-time clock for scheduled events - Source: [yFQoVGVKAQE]
- Stores timed events and graphic data - Source: [yFQoVGVKAQE]
- Transmits X10 signals over house wiring - Source: [yFQoVGVKAQE]
- Programming guide documents serial protocol completely - Source: [yFQoVGVKAQE]
- Continues operating when computer is off or busy - Source: [yFQoVGVKAQE]
- Software available for PC/XT, IBM PC compatibles - Source: [yFQoVGVKAQE]

### LED/CFL Compatibility Issues
- LED and CFL bulbs don't work well with X10 wall switches - Source: [yFQoVGVKAQE]
- Wall switches were parasitically powered through incandescent bulbs - Source: [yFQoVGVKAQE]
- Incandescent acted as resistor providing power to switch electronics - Source: [yFQoVGVKAQE]
- LED/CFL too efficient to provide parasitic power - Source: [yFQoVGVKAQE]
- Appliance modules with relays still work with any load - Source: [yFQoVGVKAQE]

### ADC-1 Data Acquisition and Control System (1983)

#### Overview
- Remote Measurement Systems ADC-1 from Seattle, Washington - Source: [yFQoVGVKAQE]
- Price: $329 in 1983 (with X10 transmitter: $369) - Source: [yFQoVGVKAQE]
- One of earliest affordable home automation platforms - Source: [yFQoVGVKAQE]
- Combines sensor input with X10 control capability - Source: [yFQoVGVKAQE]

#### Specifications
- 16 analog input channels - Source: [yFQoVGVKAQE]
- 12-bit analog to digital converter - Source: [yFQoVGVKAQE]
- 4 digital inputs for monitoring on/off signals - Source: [yFQoVGVKAQE]
- 6 TTL control outputs for external devices - Source: [yFQoVGVKAQE]
- RS232 communications for computer connection - Source: [yFQoVGVKAQE]
- Power: 20mA at 5V or 35mA at 6-24V (internal 7805 regulator) - Source: [yFQoVGVKAQE]
- Can be powered from computer's power supply - Source: [yFQoVGVKAQE]

#### X10 Integration
- Separate AC line carrier transmitter box plugs into wall - Source: [yFQoVGVKAQE]
- Connects to ADC-1 via DB25 connector - Source: [yFQoVGVKAQE]
- Isolates AC voltage from sensitive analog circuitry - Source: [yFQoVGVKAQE]
- Uses optocouplers (4N33) for safety isolation - Source: [yFQoVGVKAQE]
- BSR codes transmitted within 100 nanoseconds of AC zero crossing - Source: [yFQoVGVKAQE]
- Each code takes ~22 AC cycles to transmit - Source: [yFQoVGVKAQE]

#### Supported Computers
- VIC-20 and Commodore 64 (via SIO serial) - Source: [yFQoVGVKAQE]
- Atari computers (via PEEK/POKE commands) - Source: [yFQoVGVKAQE]
- S-100 systems: Altair, IMSAI, North Star Horizon - Source: [yFQoVGVKAQE]
- Osborne 1 and Osborne Executive - Source: [yFQoVGVKAQE]
- IBM PC (via COM port) - Source: [yFQoVGVKAQE]
- Apple II and Macintosh - Source: [yFQoVGVKAQE]
- TRS-80 Model 100 and Color Computer - Source: [yFQoVGVKAQE]
- TI-99/4A, Victor 9000, Epson HX-20 - Source: [yFQoVGVKAQE]

#### Supported Sensors
- Temperature sensors (Analog Devices AD590, $7) - Source: [yFQoVGVKAQE]
- Thermocouples - Source: [yFQoVGVKAQE]
- Wind speed sensors/anemometers ($45) - Source: [yFQoVGVKAQE]
- Light level photovoltaic cells ($6) - Source: [yFQoVGVKAQE]
- AC current clamp for power monitoring ($75) - Source: [yFQoVGVKAQE]
- Optical encoders - Source: [yFQoVGVKAQE]
- Floor mat pressure sensors - Source: [yFQoVGVKAQE]
- Ultrasonic sensors - Source: [yFQoVGVKAQE]
- Security system sensors - Source: [yFQoVGVKAQE]
- Relative humidity sensor ($100 calibrated) - Source: [yFQoVGVKAQE]
- Onboard temperature sensor included - Source: [yFQoVGVKAQE]

#### Internal Construction
- Uses Intersil 12-bit AD converter ICs - Source: [yFQoVGVKAQE]
- CMOS logic (40174, etc.) - Source: [yFQoVGVKAQE]
- No microcontroller or CPU - command processing in converter chips - Source: [yFQoVGVKAQE]
- Single-sided PCB, made in USA - Source: [yFQoVGVKAQE]
- Date code 1982 on components - Source: [yFQoVGVKAQE]

#### Programming
- BASIC examples provided for each supported computer - Source: [yFQoVGVKAQE]
- Fortran libraries written by Dr. Larry Shore (Bates College) - Source: [yFQoVGVKAQE]
- Complete instruction set documented in manual - Source: [yFQoVGVKAQE]
- Allows if/then automation based on sensor values - Source: [yFQoVGVKAQE]
- More capable than standalone X10 controllers - Source: [yFQoVGVKAQE]

## Digital Storage Scope Add-Ons

### Epic Instruments Wavesaver 10

#### Overview
- Converts analog oscilloscope into digital storage scope - Source: [yFQoVGVKAQE]
- Epic Instruments, Foster City, California - Source: [yFQoVGVKAQE]
- Model 10H: $1,295 in 1984 - Source: [yFQoVGVKAQE]
- Records transient waveforms for flicker-free display - Source: [yFQoVGVKAQE]

#### Specifications
- 8-bit vertical resolution (256 levels) - Source: [yFQoVGVKAQE]
- 10 MHz maximum sampling rate - Source: [yFQoVGVKAQE]
- 4K x 8-bit memory (4096 sample points) - Source: [yFQoVGVKAQE]
- Static RAM storage (expensive in 1984) - Source: [yFQoVGVKAQE]
- Output: 0-8V, with 4V = zero point (127 digital) - Source: [yFQoVGVKAQE]
- Constant 400 kHz output sweep frequency - Source: [yFQoVGVKAQE]
- Total output sweep time: 10.24 milliseconds - Source: [yFQoVGVKAQE]

#### How It Works
- Digitizes analog input via ADC - Source: [yFQoVGVKAQE]
- Stores waveform in digital memory buffer - Source: [yFQoVGVKAQE]
- DAC (DAC08) converts back to analog for display - Source: [yFQoVGVKAQE]
- Continuously plays back stored waveform to scope - Source: [yFQoVGVKAQE]
- Scope becomes just a display device - Source: [yFQoVGVKAQE]
- Pre-trigger and post-trigger capture modes - Source: [yFQoVGVKAQE]
- Auto-arm function for semi-realtime recording - Source: [yFQoVGVKAQE]

#### Controls
- Trigger level adjustment - Source: [yFQoVGVKAQE]
- Offset/center control - Source: [yFQoVGVKAQE]
- AC/DC/Ground input coupling - Source: [yFQoVGVKAQE]
- Internal/external clock selection - Source: [yFQoVGVKAQE]
- Time per point adjustment (effective time base) - Source: [yFQoVGVKAQE]
- Manual arm and trigger buttons - Source: [yFQoVGVKAQE]
- Volts per division selection - Source: [yFQoVGVKAQE]

#### Connections
- Scope output (BNC) - analog waveform to oscilloscope - Source: [yFQoVGVKAQE]
- Trigger output (BNC) - for scope external trigger - Source: [yFQoVGVKAQE]
- Input (BNC) - signal to capture - Source: [yFQoVGVKAQE]
- External clock input - Source: [yFQoVGVKAQE]
- Digital port (15-pin) - parallel data output - Source: [yFQoVGVKAQE]
- Plotter output - chart recorder compatible - Source: [yFQoVGVKAQE]

#### Recommended Scope Settings
- Time base: 1 millisecond per division - Source: [yFQoVGVKAQE]
- Vertical: 2 volts per division - Source: [yFQoVGVKAQE]
- External trigger from Wavesaver trigger output - Source: [yFQoVGVKAQE]
- Settings fixed regardless of captured signal - Source: [yFQoVGVKAQE]

#### Wave Display Software
- PC software for viewing captured waveforms - Source: [yFQoVGVKAQE]
- Requires IBM PC/XT or compatible - Source: [yFQoVGVKAQE]
- MS-DOS 1.1 or 2.0 - Source: [yFQoVGVKAQE]
- 128KB RAM minimum - Source: [yFQoVGVKAQE]
- CGA graphics output - Source: [yFQoVGVKAQE]
- $100 for software package - Source: [yFQoVGVKAQE]
- Required special data acquisition card (separate from Wavesaver) - Source: [yFQoVGVKAQE]

#### Internal Construction
- Multiple TTL logic ICs - Source: [yFQoVGVKAQE]
- Eight 4K x 1 static RAM chips (date code 8324) - Source: [yFQoVGVKAQE]
- Main ADC chip had part number intentionally sanded off - Source: [yFQoVGVKAQE]
- DAC08 digital-to-analog converter for output - Source: [yFQoVGVKAQE]
- Internal transformer and 7805 voltage regulator - Source: [yFQoVGVKAQE]
- Calibration potentiometers on front-end board - Source: [yFQoVGVKAQE]
- Made in USA - Source: [yFQoVGVKAQE]

#### Testing Notes (2025)
- Unit still functional after 40+ years - Source: [yFQoVGVKAQE]
- Controls may be scratchy (needs DeoxIT) - Source: [yFQoVGVKAQE]
- DC offset may have drifted from calibration - Source: [yFQoVGVKAQE]
- BNC connectors may need cleaning - Source: [yFQoVGVKAQE]
- Captures 1 kHz test signals correctly - Source: [yFQoVGVKAQE]
- High-frequency response limited (aliasing at 1 MHz) - Source: [yFQoVGVKAQE]
- Triangle waves show rounding at higher frequencies - Source: [yFQoVGVKAQE]

### Historical Context: Analog vs Digital Storage Scopes

#### Analog Storage Tubes
- Tektronix developed digital storage tubes in the 1970s - Source: [yFQoVGVKAQE]
- Phosphor itself had "infinite persistence" - Source: [yFQoVGVKAQE]
- Used charged plates and special phosphors - Source: [yFQoVGVKAQE]
- Suffered from blooming and fading effects - Source: [yFQoVGVKAQE]

#### Early Digital Storage Scopes
- CRT-based scopes with computer and frame buffer - Source: [yFQoVGVKAQE]
- Tektronix and HP (Agilent) made expensive professional units - Source: [yFQoVGVKAQE]
- Extremely expensive until relatively recently - Source: [yFQoVGVKAQE]
- Rigol scopes in 2010s made DSO affordable (~$400) - Source: [yFQoVGVKAQE]

#### Modern Comparison
- Cheap handheld DSO multimeters now available for ~$80 - Source: [yFQoVGVKAQE]
- Far more capable than 1984's most expensive equipment - Source: [yFQoVGVKAQE]
- Battery powered, portable, multi-channel - Source: [yFQoVGVKAQE]
- Shows how far test equipment has advanced - Source: [yFQoVGVKAQE]

## Tools Reference

### Soldering
- TS100 Soldering Iron - Source: [_0XGFz67DIc]
- Hakko FR301 Desoldering Iron - Source: [_0XGFz67DIc]

#### iFixit FixHub Battery Powered Soldering Iron
- Battery powered soldering station - Source: [pKDRJWhd1CY]
- Quick heat-up time - Source: [pKDRJWhd1CY]
- Portable without power cord - Source: [pKDRJWhd1CY]
- Available from ifixit.com - Source: [pKDRJWhd1CY]
- More expensive than generic alternatives - Source: [pKDRJWhd1CY]

#### Pineill Battery Powered Soldering Iron
- Similar concept to iFixit FixHub at lower price - Source: [pKDRJWhd1CY]
- Battery powered, cordless operation - Source: [pKDRJWhd1CY]
- Comparable performance for basic work - Source: [pKDRJWhd1CY]
- Generic brand alternative - Source: [pKDRJWhd1CY]
- Trade-off between price and build quality - Source: [pKDRJWhd1CY]

### Testing & Measurement
- Rigol DS1054Z Four Channel Oscilloscope - Source: [_0XGFz67DIc]
- EEVBlog 121GW Multimeter - Source: [_0XGFz67DIc]

#### EEVBlog 121GW Multimeter Issues
- Known issue: Range switch can become unreliable over time - Source: [qk5mpvRM04Y]
- Symptoms: Erratic readings, range not changing properly - Source: [qk5mpvRM04Y]
- May require disassembly and switch cleaning - Source: [qk5mpvRM04Y]
- Otherwise excellent multimeter for the price - Source: [qk5mpvRM04Y]

#### USB-C Cable Tester (C2C CaberQU)
- Tests USB-C cable capabilities and wiring - Source: [qk5mpvRM04Y]
- Shows which wires are present in cable - Source: [qk5mpvRM04Y]
- Identifies data-only vs power delivery capable cables - Source: [qk5mpvRM04Y]
- Important for USB-C PD power bank applications - Source: [qk5mpvRM04Y]
- Not all USB-C cables support full power delivery - Source: [qk5mpvRM04Y]
- Cheap cables may have missing wires - Source: [qk5mpvRM04Y]
- DSLogic Basic Logic Analyzer - Source: [_0XGFz67DIc]
- Elenco LP-560 Logic Probe - Source: [_0XGFz67DIc]
- TL866II Plus (MiniPro) chip tester/EPROM programmer - Source: [_0XGFz67DIc]
- Retro Chip Tester Pro - Source: [_0XGFz67DIc]
- CRT Tester: Test emissions and determine G2/screen voltage requirements (200-300V vs 500-600V range) - Source: [_uq86UDmbsU]

### Hand Tools

#### Hemostats for Electronics Work
- Medical hemostats useful as heat sinks when soldering - Source: [xWDg10gnuVI]
- Clamp to component leads to draw heat away from sensitive parts - Source: [xWDg10gnuVI]
- Also useful as third hand for holding small components - Source: [xWDg10gnuVI]
- Various sizes available, straight and curved tips - Source: [xWDg10gnuVI]
- Can hold wires while soldering - Source: [xWDg10gnuVI]
- Locking mechanism keeps grip without constant pressure - Source: [xWDg10gnuVI]

- O-Ring Pick Set: Useful for lifting chips off boards without damage - Source: [_0XGFz67DIc]
- Plato 170 (clone) side cutters - Source: [_0XGFz67DIc]
- Head-worn magnifying goggles/dual lens flip-in head magnifier - Source: [_0XGFz67DIc]
- Magnetic screw holder/parts tray - Source: [_0XGFz67DIc]
- Jonard Tools EX-2 Chip Extractor (24-40 pins) - Source: [-9Ae-Lbz8AA]
- Wiha Precision Chip Lifter - Source: [-9Ae-Lbz8AA]
- Titanium tweezers: Solder doesn't stick to them, lightweight, excellent for SMD work - Source: [-L1IebWYEM4]
- Conductive brush multimeter probe: Metal bristle brush attached to multimeter lead for quickly tracing PCB connections - Source: [-L1IebWYEM4]
- Custom coax cables: BNC to RCA, F-connector to BNC with baluns for test equipment - Source: [-L1IebWYEM4]
- Extra-long screwdrivers: Essential for reaching recessed screws in CRT monitors and other deep enclosures - Source: [34S74BvZnhQ]
- 3D printable IC leg straightener: thingiverse.com/thing:4704636 - straightens bent DIP pins before insertion - Source: [34S74BvZnhQ]

### CRT Alignment/Adjustment Tools
- Plastic adjustment tools for CRT chokes and variable coils - Source: [KnTiOoZreD8]
- Must use plastic/non-metallic tools (metal can affect tuning) - Source: [KnTiOoZreD8]
- Extender straw allows adjustments at safe distance from high voltage - Source: [KnTiOoZreD8]
- Keeps fingers away from dangerous components in live monitors - Source: [KnTiOoZreD8]
- Often sold in pocket protector style holders - Source: [KnTiOoZreD8]

### Fiberglass Cleaning Brushes
- Glass fiber cleaning pen for PCBs - Source: [kncrJYTRbnc]
- Oraly brand (German company) offers quality brushes - Source: [kncrJYTRbnc]
- Much stiffer bristle than cheap AliExpress alternatives - Source: [kncrJYTRbnc]
- Refill packs available (AliExpress versions often have no refills) - Source: [kncrJYTRbnc]
- Different thicknesses and bristle styles available - Source: [kncrJYTRbnc]
- Good for cleaning corrosion and oxidation from contacts and PCB pads - Source: [kncrJYTRbnc]
- Can remove labels/stickers from components - Source: [kncrJYTRbnc]

### IC Organization Strategies
- For large collections, bin chips by number range (7400-7499, etc.) - Source: [ueyv2vRIQK8]
- Separate common types from exotic/rare chips - Source: [ueyv2vRIQK8]
- Label bins clearly by chip family or number range - Source: [ueyv2vRIQK8]
- Spreadsheet inventory helps find chips quickly - Source: [ugu_7DW-wCI]
- Time consuming to catalog but saves search time later - Source: [ugu_7DW-wCI]

### Vintage ICs Reference
- SPO256 Speech Synthesizer: General Instruments chip used in many 1980s speech applications - Source: [34S74BvZnhQ]
- SPO256 used in: Currah µSpeech (ZX Spectrum), SSI-263 (Apple II), various TRS-80 speech units - Source: [34S74BvZnhQ]

#### TIL-311 Hexadecimal Display
- Texas Instruments 7-segment display with integrated TTL logic - Source: [TaHKjittUNI]
- Combines LED display with internal decoder, latch, and driver - Source: [TaHKjittUNI]
- 4-bit latched input supports hexadecimal (0-F) display - Source: [TaHKjittUNI]
- Individual corner pixels allow A, b, C, d, E, F characters (not just 0-9) - Source: [TaHKjittUNI]
- Corner pixels driven separately unlike standard 7-segment displays - Source: [TaHKjittUNI]
- Standard 7-segment shows lowercase "d" for D (would look like 0 otherwise) - Source: [TaHKjittUNI]
- TIL-311 shows proper uppercase D with corner pixels off - Source: [TaHKjittUNI]
- Blanking input pin available for display control - Source: [TaHKjittUNI]
- Separate decimal point output - Source: [TaHKjittUNI]
- Date codes from 1976 seen on available chips - Source: [TaHKjittUNI]
- TAOS acquired TI display product line (datasheet dated 2004) - Source: [TaHKjittUNI]
- Older LEDs much dimmer than modern equivalents - Source: [TaHKjittUNI]
- Cool for 70s-era computer projects - Source: [TaHKjittUNI]

#### 65C816 Processor
- Western Design Center 16-bit processor (Apple IIgs CPU) - Source: [TaHKjittUNI]
- Also used in Super Nintendo (integrated form) - Source: [TaHKjittUNI]
- Can be used with adapter in 6502 machines like VIC-20 - Source: [TaHKjittUNI]
- Requires special programming to take advantage of 16-bit features - Source: [TaHKjittUNI]

#### 68010 PLCC Package
- Motorola 68010 available in PLCC (surface mount) package - Source: [TaHKjittUNI]
- Can upgrade Macintosh Classic (which has surface mount 68000) - Source: [TaHKjittUNI]
- Slight speed boost over 68000 - Source: [TaHKjittUNI]
- Requires removing surface mount CPU and adding PLCC socket - Source: [TaHKjittUNI]

### EPROM Handling and Protection
- EPROMs require 253.7nm UVC light to erase - not present in indoor LED lighting - Source: [a1e-NGZZZEA]
- Paper stickers fully protect EPROMs from UV erasure (tested 780 minutes in eraser) - Source: [a1e-NGZZZEA]
- Foil/metallic stickers also protect (obviously block all light) - Source: [a1e-NGZZZEA]
- Uncovered EPROMs erase in ~15-30 minutes in UV eraser - Source: [a1e-NGZZZEA]
- Indoor lighting (LED, fluorescent) won't erase EPROMs - no significant UV output - Source: [a1e-NGZZZEA]
- Sunlight can erase EPROMs over extended exposure (UVC in sunlight) - Source: [a1e-NGZZZEA]
- EPROMs inside computers are completely safe - no UV reaches them - Source: [a1e-NGZZZEA]
- Post-it note paper is sufficient protection if concerned - Source: [a1e-NGZZZEA]

### Display/Video
- RetroTink 2X Upconverter: Connect retro computers (like C64) to HDMI displays - Source: [_0XGFz67DIc]

### Chip Removal
- Damage-free chip removal technique (referenced video) - Source: [_0XGFz67DIc]

### ROMulator (bitfixer)
- FPGA-based ROM/RAM replacer for 6502 and Z80 machines - Source: [1W5J_WOIxbc]
- Plugs into CPU socket, intercepts memory addressing - Source: [1W5J_WOIxbc]
- Configure via Raspberry Pi to load ROM images and create memory maps - Source: [1W5J_WOIxbc]
- Can use ESP8266/ESP32 instead of Pi (included programmer kit) - Source: [1W5J_WOIxbc]
- DIP switches configure memory maps - Source: [1W5J_WOIxbc]
- Can dump entire system memory to Pi for analysis - Source: [1W5J_WOIxbc]
- Useful for debugging bad RAM select logic (bypasses motherboard) - Source: [1W5J_WOIxbc]
- Z80 version: make program_z80 (build and flash from Pi) - Source: [1W5J_WOIxbc]
- Website: bitfixer.com - Source: [1W5J_WOIxbc]
- Less expensive than competitors with more flexibility - Source: [1W5J_WOIxbc]
- 6502 version works with PET, VIC-20, other 6502 machines - Source: [1W5J_WOIxbc]
- Z80 version works with TRS-80, ZX Spectrum, CP/M machines - Source: [1W5J_WOIxbc]

### EPROM Emulator (Open Source by Kris Sekula)

#### Overview
- Open source EPROM emulator for testing/development - Source: [JR0DCzCiAPk]
- Created by Kris Sekula (mygeekyhobby.com) - Source: [JR0DCzCiAPk]
- Arduino Nano based design - Source: [JR0DCzCiAPk]
- GitHub: github.com/Kris-Sekula/EPROM-EMU-NG - Source: [JR0DCzCiAPk]

#### Supported EPROM Types
- 2716 (2KB) - Source: [JR0DCzCiAPk]
- 2732 (4KB) - Source: [JR0DCzCiAPk]
- 2764 (8KB) - Source: [JR0DCzCiAPk]
- 27128 (16KB) - Source: [JR0DCzCiAPk]
- 27256 (32KB) - Source: [JR0DCzCiAPk]
- 27512 (64KB) - Source: [JR0DCzCiAPk]

#### Features
- SPI flash for persistent storage of images - Source: [JR0DCzCiAPk]
- Images persist across power cycles - Source: [JR0DCzCiAPk]
- Auto-reset feature: can automatically reset target system when new image loaded - Source: [JR0DCzCiAPk]
- Useful for rapid iteration during ROM development - Source: [JR0DCzCiAPk]
- USB interface for loading images from PC - Source: [JR0DCzCiAPk]

#### Use Cases
- Testing diagnostic ROMs without burning EPROMs - Source: [JR0DCzCiAPk]
- ROM development and debugging - Source: [JR0DCzCiAPk]
- Trying different firmware versions quickly - Source: [JR0DCzCiAPk]
- Vintage computer repair (test with known-good ROM) - Source: [JR0DCzCiAPk]

#### Construction
- Open source hardware design - Source: [JR0DCzCiAPk]
- PCB files available on GitHub - Source: [JR0DCzCiAPk]
- Uses common Arduino Nano clone - Source: [JR0DCzCiAPk]
- Total cost of parts relatively low - Source: [JR0DCzCiAPk]
