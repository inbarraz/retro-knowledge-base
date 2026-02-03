# Nintendo

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| NES (Nintendo Entertainment System) | Game Console | [Ls46eQOCkN8], [LwC4JbUzjlE], [szWwKmitFC4] |
| SNES (Super Nintendo) | Game Console | [Ls46eQOCkN8] |
| Famicom | Game Console | [pKDRJWhd1CY], [ueyv2vRIQK8] |

## Platform-Specific Knowledge

### NES (Nintendo Entertainment System)

#### PPU (Picture Processing Unit) - 2C02

##### Overview
- Ricoh 2C02 custom chip handles all NES graphics - Source: [LwC4JbUzjlE]
- Generates composite video output - Source: [LwC4JbUzjlE]
- Multiple revisions: 2C02E, 2C02G most common - Source: [LwC4JbUzjlE]
- PPU revision printed on chip package - Source: [LwC4JbUzjlE]

##### Rev E vs Rev G Differences
- Both produce compatible composite video - Source: [LwC4JbUzjlE]
- EXT0-3 signals differ between revisions - Source: [LwC4JbUzjlE]
- EXT signals used by some FPGA RGB mods - Source: [LwC4JbUzjlE]
- Rev G EXT signals more robust than Rev E - Source: [LwC4JbUzjlE]

##### FPGA RGB Mod Compatibility (Lava RSC)
- Lava RSC Famiclone uses FPGA for RGB reconstruction - Source: [LwC4JbUzjlE]
- FPGA reads PPU EXT0-3 signals for color data - Source: [LwC4JbUzjlE]
- Rev E PPU may cause "sparkles" (random pixel errors) - Source: [LwC4JbUzjlE]
- Rev G PPU works more reliably with FPGA - Source: [LwC4JbUzjlE]
- Pin 21 multiplexed: composite video out AND EXT4 input - Source: [LwC4JbUzjlE]

##### Level Shifter Issues
- FPGA runs at 3.3V, PPU runs at 5V - Source: [LwC4JbUzjlE]
- 74LVC541 used as level shifter - Source: [LwC4JbUzjlE]
- 74LVC is CMOS, has different threshold than TTL - Source: [LwC4JbUzjlE]
- CMOS high threshold: ~2.5V (50% of Vcc) - Source: [LwC4JbUzjlE]
- TTL high threshold: ~2.0V - Source: [LwC4JbUzjlE]
- Marginal signals may work with TTL but fail with CMOS - Source: [LwC4JbUzjlE]
- Rev E PPU may have marginal EXT output levels - Source: [LwC4JbUzjlE]

##### Diagnosing PPU Issues
- "Sparkles" = random bright pixels flashing on screen - Source: [LwC4JbUzjlE]
- Usually data corruption, not PPU failure - Source: [LwC4JbUzjlE]
- Test by swapping PPU with known-good chip - Source: [LwC4JbUzjlE]
- PPU socket allows easy swapping - Source: [LwC4JbUzjlE]

##### CPU/PPU Identification
- 2C02 = PPU (Picture Processing Unit) - Source: [LwC4JbUzjlE]
- 2A03 = CPU (custom 6502 with APU) - Source: [LwC4JbUzjlE]
- RP2A3G = CPU (6502 with built-in sound/APU) - Source: [szWwKmitFC4]
- RP22G = PPU (Picture Processing Unit) - Source: [szWwKmitFC4]
- Don't confuse the two when troubleshooting - Source: [LwC4JbUzjlE]

#### CIC Lockout Chip

##### Overview
- Nintendo's copy protection chip - Source: [Ls46eQOCkN8], [LwC4JbUzjlE]
- Console CIC authenticates with cartridge CIC - Source: [LwC4JbUzjlE]
- Causes reset loop if authentication fails - Source: [LwC4JbUzjlE]
- Different regional lockout chips (NTSC, PAL) - Source: [LwC4JbUzjlE]

##### Bypass Methods
- Cut pin 4 on console CIC chip - Source: [LwC4JbUzjlE], [szWwKmitFC4]
- Pin 4 connects to 5V (thick trace visible) - Source: [szWwKmitFC4]
- Cutting disconnects CIC from reset line control - Source: [szWwKmitFC4]
- Replace CIC with bypass chip - Source: [Ls46eQOCkN8]
- Some replacement 72-pin connectors include bypass - Source: [Ls46eQOCkN8]
- NESRGB mod board includes CIC bypass - Source: [LwC4JbUzjlE]

##### CIC Chip Failure Modes
- Failed CIC can hold system in permanent reset - Source: [szWwKmitFC4]
- Symptom: System powers on but no video (not flashing) - Source: [szWwKmitFC4]
- Pin 9 is reset output - should go high when running - Source: [szWwKmitFC4]
- Failed chip keeps pin 9 low constantly - Source: [szWwKmitFC4]
- CIC senses reset button via pin 7 through LED - Source: [szWwKmitFC4]
- Workaround: Remove CIC entirely and add manual reset circuit - Source: [szWwKmitFC4]
- Simple fix: Pull-up resistor from pin 9 pad to 5V after removing chip - Source: [szWwKmitFC4]

#### 72-Pin Connector Issues

##### Symptoms
- Blinking power light - Source: [Ls46eQOCkN8]
- Gray screen or no video - Source: [Ls46eQOCkN8]
- Games boot intermittently - Source: [Ls46eQOCkN8]
- Pressing down on cartridge helps contact - Source: [Ls46eQOCkN8]

##### Traditional Repair
- Bend pins back using narrow tool - Source: [Ls46eQOCkN8]
- Clean connector with IPA - Source: [Ls46eQOCkN8]
- Boil connector in water (controversial) - Source: [Ls46eQOCkN8]
- Replace with new 72-pin connector - Source: [Ls46eQOCkN8]
- DeoxIT on connector: Almost always fixes cartridge reading issues - Source: [szWwKmitFC4]
- Magic eraser to polish oxidized connector pins - Source: [szWwKmitFC4]
- Edge connector is NOT gold plated - oxidizes over time - Source: [szWwKmitFC4]
- Connector reliability often blamed on design but usually just needs cleaning - Source: [szWwKmitFC4]

##### Nintendrawer Replacement
- 3D printed mechanism replacement for 72-pin connector - Source: [Ls46eQOCkN8]
- Complete cartridge slot mechanism, not just connector - Source: [Ls46eQOCkN8]
- Top-loading design (like NES-101) - Source: [Ls46eQOCkN8]
- Includes CIC bypass chip option - Source: [Ls46eQOCkN8]
- Approximately $55 - Source: [Ls46eQOCkN8]
- Eliminates need to press down on cartridge - Source: [Ls46eQOCkN8]
- More reliable than original zero-insertion-force design - Source: [Ls46eQOCkN8]

#### RF Modulator Box

##### Overview
- Contains voltage regulator AND RF modulator - Source: [szWwKmitFC4]
- 9V AC input rectified to DC, then regulated to 5V - Source: [szWwKmitFC4]
- Heat sink connects to metal RF shield - Source: [szWwKmitFC4]
- Outputs both composite video and RF signal - Source: [szWwKmitFC4]
- Channel selector switch (3/4) on box - Source: [szWwKmitFC4]

##### Internal Function
- Buffers/amplifies PPU composite video output - Source: [szWwKmitFC4]
- PPU cannot directly drive 75 ohm video load - Source: [szWwKmitFC4]
- Direct connection to video out kills signal - Source: [szWwKmitFC4]
- Buffer transistor circuit needed for proper output - Source: [szWwKmitFC4]
- Fixes video to proper NTSC 1V peak-to-peak - Source: [szWwKmitFC4]

##### Power Supply Compatibility
- Atari 400/800/810 power supplies work (9V AC) - Source: [szWwKmitFC4]
- Bridge rectifier inside allows any polarity DC input - Source: [szWwKmitFC4]
- 9V DC will also work due to rectifier - Source: [szWwKmitFC4]

#### Motherboard Testing Without RF Modulator

##### Direct Power Feed
- Feed regulated 5V directly to motherboard - Source: [szWwKmitFC4]
- Connect to TTL IC Vcc pin (middle pin typically) - Source: [szWwKmitFC4]
- Ground connects to ground plane - Source: [szWwKmitFC4]
- System draws ~280mA when running - Source: [szWwKmitFC4]

##### Video Signal Testing
- Raw PPU composite output has DC offset - Source: [szWwKmitFC4]
- Inline capacitor needed to block DC - Source: [szWwKmitFC4]
- Output too hot (~1.4V peak) without RF modulator buffer - Source: [szWwKmitFC4]
- Cannot directly drive 75 ohm load (kills signal) - Source: [szWwKmitFC4]
- Oscilloscope useful for verifying video signal present - Source: [szWwKmitFC4]

#### Controller Port Wiring

##### Factory Defects
- Wires can be pinched under standoffs during assembly - Source: [szWwKmitFC4]
- Broken wire causes controller/light gun issues - Source: [szWwKmitFC4]
- Controller may work but light gun fails (separate signal) - Source: [szWwKmitFC4]
- Check wire routing if controller port issues - Source: [szWwKmitFC4]

#### Motherboard Reliability

##### General Notes
- NES motherboards extremely reliable - Source: [szWwKmitFC4]
- Scrap boards often work perfectly with DeoxIT - Source: [szWwKmitFC4]
- Custom ICs rarely fail - Source: [szWwKmitFC4]
- SRAM is standard type, easily replaced - Source: [szWwKmitFC4]
- Different PCB revisions may have different SRAM footprints - Source: [szWwKmitFC4]
- Bottom expansion port has same signals as cartridge port - Source: [szWwKmitFC4]
- Was intended for Japanese-style Famicom Disk System attachment - Source: [szWwKmitFC4]

### Famicom (Japanese NES)

#### Overview
- Original Japanese version of the NES - Source: [ueyv2vRIQK8]
- Different cartridge connector than US NES (60-pin vs 72-pin) - Source: [ueyv2vRIQK8]
- Hardwired controllers (non-detachable) on original model - Source: [ueyv2vRIQK8]
- Expansion audio supported via cartridge connector - Source: [ueyv2vRIQK8]

#### Famicom vs NES Differences

##### Expansion Audio
- Famicom cartridge connector has audio mixing pins - Source: [ueyv2vRIQK8]
- Some games have extra sound chips on cartridge (VRC6, VRC7, Namco 163, etc.) - Source: [ueyv2vRIQK8]
- Famicom mixes cartridge audio with internal APU - Source: [ueyv2vRIQK8]
- NES 72-pin connector lacks audio mixing - expansion audio lost on US carts - Source: [ueyv2vRIQK8]
- Games like Castlevania III have different (lesser) music on NES vs Famicom - Source: [ueyv2vRIQK8]

##### Mappers
- MMC5 mapper supports expansion audio and enhanced graphics - Source: [ueyv2vRIQK8]
- Certain mappers only used in Japan due to NES limitations - Source: [ueyv2vRIQK8]

#### Composite Video Mod
- Common mod to bypass RF modulator - Source: [ueyv2vRIQK8]
- Provides cleaner video than RF output - Source: [ueyv2vRIQK8]
- Internal PPU outputs composite, just needs buffering - Source: [ueyv2vRIQK8]

#### Cartridge Contact Cleaning
- Use DeoxIT for cleaning cartridge edge contacts - Source: [ueyv2vRIQK8]
- Famicom cart contacts are NOT gold plated - Source: [ueyv2vRIQK8]
- Magic eraser works well for polishing oxidized contacts - Source: [ueyv2vRIQK8]
- Never use magic eraser on gold-plated contacts (removes gold) - Source: [ueyv2vRIQK8]

### SNES (Super Nintendo Entertainment System)

#### Audio System

##### SPC700 DSP
- Sony SPC700 digital signal processor handles all SNES audio - Source: [Ls46eQOCkN8]
- 64KB dedicated audio RAM - Source: [Ls46eQOCkN8]
- 8 stereo voices - Source: [Ls46eQOCkN8]
- Wavetable synthesis with sample playback - Source: [Ls46eQOCkN8]

##### Super MIDI Pak

###### Overview
- SNES cartridge that converts console to MIDI synthesizer - Source: [Ls46eQOCkN8]
- Uses SPC700 DSP as General MIDI sound module - Source: [Ls46eQOCkN8]
- Approximately $120 - Source: [Ls46eQOCkN8]
- Created by Amaury Carvalho - Source: [Ls46eQOCkN8]

###### Features
- Standard MIDI input jack on cartridge - Source: [Ls46eQOCkN8]
- General MIDI compatible instrument set - Source: [Ls46eQOCkN8]
- 8 simultaneous voices (SNES hardware limit) - Source: [Ls46eQOCkN8]
- Roland SC-55 style sound font included - Source: [Ls46eQOCkN8]
- Sounds authentic to 16-bit era - Source: [Ls46eQOCkN8]

###### Limitations
- 8 voice polyphony (vs 24+ on professional synths) - Source: [Ls46eQOCkN8]
- Voice stealing when exceeding polyphony - Source: [Ls46eQOCkN8]
- Some complex MIDI sequences may sound thin - Source: [Ls46eQOCkN8]
- Perfect for chiptune/retro music production - Source: [Ls46eQOCkN8]

###### Connection
- Any MIDI controller or sequencer works - Source: [Ls46eQOCkN8]
- Use SNES composite or RGB output for audio - Source: [Ls46eQOCkN8]
- No display needed (just audio) - Source: [Ls46eQOCkN8]

## Modern Accessories

### Flying Rommy EPROM Emulator
- ESP32-based ROM emulator - Source: [Ls46eQOCkN8]
- Emulates EPROMs in real-time - Source: [Ls46eQOCkN8]
- Upload ROM images via WiFi or USB - Source: [Ls46eQOCkN8]
- Works with NES, SNES, and other cartridge systems - Source: [Ls46eQOCkN8]
- Useful for development and testing - Source: [Ls46eQOCkN8]
- Open source project - Source: [Ls46eQOCkN8]
- GitHub: Available on GitHub (search "Flying Rommy") - Source: [Ls46eQOCkN8]

## General Notes

### TTL vs CMOS Logic Thresholds
- Important when interfacing 5V chips with 3.3V systems - Source: [LwC4JbUzjlE]
- TTL low: 0V to 0.8V - Source: [LwC4JbUzjlE]
- TTL high: 2.0V to 5V - Source: [LwC4JbUzjlE]
- CMOS low: 0V to ~1.5V (30% of Vcc) - Source: [LwC4JbUzjlE]
- CMOS high: ~2.5V to 5V (50% of Vcc) - Source: [LwC4JbUzjlE]
- 74LVC series are CMOS, not TTL compatible thresholds - Source: [LwC4JbUzjlE]
- 74HCT series have TTL-compatible input thresholds - Source: [LwC4JbUzjlE]
- Marginal signals may work with HCT but fail with LVC - Source: [LwC4JbUzjlE]
