# Commodore

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| SuperPET 9000 | Professional Computer | [gNbM0UzWrnQ] |
| VIC-20 Diagnostic Harness | Test Equipment | [GUvasXbxUPg] |
| C64 | Home Computer | [b-oHw0VBvU8], [icnPtyovOKU] |
| MPS-803 | Dot Matrix Printer | [icnPtyovOKU] |
| C128 | Desktop Computer | [0u6I_VAO22A], [2C3Y-3Smhz8] |
| Amiga 1080 | CRT Monitor | [8cLNKB_sajA] |
| 1084 | CRT Monitor | [8cLNKB_sajA], [gISS9JsnRX8], [rB_Sayi600o] |
| 1802 | CRT Monitor | [efj8YUYUKSw] |
| C16 | Desktop Computer | [758KMi_EG1Y] |
| Plus/4 | Desktop Computer | [758KMi_EG1Y] |
| 1551 | Floppy Drive | [758KMi_EG1Y], [eFatlDatjZM] |
| 1531 | Datasette | [758KMi_EG1Y], [TaHKjittUNI] |
| VIC-20 | Home Computer | [AT7oZ_xD2Go], [b-oHw0VBvU8], [EhDOV2oMAQM], [NYybIWL2o0o] |
| MOS 6582 SID | Sound Chip | [EhDOV2oMAQM] |
| C64G | Home Computer (German) | [mDpZhaCbL-k] |
| DesTest Max-Switch | RAM Test Cartridge | [M64hCqBpSDE] |
| SwiftLink | Serial Cartridge | [M64hCqBpSDE] |
| Enhancer 2000 | 1541 Clone Drive | [AT7oZ_xD2Go] |
| Amiga 500 | Home Computer | [eFatlDatjZM], [ksimpQeU3QA], [r8wuX5SwCOM] |
| Amiga 2000 HD | Desktop Computer | [SWpL6aqQDlY] |
| A2091 | SCSI Controller | [SWpL6aqQDlY] |
| A2286 | 286 Bridge Board | [SWpL6aqQDlY] |
| 68030 Accelerator | CPU Accelerator | [SWpL6aqQDlY] |
| C64 Direct-to-TV | Single-Chip C64 | [X5q25JlkuAc] |
| C64 Mini | Emulation Console | [X5q25JlkuAc] |
| C64 Maxi | Emulation Console | [X5q25JlkuAc] |
| Ultimate 64 Elite | FPGA Recreation | [X5q25JlkuAc] |

## Platform-Specific Knowledge

### Amiga 2000

#### Overview
- Desktop Amiga with expansion slots - Source: [SWpL6aqQDlY]
- Susceptible to battery leak damage near CPU - Source: [SWpL6aqQDlY]
- More difficult to repair than Amiga 500 - Source: [SWpL6aqQDlY]
- Large case makes access and work difficult - Source: [SWpL6aqQDlY]

#### Battery Leak Damage
- Battery located near CPU area - Source: [SWpL6aqQDlY]
- Corrosion damages CPU socket traces - Source: [SWpL6aqQDlY]
- Damage can extend to processor expansion slot - Source: [SWpL6aqQDlY]
- Corrosion also damages slot contact fingers - Source: [SWpL6aqQDlY]
- May require multiple repair attempts - Source: [SWpL6aqQDlY]
- Traces can test fine with multimeter but fail under load - Source: [SWpL6aqQDlY]

#### Intermittent CPU Socket Issues
- Symptom: Black screen with sync signals but no video - Source: [SWpL6aqQDlY]
- Power LED may not go from dim to bright - Source: [SWpL6aqQDlY]
- Pressing down on CPU socket can make it boot - Source: [SWpL6aqQDlY]
- Flexing motherboard affects connection - Source: [SWpL6aqQDlY]
- Proper fix: Remove socket, sand solder mask, inspect all traces - Source: [SWpL6aqQDlY]
- Quick hack: Wedge something under CPU socket to apply pressure - Source: [SWpL6aqQDlY]

#### Hardware Notes
- Uses metric screws throughout (not PC compatible) - Source: [SWpL6aqQDlY]
- Slot bracket screws are metric - Source: [SWpL6aqQDlY]
- Hard to find replacement screws - Source: [SWpL6aqQDlY]
- Can have 2MB chip RAM with Agnes upgrade - Source: [SWpL6aqQDlY]

#### Floppy Drives
- Drives rely on door spring tension for ejection - Source: [SWpL6aqQDlY]
- Drive without cover won't eject disks properly - Source: [SWpL6aqQDlY]

### Commodore A2091 SCSI Controller

#### Overview
- 16-bit Zorro II SCSI card - Source: [SWpL6aqQDlY]
- Supports DMA transfer for good performance - Source: [SWpL6aqQDlY]
- Has RAM expansion capability - Source: [SWpL6aqQDlY]
- Reliable with real SCSI hard drives - Source: [SWpL6aqQDlY]

#### SCSI2SD Compatibility Issues
- Random disk errors when using SCSI2SD - Source: [SWpL6aqQDlY]
- Multiple A2091 cards exhibit same problem - Source: [SWpL6aqQDlY]
- Works fine with spinning SCSI hard drives - Source: [SWpL6aqQDlY]
- May need specific SCSI2SD settings for compatibility - Source: [SWpL6aqQDlY]

### Commodore 68030 Accelerator Card

#### Overview
- 68030 CPU at 25MHz with FPU - Source: [SWpL6aqQDlY]
- 4MB 32-bit RAM onboard - Source: [SWpL6aqQDlY]
- Plugs into processor expansion slot - Source: [SWpL6aqQDlY]

#### Boot Process
- Requires motherboard CPU to work for initial boot - Source: [SWpL6aqQDlY]
- System bootstraps with motherboard 68000 first - Source: [SWpL6aqQDlY]
- Then hands off to accelerator card - Source: [SWpL6aqQDlY]
- Accelerator ROM handles takeover - Source: [SWpL6aqQDlY]
- Once running, very stable - motherboard CPU issues don't affect operation - Source: [SWpL6aqQDlY]

### Commodore A2286 Bridge Board

#### Overview
- 286 AT emulator board for Amiga 2000 - Source: [SWpL6aqQDlY]
- Better than XT bridge board (more common) - Source: [SWpL6aqQDlY]

#### RAM Limitation
- Too much RAM in Amiga can cause bridge board issues - Source: [SWpL6aqQDlY]
- May need to limit system RAM for compatibility - Source: [SWpL6aqQDlY]


### Commodore SuperPET 9000

#### Overview
- Dual-processor PET computer - Source: [gNbM0UzWrnQ]
- Contains both 6809 and 6502 CPUs - Source: [gNbM0UzWrnQ]
- 6809 used for advanced programming languages - Source: [gNbM0UzWrnQ]
- 6502 maintains standard PET compatibility - Source: [gNbM0UzWrnQ]
- Educational/professional market target - Source: [gNbM0UzWrnQ]
- Rare and sought-after machine - Source: [gNbM0UzWrnQ]

#### Software
- Waterloo Micro software development environment - Source: [gNbM0UzWrnQ]
- Pascal programming language support - Source: [gNbM0UzWrnQ]
- Fortran programming language support - Source: [gNbM0UzWrnQ]
- COBOL programming language support - Source: [gNbM0UzWrnQ]
- APL programming language support - Source: [gNbM0UzWrnQ]
- Languages run on 6809 processor - Source: [gNbM0UzWrnQ]

#### User Port Connectors
- 24-pin card edge connector for user port - Source: [gNbM0UzWrnQ]
- Same connector style used on C64 and other Commodore computers - Source: [gNbM0UzWrnQ]
- Connectors available from VCF swap meets - Source: [gNbM0UzWrnQ]

### Commodore 128

#### Idun Cartridge
- Pronounced "Eden" not "I-done" - Source: [0u6I_VAO22A]
- Raspberry Pi + Propeller 1 microcontroller design - Source: [0u6I_VAO22A]
- Works with Pi Zero 2 (recommended), any recent Pi compatible - Source: [0u6I_VAO22A]
- DOS-like shell interface, works in 40-col, 80-col, and C64 mode - Source: [0u6I_VAO22A]
- Virtual drive emulation (no IEC connection needed) - Source: [0u6I_VAO22A]
- Loads D64 images and tape software quickly - Source: [0u6I_VAO22A]
- Telnet BBS access through WiFi - Source: [0u6I_VAO22A]
- VT-100 terminal emulator with ANSI font support - Source: [0u6I_VAO22A]
- Lua scripting runs on Pi, feeds back to C128 - Source: [0u6I_VAO22A]
- Can do high-res graphics with calculations on Pi - Source: [0u6I_VAO22A]
- 3D printed case available - Source: [0u6I_VAO22A]
- GitHub: github.com/idun-project/idun-cartridge - Source: [0u6I_VAO22A]

#### Memory Architecture
- Two banks of 64K RAM (Bank 0 and Bank 1) - Source: [2C3Y-3Smhz8]
- MMU supports up to 256K (four banks) but only two populated on standard boards - Source: [2C3Y-3Smhz8]
- First 0x400 bytes always mapped from Bank 0 (zero page, stack) - Source: [2C3Y-3Smhz8]
- Screen buffer typically at 0x400-0x800 in text mode - Source: [2C3Y-3Smhz8]
- VIC-2E (48-pin) handles display, similar to C64's VIC-2 - Source: [2C3Y-3Smhz8]
- Color RAM is separate static RAM, not part of main memory - Source: [2C3Y-3Smhz8]

#### RAM Diagnostics Without Special Tools
- Screen code 32 decimal = space, 48 decimal = zero character - Source: [2C3Y-3Smhz8]
- If zeros appear instead of spaces, calculate which data bit is stuck - Source: [2C3Y-3Smhz8]
- Space = 0b00100000, Zero = 0b00110000, difference is data bit 4 - Source: [2C3Y-3Smhz8]
- Look up RAM chip pinout in schematic to find chip for that data bit - Source: [2C3Y-3Smhz8]
- C128 schematics: zimmers.net/anonftp/pub/cbm/schematics/computers/c128/ - Source: [2C3Y-3Smhz8]
- C128 RAM map: cubic.org/~doj/c64/mapping128.pdf - Source: [2C3Y-3Smhz8]
- Flashing characters indicate intermittent RAM failure - Source: [2C3Y-3Smhz8]
- Random crashes = bad RAM in zero page or stack area - Source: [2C3Y-3Smhz8]

#### RAM Chip Layout
- Lower row of RAM chips = Bank 0 - Source: [2C3Y-3Smhz8]
- Upper row of RAM chips = Bank 1 - Source: [2C3Y-3Smhz8]
- RAS line common to all RAM chips - Source: [2C3Y-3Smhz8]
- CAS line separated: RAM_CAS0 for Bank 0, RAM_CAS1 for Bank 1 - Source: [2C3Y-3Smhz8]

#### RAM Repair - Piggyback Method
- Place known-good chip on top of suspected bad chip - Source: [2C3Y-3Smhz8]
- If screen clears up, that chip is confirmed bad - Source: [2C3Y-3Smhz8]
- Works because good chip can override stuck-high outputs - Source: [2C3Y-3Smhz8]
- CRITICAL: Orient chip correctly (notch facing same direction) - Source: [2C3Y-3Smhz8]
- Putting chip on wrong way won't damage chips but won't work - Source: [2C3Y-3Smhz8]

#### RAM Repair - No-Desolder Method
- Cut only pins 2 and 14 on 4164 (output pins) - Source: [2C3Y-3Smhz8]
- Solder new RAM chip directly on top of old chip - Source: [2C3Y-3Smhz8]
- Bend pins 2 and 14 outward on new chip to clear cut pins - Source: [2C3Y-3Smhz8]
- All other pins are inputs and can remain connected - Source: [2C3Y-3Smhz8]
- Eliminates bus conflict from output drivers - Source: [2C3Y-3Smhz8]
- Safer than desoldering if inexperienced - won't damage traces - Source: [2C3Y-3Smhz8]
- 41256 chips can substitute for 4164 (extra pin 1 not used) - Source: [2C3Y-3Smhz8]

#### SRAM Replacement Module (Modern)
- PCB module replaces all DRAM chips with single SRAM chip - Source: [FnLKPVzK7bo]
- Socket into existing DRAM positions or solder directly - Source: [FnLKPVzK7bo]
- Uses Cypress SRAM chip (much larger capacity than 64K, but only using 64K) - Source: [FnLKPVzK7bo]
- Far faster than 200ns 4164 DRAM - Source: [FnLKPVzK7bo]
- Potential compatibility issues with VIC-2 Kari FPGA replacement - Source: [FnLKPVzK7bo]
- VIC-2 graphics chip reads RAM directly for display - timing differences may cause issues - Source: [FnLKPVzK7bo]
- Works well on original machines, FPGA replacements may need tuning - Source: [FnLKPVzK7bo]
- Good long-term solution as 4164 chips become scarce - Source: [FnLKPVzK7bo]

#### Common Issues
- MT RAM (Micron Technology) fails at high rate - Source: [2C3Y-3Smhz8]
- Non-MT RAM also fails but less frequently - Source: [2C3Y-3Smhz8]
- All C128s have factory bodge wire from chip to Z80 CPU - Source: [2C3Y-3Smhz8]

### Commodore Amiga 1080 Monitor

#### Overview
- First monitor released with Amiga 1000 (November 1985) - Source: [8cLNKB_sajA]
- Predecessor to famous 1084 line - essentially same design - Source: [8cLNKB_sajA]
- Very versatile: works with Amiga, C64, C128, IBM PC (CGA), Apple II - Source: [8cLNKB_sajA]
- 9-pin digital/analog input plus chroma/luma (S-video type) input - Source: [8cLNKB_sajA]
- Isolated transformer design (safe grounding, not hot chassis) - Source: [8cLNKB_sajA]

#### Inputs
- 9-pin digital RGB (TTL CGA compatible) - Source: [8cLNKB_sajA]
- Analog RGB input on same connector - Source: [8cLNKB_sajA]
- Chroma/luma input (S-video style) for C64/C128 - Source: [8cLNKB_sajA]
- Composite video for Apple II and other computers - Source: [8cLNKB_sajA]

#### Power Supply
- Switch mode power supply (not linear dropper) - Source: [8cLNKB_sajA]
- B+ voltage: 115VDC from switching supply - Source: [8cLNKB_sajA]
- Has 3A fuse and 1.2A fuse (B+ rail) - Source: [8cLNKB_sajA]
- Flyback generates all other voltages from B+ - Source: [8cLNKB_sajA]
- Power LED powered from flyback rail - no LED = no horizontal drive - Source: [8cLNKB_sajA]

#### Cracked PCB Repair (from drop damage)
- Flyback transformer stabilized by plastic bracket to case - Source: [8cLNKB_sajA]
- Drop damage can snap bracket and crack PCB around flyback - Source: [8cLNKB_sajA]
- Cracks break traces to flyback pins - must bodge wire across - Source: [8cLNKB_sajA]
- Methodically check each pin trace for continuity across crack - Source: [8cLNKB_sajA]
- Use thick wire for high-current horizontal drive transistor traces - Source: [8cLNKB_sajA]
- Apply hot glue to stabilize bodge wires after repair - Source: [8cLNKB_sajA]

#### Troubleshooting
- Check horizontal drive transistor base for 15.7kHz drive signal - Source: [8cLNKB_sajA]
- No signal on collector = trace broken between B+ and transistor - Source: [8cLNKB_sajA]
- Use battery-powered oscilloscope near high voltage sections - Source: [8cLNKB_sajA]
- Normal high voltage: ~26.5kV (max 27.5kV for X-ray protection) - Source: [8cLNKB_sajA]

#### Color Purity Adjustment
- Remove yoke wedges (glued plastic spacers) - Source: [8cLNKB_sajA]
- Loosen yoke tie-down and slide yoke forward - Source: [8cLNKB_sajA]
- Adjust purity rings (closest to front) for even color distribution - Source: [8cLNKB_sajA]
- Slide yoke back for proper beam landing - Source: [8cLNKB_sajA]
- Reinsert wedges to adjust convergence - Source: [8cLNKB_sajA]
- Time-consuming and fiddly process - Source: [8cLNKB_sajA]

#### Neck Board Capacitors
- B+ comes in at 130V via large electrolytic (4.7µF 160V) - Source: [8cLNKB_sajA]
- Second cap (100µF 16V) for bias circuit - Source: [8cLNKB_sajA]
- Ripple in picture may indicate failing neck board caps - Source: [8cLNKB_sajA]

#### Degaussing
- Built-in degauss coil may fail (thermistor burns out) - Source: [8cLNKB_sajA]
- Manual degaussing coil can help with color purity - Source: [8cLNKB_sajA]
- Normal degaussing time: ~10 seconds max, don't overdo it - Source: [8cLNKB_sajA]

### Commodore 1084 Monitor

#### Variations (Phillips/Boxy Version)
- 1084 mono and 1084-S stereo versions exist - Source: [gISS9JsnRX8], [rB_Sayi600o]
- Manufactured by Phillips for Commodore - Source: [gISS9JsnRX8], [rB_Sayi600o]
- Sold under Phillips, Magnavox, and Commodore brands - Source: [gISS9JsnRX8], [rB_Sayi600o]
- North American NTSC version only decodes NTSC composite - Source: [gISS9JsnRX8]
- PAL version only decodes PAL composite - Source: [gISS9JsnRX8]
- RGB input works with both 50Hz and 60Hz signals - Source: [gISS9JsnRX8]
- Monitor automatically adjusts height for 50Hz vs 60Hz - Source: [gISS9JsnRX8]
- Case is painted so doesn't yellow, but can scratch - Source: [rB_Sayi600o]
- Front door always breaks (plastic is brittle) - Source: [rB_Sayi600o]
- Provisions for tilt-swivel stand under base (rarely seen) - Source: [rB_Sayi600o]

#### Inputs
- TTL RGB (CGA compatible) - Source: [gISS9JsnRX8]
- Analog RGB through D-connector - Source: [gISS9JsnRX8]
- Composite video - Source: [gISS9JsnRX8]
- Luma/Chroma (S-video style) for C64/C128/Atari 800 - Source: [gISS9JsnRX8], [rB_Sayi600o]
- Audio input with built-in speaker - Source: [gISS9JsnRX8]

#### Sync Signal Flexibility (Boxy Phillips Version)
- Analog RGB input accepts H+V sync OR composite sync - Source: [rB_Sayi600o]
- Two pins on connector for H sync and V sync - Source: [rB_Sayi600o]
- Internally combines sync signals then splits them again - Source: [rB_Sayi600o]
- Can feed composite sync into either H or V pin and it works - Source: [rB_Sayi600o]
- Compatible with: Apple IIgs (composite sync), Atari ST (H+V sync), CoCo 3 (composite), Amiga (both) - Source: [rB_Sayi600o]
- Most flexible 1084 variant for sync compatibility - Source: [rB_Sayi600o]
- Later 1084s (Amiga 4000 era) only accept composite sync - Source: [rB_Sayi600o]

#### TTL RGB Board (Internal)
- Small shielded vertical board converts digital RGB to analog - Source: [rB_Sayi600o]
- CRT requires analog RGB internally - Source: [rB_Sayi600o]
- Uses resistors, diodes, transistors for primitive DAC - Source: [rB_Sayi600o]
- Handles CGA brown color exception (dark yellow remapped) - Source: [rB_Sayi600o]

##### Early Version Dual Mode (1986 era)
- Some early Phillips 1084s have dual RGB decode modes - Source: [rB_Sayi600o]
- Mode 1: CGA color mapping - Source: [rB_Sayi600o]
- Mode 2: Apple RGB color mapping (Apple III, Apple IIe RGB card) - Source: [rB_Sayi600o]
- Apple RGB has different color palette than CGA - Source: [rB_Sayi600o]
- Switch mode by grounding extra pin on connector - Source: [rB_Sayi600o]
- Without correct mode, Apple RGB colors look wrong (except black/white) - Source: [rB_Sayi600o]
- Later 1084s (1988+) only support CGA mode - Source: [rB_Sayi600o]

#### Chroma/Luma vs Composite Switch
- Button on back switches between composite and chroma/luma - Source: [rB_Sayi600o]
- Chroma/luma mode disables notch filter - Source: [rB_Sayi600o]
- With only composite connected, chroma/luma mode = sharp B&W - Source: [rB_Sayi600o]
- Monochrome signal through composite in chroma mode = very sharp - Source: [rB_Sayi600o]
- Can display 80-column text clearly with chroma/luma mode - Source: [rB_Sayi600o]
- Same design as Commodore 1702 but with higher resolution CRT - Source: [rB_Sayi600o]

#### High Resolution CRT
- Higher dot pitch than 1702 (smaller phosphor dots) - Source: [rB_Sayi600o]
- Better resolving power for fine detail than 1702 - Source: [rB_Sayi600o]
- Trade-off: Less vibrant/bright than 1702 (more blocked by shadow mask) - Source: [rB_Sayi600o]
- 80-column text sharp on this CRT vs blurry on 1702 - Source: [rB_Sayi600o]
- Handles Amiga high-res modes well - Source: [rB_Sayi600o]

#### VCR Button
- Button on back labeled "VCR" - Source: [rB_Sayi600o]
- Affects sync decoder chip - Source: [rB_Sayi600o]
- Purpose unclear, manual says use when connecting VCR - Source: [rB_Sayi600o]

#### Controls
- H-size and V-size accessible on back (not through holes) - Source: [rB_Sayi600o]
- Earlier 1084s require screwdriver through case holes - Source: [rB_Sayi600o]
- Sharpness, color, hue (NTSC only), brightness, contrast on front - Source: [rB_Sayi600o]
- PAL monitors have no hue control (color set by signal) - Source: [rB_Sayi600o]

#### Testing Procedure
- Listen for loud whine (shorted flyback) - Source: [rB_Sayi600o]
- Listen for arcing/snapping (dying flyback) - Source: [rB_Sayi600o]
- Arcing causes momentary picture shrink and dim - Source: [rB_Sayi600o]
- Look for black soot around anode cap (high hours indicator) - Source: [rB_Sayi600o]
- Check color balance on white - slightly green = weak blue gun - Source: [rB_Sayi600o]
- Power supply test: Bright/dark transitions shouldn't cause geometry bulge - Source: [rB_Sayi600o]

#### NTSC Brightness Calibration
- Color bars pattern has three black levels in bottom area - Source: [rB_Sayi600o]
- Middle bar is "blacker than black" - shouldn't be visible - Source: [rB_Sayi600o]
- Adjust brightness so you can JUST see the reference black bar - Source: [rB_Sayi600o]
- Contrast (picture) adjusts white level/brightness - Source: [rB_Sayi600o]
- Brightness too high = washed out, gray blacks - Source: [rB_Sayi600o]

#### Flyback Transformer Reliability
- Early white flyback with blue AND red caps: RELIABLE, never fails - Source: [gISS9JsnRX8]
- Black flyback version: RELIABLE, no known failures - Source: [gISS9JsnRX8]
- Later white flyback WITHOUT blue cap: UNRELIABLE, all eventually fail - Source: [gISS9JsnRX8]
- Bad flybacks have red cap only plus two black wires (screen and focus) - Source: [gISS9JsnRX8]
- Monitor date code 1987-1988: Likely has good flyback - Source: [gISS9JsnRX8]
- Monitor date code 1989+: Likely has bad flyback - Source: [gISS9JsnRX8]
- Look through case slats with flashlight to identify flyback type - Source: [gISS9JsnRX8]
- Replacement flybacks available (see Retro Channel video) - Source: [gISS9JsnRX8]

#### SCART RGB Modification (Ultimate Version)
- Co-developed by Adrian and Mark at The Retro Channel - Source: [gISS9JsnRX8]
- SCART jack footprint already exists on PCB - just remove solder from pins - Source: [gISS9JsnRX8]
- Instructions: imgur.com/gallery/1084s-scart-mod-component-locations-xMcx2ZE - Source: [gISS9JsnRX8]
- Companion video by Mark at Retro Channel has detailed walkthrough - Source: [gISS9JsnRX8]
- Different instructions for mono (1084) vs stereo (1084-S) versions - Source: [gISS9JsnRX8]

#### SCART Mod Components (Mono Version)
- Install SCART connector on PCB footprint - Source: [gISS9JsnRX8]
- Add jumper link between scar composite input and yellow composite jack - Source: [gISS9JsnRX8]
- Install 22k resistor at R303 - Source: [gISS9JsnRX8]
- Install 5.6k resistors at R305 and R306 (combines stereo to mono) - Source: [gISS9JsnRX8]
- Add jumper link J9275 for audio routing - Source: [gISS9JsnRX8]
- Check for existing jumper links (vary between monitors) - Source: [gISS9JsnRX8]

#### VCR Switch Mod (Fast Blanking Override)
- VCR switch on back rarely used - enables "freewheel sync" for PAL VCRs - Source: [gISS9JsnRX8]
- Can be repurposed to force RGB mode (fast blanking override) - Source: [gISS9JsnRX8]
- Wire 10K resistor + 1N4148 diode from switch to RGB/composite switching IC - Source: [gISS9JsnRX8]
- Diode band faces front of monitor - Source: [gISS9JsnRX8]
- When pushed in: Forces RGB mode with sync from composite jack - Source: [gISS9JsnRX8]
- Useful for game consoles (PlayStation) that output RGB with composite sync - Source: [gISS9JsnRX8]

#### PlayStation 1/2 RGB Connection
- PS1/PS2 output RGB but sync is on composite video pin (SCART standard) - Source: [gISS9JsnRX8]
- Monitor's D-connector RGB input expects TTL sync, not composite video - Source: [gISS9JsnRX8]
- Without mod: Picture looks fine initially but rolls when graphics appear - Source: [gISS9JsnRX8]
- Sync separator IC gets confused by video information in composite signal - Source: [gISS9JsnRX8]
- With VCR switch mod: Connect RGB to D-jack, composite to yellow jack, push VCR button - Source: [gISS9JsnRX8]

#### General Reliability
- Caps are rock solid, rarely need replacement - Source: [gISS9JsnRX8]
- Most common issue: Bad solder joints around flyback - Source: [gISS9JsnRX8]
- RF shield (North America only) difficult to remove - use side cutters - Source: [gISS9JsnRX8]
- Shield not necessary and not present on monitors sold elsewhere - Source: [gISS9JsnRX8]

#### TTL RGB Converter Board
- Vertical daughter board converts CGA TTL RGB to analog - Source: [gISS9JsnRX8]
- Monitor needs analog RGB internally - Source: [gISS9JsnRX8]
- Older versions supported Apple IIgs RGB mode (different color mapping) - Source: [gISS9JsnRX8]
- Later versions (this one) only support standard CGA TTL - Source: [gISS9JsnRX8]

### Commodore 1802 Monitor

#### Overview
- 13" CRT replacement for Commodore 1702 - Source: [efj8YUYUKSw]
- Beige color to match C64C and Amiga - Source: [efj8YUYUKSw]
- Made by Daewoo in Korea (1985-1986 manufacture) - Source: [efj8YUYUKSw]
- Rarer than other Commodore monitors - Source: [efj8YUYUKSw]
- Front door often missing (commonly broke off) - Source: [efj8YUYUKSw]

#### Inputs
- Separated luma/chroma input (like 1702) - Source: [efj8YUYUKSw]
- Composite video input - Source: [efj8YUYUKSw]
- Monochrome input (additional feature vs 1702) - Source: [efj8YUYUKSw]
- Monochrome input: same resolution as S-video, green tint - Source: [efj8YUYUKSw]
- 80-column text not sharp enough on this CRT (low dot pitch) - Source: [efj8YUYUKSw]
- Three position switch selects input mode - Source: [efj8YUYUKSw]

#### Design Notes
- Picture vertically shifted down by design - Source: [efj8YUYUKSw]
- Designed for C64 which has picture closer to top - Source: [efj8YUYUKSw]
- No vertical position control on this monitor - Source: [efj8YUYUKSw]
- Smaller speaker than 1702 (worse sound quality) - Source: [efj8YUYUKSw]

#### Main IC
- Toshiba TA7670P video processing IC - Source: [efj8YUYUKSw]
- Handles both horizontal and vertical oscillator functions - Source: [efj8YUYUKSw]
- Similar to IC used in contemporary monitors - Source: [efj8YUYUKSw]

#### Common Failure Mode
- C310: 470µF 35V electrolytic in vertical deflection circuit - Source: [efj8YUYUKSw]
- Located near power resistors that get very hot - Source: [efj8YUYUKSw]
- Capacitor bakes and leaks over time - Source: [efj8YUYUKSw]
- Symptoms: Collapsed vertical deflection (image in middle third of screen) - Source: [efj8YUYUKSw]
- Visual inspection shows brown gunk and corrosion near cap - Source: [efj8YUYUKSw]
- Cap leakage can corrode nearby component leads - Source: [efj8YUYUKSw]

#### Repair
- Replace C310 with equivalent (470µF 35V or higher voltage) - Source: [efj8YUYUKSw]
- Clean board thoroughly with IPA after removing leaked electrolyte - Source: [efj8YUYUKSw]
- Check nearby resistor leads for corrosion damage - Source: [efj8YUYUKSw]
- Other capacitors often fine (Daewoo-branded caps were good quality) - Source: [efj8YUYUKSw]

#### Diagnostics
- ESR meter useful for in-circuit capacitor testing - Source: [efj8YUYUKSw]
- Look for high D values at 1kHz - Source: [efj8YUYUKSw]
- For vertical circuits, test at 100Hz (closer to 60Hz vertical rate) - Source: [efj8YUYUKSw]
- Visual inspection for brown/baked areas near hot components - Source: [efj8YUYUKSw]
- Tantalums typically measure lower than electrolytics (different technology) - Source: [efj8YUYUKSw]

#### Shipping Damage
- Brittle plastic from age/yellowing - Source: [efj8YUYUKSw]
- Internal mounting standoffs commonly snap during shipping - Source: [efj8YUYUKSw]
- Can be repaired with plastic welder/epoxy - Source: [efj8YUYUKSw]

### Commodore 16 / Plus/4

#### Overview
- 264 series computers with improved BASIC 3.5 - Source: [758KMi_EG1Y]
- More RAM available for BASIC (60,000 bytes free) - Source: [758KMi_EG1Y]
- Uses DC barrel jack for power (center negative) - Source: [758KMi_EG1Y]
- Has redefine colors (more than 16 colors available) - Source: [758KMi_EG1Y]

#### Limitations vs C64
- No hardware sprites - Source: [758KMi_EG1Y]
- No hardware scrolling - Source: [758KMi_EG1Y]
- Sound similar to VIC-20 (simplistic) - Source: [758KMi_EG1Y]
- Weird keyboard layout - Source: [758KMi_EG1Y]
- Not compatible with C64 software - Source: [758KMi_EG1Y]

#### 8501 CPU Replacement (Daniel Manon)
- Original 8501 CPUs extremely failure-prone - Source: [OU_S0Zk9Qx0]
- Very hard to find replacements as they only made chips for TED machines - Source: [OU_S0Zk9Qx0]
- Daniel Manon created 6502-based replacement using standard 6502 + GAL 16V8 + bus transceivers - Source: [OU_S0Zk9Qx0]
- Available at: freepascal.org/~daniel/8501/ - Source: [OU_S0Zk9Qx0]
- PCBs available at PCBWay - Source: [OU_S0Zk9Qx0]
- Uses 74-series logic chips for extra I/O port functionality - Source: [OU_S0Zk9Qx0]
- Alternative: 6510 (C64 CPU) replacement requires kernel ROM modification - Source: [OU_S0Zk9Qx0]
- 6510 replacement has compatibility issues with advanced games using fast loaders - Source: [OU_S0Zk9Qx0]
- 6502-based replacement has better game compatibility than 6510 version - Source: [OU_S0Zk9Qx0]

#### 6529 Single Port Interface Replacement
- Daniel Manon replacement using 74-series logic chip - Source: [OU_S0Zk9Qx0]
- Original 6529 SPI chips becoming harder to find - Source: [OU_S0Zk9Qx0]
- Used for I/O ports in TED machines - Source: [OU_S0Zk9Qx0]

#### GAL-based PLA Replacement
- C16/116/Plus4 PLA replacement using GAL 16V8 chips - Source: [OU_S0Zk9Qx0]
- Same concept as C64 GAL PLA but uses 16V8 instead of 20V8 - Source: [OU_S0Zk9Qx0]
- Available from Daniel Manon: freepascal.org/~daniel/c16pla/ - Source: [OU_S0Zk9Qx0]

#### TED Chip Issues
- TED chip (graphics/sound) is the only irreplaceable custom chip - Source: [OU_S0Zk9Qx0]
- CPU, PLA, and SPI all now have replacement options - Source: [OU_S0Zk9Qx0]
- FPGA TED replacement in development would allow complete machine reconstruction - Source: [OU_S0Zk9Qx0]

#### PAL/NTSC Switching (Mod)
- Uses clock synthesizer to generate master clock - Source: [758KMi_EG1Y]
- Arduino powers synthesizer chip - Source: [758KMi_EG1Y]
- EPROM in ROM socket switches kernel between regions - Source: [758KMi_EG1Y]
- Hold reset: 1 blink = NTSC, 2 blinks = PAL - Source: [758KMi_EG1Y]

### Commodore 1551 Floppy Drive

#### Overview
- Floppy drive for C16/Plus4 264 series computers - Source: [758KMi_EG1Y]
- Uses parallel interface via cartridge port (TCBM protocol) - Source: [758KMi_EG1Y]
- Faster than 1541 serial IEC interface - Source: [758KMi_EG1Y]
- Requires external power (240V UK or 120V US versions) - Source: [758KMi_EG1Y]
- Uses Mitsumi mechanism (same as 1541) - Source: [758KMi_EG1Y]
- Single-sided drive, no track zero sensor - Source: [758KMi_EG1Y]

#### Internal Hardware
- 6510T CPU (2MHz version of C64 CPU) - Source: [758KMi_EG1Y]
- 6525 TPI (IO controller) - Source: [758KMi_EG1Y]
- 16KB RAM (vs 2KB in 1541) - Source: [758KMi_EG1Y]
- Single ROM chip in socket - Source: [758KMi_EG1Y]
- PLA chip (failure-prone like C64 PLA) - Source: [758KMi_EG1Y]
- Hitachi HD61215P chip - Source: [758KMi_EG1Y]

#### Cartridge Interface
- 6523T TPI (DIP-28 version of 6525) - Source: [758KMi_EG1Y]
- 251641-03 PLA chip (also failure-prone) - Source: [758KMi_EG1Y]
- PLA maps TPI to memory addresses in computer - Source: [758KMi_EG1Y]
- Replaceable with PLA Advanced or Super PLA v4 - Source: [758KMi_EG1Y]

#### Case Compatibility
- Mechanism and metal chassis same as 1541 - Source: [758KMi_EG1Y]
- Can swap into 1541 case (need to modify rear panel) - Source: [758KMi_EG1Y]
- 1541 case has IEC holes where 1551 has TCBM cable hole - Source: [758KMi_EG1Y]
- Dremel/nibble new hole for TCBM cable - Source: [758KMi_EG1Y]

#### Power Supply Conversion
- Linear regulators generate heat - Source: [758KMi_EG1Y]
- Can swap transformer from US 1541 for 120V operation - Source: [758KMi_EG1Y]
- Or: Remove linear regulators, add switching PSU modules - Source: [758KMi_EG1Y]
- Connect 5V and 12V directly to input side - Source: [758KMi_EG1Y]
- Results in much lighter, cooler drive - Source: [758KMi_EG1Y]

#### Troubleshooting
- Power LED should flash once on power-up after self-test - Source: [758KMi_EG1Y]
- Diagnostic may require computer to be connected and powered - Source: [758KMi_EG1Y]
- Without ROM: spindle runs indefinitely - Source: [758KMi_EG1Y]
- Check cartridge PLA chip select line (pin 18) for activity - Source: [758KMi_EG1Y]
- 1984-era PLAs notoriously unreliable - Source: [758KMi_EG1Y]

#### Resources
- Reverse-engineered schematics available - Source: [758KMi_EG1Y]
- 1541 to 1551 conversion possible with CPLD mod - Source: [758KMi_EG1Y]
- Blog: pagetable.com/?p=1331 - Source: [758KMi_EG1Y]
- Hungarian 1541 conversion: hup.hu/node/120659 - Source: [758KMi_EG1Y]

#### Gatoraid Chip Variants (HD61215P)
- 1551 uses Hitachi HD61J215P gate array chip - Source: [eFatlDatjZM]
- Hitachi HD61K variant exists but different package (high-density DIP) - Source: [eFatlDatjZM]
- J vs K variant: One letter difference, completely different pinout - Source: [eFatlDatjZM]
- HD61K chip NOT compatible without adapter - Source: [eFatlDatjZM]
- 1541 Gatoraid may work in 1551 (reports vary) but not vice versa - Source: [eFatlDatjZM]
- Faulty Gatoraid symptoms: Drive only outputs one pulse instead of two on certain signal - Source: [eFatlDatjZM]
- Mark from Retro Channel identified the specific signal issue - Source: [eFatlDatjZM]

### Commodore 64 "Breadbin" Reliability

#### PLA Chip Reliability
- Signetics 82S100: Ultra-reliable, runs hot but never fails - Source: [b-oHw0VBvU8]
- Philips PLS100: Same as 82S100, equally reliable - Source: [b-oHw0VBvU8]
- MOS/Commodore PLAs: Notoriously unreliable, frequent failures - Source: [b-oHw0VBvU8]
- Failed MOS PLA causes bus conflicts, black screens - Source: [b-oHw0VBvU8]
- Signetics-branded PLAs were programmed by Commodore on purchased chips - Source: [b-oHw0VBvU8]

#### PLA Marginal Failure Symptoms
- May pass basic boot test but fail with certain cartridges - Source: [icnPtyovOKU]
- EasyFlash cartridge won't work with marginal PLA - Source: [icnPtyovOKU]
- EasyFlash does "trickery" that requires fully working PLA - Source: [icnPtyovOKU]
- Can swap kernels in real time, needs good PLA - Source: [icnPtyovOKU]
- Mark marginal PLAs with "X" or "P" for partially dead - Source: [icnPtyovOKU]
- Soviet clone PLAs (82S100 compatible) available as replacement - Source: [icnPtyovOKU]
- Soviet PLAs programmable with Data IO 2900 or compatible programmer - Source: [icnPtyovOKU]

#### Fuse Blowing Troubleshooting

##### Overview
- C64 fuse is on the 9V AC input from power connector - Source: [icnPtyovOKU]
- 9V AC is bridge rectified to generate 5V and 12V rails - Source: [icnPtyovOKU]
- 12V rail powers SID and VIC-II chips - Source: [icnPtyovOKU]
- Standard fuse is 1.5 amp 250V - Source: [icnPtyovOKU]

##### Diagnostic Approach
1. Check bridge rectifier for shorts (diode check on multimeter) - Source: [icnPtyovOKU]
2. Check 5V and 12V regulators for shorts - Source: [icnPtyovOKU]
3. Remove SID and VIC-II chips, power up without them - Source: [icnPtyovOKU]
4. Measure current draw across fuse position with clip leads - Source: [icnPtyovOKU]
5. Compare to known-good machine (ZIF-64 or similar) - Source: [icnPtyovOKU]

##### Normal Current Draw
- Board without SID/VIC: ~250-340 mA (varies slightly) - Source: [icnPtyovOKU]
- Full board with SID/VIC: ~710-720 mA - Source: [icnPtyovOKU]
- 1.5A fuse provides headroom above normal operation - Source: [icnPtyovOKU]

##### Common Causes
- Undersized replacement fuse (wrong amperage) - Source: [icnPtyovOKU]
- Faulty power supply providing wrong voltage - Source: [icnPtyovOKU]
- Overvoltage from bad power brick (damages TTL logic) - Source: [icnPtyovOKU]
- 7-8V on 5V rail destroys chips - Source: [icnPtyovOKU]

##### Testing Without Blowing Fuses
- Can temporarily jumper fuse position with clip lead for testing - Source: [icnPtyovOKU]
- If component shorts, it will blow up (component sacrificed) - Source: [icnPtyovOKU]
- Not recommended for preserving equipment - Source: [icnPtyovOKU]
- Better to measure resistance/current before full power - Source: [icnPtyovOKU]

##### Cassette Port Power
- 9V DC (unregulated, after bridge rectifier) goes to cassette port - Source: [icnPtyovOKU]
- Powers the motor in Datasette tape drive - Source: [icnPtyovOKU]
- Zener-based supply provides ~6V for motor - Source: [icnPtyovOKU]

#### RAM Chip Reliability
- MOS branded RAM very unreliable - Source: [b-oHw0VBvU8]
- Okie/Toshiba/name-brand RAM more reliable - Source: [b-oHw0VBvU8]
- Single MOS RAM chip in otherwise name-brand array often fails first - Source: [b-oHw0VBvU8]

#### Diagnostic Testing
- VIC-20 diagnostic harness: github.com/svenpetersen1965/VIC-20_Diagnostics - Source: [b-oHw0VBvU8]
- C64 diagnostic harness: github.com/svenpetersen1965/C64-Diagnostic-Rev.-586220-Harness - Source: [b-oHw0VBvU8]
- ZIF-64 test board: All chips socketed for easy swap testing - Source: [b-oHw0VBvU8]

#### SID Chip Issues
- Can develop marginal issues that don't show on standard tests - Source: [b-oHw0VBvU8]
- May pass diagnostic tones but sound "weird" on complex music - Source: [b-oHw0VBvU8]
- Lost filters or channels cause subtle but noticeable differences - Source: [b-oHw0VBvU8]
- Mark marginal SIDs with "M" to indicate not fully reliable - Source: [b-oHw0VBvU8]

#### 6581 vs 8580 SID Differences
- 6581: Original SID, requires 12V supply - Source: [qk5mpvRM04Y]
- 8580: Later revision, runs on 9V (some variants 5V only) - Source: [qk5mpvRM04Y]
- Cannot swap 6581 into 8580 socket without voltage modification - Source: [qk5mpvRM04Y]
- 6581 in 8580 machine will be underpowered and sound wrong - Source: [qk5mpvRM04Y]
- 8580 in 6581 machine may be damaged by overvoltage - Source: [qk5mpvRM04Y]
- Check motherboard revision before swapping SID chips - Source: [qk5mpvRM04Y]
- C64C typically uses 8580, breadbin typically uses 6581 - Source: [qk5mpvRM04Y]

#### SID Replacement Options

##### SIDKick Pico
- Open-source SID replacement using Raspberry Pi Pico (RP2040) - Source: [cQGWcHCzZmU]
- GitHub: github.com/frntc/SIDKick-pico - Source: [cQGWcHCzZmU]
- Available in PWM and DAC versions - Source: [cQGWcHCzZmU]
- DAC version sounds substantially better than PWM version - Source: [cQGWcHCzZmU]
- Uses reSID emulation engine - Source: [cQGWcHCzZmU]
- Can emulate 6581 or 8580 - Source: [cQGWcHCzZmU]
- Supports dual SID (second SID address configurable) - Source: [cQGWcHCzZmU]
- FM OPL sound expander emulation built-in - Source: [cQGWcHCzZmU]
- Paddle and mouse support - Source: [cQGWcHCzZmU]
- Built-in configuration utility (CIS 54301) runs from SID socket - Source: [cQGWcHCzZmU]
- PRGs can be loaded directly from SID socket - Source: [cQGWcHCzZmU]
- Very inexpensive compared to other replacements (~$4 parts cost) - Source: [cQGWcHCzZmU]
- Available pre-assembled from American Retro Shop - Source: [cQGWcHCzZmU]
- Works in any C64 (long board or short board) - runs on 5V only - Source: [cQGWcHCzZmU]
- Use small pins to avoid damaging SID socket - Source: [cQGWcHCzZmU]

###### SIDKick Pico DAC Module
- Optional external DAC board for improved audio quality - Source: [Rgt9ZWYsMTE]
- 24-bit 96kHz audio output (far exceeds original SID specs) - Source: [Rgt9ZWYsMTE]
- Plugs into the SIDKick Pico main board via header - Source: [Rgt9ZWYsMTE]
- DAC module version sounds noticeably better than PWM-only version - Source: [Rgt9ZWYsMTE]
- Configuration utility works even with no real SID chip present - Source: [Rgt9ZWYsMTE]
- SIDKick can run standalone as the only "SID" in the system - Source: [Rgt9ZWYsMTE]

##### ArmSID
- ARM Cortex-based SID replacement - Source: [cQGWcHCzZmU]
- Not open source - Source: [cQGWcHCzZmU]
- In testing, sounded closest to original 6581 AR4 - Source: [cQGWcHCzZmU]

##### FPGASID
- FPGA-based SID replacement - Source: [cQGWcHCzZmU]
- More expensive than RP2040-based options - Source: [cQGWcHCzZmU]
- Has blue LED indicator - Source: [cQGWcHCzZmU]

##### SwinSID
- ATmega-based SID replacement - Source: [cQGWcHCzZmU]
- Not recommended - poor sound quality - Source: [cQGWcHCzZmU]
- Uses different approach that doesn't capture SID character well - Source: [cQGWcHCzZmU]

##### SID Comparison Notes
- "Ode to 64" SID tune good for testing filter differences between SIDs - Source: [cQGWcHCzZmU]
- csdb.dk has SID tunes for testing - Source: [cQGWcHCzZmU]
- Different 6581 chips sound noticeably different from each other - Source: [cQGWcHCzZmU]
- 6581 AR4 considered particularly good sounding - Source: [cQGWcHCzZmU]
- Real SIDs have variance; emulations can't match every original - Source: [cQGWcHCzZmU]
- Analog filters in original SID create "magic" that's hard to emulate - Source: [cQGWcHCzZmU]

#### VIC Chip Color Issues
- Early VIC chips (1981) may have washed-out colors - Source: [b-oHw0VBvU8]
- Later chips (1983+) produce correct vibrant colors - Source: [b-oHw0VBvU8]
- Doesn't affect functionality, just color accuracy - Source: [b-oHw0VBvU8]

### VIC-20 Cost-Reduced Board

#### Characteristics
- Same size as C64 short board - Source: [b-oHw0VBvU8]
- Uses C64-style power supply (DC input, no internal regulator) - Source: [b-oHw0VBvU8]
- Much cooler running than early VIC-20 boards - Source: [b-oHw0VBvU8]
- Fits in standard breadbin case with adapter bracket - Source: [b-oHw0VBvU8]
- Can also fit C64 short board in same bracket/case - Source: [b-oHw0VBvU8]
- Power LED holder often falls out (poor retention design) - Source: [b-oHw0VBvU8]

#### Reliability
- Very reliable machines when well-maintained - Source: [b-oHw0VBvU8]
- Generally work if not stored in damp/corroded conditions - Source: [b-oHw0VBvU8]

### Enhancer 2000 (1541 Clone)

#### Overview
- IEC-compatible disk drive clone by Comtel Group (Santa Ana, CA) - Source: [AT7oZ_xD2Go]
- Manufactured by Chinon (disk mechanism) - Source: [AT7oZ_xD2Go]
- Uses Chinon AF-051A mechanism - Source: [AT7oZ_xD2Go]
- Beltless direct drive construction - Source: [AT7oZ_xD2Go]
- Much cooler running than 1541 (external power supply) - Source: [AT7oZ_xD2Go]
- External 5V/12V DC power supply with DIN connector - Source: [AT7oZ_xD2Go]

#### Hardware
- Two 6522 VIA chips (Rockwell, 1984) - Source: [AT7oZ_xD2Go]
- Ricoh 65C02 processor (stock configuration) - Source: [AT7oZ_xD2Go]
- 16KB ROM (27128 EPROM) - Source: [AT7oZ_xD2Go]
- Static RAM - Source: [AT7oZ_xD2Go]
- Brass screw inserts (better construction than plastic threads) - Source: [AT7oZ_xD2Go]
- All-metal latching mechanism - Source: [AT7oZ_xD2Go]

#### Compatibility
- Works with standard 1541 ROM (full compatibility) - Source: [AT7oZ_xD2Go]
- Works with Action Replay fast loader - Source: [AT7oZ_xD2Go]
- Works with Epyx Fast Load cartridge - Source: [AT7oZ_xD2Go]
- Ultima 6, Life Force, Portal all loaded successfully - Source: [AT7oZ_xD2Go]
- Some software fast loaders work fine - Source: [AT7oZ_xD2Go]

#### Incompatibility Issues
- 65C02 lacks undocumented 6502 instructions used by some fast loaders - Source: [AT7oZ_xD2Go]
- Replace Ricoh 65C02 with MOS 6502 for full compatibility - Source: [AT7oZ_xD2Go]
- JiffyDOS doesn't work properly (step rate too fast for mechanism) - Source: [AT7oZ_xD2Go]
- Custom JiffyDOS version existed but appears lost - Source: [AT7oZ_xD2Go]

#### ROM Information
- Stock ROM version 2.0 - Source: [AT7oZ_xD2Go]
- Hidden copyright text in ROM: "all portions of this rom are copyrighted fish are frogs space for rent cheap beware the hidden copyright notice" - Source: [AT7oZ_xD2Go]
- Original v1 ROM was too similar to Commodore ROM (legal trouble) - Source: [AT7oZ_xD2Go]
- v2 ROM modified to avoid copyright issues - Source: [AT7oZ_xD2Go]
- Zimmers.net has Enhancer 2000 ROMs archived - Source: [AT7oZ_xD2Go]

#### LED Indicators
- Green power LED - Source: [AT7oZ_xD2Go]
- Activity LED (solid when motor spinning) - Source: [AT7oZ_xD2Go]
- Error LED (blinks during disk access like 1541 activity light) - Source: [AT7oZ_xD2Go]

### VIC-20

#### Diagnostic Harness (Test Cartridge System)
- VIC-20 diagnostic cartridge by Sven Petersen - Source: [GUvasXbxUPg]
- GitHub: github.com/svenpetersen1965/VIC-20_Diagnostics - Source: [GUvasXbxUPg]
- Complete test harness for VIC-20 systems - Source: [GUvasXbxUPg]
- Tests RAM, keyboard, joystick ports, user port - Source: [GUvasXbxUPg]
- Cartridge contains diagnostic ROM and test routines - Source: [GUvasXbxUPg]
- Loopback plugs required for port testing - Source: [GUvasXbxUPg]
- User port loopback tests parallel port functionality - Source: [GUvasXbxUPg]
- Joystick loopback tests all port lines - Source: [GUvasXbxUPg]
- Can identify specific bad RAM chips by address - Source: [GUvasXbxUPg]
- Essential tool for VIC-20 repair and verification - Source: [GUvasXbxUPg]

#### ROM Chip Testing with Retro Chip Tester Pro
- VIC-20 ROMs are 2364 type (same as C64) - Source: [NYybIWL2o0o]
- Part numbers: 901486-01 (Basic ROM), 901486-06 (NTSC Kernel ROM), 901460-03 - Source: [NYybIWL2o0o]
- 901486-01 also used in VIC-1001 (Japanese model) - Source: [NYybIWL2o0o]
- Retro Chip Tester Pro verifies ROM checksums against known-good values - Source: [NYybIWL2o0o]
- Pass on tester doesn't guarantee chip works in real machine - Source: [NYybIWL2o0o]
- Mark tested chips with tick mark for verification - Source: [NYybIWL2o0o]

#### Board Versions

##### Early VIC-20 Board
- Large motherboard with internal linear regulator - Source: [NYybIWL2o0o]
- Gets very hot during operation - Source: [NYybIWL2o0o]
- Two-pin AC power supply connector - Source: [NYybIWL2o0o]
- Different form factor from cost-reduced version - Source: [NYybIWL2o0o]

##### Cost-Reduced Board (CR/Rev D)
- Same physical size as C64 short board - Source: [NYybIWL2o0o]
- Uses C64-style power supply (5V DC input) - Source: [NYybIWL2o0o]
- No internal regulator/heat sink - runs much cooler - Source: [NYybIWL2o0o]
- RF shield adapter bracket required for US breadbin case - Source: [NYybIWL2o0o]
- Soldered tabs on bracket need desoldering to remove board - Source: [NYybIWL2o0o]
- European case bottoms have extra standoffs for short boards - Source: [NYybIWL2o0o]
- US case bottoms only have original standoff positions - Source: [NYybIWL2o0o]
- Inductor scratches on top indicate board was stacked with others - Source: [NYybIWL2o0o]

##### ROM Socket Positions (Cost-Reduced Board)
- UE11 and UE12 are the two ROM sockets - Source: [NYybIWL2o0o]
- Basic ROM (901486-01) goes in lower socket - Source: [NYybIWL2o0o]
- Kernel ROM (901486-06) goes in upper socket - Source: [NYybIWL2o0o]
- All chips insert with notch facing up - Source: [NYybIWL2o0o]
- Schematics unhelpful - just list "2364" without ROM function - Source: [NYybIWL2o0o]
- Zimmers.net has VIC-20CR schematics - Source: [NYybIWL2o0o]

#### Early "PET-Style" Keyboard
- Very early VIC-20s had PET-style keyboard - Source: [NYybIWL2o0o]
- Same font/legends as PET computers - Source: [NYybIWL2o0o]
- CLEAR/HOME key has PET styling - Source: [NYybIWL2o0o]
- Bracket holds wire differently than later keyboards - Source: [NYybIWL2o0o]
- Uses spring mechanism under keys - Source: [NYybIWL2o0o]
- Keys are VERY difficult to remove (strongly attached) - Source: [NYybIWL2o0o]
- Can be used in C64 for unique look (different font appearance) - Source: [NYybIWL2o0o]
- Restore with 303 protectant for shiny appearance - Source: [NYybIWL2o0o]

#### Common Symptoms

##### Black Screen with No Video
- Black screen but video sync present indicates machine attempting to run - Source: [NYybIWL2o0o]
- Color bars appear on RetroTINK when machine powered off - Source: [NYybIWL2o0o]
- Powering on produces blank output (not complete absence of signal) - Source: [NYybIWL2o0o]
- Suggests CPU running but no display output - Source: [NYybIWL2o0o]
- Check 6560 video chip and ROMs first - Source: [NYybIWL2o0o]

#### Power Verification
- Always check for 5V on power rails first - Source: [NYybIWL2o0o]
- 4.8-5.0V is normal operating range - Source: [NYybIWL2o0o]
- Dead machine with good power = logic/chip failure - Source: [NYybIWL2o0o]

#### Pin Straightening Tool
- Flat-nose needle-nose pliers ideal for IC pin straightening - Source: [NYybIWL2o0o]
- Bent angle makes reaching pins easier - Source: [NYybIWL2o0o]
- Non-textured jaws won't chew up IC pins - Source: [NYybIWL2o0o]
- Knurled/textured pliers damage pin finish - Source: [NYybIWL2o0o]

#### Keyboard Variations
- Later VIC-20s have thinner font keycaps ("Euro keys") - Source: [AT7oZ_xD2Go]
- Keyboard feels more solid than late C64 keyboards - Source: [AT7oZ_xD2Go]
- Different key plunger design than C64 (incompatible replacements) - Source: [AT7oZ_xD2Go]
- Keyboard construction has thicker structure around perimeter - Source: [AT7oZ_xD2Go]
- No ferrite ring on keyboard cable (unusual for North America) - Source: [AT7oZ_xD2Go]

#### Cost-Reduced VIC-20
- Smaller motherboard (same size as C64 short board) - Source: [AT7oZ_xD2Go]
- Plastic badge (later C64s had metal badges) - Source: [AT7oZ_xD2Go]
- Power LED can fall inside case (poor retention design) - Source: [AT7oZ_xD2Go]
- Uses C64-style power supply connector - Source: [AT7oZ_xD2Go]

#### Reliability
- More reliable than C64 due to fewer custom chips - Source: [AT7oZ_xD2Go]
- Only custom chip is VIC video chip - Source: [AT7oZ_xD2Go]
- No PLA, no SID, no other failure-prone custom ICs - Source: [AT7oZ_xD2Go]

#### Lumacode Video Mod (c0pperdragon)
- Lumacode board available for VIC-20 video chip - Source: [Ga8mk2ErS7w]
- Encodes pixel data digitally instead of analog conversion - Source: [Ga8mk2ErS7w]
- Provides perfect pixel-accurate video capture - Source: [Ga8mk2ErS7w]
- Requires RGB2HDMI with Lumacode firmware profile - Source: [Ga8mk2ErS7w]
- Must wire to BOTH pin 2 AND pin 4 on analog comparator board - Source: [Ga8mk2ErS7w]
- Using only one pin causes incomplete color data - Source: [Ga8mk2ErS7w]

### C64 Accelerators

#### Turbo Chameleon 64

##### Overview
- FPGA-based cartridge accelerator for C64 - Source: [vBTDMKBYTpo]
- Contains complete C64 core in FPGA - Source: [vBTDMKBYTpo]
- Uses actual C64 for I/O (video, sound, joysticks) - Source: [vBTDMKBYTpo]
- All RAM in cartridge, mirrored to host C64's VIC chip - Source: [vBTDMKBYTpo]

##### Features
- VGA output - Source: [vBTDMKBYTpo]
- PS/2 keyboard ports - Source: [vBTDMKBYTpo]
- SD card slot (emulates disk drive) - Source: [vBTDMKBYTpo]
- IR port for wireless gamepad - Source: [vBTDMKBYTpo]
- Ethernet port (optional card) - Source: [vBTDMKBYTpo]

##### Turbo Modes
- 2MHz mode: Slight speedup, good for PAL game compatibility on NTSC - Source: [vBTDMKBYTpo]
- 3MHz, 4MHz, 5MHz, 6MHz options available - Source: [vBTDMKBYTpo]
- "No limit" mode: Maximum FPGA speed - Source: [vBTDMKBYTpo]
- Can also slow down to 75%, 50%, 25% for debugging - Source: [vBTDMKBYTpo]
- Button on cartridge toggles turbo on/off - Source: [vBTDMKBYTpo]
- DO30 bit option: Honors C128-style fast mode requests - Source: [vBTDMKBYTpo]

##### Performance vs SuperCPU
- At "no limit": ~0.1-0.2 seconds per hash (Bitcoin mining test) - Source: [vBTDMKBYTpo]
- Slightly slower than fully optimized SuperCPU - Source: [vBTDMKBYTpo]
- Advantage: Works in graphics mode without slowdown - Source: [vBTDMKBYTpo]
- SuperCPU needs text-only mode for maximum speed - Source: [vBTDMKBYTpo]
- Much more readily available than SuperCPU - Source: [vBTDMKBYTpo]

#### SuperCPU

##### Overview
- 65816 CPU accelerator running at 20MHz - Source: [vBTDMKBYTpo]
- Made by CMD (Creative Micro Designs) - Source: [vBTDMKBYTpo]
- Extremely rare and expensive today - Source: [vBTDMKBYTpo]
- Has onboard cache memory - Source: [vBTDMKBYTpo]

##### Performance
- With optimizations (text mode only): ~0.1 seconds per hash - Source: [vBTDMKBYTpo]
- Stock configuration: ~0.3 seconds per hash - Source: [vBTDMKBYTpo]
- Slightly faster than Turbo Chameleon in optimized mode - Source: [vBTDMKBYTpo]
- Must minimize memory mirroring to C64 for maximum speed - Source: [vBTDMKBYTpo]

### C64 Lumacode Video Mod (c0pperdragon)
- Lumacode board available for C64 VIC-II chip - Source: [Ga8mk2ErS7w]
- Digital encoding eliminates analog noise and jailbars - Source: [Ga8mk2ErS7w]
- Requires RGB2HDMI with Lumacode firmware profile - Source: [Ga8mk2ErS7w]
- Critical wiring: Connect Lumacode signal to BOTH pin 2 AND pin 4 - Source: [Ga8mk2ErS7w]
- Using only one pin results in missing color information - Source: [Ga8mk2ErS7w]
- c0pperdragon documentation has exact wiring details - Source: [Ga8mk2ErS7w]

### C64 Corrosion Survival (Field-Found Machines)

#### Outdoor Storage Survival
- C64s can survive years of outdoor storage with surprising results - Source: [cuBAq110pr8]
- Machines found in barns, sheds, even fields may still work - Source: [cuBAq110pr8]
- Key factor: Was machine stored with case closed? - Source: [cuBAq110pr8]
- Dirt/debris on exterior doesn't mean interior damage - Source: [cuBAq110pr8]

#### Evapo-Rust Treatment for Corrosion
- Evapo-Rust (non-toxic rust remover) works on PCB corrosion - Source: [cuBAq110pr8]
- Submerge entire motherboard in Evapo-Rust solution - Source: [cuBAq110pr8]
- Removes rust from RF shields, chassis, exposed metal - Source: [cuBAq110pr8]
- Does not damage ICs, capacitors, or PCB substrate - Source: [cuBAq110pr8]
- Rinse thoroughly with water after treatment - Source: [cuBAq110pr8]
- Allow complete drying before powering on (days, not hours) - Source: [cuBAq110pr8]

#### Nail Polish Corrosion Protection
- Clear nail polish protects corroded but functional traces - Source: [cuBAq110pr8]
- Apply over cleaned corrosion areas after confirming functionality - Source: [cuBAq110pr8]
- Prevents further oxidation of exposed copper - Source: [cuBAq110pr8]
- Do NOT apply to edge connectors or points requiring contact - Source: [cuBAq110pr8]
- Cheap insurance against progressive trace damage - Source: [cuBAq110pr8]

#### PCB Trace Monitoring
- Take photos of corroded areas for future comparison - Source: [cuBAq110pr8]
- Traces can continue corroding under solder mask - Source: [cuBAq110pr8]
- Check suspect areas periodically with continuity tester - Source: [cuBAq110pr8]
- Green discoloration spreading = active corrosion - Source: [cuBAq110pr8]
- Early intervention prevents total trace failure - Source: [cuBAq110pr8]

#### Case Cleaning
- Pressure washer effective for heavily soiled cases - Source: [cuBAq110pr8]
- Dish soap and water for interior cleaning - Source: [cuBAq110pr8]
- Allow complete drying before reassembly - Source: [cuBAq110pr8]
- Keyboard membranes may not survive soaking (test separately) - Source: [cuBAq110pr8]

#### Keyboard Recovery
- C64 keyboards are surprisingly resilient - Source: [cuBAq110pr8]
- Clean membrane contacts with IPA if intermittent - Source: [cuBAq110pr8]
- Key plungers can be removed and cleaned individually - Source: [cuBAq110pr8]
- Replacement membranes available if original fails - Source: [cuBAq110pr8]

### Amiga 500

#### Green Screen Flash (RAM Diagnostic)
- Green flash on boot = RAM problem - Source: [iHR4YDJTPrA]
- Amiga 500 performs memory test at power-on - Source: [iHR4YDJTPrA]
- Flash color indicates memory type failing - Source: [iHR4YDJTPrA]
- Green = chip RAM (slow RAM in lower addresses) - Source: [iHR4YDJTPrA]
- Other colors indicate fast RAM or trapdoor expansion issues - Source: [iHR4YDJTPrA]

#### Memory Architecture
- Chip RAM: Lower memory, accessible by both CPU and custom chips (Agnus/Agnes) - Source: [iHR4YDJTPrA]
- Fast RAM: Upper memory, CPU-only access, faster for software - Source: [iHR4YDJTPrA]
- Slow RAM (trapdoor): 512K expansion, same speed as chip RAM - Source: [iHR4YDJTPrA]
- Agnus chip controls memory access, DMA for graphics/sound - Source: [iHR4YDJTPrA]

#### A501 512K RAM Expansion (Trapdoor)
- Common failure: NiCad battery on clock chip leaks - Source: [iHR4YDJTPrA]
- Battery leakage corrodes PCB traces and components - Source: [iHR4YDJTPrA]
- Recommended: Remove NiCad and replace with CR2032 holder - Source: [iHR4YDJTPrA]
- Adding diode prevents charging non-rechargeable battery - Source: [iHR4YDJTPrA]
- Clean corrosion thoroughly before installing new battery - Source: [iHR4YDJTPrA]

#### CPU Socket Issues
- 68000 CPU in DIP-64 socket can work loose over time - Source: [iHR4YDJTPrA]
- Symptoms: Random crashes, failure to boot - Source: [iHR4YDJTPrA]
- Fix: Reseat CPU firmly in socket - Source: [iHR4YDJTPrA]
- May need to replace socket if pins are corroded or loose - Source: [iHR4YDJTPrA]

#### Terrible Fire TF536 Accelerator

##### Overview
- 68030 accelerator for Amiga 500/500+ - Source: [iHR4YDJTPrA]
- Runs at 40MHz (vs original 7MHz 68000) - Source: [iHR4YDJTPrA]
- Uses SDRAM for fast memory - Source: [iHR4YDJTPrA]
- Open source hardware design - Source: [iHR4YDJTPrA]

##### Installation
- Plugs into 68000 CPU socket - Source: [iHR4YDJTPrA]
- CPU relocator may be needed for clearance in case - Source: [iHR4YDJTPrA]
- Relocator extends CPU socket upward and adds horizontal offset - Source: [iHR4YDJTPrA]
- Check case clearance before installing - Source: [iHR4YDJTPrA]

##### Features
- 68881/68882 FPU socket for math coprocessor - Source: [iHR4YDJTPrA]
- 128MB fast RAM option - Source: [iHR4YDJTPrA]
- IDE header for internal hard drive - Source: [iHR4YDJTPrA]
- Compatible with Kickstart 1.3 and later - Source: [iHR4YDJTPrA]

##### Performance
- Massive speedup for Workbench and applications - Source: [iHR4YDJTPrA]
- Games may run too fast (need degrader) - Source: [iHR4YDJTPrA]
- CPU-intensive demos show dramatic improvement - Source: [iHR4YDJTPrA]

#### Power PC Board (KF Computer Systems)

##### Overview
- PC emulator card for Amiga 500 trapdoor expansion - Source: [eFatlDatjZM]
- Made by KF Computer Systems, Netherlands - Source: [eFatlDatjZM]
- Adds PC XT emulation to Amiga 500 - Source: [eFatlDatjZM]
- Part number P25-42 (version 2) - Source: [eFatlDatjZM]
- amiga.resource.cx/exp/powerpc - Source: [eFatlDatjZM]

##### Hardware
- NEC V30 processor (Intel 8088 compatible) - Source: [eFatlDatjZM]
- Made in Ireland - Source: [eFatlDatjZM]
- Version 1: V30 at 8MHz, no hard drive support - Source: [eFatlDatjZM]
- Version 2 (P25-42): 10MHz, hard drive controller support - Source: [eFatlDatjZM]
- Supported controllers: A590, ALF, GVP, others - Source: [eFatlDatjZM]

##### Memory
- 1MB RAM onboard (512K for Amiga fast RAM + 512K for PC) - Source: [eFatlDatjZM]
- PC emulation gets 640K + extra in EGA/VGA mode - Source: [eFatlDatjZM]
- 200K extra RAM available for reset-proof MS-DOS RAM disc - Source: [eFatlDatjZM]
- Uses 256Kx4 DRAM chips (4 chips = 512K per function) - Source: [eFatlDatjZM]
- Additional single 1-bit wide RAM chip (possibly for parity) - Source: [eFatlDatjZM]

##### Video Emulation
- CGA, MDA, EGA, and VGA video modes - Source: [eFatlDatjZM]
- 640x400 resolution, 16 colors in enhanced modes - Source: [eFatlDatjZM]
- Uses Amiga display hardware for output - Source: [eFatlDatjZM]

##### Features
- Uses Amiga serial port (up to 19.2kbps) - Source: [eFatlDatjZM]
- Uses Amiga floppy controller - Source: [eFatlDatjZM]
- Uses Amiga parallel port - Source: [eFatlDatjZM]
- Battery-backed clock - Source: [eFatlDatjZM]
- Emulates PC speaker (beeps) - Source: [eFatlDatjZM]
- NOT compatible with NTSC Amigas (PAL only) - Source: [eFatlDatjZM]
- Does NOT multitask with AmigaOS - exclusive PC mode - Source: [eFatlDatjZM]

##### Battery Maintenance
- Uses coin cell battery (may bulge over time) - Source: [eFatlDatjZM]
- Remove and replace with battery holder - Source: [eFatlDatjZM]
- Clean any corrosion before installing new battery - Source: [eFatlDatjZM]
- Apply nail polish to exposed copper after cleaning - Source: [eFatlDatjZM]

##### Compatibility Notes
- Some cards were side-car expansion for A500 (not trapdoor) - Source: [eFatlDatjZM]
- Zorro2 adapter version also exists - Source: [eFatlDatjZM]
- Trapdoor version retains use of side expansion port - Source: [eFatlDatjZM]
- Price was £324 including VAT in 1990 (expensive) - Source: [eFatlDatjZM]

##### NTSC Conversion Notes
- Converting A500 to PAL may require new crystal and jumpers - Source: [eFatlDatjZM]
- Agnus/Denise chip swaps may be needed - Source: [eFatlDatjZM]
- Details unknown - need research for specific mod procedure - Source: [eFatlDatjZM]

#### RAM Chip Failures (Oki RAM)

##### Overview
- Oki RAM chips have high failure rate in Amiga 500 - Source: [ksimpQeU3QA]
- Commonly fail with addressing errors rather than data errors - Source: [ksimpQeU3QA]
- A8 address line failures are particularly common - Source: [ksimpQeU3QA]

##### Symptoms
- Yellow screen (CPU crash not handled by guru meditation) - Source: [ksimpQeU3QA]
- Green flash at boot (chip RAM failure detected) - Source: [ksimpQeU3QA]
- Machine works initially then fails after warmup - Source: [ksimpQeU3QA]
- Intermittent failures that come and go - Source: [ksimpQeU3QA]

##### Why Piggyback Method Doesn't Work for Address Errors
- Piggyback method only works for data line (output) failures - Source: [ksimpQeU3QA]
- Address pins are inputs - can't override with another chip - Source: [ksimpQeU3QA]
- If chip has internal address decode failure, external signals can't fix it - Source: [ksimpQeU3QA]
- Must replace chip entirely for addressing errors - Source: [ksimpQeU3QA]

##### Diagnostic Approach with Logica ROM
- Logica diagnostic ROM has "user memory" mode - Source: [ksimpQeU3QA]
- Tests each of the 16 chip RAM chips individually - Source: [ksimpQeU3QA]
- Shows which specific chip(s) are failing - Source: [ksimpQeU3QA]
- More precise than standard DiagROM which tests memory as a whole - Source: [ksimpQeU3QA]

##### March Test Algorithm
- Superior RAM test algorithm compared to basic pattern tests - Source: [ksimpQeU3QA]
- Detects address line failures that simpler tests miss - Source: [ksimpQeU3QA]
- Writes and reads in specific march pattern to catch aliasing - Source: [ksimpQeU3QA]
- Same algorithm used in TRS-80 diagnostic ROM - Source: [ksimpQeU3QA]
- Takes longer but catches more failures - Source: [ksimpQeU3QA]

##### 4164 vs 41256 Compatibility
- Some A500 boards use 41256 (256K) chips with only 64K used - Source: [ksimpQeU3QA]
- Can substitute 4164 for 41256 in emergency - Source: [ksimpQeU3QA]
- Original Amiga 500 uses sixteen 4164 chips for 512K chip RAM - Source: [ksimpQeU3QA]

### Amiga 500 Rev 5 Board

#### Overview
- Rev 5 is an older motherboard revision - Source: [r8wuX5SwCOM]
- Uses 1-bit RAM chips (not 4-bit like later boards) - Source: [r8wuX5SwCOM]
- Does not have onboard 1MB RAM option - Source: [r8wuX5SwCOM]
- Kickstart 1.2 was common on these boards - Source: [r8wuX5SwCOM]

#### 512K ROM Upgrade Modification
- Rev 5 boards cannot use 512K ROMs (Kickstart 2.0+) without modification - Source: [r8wuX5SwCOM]
- Original board only wired for 256K ROM - Source: [r8wuX5SwCOM]
- Requires three changes to the ROM socket - Source: [r8wuX5SwCOM]

##### Pin 31 Modification
- Lift pin 31 on the ROM chip out of the socket - Source: [r8wuX5SwCOM]
- Connect lifted pin 31 to pin 21 on the ROM (VCC/5V) - Source: [r8wuX5SwCOM]
- This puts the ROM in 16-bit mode - Source: [r8wuX5SwCOM]
- Pin 31 on socket was originally connected to wrong signal - Source: [r8wuX5SwCOM]

##### Address Line 17 (A17) Addition
- Pin 1 on 512K ROM is Address Line 17 (A17) - Source: [r8wuX5SwCOM]
- Original socket pin 1 is not connected - Source: [r8wuX5SwCOM]
- Must connect ROM pin 1 to A17 signal from CPU - Source: [r8wuX5SwCOM]
- CPU pin 45 is A17 on the 68000 - Source: [r8wuX5SwCOM]
- Note: 68000 is installed with notch DOWN, ROM has notch UP - Source: [r8wuX5SwCOM]

##### Permanent Motherboard Modification
- Cut trace going to socket pin 31 on both sides - Source: [r8wuX5SwCOM]
- Bodge wire from socket pin 31 to VCC - Source: [r8wuX5SwCOM]
- Bodge wire from socket pin 1 (normally unconnected) to CPU A17 - Source: [r8wuX5SwCOM]
- Also connect A17 to Agnus chip if trace ran there - Source: [r8wuX5SwCOM]
- Hot glue to secure bodge wires - Source: [r8wuX5SwCOM]
- After mod, socket accepts 512K ROMs directly - Source: [r8wuX5SwCOM]

##### Commodore's Solution
- Commodore shipped 2.04 mask ROMs with jumper wire from pin 1 to pin 31 - Source: [r8wuX5SwCOM]
- This bodge on the chip allowed it to work in older boards - Source: [r8wuX5SwCOM]
- Mask ROM didn't need pin 31 function so jumper was safe - Source: [r8wuX5SwCOM]

#### Diagnostic ROM Issues on Rev 5
- Logica diagnostic ROM may show black screen without mod - Source: [r8wuX5SwCOM]
- DiagROM may show errors or color flashes - Source: [r8wuX5SwCOM]
- Wrong ROM checksum = probably need address line mod - Source: [r8wuX5SwCOM]
- Original 1.2/1.3 ROMs work fine without mod (256K) - Source: [r8wuX5SwCOM]

#### DigiFeX VIP S-Video Adapter

##### Overview
- External video adapter for Amiga 500/2000 - Source: [r8wuX5SwCOM]
- Plugs into video port on back of Amiga - Source: [r8wuX5SwCOM]
- Provides color composite and S-Video output - Source: [r8wuX5SwCOM]
- RGB pass-through connector - Source: [r8wuX5SwCOM]
- Necessary because A500/A2000 only have mono composite built-in - Source: [r8wuX5SwCOM]

##### Video Output Quality
- S-Video output looks surprisingly good on 1702 monitor - Source: [r8wuX5SwCOM]
- 80-column text fully readable over S-Video - Source: [r8wuX5SwCOM]
- Color quality is vibrant - Source: [r8wuX5SwCOM]
- If Commodore had built S-Video in, 1702 would have been viable A500 monitor - Source: [r8wuX5SwCOM]

##### Power Fluctuation Issue
- Image intensity may fluctuate when floppy drive accesses - Source: [r8wuX5SwCOM]
- Likely caused by 12V rail variation under load - Source: [r8wuX5SwCOM]
- May indicate capacitors in VIP box need replacement - Source: [r8wuX5SwCOM]
- RGB output from motherboard doesn't have this problem - Source: [r8wuX5SwCOM]

#### Membrane Keyboard Issues
- Amiga 500 uses membrane keyboard (Mitsumi type) - Source: [r8wuX5SwCOM]
- No replacement membranes readily available for A500 - Source: [r8wuX5SwCOM]
- Membrane can fail from moisture exposure - Source: [r8wuX5SwCOM]
- Individual keys stop working (Escape, F1 common failures) - Source: [r8wuX5SwCOM]
- Pressing keys while twisting keyboard doesn't help if membrane bad - Source: [r8wuX5SwCOM]
- A600/A1200 replacement membranes exist but not A500 - Source: [r8wuX5SwCOM]

#### Edge Connector Corrosion

##### Cleaning Procedure
- Naval jelly (phosphoric acid gel) effective for connector corrosion - Source: [r8wuX5SwCOM]
- Paint on with brush, leave 5 minutes - Source: [r8wuX5SwCOM]
- Rinse thoroughly under faucet with soap and brush - Source: [r8wuX5SwCOM]
- Critical: Remove ALL naval jelly residue - Source: [r8wuX5SwCOM]
- Use Magic Eraser to polish gold contacts - Source: [r8wuX5SwCOM]

##### Protection After Cleaning
- Apply clear nail polish over exposed copper after cleaning - Source: [r8wuX5SwCOM]
- Multiple coats for good coverage - Source: [r8wuX5SwCOM]
- Prevents further corrosion of cleaned areas - Source: [r8wuX5SwCOM]
- Do NOT apply to gold contact surfaces - Source: [r8wuX5SwCOM]

##### Trace Verification
- Use multimeter to verify all edge connector traces intact - Source: [r8wuX5SwCOM]
- Check vias going to finger contacts - Source: [r8wuX5SwCOM]
- Corrosion can break traces under solder mask - Source: [r8wuX5SwCOM]
- Bodge wires may be needed if traces broken - Source: [r8wuX5SwCOM]

#### Dremel Corrosion Removal
- Soft rubber tip on Dremel effective for removing corrosion - Source: [r8wuX5SwCOM]
- Exposes bare copper but doesn't damage PCB - Source: [r8wuX5SwCOM]
- Follow up with nail polish to protect exposed copper - Source: [r8wuX5SwCOM]

#### A501 RAM Expansion Compatibility
- Cleaned edge connector works with A501/Commodore 501 - Source: [r8wuX5SwCOM]
- Test by checking memory reported by Workbench - Source: [r8wuX5SwCOM]
- Full 1MB should be available with A501 installed - Source: [r8wuX5SwCOM]

### MOS 6582 SID Chip

#### Overview
- Sound Interface Device variant - Source: [EhDOV2oMAQM]
- Different from standard 6581 SID - Source: [EhDOV2oMAQM]
- Datasheet available at: archive.6502.org/datasheets/mos_6582_sid.pdf - Source: [EhDOV2oMAQM]

#### Voltage Differences
- 6582: VDD (pin 28) is 9V DC - Source: [EhDOV2oMAQM]
- 6581: VDD is 12V - Source: [EhDOV2oMAQM]
- May be drop-in compatible with 8580 (shortboard C64s) - Source: [EhDOV2oMAQM]
- Do NOT use in machines expecting 12V on VDD - Source: [EhDOV2oMAQM]

#### Sound Characteristics
- Internal sound circuitry similar to original 6581 - Source: [EhDOV2oMAQM]
- 8580/8500 series have different filters, sound different - Source: [EhDOV2oMAQM]
- Some software designed specifically for 6581 or 8580 - Source: [EhDOV2oMAQM]
- Filters sound most different between chip variants - Source: [EhDOV2oMAQM]

#### Compatibility
- May allow 6581-targeted software on shortboard machines - Source: [EhDOV2oMAQM]
- Further testing needed to confirm compatibility - Source: [EhDOV2oMAQM]
- Date code 1992 on example chip (Philippines manufacture) - Source: [EhDOV2oMAQM]

### VIC-20 40-Column Display

#### Homebrew RAM/ROM Expansion Cart
- User-made expansion cart with 32K RAM + 8K ROM - Source: [EhDOV2oMAQM]
- Files available at: defiancestudios.com/2022/04/17/vic-20-memory-expansion/ - Source: [EhDOV2oMAQM]
- Uses 27C2001 EPROM for multiple ROM images - Source: [EhDOV2oMAQM]
- Uses static RAM chip for memory expansion - Source: [EhDOV2oMAQM]
- Simple design: one 74LS21, EEPROM, SRAM, DIP switches - Source: [EhDOV2oMAQM]
- Reset switch included - Source: [EhDOV2oMAQM]
- DIP switches configure RAM blocks and ROM selection - Source: [EhDOV2oMAQM]

#### VIC-40 Mode
- 40-column display mode from Ahoy! magazine October 1984 - Source: [EhDOV2oMAQM]
- Uses high-resolution bitmap graphics for 40x25 display - Source: [EhDOV2oMAQM]
- Resolution: 160x160 dots - Source: [EhDOV2oMAQM]
- Not true 40-column mode - uses bitmap to simulate text - Source: [EhDOV2oMAQM]
- Scrolling noticeably slower than normal mode - Source: [EhDOV2oMAQM]
- Can display both character sets simultaneously - Source: [EhDOV2oMAQM]
- 128 characters stored (reverse field generated on-the-fly) - Source: [EhDOV2oMAQM]
- Color limited to blocks (like ZX Spectrum color clash) - Source: [EhDOV2oMAQM]
- 220 color blocks available on screen - Source: [EhDOV2oMAQM]
- Ctrl+number changes color, Shift restarts if paused - Source: [EhDOV2oMAQM]
- Uses about 8K more RAM than normal mode - Source: [EhDOV2oMAQM]
- Compatible with PET BASIC poke locations - Source: [EhDOV2oMAQM]

#### VIC-20 Memory Map
- Block 5 (cartridge space) at $8000 - Source: [EhDOV2oMAQM]
- Internal RAM normally at $1000 - Source: [EhDOV2oMAQM]
- Adding RAM can move graphics space - Source: [EhDOV2oMAQM]
- Memory map changes based on expansion configuration - Source: [EhDOV2oMAQM]
- BASIC requires continuous memory for maximum bytes free - Source: [EhDOV2oMAQM]

#### BASIC Version Differences
- VIC-20 and C64 use BASIC 2.0 - Source: [EhDOV2oMAQM]
- Later PETs (4016, 4032) use BASIC 4.0 - Source: [EhDOV2oMAQM]
- BASIC 4.0 adds disk commands like DIRECTORY, DSAVE - Source: [EhDOV2oMAQM]
- BASIC 4.0 can break compatibility with some software - Source: [EhDOV2oMAQM]
- C128 uses BASIC 7.0 with many new features - Source: [EhDOV2oMAQM]

### C64 Breadbin Rubber Dome Keyboard (TKR J075AQ)

#### Overview
- Rare alternative keyboard type for C64 breadbin - Source: [EwplTQDS_3I]
- Uses rubber domes instead of springs - Source: [EwplTQDS_3I]
- PCB marked: TKR J075AQ R320101 - Source: [EwplTQDS_3I]
- Listed as "Type 2" in retroleum.co.uk keyboard documentation - Source: [EwplTQDS_3I]

#### Physical Differences
- No springs under keys - rubber domes provide return force - Source: [EwplTQDS_3I]
- Different key mount height than standard C64 keys - Source: [EwplTQDS_3I]
- Keys incompatible with standard C64 keyboards - Source: [EwplTQDS_3I]
- Cross mount on keys doesn't fit standard C64 keyboard plungers - Source: [EwplTQDS_3I]
- Shift lock switch is round (standard C64 is square) - Source: [EwplTQDS_3I]

#### Typing Feel
- Much mushier feel than spring-based keyboards - Source: [EwplTQDS_3I]
- Generally less desirable for typing - Source: [EwplTQDS_3I]
- Rubber dome provides feedback but not same tactile response - Source: [EwplTQDS_3I]

#### Rubber Dome Issues
- Rubber domes can fall off when keyboard disassembled - Source: [EwplTQDS_3I]
- Contact pad is inside each rubber dome - Source: [EwplTQDS_3I]
- Missing rubber dome = non-functional key - Source: [EwplTQDS_3I]
- Spring can substitute to make key return but won't make contact - Source: [EwplTQDS_3I]
- Reassembly is difficult - domes must align precisely - Source: [EwplTQDS_3I]

#### Rarity
- Very uncommon variant - most C64s have spring keyboards - Source: [EwplTQDS_3I]
- Little documentation available online - Source: [EwplTQDS_3I]
- Reference: blog.retroleum.co.uk/electronics-articles/c64-keyboard-info/ - Source: [EwplTQDS_3I]

### EVO64 Modern C64 Motherboard

#### Overview
- Modern replacement motherboard for Commodore 64 - Source: [eyV7kaEMcfs]
- Website: evo64.com - Source: [eyV7kaEMcfs]
- Black PCB with gold-plated contacts - Source: [eyV7kaEMcfs]
- Long board replica form factor - Source: [eyV7kaEMcfs]

#### Original Chips Required
- 6510 CPU (original required) - Source: [eyV7kaEMcfs]
- Two 6526 CIA chips (originals required) - Source: [eyV7kaEMcfs]
- VIC-II video chip (original required) - Source: [eyV7kaEMcfs]
- 2114 SRAM for color RAM (original required) - Source: [eyV7kaEMcfs]

#### Modern Replacements Used
- RAM: Surface-mount DRAM instead of original 4164s - Source: [eyV7kaEMcfs]
- PLA: QA PLA (quad PLA) surface-mount replacement - Source: [eyV7kaEMcfs]
- ROM: Multi-ROM with selectable kernels - Source: [eyV7kaEMcfs]
- TTL logic: Surface-mount equivalents - Source: [eyV7kaEMcfs]
- Modern clock generator with both PAL and NTSC crystals - Source: [eyV7kaEMcfs]

#### VIC-II Compatibility
- Supports both 6000-series (longboard) and 8000-series (shortboard) VIC-II - Source: [eyV7kaEMcfs]
- Must match chip voltage with board setting - Source: [eyV7kaEMcfs]
- PAL/NTSC determined by VIC-II chip and clock setting - Source: [eyV7kaEMcfs]
- Cannot use PAL VIC-II with NTSC clock or vice versa - Source: [eyV7kaEMcfs]

#### SID Compatibility
- Supports both 6581 (12V) and 8580 (9V) SID chips - Source: [eyV7kaEMcfs]
- Dual SID support for stereo - Source: [eyV7kaEMcfs]
- Optional Tube64 vacuum tube audio preamp module - Source: [eyV7kaEMcfs]

#### Clear Video / Jailbar Fix
- Built-in clear video modification - Source: [eyV7kaEMcfs]
- Surface-mount version of jailbar elimination circuit - Source: [eyV7kaEMcfs]
- Adjustment pots included - Source: [eyV7kaEMcfs]
- May work better than traditional mods due to PCB layout - Source: [eyV7kaEMcfs]

#### Tube64 Audio Preamp
- Optional vacuum tube preamp module - Source: [eyV7kaEMcfs]
- Installs where RF modulator would be - Source: [eyV7kaEMcfs]
- Uses actual vacuum tube for audio path - Source: [eyV7kaEMcfs]
- USB audio DAC output for direct digital capture - Source: [eyV7kaEMcfs]
- Requires 30W or better power supply - Source: [eyV7kaEMcfs]

#### Power Supply
- Large capacitors for improved filtering - Source: [eyV7kaEMcfs]
- Bridge rectifier, fuse, and choke as standard - Source: [eyV7kaEMcfs]
- Voltage regulation for different VIC-II and SID variants - Source: [eyV7kaEMcfs]

### C64G (German Variant)

#### Overview
- German market variant of Commodore 64 - Source: [mDpZhaCbL-k]
- Made in West Germany, 1988 - Source: [mDpZhaCbL-k]
- Breadbin-style case but with 64C shortboard internally - Source: [mDpZhaCbL-k]
- Light-colored keyboard - Source: [mDpZhaCbL-k]
- Gray badge instead of rainbow badge - Source: [mDpZhaCbL-k]

#### Differences from Aldi C64
- Aldi C64: Made in USA in 1987 specifically for German Aldi stores - Source: [mDpZhaCbL-k]
- C64G: Made in West Germany in 1988 - Source: [mDpZhaCbL-k]
- Both use breadbin case with newer internals - Source: [mDpZhaCbL-k]
- Different manufacturing origins and dates - Source: [mDpZhaCbL-k]

#### Internal Hardware
- Uses 64C shortboard design - Source: [mDpZhaCbL-k]
- More integrated than original longboard design - Source: [mDpZhaCbL-k]
- Standard C64 compatibility maintained - Source: [mDpZhaCbL-k]

#### JiffyDOS Modification
- Example unit had JiffyDOS mod installed - Source: [mDpZhaCbL-k]
- Switchless JiffyDOS version - no external switch needed - Source: [mDpZhaCbL-k]
- Dramatically speeds up disk operations - Source: [mDpZhaCbL-k]
- Works with JiffyDOS-equipped drives - Source: [mDpZhaCbL-k]

### DesTest Max-Switch (C64 RAM Tester)

#### Overview
- C64 RAM test cartridge - Source: [M64hCqBpSDE]
- Tests all 64K of system RAM - Source: [M64hCqBpSDE]
- Uses innovative ROM switching technique - Source: [M64hCqBpSDE]
- More thorough than standard diagnostic cartridges - Source: [M64hCqBpSDE]

#### How It Works
- Standard test cartridges can't test RAM under ROM area - Source: [M64hCqBpSDE]
- Max-Switch uses real-time ROM switching - Source: [M64hCqBpSDE]
- Temporarily disables ROM to test underlying RAM - Source: [M64hCqBpSDE]
- Re-enables ROM after each test cycle - Source: [M64hCqBpSDE]
- Tests ALL 64K including RAM under BASIC/Kernal ROMs - Source: [M64hCqBpSDE]

#### Testing Algorithm
- Uses March testing algorithm - Source: [M64hCqBpSDE]
- March test catches address line faults - Source: [M64hCqBpSDE]
- Detects stuck bits and cross-talk issues - Source: [M64hCqBpSDE]
- More reliable than simple pattern tests - Source: [M64hCqBpSDE]

#### Advantages
- Finds problems that other testers miss - Source: [M64hCqBpSDE]
- Tests RAM that's normally hidden by ROM overlay - Source: [M64hCqBpSDE]
- Professional-grade diagnostic tool - Source: [M64hCqBpSDE]
- Essential for thorough C64 repair verification - Source: [M64hCqBpSDE]

### SwiftLink (C64 Serial Cartridge)

#### Overview
- Serial port cartridge for Commodore 64 - Source: [M64hCqBpSDE]
- Provides RS-232 serial communication - Source: [M64hCqBpSDE]
- Replica of original Creative Micro Designs SwiftLink - Source: [M64hCqBpSDE]

#### Hardware
- Uses 6551 ACIA (Asynchronous Communications Interface Adapter) - Source: [M64hCqBpSDE]
- Standard RS-232 voltage levels - Source: [M64hCqBpSDE]
- DB-9 or DB-25 serial connector - Source: [M64hCqBpSDE]

#### Performance
- Up to 38.4 kbps serial communication - Source: [M64hCqBpSDE]
- Much faster than C64 user port serial solutions - Source: [M64hCqBpSDE]
- IRQ-driven for efficient CPU usage - Source: [M64hCqBpSDE]

#### Applications
- Terminal emulation for BBS access - Source: [M64hCqBpSDE]
- File transfer using Kermit, XMODEM, etc. - Source: [M64hCqBpSDE]
- Modern WiFi modem connection - Source: [M64hCqBpSDE]
- Connecting to Unix/Linux systems - Source: [M64hCqBpSDE]

## Chip Testing (6510/6526)

### 6510 CPU Testing
- Use ZIF socket test machine for quick chip testing - Source: [kncrJYTRbnc]
- 6510 CPUs from 1984 are common - Source: [kncrJYTRbnc]
- 6510 is generally a reliable IC - unusual when one fails - Source: [kncrJYTRbnc]
- Putting 6510 in socket backwards doesn't damage it (resilient part) - Source: [kncrJYTRbnc]
- Mark tested chips with tick/check mark for known-good status - Source: [kncrJYTRbnc]
- Mark bad chips with X to indicate failure - Source: [kncrJYTRbnc]

### 6526 CIA Testing
- More prone to failure than 6510 CPU - Source: [kncrJYTRbnc]
- Therefore more rare and valuable - Source: [kncrJYTRbnc]
- Test by swapping into known-working C64 - Source: [kncrJYTRbnc]
- Look for flashing cursor after boot (good sign) - Source: [kncrJYTRbnc]
- Type on keyboard to verify CIA is working - Source: [kncrJYTRbnc]
- Failure modes: non-flashing cursor, won't boot, no keyboard response - Source: [kncrJYTRbnc]
- CIAs tend to fail completely rather than partially - Source: [kncrJYTRbnc]

## Modern C64 Hardware

### C64 Direct-to-TV (C64 DTV)

#### Overview
- Single-chip implementation of Commodore 64 contained in joystick - Source: [X5q25JlkuAc]
- NOT emulation - real C64 ASIC running at 32MHz - Source: [X5q25JlkuAc]
- 30 built-in games - Source: [X5q25JlkuAc]
- First appeared late 2004 for US/Canadian market - Source: [X5q25JlkuAc]
- Manufactured by Mammoth Toys - Source: [X5q25JlkuAc]

#### Hardware Implementation
- ASIC implements 6510, VIC-2, SID, CIA, and PLA - Source: [X5q25JlkuAc]
- 2MB of ROM for games - Source: [X5q25JlkuAc]
- Composite video output - Source: [X5q25JlkuAc]
- Binaural audio output - Source: [X5q25JlkuAc]
- Uses Competition Pro style joystick form factor - Source: [X5q25JlkuAc]

#### Versions
- DTV1: NTSC only, late 2004, original C64 graphics - Source: [X5q25JlkuAc]
- DTV2: PAL version, late 2005, added chunky 256-color mode and blitter - Source: [X5q25JlkuAc]
- DTV2+ chips could do NTSC and PAL but hardwired for PAL in consumer units - Source: [X5q25JlkuAc]

#### Modding Capability
- Internal solder pads exposed for modifications - Source: [X5q25JlkuAc]
- Can add: keyboard connector, external joysticks, floppy connector - Source: [X5q25JlkuAc]
- Can add: power supply connector, S-video output, user port - Source: [X5q25JlkuAc]
- Can be placed in original C64 casing with keyboard - Source: [X5q25JlkuAc]
- SD card interface available via mod - Source: [X5q25JlkuAc]
- Data transfer cable modifications possible - Source: [X5q25JlkuAc]

#### Limitations
- No support for SID filters (sound not quite right) - Source: [X5q25JlkuAc]
- DTV2+ added 8-bit digital sound and envelope generator - Source: [X5q25JlkuAc]
- Internal flash memory is read-only (no high score saving) - Source: [X5q25JlkuAc]
- Flash chips specified for limited writes only - Source: [X5q25JlkuAc]
- F7 key doesn't work with standard keyboard mod - Source: [X5q25JlkuAc]
- PAL version has color palette issues requiring fix - Source: [X5q25JlkuAc]

### C64 Mini

#### Overview
- Modern ARM-based C64 emulation device - Source: [X5q25JlkuAc]
- Uses software emulation (likely VICE-based) - Source: [X5q25JlkuAc]
- Small form factor C64 replica - Source: [X5q25JlkuAc]
- HDMI output for modern displays - Source: [X5q25JlkuAc]
- USB input for joysticks and keyboards - Source: [X5q25JlkuAc]

#### Included Accessories
- Competition Pro style USB joystick - Source: [X5q25JlkuAc]
- Joystick has extra buttons for menu navigation - Source: [X5q25JlkuAc]
- HDMI and USB cables included - Source: [X5q25JlkuAc]

#### Hardware Limitations
- Keyboard is non-functional (decorative only) - Source: [X5q25JlkuAc]
- No headphone jack (audio through HDMI only) - Source: [X5q25JlkuAc]
- Only two USB ports - Source: [X5q25JlkuAc]
- Soft power switch - Source: [X5q25JlkuAc]

#### Software Features
- Can emulate C64 and VIC-20 (with firmware update) - Source: [X5q25JlkuAc]
- NTSC and PAL C64 modes available - Source: [X5q25JlkuAc]
- Boot to carousel or BASIC screen - Source: [X5q25JlkuAc]
- USB thumb drive for loading custom software - Source: [X5q25JlkuAc]
- Multiple display options: pixel perfect, CRT emulation, 4:3 aspect - Source: [X5q25JlkuAc]

#### Color Palette Issues
- Uses PAL-style washed out color palette even in NTSC mode - Source: [X5q25JlkuAc]
- Colors are muted/pastely compared to real NTSC C64 - Source: [X5q25JlkuAc]
- No option to select more vibrant NTSC color palettes - Source: [X5q25JlkuAc]
- VICE emulator offers Sony palette options that are more vibrant - Source: [X5q25JlkuAc]

### C64 Maxi (The C64)

#### Overview
- Full-size C64 replica with working keyboard - Source: [X5q25JlkuAc]
- Same internal hardware as C64 Mini - Source: [X5q25JlkuAc]
- Uses software emulation (likely VICE-based) - Source: [X5q25JlkuAc]
- Better option than Mini due to working keyboard - Source: [X5q25JlkuAc]

#### Physical Design
- Same port layout as real C64 plus extra USB port on back - Source: [X5q25JlkuAc]
- Three USB ports total (vs two on Mini) - Source: [X5q25JlkuAc]
- Keyboard uses membrane switches - Source: [X5q25JlkuAc]
- Key legends appear to be printed (not double-shot) - may wear over time - Source: [X5q25JlkuAc]
- Case color slightly less orangey than original C64 - Source: [X5q25JlkuAc]
- Very solid construction, not creaky like originals - Source: [X5q25JlkuAc]

#### Known Issues
- Same color palette issues as Mini - Source: [X5q25JlkuAc]
- Integer scaling causes uneven character widths in some modes - Source: [X5q25JlkuAc]
- CRT emulation mode has fake scanlines some users dislike - Source: [X5q25JlkuAc]
- Menu navigation not intuitive from keyboard alone - Source: [X5q25JlkuAc]
- Arrow keys don't work for carousel navigation (needs joystick) - Source: [X5q25JlkuAc]

#### Firmware Features
- 64 built-in games - Source: [X5q25JlkuAc]
- VIC-20 emulation mode - Source: [X5q25JlkuAc]
- REU (RAM expansion unit) emulation - Source: [X5q25JlkuAc]
- Multiple disk drive emulation - Source: [X5q25JlkuAc]
- USB drive for loading custom software - Source: [X5q25JlkuAc]

### Ultimate 64 Elite

#### Overview
- FPGA-based recreation of Commodore 64 - Source: [X5q25JlkuAc]
- Made by Gideon (community project) - Source: [X5q25JlkuAc]
- Fits in standard C64 case - Source: [X5q25JlkuAc]
- Compatible with original cartridges, keyboards, peripherals - Source: [X5q25JlkuAc]

#### FPGA Implementation
- Uses both Altera and Xilinx FPGAs - Source: [X5q25JlkuAc]
- Emulates 64 in hardware via FPGA - Source: [X5q25JlkuAc]
- SID emulation built-in but can use real SID chips - Source: [X5q25JlkuAc]
- Dual SID support on board - Source: [X5q25JlkuAc]

#### Connectivity
- HDMI output - Source: [X5q25JlkuAc]
- Ethernet port - Source: [X5q25JlkuAc]
- WiFi module - Source: [X5q25JlkuAc]
- Multiple USB ports (internal and external) - Source: [X5q25JlkuAc]
- SD card slot - Source: [X5q25JlkuAc]
- Standard joystick ports - Source: [X5q25JlkuAc]
- IEC serial port for disk drives - Source: [X5q25JlkuAc]
- Cassette port - Source: [X5q25JlkuAc]
- Cartridge port - Source: [X5q25JlkuAc]
- RGB output - Source: [X5q25JlkuAc]

#### Other Features
- Barrel jack power input - Source: [X5q25JlkuAc]
- Soft power switch - Source: [X5q25JlkuAc]
- Clock battery for RTC - Source: [X5q25JlkuAc]
- Keyboard connector for C64 keyboard - Source: [X5q25JlkuAc]

### Modern C64 Cases (Pixels Past / c64.de)

#### Overview
- Modern reproduction C64C cases from original tooling - Source: [X5q25JlkuAc]
- Accurate to original specifications - Source: [X5q25JlkuAc]
- Available in multiple colors - Source: [X5q25JlkuAc]

#### Color Options
- Classic beige - Source: [X5q25JlkuAc]
- Bread bin gray - Source: [X5q25JlkuAc]
- SX-64 style - Source: [X5q25JlkuAc]
- Retro black - Source: [X5q25JlkuAc]
- Transparent (for showing off internals) - Source: [X5q25JlkuAc]

#### Accessories
- Modern keyboard mounts (metal, flashy designs) - Source: [X5q25JlkuAc]
- 3D printed keyboard mounts available (Pixel Wizard Retro Shop) - Source: [X5q25JlkuAc]
- Case badges (large for breadbin, small for C64C) - Source: [X5q25JlkuAc]
- LED strips for internal lighting (addressable RGB) - Source: [X5q25JlkuAc]
- Assembly guide included - Source: [X5q25JlkuAc]
- Bottom case badge available - Source: [X5q25JlkuAc]

### MOS 6526 CIA Chip Reliability

#### Achilles Heel of C64
- CIA chips most failure-prone component in C64 - Source: [X5q25JlkuAc]
- More rare and valuable than 6510 CPU due to failure rate - Source: [X5q25JlkuAc]
- No good aftermarket replacement exists yet - Source: [X5q25JlkuAc]
- ZIP-64 test machine can test 6526 chips - Source: [X5q25JlkuAc]
