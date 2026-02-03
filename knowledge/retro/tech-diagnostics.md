# Diagnostics and Testing Techniques

> Part of the retro knowledge base. See also: tech-*.md files for other categories.

## Contents
- [Diagnostics](#diagnostics)
- [Analog Signature Analysis](#analog-signature-analysis)
- [Shorted Tantalum Capacitor Diagnosis](#shorted-tantalum-capacitor-diagnosis)

## Diagnostics

### Visual Inspection
- Check for missing chips in sockets - may indicate pillaged parts - Source: [_0XGFz67DIc]
- Look for modified/added wires indicating previous repairs or conversions - Source: [_0XGFz67DIc]
- Check for hygroscopic glue on CRT yokes - becomes conductive when wet, can corrode enamel-coated copper windings - Source: [_MljEAIpQ8g]
- Inspect high voltage anode cable condition - becomes brittle/crispy with age, may crumble if manipulated - Source: [_MljEAIpQ8g]
- Look for soot inside CRT top cover - indicates significant run time - Source: [_MljEAIpQ8g]
- Check for NiCad battery leakage/corrosion on clock boards - visible corrosion indicates damage - Source: [_muHEAJ7dko]
- Hand-bent IC pins indicate manual modifications or connections to other boards - Source: [_muHEAJ7dko]
- Wire-wrap and enamel wire construction indicates homebrew/kit computer - Source: [_muHEAJ7dko]
- Bus connector edge shape helps identify bus standard (S-100 has no center notch) - Source: [_muHEAJ7dko]

### Electronic Testing
- ROM chip testing with Retro Chip Tester Pro: Verify correct pin orientation (e.g., pin 20 low for some chips) - Source: [_0XGFz67DIc]
- CPU swap testing: Replace CPU with known-good unit to isolate CPU vs. other issues - Source: [_0XGFz67DIc]
- When garbage appears on screen with clear image, systematically test ROM and other chips - Source: [_0XGFz67DIc]

### AT Power Supply Testing

#### Pre-Test Isolation
- Unplug all peripherals (drives, cards) before testing power supply - Source: [vh9fVhSNzGg]
- Prevents bad PSU from damaging other components - Source: [vh9fVhSNzGg]
- A failing PSU can output over-voltage (e.g., 8-9V on 5V rail) and damage motherboard - Source: [vh9fVhSNzGg]

#### Testing with Load
- AT power supplies generally work without load but better to add one - Source: [vh9fVhSNzGg]
- Use car light bulb as dummy load on 5V rail - Source: [vh9fVhSNzGg]
- Connect bulb between red wire (5V) and black wire (ground) - Source: [vh9fVhSNzGg]
- Check voltages with multimeter: 5V rail, 12V rail - Source: [vh9fVhSNzGg]
- Example readings: 5.08V on 5V rail, 11.9V on 12V rail = working PSU - Source: [vh9fVhSNzGg]

#### AT Power Switch Safety
- AT power supplies have physical power switch with mains voltage on wires - Source: [vh9fVhSNzGg]
- Mains voltage runs through wires from PSU to front panel switch - Source: [vh9fVhSNzGg]
- Do not touch exposed wires near power switch area - Source: [vh9fVhSNzGg]
- Some have rubber sleeves but bits may still be exposed - Source: [vh9fVhSNzGg]

#### AT Power Connector Polarity
- Black wires always go together in the middle when connecting - Source: [vh9fVhSNzGg]
- Reversing connector shorts 5V rail to other signals causing damage - Source: [vh9fVhSNzGg]
- P8 and P9 connectors must be oriented correctly - Source: [vh9fVhSNzGg]

#### Initial Power-Up Procedure
- Test PSU independently first with dummy load - Source: [vh9fVhSNzGg]
- Connect only motherboard initially - Source: [vh9fVhSNzGg]
- Use POST card to monitor voltages and POST codes - Source: [vh9fVhSNzGg]
- Plug in old sacrificial hard drive for additional load if needed - Source: [vh9fVhSNzGg]

### POST Code Analysis

#### POST Cards on XT Systems
- POST codes do not work on PC/XT (no POST code output by BIOS) - Source: [noRZC9y9Uz0]
- POST cards still useful for monitoring voltage rails on XT - Source: [noRZC9y9Uz0]
- Can connect speaker output from POST card to motherboard speaker header - Source: [noRZC9y9Uz0]
- POST code FF indicates system has completed POST and is trying to work - Source: [noRZC9y9Uz0]

#### Traditional POST Cards
- Display hexadecimal POST codes from motherboard BIOS - Source: [FnLKPVzK7bo]
- Standard port: 80h (IBM PC compatible) - Source: [FnLKPVzK7bo]
- Compaq port: 84h - Source: [FnLKPVzK7bo]
- IBM PS/2 ISA port: 90h - Source: [FnLKPVzK7bo]
- LS port: 300h - Source: [FnLKPVzK7bo]
- Olivetti port: 378h - Source: [FnLKPVzK7bo]
- Chinese clone POST cards often respond to ports 80, 84, AND 300 simultaneously - Source: [FnLKPVzK7bo]
- Period-correct diagnostic cards may show DMA and interrupt activity - Source: [FnLKPVzK7bo]
- Some cards include speaker for audio feedback - Source: [FnLKPVzK7bo]

#### POST Code Requirements
- Requires functional BIOS ROM executing code - Source: [FnLKPVzK7bo]
- Requires functional CPU executing code - Source: [FnLKPVzK7bo]
- No POST codes = dead CPU, dead BIOS ROM, or power issue - Source: [FnLKPVzK7bo]
- FF = system has booted, POST complete - Source: [FnLKPVzK7bo]
- C1 (example) = RAM check failure - Source: [FnLKPVzK7bo]

#### DOS Debug Program for POST Testing
- Can manually write to POST ports using DEBUG - Source: [FnLKPVzK7bo]
- Syntax: O <port> <value> (e.g., O 80 AA) - Source: [FnLKPVzK7bo]
- Useful for testing which ports a POST card responds to - Source: [FnLKPVzK7bo]

#### PicoPOST (Modern Software-Defined)
- Raspberry Pi Pico-based POST analyzer for ISA bus - Source: [FnLKPVzK7bo]
- Software-defined, firmware updateable - Source: [FnLKPVzK7bo]
- OLED display connected via SATA cable (cheap, high-speed transport) - Source: [FnLKPVzK7bo]
- Supports multiple IO ports (80, 84, 90, 300, 378) - Source: [FnLKPVzK7bo]
- Shows POST code history - Source: [FnLKPVzK7bo]
- Includes voltage rail monitoring (5V, 12V, -12V) - Source: [FnLKPVzK7bo]
- GitHub: github.com/TheRetroWeb/PicoPOST - Source: [FnLKPVzK7bo]
- PCB version 1.0 may have hardware/firmware issues with some ports - Source: [FnLKPVzK7bo]
- May show spurious readings from ISA bus activity - Source: [FnLKPVzK7bo]
- Setting resets after power cycle (must re-select port) - Source: [FnLKPVzK7bo]
- Suggestion: Add onboard speaker, integrated OLED screen - Source: [FnLKPVzK7bo]

### Cache Memory Testing
- CacheChk utility by Ray Van Tassel (1995-1998) - Source: [5Gfr6lW49aI], [HtrAvQGuXTw]
- Measures microseconds per kilobyte at different block sizes - Source: [5Gfr6lW49aI]
- Performance drops when block size exceeds cache size - Source: [5Gfr6lW49aI]
- 386DX: 64KB L1 cache typical, ~47µs/KB cached vs ~78µs/KB uncached - Source: [5Gfr6lW49aI]
- Some motherboards only cache first 16MB of RAM - test shows slowdown above 16MB - Source: [5Gfr6lW49aI]
- 386 has no on-die cache (L1 is external), 486 has on-die L1 - Source: [5Gfr6lW49aI]
- Speed600 and SpeedSys utilities useful for cache validation - Source: [HtrAvQGuXTw]
- Compare cached vs uncached performance to verify cache working - Source: [HtrAvQGuXTw]
- CacheChk shows SRAM cache detected (e.g., 64KB at 50ns) vs main memory (e.g., 71ns) - Source: [noRZC9y9Uz0]
- Cache gives ~150% read speed improvement over uncached main memory - Source: [noRZC9y9Uz0]

### CPU Speed Benchmarking

#### Speed600/Landmark Speed Test
- Landmark speed test: Standard DOS benchmark, shows CPU speed relative to original XT - Source: [noRZC9y9Uz0]
- Can change turbo jumper and see real-time speed change - Source: [noRZC9y9Uz0]
- 386DX-33 shows ~54MHz equivalent (25x faster than XT) - Source: [noRZC9y9Uz0]
- Useful for verifying turbo switch function and clock speed - Source: [noRZC9y9Uz0]
- Date shown (1993) indicates program age, commonly used in computer stores - Source: [noRZC9y9Uz0]

#### CheckIt Diagnostics
- Comprehensive system diagnostics for DOS - Source: [noRZC9y9Uz0]
- System board test verifies basic hardware function - Source: [noRZC9y9Uz0]
- Useful for quick pass/fail verification of motherboard - Source: [noRZC9y9Uz0]

### Chip Testing
- Use TL866II Plus (MiniPro) for EPROM programming and chip testing - Source: [_0XGFz67DIc]

### MC68000 Free Run Tester

#### Overview
- Standalone CPU tester for Motorola 68000 processors - Source: [oJ486-I3IuI]
- Project by Mercury Coding - Source: [oJ486-I3IuI]
- Website: mercurycoding.com/blog.html - Source: [oJ486-I3IuI]
- Tests if CPU is functional and detects fakes/rebadges - Source: [oJ486-I3IuI]

#### How It Works
- Locks data bus so CPU executes equivalent of NOP continuously - Source: [oJ486-I3IuI]
- CPU "free runs" through entire address space repeatedly - Source: [oJ486-I3IuI]
- LEDs on address lines A1-A23 show counting pattern - Source: [oJ486-I3IuI]
- If CPU is functional, address lines sequence through all values - Source: [oJ486-I3IuI]

#### Speed Testing
- Multiple crystal oscillators: 16 MHz and 12 MHz - Source: [oJ486-I3IuI]
- DIP switches select clock divider for speeds from 750 kHz to 16 MHz - Source: [oJ486-I3IuI]
- Coax connector for external custom clock frequency - Source: [oJ486-I3IuI]
- Can verify if rebadged chip meets claimed speed rating - Source: [oJ486-I3IuI]
- Run at marked speed to check if CPU locks up - Source: [oJ486-I3IuI]

#### Features
- ZIF socket for standard DIP-64 68000 - Source: [oJ486-I3IuI]
- Adapter for high-density 1.78mm pin packages (like C64 PLA) - Source: [oJ486-I3IuI]
- Reset and Halt buttons - Source: [oJ486-I3IuI]
- Function code LEDs (FC0, FC1, FC2) for monitoring bus status - Source: [oJ486-I3IuI]
- 24-pin ATX power connector (Pico PSU recommended) - Source: [oJ486-I3IuI]

#### Usage Notes
- Good for quick pass/fail testing - Source: [oJ486-I3IuI]
- Leave running for extended time to catch intermittent failures - Source: [oJ486-I3IuI]
- Missing LED indicates bad address line driver - Source: [oJ486-I3IuI]
- Note: Design lacks current-limiting resistors on LEDs - Source: [oJ486-I3IuI]
- LEDs connected directly between address lines and 5V rail - Source: [oJ486-I3IuI]
- Not recommended for hours-long burn-in (LED short could damage CPU) - Source: [oJ486-I3IuI]

#### Rebadge Detection
- Chinese 68000s often rebadged with false speed ratings - Source: [oJ486-I3IuI]
- Original manufacturer silkscreen sanded off, Motorola logo laser etched - Source: [oJ486-I3IuI]
- Running at claimed speed tests authenticity - Source: [oJ486-I3IuI]
- 68000 vs 68010 cannot be distinguished visually if rebadged - Source: [oJ486-I3IuI]

### Chips That Test Good But Fail In-Circuit

#### Weak Output Driver Diagnosis
- Chip may test OK in Retro Chip Tester Pro but fail in actual circuit - Source: [VKiuJbhVbrk]
- Output driver too weak to drive bus lines under load of full motherboard - Source: [VKiuJbhVbrk]
- Manifests as signal going high briefly then dropping to low - Source: [VKiuJbhVbrk]
- Good chip: signal stays high for entire enable pulse width - Source: [VKiuJbhVbrk]
- Bad chip: brief spike at enable, then drops low immediately - Source: [VKiuJbhVbrk]

#### 74LS373 DMA Address Latch Failure (PC XT)
- 74LS373 generates address lines for DMA transfers (A8-A19) - Source: [VKiuJbhVbrk]
- Symptom: floppy controller doesn't work, data goes to wrong RAM address - Source: [VKiuJbhVbrk]
- System otherwise boots because DRAM refresh still works - Source: [VKiuJbhVbrk]
- PC XT uses DMA channel 0 for DRAM refresh - must work for system to run - Source: [VKiuJbhVbrk]
- Floppy controller uses different DMA channel (channel 2) - Source: [VKiuJbhVbrk]
- Some address lines may work while others fail (weak on specific pin) - Source: [VKiuJbhVbrk]

#### Oscilloscope Diagnosis Method
- Connect channel 1 to chip enable pin (pin 1 on 74LS373) - Source: [VKiuJbhVbrk]
- Connect channel 2 to suspect output pin - Source: [VKiuJbhVbrk]
- Trigger on enable signal going low (active) - Source: [VKiuJbhVbrk]
- Watch if output holds high for entire enable pulse duration - Source: [VKiuJbhVbrk]
- Bad chip: output goes high momentarily then drops to low - Source: [VKiuJbhVbrk]
- Compare each output pin to find which specific line is failing - Source: [VKiuJbhVbrk]

#### Why Testers Miss This
- Chip testers don't load outputs like full system bus does - Source: [VKiuJbhVbrk]
- Marginal chip can drive light test load but not heavy bus load - Source: [VKiuJbhVbrk]
- In-circuit testing with scope shows real-world behavior - Source: [VKiuJbhVbrk]

### Rebadged 74-Series Logic ICs

#### Detection Method
- Rub chip marking with IPA (isopropyl alcohol) - Source: [VKiuJbhVbrk]
- Fake markings may dissolve revealing original underneath - Source: [VKiuJbhVbrk]
- Example: YRS-branded chips actually Motorola parts underneath - Source: [VKiuJbhVbrk]
- Rebadging happened even in 1980s, not just modern clones - Source: [VKiuJbhVbrk]

#### Rebadged Chip Quality Concerns
- May be factory rejects relabeled and sold - Source: [VKiuJbhVbrk]
- Original marking sanded off, new marking painted on - Source: [VKiuJbhVbrk]
- More likely to have marginal/weak outputs - Source: [VKiuJbhVbrk]
- Consider suspect if in area of known damage (battery leak, etc.) - Source: [VKiuJbhVbrk]

### Retro Chip Tester Professional
- Comprehensive IC tester for vintage chips - Source: [08wKjCzk_MQ]
- Website: 8bit-museum.de/rct - Source: [08wKjCzk_MQ]
- Tests DRAM, SRAM, EPROMs, and many other vintage ICs - Source: [08wKjCzk_MQ]
- Has adapter for 4116 DRAM (needs -5V and +12V) via DC-DC converter module - Source: [08wKjCzk_MQ]
- Available adapters: ZIP memory, C64 cartridges, Atari 2600 cartridges, 1702 EPROM, SIM/SIP modules - Source: [08wKjCzk_MQ]
- Available pre-assembled (~$40) or as DIY kit - Source: [08wKjCzk_MQ]

### EPROM Verification (Rebadge Detection)
- Look through EPROM window at die markings - Source: [6YU9IUAsIrE]
- Cheap USB microscopes can show manufacturer logo and part number - Source: [6YU9IUAsIrE]
- Validates chip wasn't rebadged (common from AliExpress) - Source: [6YU9IUAsIrE]
- Die markings show original manufacturer (TI logo, Fujitsu, etc.) - Source: [6YU9IUAsIrE]
- Retro Chip Tester Pro for verifying ROM chips - Source: [_0XGFz67DIc]
- 2708 EPROMs require +5V, -5V, AND +12V to read - standard programmers cannot read them - Source: [_muHEAJ7dko]
- Retro Chip Tester Pro can potentially read/write 2708s with correct add-on board - Source: [_muHEAJ7dko]
- 4164 DRAM testers available (USB powered, tests 16K/64K/256K chips) - Source: [2C3Y-3Smhz8]
- MT (Micron Technology) RAM has high failure rate vs other brands - Source: [2C3Y-3Smhz8]

### RAM Diagnostics via Screen Display
- Convert displayed garbage characters to binary to identify bad bit - Source: [2C3Y-3Smhz8]
- Compare expected value (e.g., space = 32) vs displayed value (e.g., 0 = 48) - Source: [2C3Y-3Smhz8]
- XOR the binary values to find the stuck bit - Source: [2C3Y-3Smhz8]
- Look up data bit to RAM chip mapping in schematics - Source: [2C3Y-3Smhz8]
- Flashing characters = intermittent bit failure - Source: [2C3Y-3Smhz8]
- Use C64/C128 Programmer's Reference Manual screen code tables - Source: [2C3Y-3Smhz8]

### Video Card Stuck Bit Analysis
- Systematic method for diagnosing character substitution errors - Source: [I-im7v0QVdw]
- Works for any text-mode video card (CGA, MDA, EGA, Hercules) - Source: [I-im7v0QVdw]
- Convert displayed character and expected character to binary - Source: [I-im7v0QVdw]
- XOR the two values - result shows which bit is stuck - Source: [I-im7v0QVdw]
- Confirm by testing multiple character pairs - all should show same stuck bit - Source: [I-im7v0QVdw]
- Trace data path from video RAM through latches to character generator - Source: [I-im7v0QVdw]
- 74LS273 flip-flops common failure point in data path - Source: [I-im7v0QVdw]
- Use oscilloscope to compare input vs output on suspect chips - Source: [I-im7v0QVdw]

### RAM Repair - Piggyback Method
- Place known-good chip on top of suspected bad chip - Source: [2C3Y-3Smhz8]
- If problem clears, confirms that chip is bad - Source: [2C3Y-3Smhz8]
- Good chip output drivers override stuck-high failures - Source: [2C3Y-3Smhz8]
- CRITICAL: Match pin 1 orientation exactly - Source: [2C3Y-3Smhz8]
- Creates bus conflict but TTL can pull down to override stuck high - Source: [2C3Y-3Smhz8]

### RAM Repair - No-Desolder Chip Stacking
- For 4164 DRAM: Cut only pins 2 and 14 (output pins) on old chip - Source: [2C3Y-3Smhz8]
- Solder new chip directly on top, bending pins 2 and 14 outward - Source: [2C3Y-3Smhz8]
- All other pins are inputs and can share connection - Source: [2C3Y-3Smhz8]
- Safer than desoldering for inexperienced - zero trace damage risk - Source: [2C3Y-3Smhz8]
- Use continuity tester to verify all pins connected after soldering - Source: [2C3Y-3Smhz8]
- 41256 can substitute for 4164 (pin 1 not used on 4164) - Source: [2C3Y-3Smhz8]

### XT/AT Clone RAM Troubleshooting with Schematics
- IBM 5160/5170 schematics work for most compatible clones - Source: [GMh5YUbLqLs]
- Chip designators (U1, U2, etc.) differ between IBM and clone boards - Source: [GMh5YUbLqLs]
- Use continuity tester with brush probe to find equivalent chips - Source: [GMh5YUbLqLs]
- Test from a known signal at one chip to find where it appears on clone - Source: [GMh5YUbLqLs]
- DMA refresh (DACK0) should pulse constantly during operation - Source: [GMh5YUbLqLs]
- Check DMA controller pin 25 for refresh activity - Source: [GMh5YUbLqLs]
- Compare signals between working and non-working boards of same type - Source: [GMh5YUbLqLs]
- Many signals look identical even on faulty boards (frustrating) - Source: [GMh5YUbLqLs]

### Parity Error Isolation
- Parity circuit separate from main RAM - can fail independently - Source: [GMh5YUbLqLs]
- Disable parity in BIOS to test if RAM itself is good - Source: [GMh5YUbLqLs]
- If system boots with parity disabled, suspect parity circuit/chips - Source: [GMh5YUbLqLs]
- PC Turbo BIOS (GitHub) can be modified to disable parity - Source: [GMh5YUbLqLs]
- Remove NMI handler code to fully disable parity checking - Source: [GMh5YUbLqLs]
- Some BIOSes (like "System Already") skip RAM test entirely - Source: [GMh5YUbLqLs]
- System may boot to DOS with bad RAM if tests disabled - use CheckIt to verify - Source: [GMh5YUbLqLs]

### Mac 128K/512K RAM Troubleshooting

#### Understanding the Data Path
- Video display has direct path from RAM through LS166 shift registers - Source: [IPgH8YVVye0]
- CPU access goes through LS244 buffers between RAM and data bus - Source: [IPgH8YVVye0]
- These are separate paths - one can work while other fails - Source: [IPgH8YVVye0]

#### Symptom Analysis
- Pattern on screen but no Sad Mac = CPU can't read RAM (LS244 suspect) - Source: [IPgH8YVVye0]
- Vertical lines/stripes = LS166 shift register failure - Source: [IPgH8YVVye0]
- Sad Mac with code = Specific RAM chip identified by code - Source: [IPgH8YVVye0]
- Sawtooth/checkerboard pattern = RAM writing but CPU can't read - Source: [IPgH8YVVye0]

#### Expansion Card Isolation
- Hold mouse button during power-on to disable RAM expansion cards - Source: [IPgH8YVVye0]
- Works with Maximillion and some other third-party cards - Source: [IPgH8YVVye0]
- If problem disappears, card or its RAM is suspect - Source: [IPgH8YVVye0]
- If problem remains, motherboard RAM or support chips - Source: [IPgH8YVVye0]

#### Video Without CPU
- Mac can display RAM contents even with dead CPU - Source: [IPgH8YVVye0]
- Video circuit reads RAM independently - Source: [IPgH8YVVye0]
- Useful for confirming RAM and LS166s working - Source: [IPgH8YVVye0]

### Unknown System Identification
- Check chip date codes to estimate system age - Source: [_muHEAJ7dko], [3llXvhYbryY]
- Gold ceramic packages indicate expensive/high-reliability systems - Source: [3llXvhYbryY]
- OEM part numbers (like 106966-02) help identify system origin - Source: [3llXvhYbryY]
- Look for company markings in PCB corners (often Intel, etc.) - Source: [3llXvhYbryY]
- "Scrap" markings indicate failed/rejected boards - Source: [3llXvhYbryY]
- Bodge wires common on prototype/engineering boards - Source: [3llXvhYbryY]
- Identify CPU and support chips to determine architecture - Source: [_muHEAJ7dko]
- Look for boot ROM labels (e.g., "CPM BOOT") to identify operating system - Source: [_muHEAJ7dko]
- Use riser/extender cards to work on boards outside chassis while powered - Source: [_muHEAJ7dko]
- Posts on bus connectors allow easy logic probe attachment - Source: [_muHEAJ7dko]
- Document with high-resolution photos and post to community for identification help - Source: [_muHEAJ7dko]

## Analog Signature Analysis

### Huntron Tracker
- Power-off circuit board tester using analog signature analysis - Source: [4COFqpjlGuI]
- Compares known-good board signatures against faulty boards - Source: [4COFqpjlGuI]
- Outputs precision current-limited AC sine wave to component - Source: [4COFqpjlGuI]
- Current flow = vertical trace, voltage = horizontal trace - Source: [4COFqpjlGuI]
- URL: huntron.com/products/trackers.htm - Source: [4COFqpjlGuI]

### Four Basic Analog Signatures
- Resistance: Diagonal line - Source: [4COFqpjlGuI]
- Inductance: Oblong shape (phase change) - Source: [4COFqpjlGuI]
- Capacitance: Circle/oval shape - Source: [4COFqpjlGuI]
- Semiconductor: L-shape (breakdown voltage) - Source: [4COFqpjlGuI]

### Voltage Ranges
- Older models: 10V (low), 30V (medium), 60V (high) - Source: [4COFqpjlGuI]
- Modern models have more ranges including 200mV - Source: [4COFqpjlGuI]
- Caution: Higher voltages may damage sensitive TTL logic - Source: [4COFqpjlGuI]
- Readings are peak-to-peak (10V setting = 20V p-p) - Source: [4COFqpjlGuI]

## Handheld DRAM Testers

### Simon Raybold DRAM Testers

#### Overview
- Small handheld testers for vintage DRAM chips - Source: [QljsIIPl-SE]
- STM32-based microcontroller design - Source: [QljsIIPl-SE]
- USB powered via Micro USB - Source: [QljsIIPl-SE]
- Made in England - Source: [QljsIIPl-SE]
- Available on eBay from seller "analog-kid" - Source: [QljsIIPl-SE]

#### 1-Bit DRAM Tester (Rev 6)
- Tests 4116 (16Kx1) - requires +12V/-5V generated on board - Source: [QljsIIPl-SE]
- Tests 4164 (64Kx1) - 5V only - Source: [QljsIIPl-SE]
- Tests 41256 (256Kx1) - Source: [QljsIIPl-SE]
- Tests 1Mbit x1 chips - Source: [QljsIIPl-SE]
- Tests 4108 half-good 16K chips - Source: [QljsIIPl-SE]
- Tests stacked 128Kbit chips (IBM 5170 style) - Source: [QljsIIPl-SE]
- Multiple ZIF sockets for different chip types - Source: [QljsIIPl-SE]
- LED color indicates capacity detected - Source: [QljsIIPl-SE]

#### 4-Bit DRAM Tester (Rev 2)
- Tests 4464 (64Kx4) - used in C64 shortboards - Source: [QljsIIPl-SE]
- Tests 44256 (256Kx4) - Source: [QljsIIPl-SE]
- Tests 1Mbit x4 chips - Source: [QljsIIPl-SE]
- Tests 4416 (16Kx4) - C128 video RAM - Source: [QljsIIPl-SE]
- Single ZIF socket - Source: [QljsIIPl-SE]

#### LED Status Indicators
- Blue LEDs: 16Kbit capacity (4116) - Source: [QljsIIPl-SE]
- Green LEDs: 64Kbit capacity (4164) - Source: [QljsIIPl-SE]
- Magenta/Purple LEDs: 256Kbit capacity - Source: [QljsIIPl-SE]
- Cyan LEDs: 1Mbit capacity - Source: [QljsIIPl-SE]
- Flashing LEDs: Marginal retention time - Source: [QljsIIPl-SE]
- Missing LEDs: Failed blocks - Source: [QljsIIPl-SE]

#### Test Algorithm
- High-speed fill with zeros and ones - Source: [QljsIIPl-SE]
- Hash pattern tests (odd/even) - Source: [QljsIIPl-SE]
- Random data fill and verify (multiple passes) - Source: [QljsIIPl-SE]
- Does NOT perform March test - Source: [QljsIIPl-SE]
- Repeated random tests may miss some failures March would catch - Source: [QljsIIPl-SE]

#### Caveats
- CMOS microcontroller driving TTL DRAM chips - Source: [QljsIIPl-SE]
- Threshold voltage differences can cause false failures - Source: [QljsIIPl-SE]
- Chip may test "bad" but work in real TTL computer - Source: [QljsIIPl-SE]
- Same issue affects Retro Chip Tester Pro - Source: [QljsIIPl-SE]
- Only definitive test is real Z80/6502 system with March test ROM - Source: [QljsIIPl-SE]

## Soldering Iron Heat Test for Bad Capacitors

### Overview
- Heat individual caps while observing circuit behavior - Source: [TDV9ima4dbA]
- Bad caps behave differently when warmed - Source: [TDV9ima4dbA]
- Quick way to identify faulty cap without removing components - Source: [TDV9ima4dbA]
- Useful when caps test OK on meter but fail in circuit - Source: [TDV9ima4dbA]

### Procedure
- Power up circuit with known fault symptom visible - Source: [TDV9ima4dbA]
- Touch soldering iron tip briefly to each suspect cap - Source: [TDV9ima4dbA]
- Watch for changes in circuit behavior - Source: [TDV9ima4dbA]
- Cap that makes problem WORSE when heated is likely bad - Source: [TDV9ima4dbA]
- Heat changes ESR and capacitance of failing cap - Source: [TDV9ima4dbA]

### Application: Vertical Deflection Fold-Over
- Image wraps around at bottom of screen - Source: [TDV9ima4dbA]
- Heat caps in vertical section one at a time - Source: [TDV9ima4dbA]
- Cap that causes deflection to worsen when heated is faulty - Source: [TDV9ima4dbA]
- Often a small electrolytic (22µF 6.3V typical) - Source: [TDV9ima4dbA]
- May test OK on LCR meter but have high ESR - Source: [TDV9ima4dbA]

### Cautions
- Don't overheat components - brief touch only - Source: [TDV9ima4dbA]
- Hot air gun less precise, iron better for targeting - Source: [TDV9ima4dbA]
- Be careful around high voltage sections - Source: [TDV9ima4dbA]
- Works best on analog circuits (deflection, audio, power supply) - Source: [TDV9ima4dbA]

## Horizontal Output Transistor Breakdown Testing

### Voltage-Dependent Failure Mode
- Transistor tests OK with multimeter but shorts under operating voltage - Source: [t9bs3i2-5Kc]
- Diode check shows normal 0.4V collector-base/emitter readings - Source: [t9bs3i2-5Kc]
- Breaks down when B+ voltage applied (96-120V typical) - Source: [t9bs3i2-5Kc]
- Creates dead short, causing power supply to go into protection - Source: [t9bs3i2-5Kc]
- Returns to "normal" readings when voltage removed - Source: [t9bs3i2-5Kc]
- Very difficult failure to diagnose with standard multimeter - Source: [t9bs3i2-5Kc]

### Diagnosis Method
- Feed limited current (1-3A) into B+ rail with bench supply - Source: [t9bs3i2-5Kc]
- Use thermal camera to observe what heats up - Source: [t9bs3i2-5Kc]
- Faulty transistor heats up immediately when base drive applied - Source: [t9bs3i2-5Kc]
- Heat sink around horizontal output gets hot rapidly - Source: [t9bs3i2-5Kc]
- Compare working board to faulty board at same voltage - Source: [t9bs3i2-5Kc]

### Symptoms Leading to This Fault
- SMPS clicks repeatedly trying to start (protection mode) - Source: [t9bs3i2-5Kc]
- B+ voltage present on primary but not secondary caps - Source: [t9bs3i2-5Kc]
- Lifting inductor that feeds flyback allows SMPS to run normally - Source: [t9bs3i2-5Kc]
- Short returns when voltage ramped up (voltage-dependent breakdown) - Source: [t9bs3i2-5Kc]

### Related Failure: Flyback False Positive
- Flyback may appear shorted on thermal camera - Source: [t9bs3i2-5Kc]
- Actually shunting current through from failed transistor - Source: [t9bs3i2-5Kc]
- Isolate flyback vs transistor by lifting connections - Source: [t9bs3i2-5Kc]
- Test both individually with bench supply before condemning flyback - Source: [t9bs3i2-5Kc]

## RF Signal Generator Testing

### Sencore VG91 Universal Video Generator

#### Overview
- RF test signal generator for TV testing - Source: [yswPAx7YWv4]
- Can output any RF channel (broadcast or cable) - Source: [yswPAx7YWv4]
- Generates test patterns (color bars, grayscale stair-step) - Source: [yswPAx7YWv4]
- Also outputs composite video - Source: [yswPAx7YWv4]

#### RF Output Capabilities
- Outputs any VHF channel (2-13) - Source: [yswPAx7YWv4]
- Outputs any UHF channel (14-83) - Source: [yswPAx7YWv4]
- Outputs cable TV channels - Source: [yswPAx7YWv4]
- Variable RF signal strength (dB adjustable) - Source: [yswPAx7YWv4]
- BNC output connector - Source: [yswPAx7YWv4]

#### IF Signal Output
- Can output intermediate frequencies for tuner bypass - Source: [yswPAx7YWv4]
- Useful when tuner is bad but rest of TV works - Source: [yswPAx7YWv4]
- Allows testing TV sections independently - Source: [yswPAx7YWv4]

#### Audio Features
- Test tones for sound testing - Source: [yswPAx7YWv4]
- Stereo audio output capability - Source: [yswPAx7YWv4]

#### Connection to 300 Ohm TVs
- Use 75 ohm to 300 ohm balun - Source: [yswPAx7YWv4]
- Balun converts coax output to twin lead - Source: [yswPAx7YWv4]
- Required for older TVs with twin lead inputs only - Source: [yswPAx7YWv4]

#### Diagnostic Use Cases
- Testing VHF tuner band sensitivity - Source: [yswPAx7YWv4]
- Comparing low band vs high band reception - Source: [yswPAx7YWv4]
- VHF low band: Channels 2-6 - Source: [yswPAx7YWv4]
- VHF high band: Channels 7-13 - Source: [yswPAx7YWv4]
- Isolating tuner faults to specific frequency range - Source: [yswPAx7YWv4]
- Safe to use with hot chassis TVs (RF isolated) - Source: [yswPAx7YWv4]

## Shorted Tantalum Capacitor Diagnosis

### Common Failure Mode
- 16V tantalums on 12V rail often fail short over time - Source: [h9fFt7t12j4], [LP0S9PZTb4w]
- Insufficient voltage headroom between operating and rated voltage - Source: [h9fFt7t12j4]
- Very common on 386/486-era motherboards - Source: [h9fFt7t12j4]
- Also found on PC/XT and AT-class machines - Source: [LP0S9PZTb4w]
- Can fail sequentially - fix one, another shorts - Source: [h9fFt7t12j4]
- Tantalums near power input header are prime suspects - Source: [LP0S9PZTb4w]

### Symptoms
- Power supply won't start or clicks - Source: [h9fFt7t12j4]
- Power supply starts then shuts down immediately - Source: [h9fFt7t12j4]
- ATX PSU protection circuit triggers - Source: [h9fFt7t12j4]

### Diagnosis Method
1. Identify which rail is shorted (usually 12V) - Source: [h9fFt7t12j4]
2. Use multimeter continuity: check power connector pins to ground - Source: [h9fFt7t12j4]
3. Dead short to ground = shorted component - Source: [h9fFt7t12j4]

### Thermal Camera Method
- Feed limited current (150-500mA) into shorted rail - Source: [h9fFt7t12j4]
- Use bench power supply with current limiting - Source: [h9fFt7t12j4]
- View board with thermal camera (Topdon TC 004 or similar) - Source: [h9fFt7t12j4]
- Shorted component heats up and becomes visible - Source: [h9fFt7t12j4]
- 12V @ 500mA generates enough heat to identify fault - Source: [h9fFt7t12j4]

### Repair
- Remove shorted tantalum capacitor - Source: [h9fFt7t12j4]
- Replace with 25V or 50V electrolytic for margin - Source: [h9fFt7t12j4]
- 12V rail caps are not critical - can omit entirely - Source: [h9fFt7t12j4]
- 12V rail only powers ISA bus devices - Source: [h9fFt7t12j4]
- Test for more shorts before powering up - Source: [h9fFt7t12j4]
