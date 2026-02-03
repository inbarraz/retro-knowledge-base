# IBM

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| PC (5150) | Desktop Computer | [noRZC9y9Uz0] |
| PC Convertible (5140) | Laptop | [gNbM0UzWrnQ] |
| PCjr | Desktop Computer | [_MljEAIpQ8g] |
| PCjr Monitor | CRT Monitor | [_MljEAIpQ8g] |
| PC/XT (5160) | Desktop Computer | [0u6I_VAO22A], [LP0S9PZTb4w] |
| CGA Card | Video Card | [0WMTYZ60OvE] |
| 5154 EGA Monitor | CRT Monitor | [7EezG5OzSQo] |
| 386DX Clone | Desktop Computer | [5Gfr6lW49aI], [noRZC9y9Uz0] |
| 386SX Clone (Zeos) | Desktop Computer | [h9fFt7t12j4] |
| 286 Clone Motherboards | Desktop Computer | [hStIrdagIJs], [ckTx8G3JImI] |

## Platform-Specific Knowledge

### IBM 5150 (Original PC)

#### Overview
- Original IBM Personal Computer released August 1981 - Source: [noRZC9y9Uz0]
- 8088 CPU at 4.77MHz, same as XT - Source: [noRZC9y9Uz0]
- 5 ISA expansion slots (vs 8 on XT) - Source: [noRZC9y9Uz0]
- Early versions: 16K to 64K RAM on motherboard - Source: [noRZC9y9Uz0]
- Later versions: 64K to 256K RAM on motherboard - Source: [noRZC9y9Uz0]

#### Timeline Context
- Released August 1981 - Source: [noRZC9y9Uz0]
- PC XT released March 1983 - Source: [noRZC9y9Uz0]
- Both PC and XT sold concurrently until April 1987 - Source: [noRZC9y9Uz0]
- April 1987: IBM discontinued entire product range (PC, XT, AT) for PS/2 line - Source: [noRZC9y9Uz0]

#### Common Component Pillaging
- 82284 clock generator chip commonly stolen from 5150 motherboards - Source: [noRZC9y9Uz0]
- PC Sprint accelerator plugs into 82284 socket - boards with accelerators often have chip left on accelerator board - Source: [noRZC9y9Uz0]
- 8288 bus controller usually soldered (not stolen) - Source: [noRZC9y9Uz0]
- Can borrow 82284 from XT clone motherboard for testing - Source: [noRZC9y9Uz0]

#### Pre-Power Diagnostics
- Check tantalum capacitors for shorts before applying power - Source: [noRZC9y9Uz0]
- Measure resistance between 5V (red wire) and ground (black wire) - Source: [noRZC9y9Uz0]
- 14 ohms or higher is normal; 0-1 ohm indicates short - Source: [noRZC9y9Uz0]
- Check 12V rail similarly (higher resistance expected, ~89 ohms typical) - Source: [noRZC9y9Uz0]
- Flip board over and check across individual tantalum caps - Source: [noRZC9y9Uz0]
- Tantalum shorts are "super common" on these boards - Source: [noRZC9y9Uz0]

#### Ready Light Indicator
- 5150 has "READY" light on motherboard - Source: [noRZC9y9Uz0]
- Should illuminate when system exits reset state - Source: [noRZC9y9Uz0]
- No ready light = system not starting properly - Source: [noRZC9y9Uz0]
- Ready light with no POST = CPU or clock issues - Source: [noRZC9y9Uz0]

#### Troubleshooting Dead 5150
- Missing ready light indicates system stuck in reset or not starting - Source: [noRZC9y9Uz0]
- Buzzing noise with no activity = fundamental fault - Source: [noRZC9y9Uz0]
- CPU swap test: use known-good 8088 from another board - Source: [noRZC9y9Uz0]
- Bank 0 RAM is soldered - must work for any POST - Source: [noRZC9y9Uz0]
- Upper RAM banks can be removed for testing - Source: [noRZC9y9Uz0]

### IBM 5160 (PC/XT)

#### Overview
- IBM's first PC with standard hard drive option - Source: [LP0S9PZTb4w]
- 8088 processor at 4.77MHz - Source: [LP0S9PZTb4w]
- 256KB to 640KB RAM depending on configuration - Source: [LP0S9PZTb4w]

#### Auxiliary Power Supply (Everex Micro Pack 1)
- Third-party auxiliary PSU for PC/XT - Source: [LP0S9PZTb4w]
- Adds extra power capacity for hard drives, tape drives, expansion cards - Source: [LP0S9PZTb4w]
- Mounts in 5.25" drive bay - Source: [LP0S9PZTb4w]
- Provides additional 12V and 5V power via pass-through cables - Source: [LP0S9PZTb4w]
- Useful when original PSU can't handle all peripherals - Source: [LP0S9PZTb4w]
- Tape drives particularly power-hungry, often needed aux PSU - Source: [LP0S9PZTb4w]

#### Tape Drive Support
- Teac MT-2ST tape drive commonly used in XT systems - Source: [LP0S9PZTb4w]
- Archive/QIC format tape cartridges - Source: [LP0S9PZTb4w]
- Used for backup before hard drives were affordable - Source: [LP0S9PZTb4w]
- Tape controller card required (not standard equipment) - Source: [LP0S9PZTb4w]

#### Hard Drive (Seagate ST-225)
- 20MB MFM hard drive, extremely common in PC/XT era - Source: [LP0S9PZTb4w]
- Full-height 5.25" form factor - Source: [LP0S9PZTb4w]
- Requires MFM controller card - Source: [LP0S9PZTb4w]
- Often found still working after 35+ years - Source: [LP0S9PZTb4w]

#### VARTA Battery Issues
- VARTA NiCad batteries on clock cards often leak - Source: [LP0S9PZTb4w]
- PC/XT clock not on motherboard - separate ISA card - Source: [LP0S9PZTb4w]
- Some VARTA batteries survive decades without leaking (rare) - Source: [LP0S9PZTb4w]
- Always inspect for corrosion even if battery looks OK - Source: [LP0S9PZTb4w]
- Replace with CR2032 holder or Dallas replacement module - Source: [LP0S9PZTb4w]

#### RAM Troubleshooting (Bank Swapping Method)

##### Overview
- PC/XT uses 4164 (64K x 1-bit) DRAM chips, 9 per bank - Source: [LP0S9PZTb4w]
- Bank 0: Lower 64K (required for boot) - Source: [LP0S9PZTb4w]
- Additional banks for 128K, 256K, 640K configurations - Source: [LP0S9PZTb4w]

##### Bank Swap Technique
- If RAM test fails in one bank, swap entire bank to known-good location - Source: [LP0S9PZTb4w]
- If problem follows the chips, one chip in that bank is bad - Source: [LP0S9PZTb4w]
- If problem stays in same bank position, motherboard issue - Source: [LP0S9PZTb4w]
- Swap individual chips within bank to isolate failing chip - Source: [LP0S9PZTb4w]
- Use chip tester to confirm which chip failed - Source: [LP0S9PZTb4w]

##### RAM Chip Reliability by Manufacturer
- MOS Technology (MOS) chips: Higher failure rate, especially in hot locations - Source: [LP0S9PZTb4w]
- Toshiba chips: Generally reliable, good longevity - Source: [LP0S9PZTb4w]
- Samsung chips: Generally reliable - Source: [LP0S9PZTb4w]
- NEC chips: Generally reliable - Source: [LP0S9PZTb4w]
- Lower RAM banks run hotter (Bank 0 has most memory access) - Source: [LP0S9PZTb4w]
- Consider replacing MOS chips proactively if other brands available - Source: [LP0S9PZTb4w]

#### Software Found on PC/XT Systems

##### QA Database (Symantec, 1986)
- Early database software for DOS - Source: [LP0S9PZTb4w]
- Symantec before they became antivirus company - Source: [LP0S9PZTb4w]
- Menu-driven interface, predates GUI era - Source: [LP0S9PZTb4w]

##### First Publisher
- Early desktop publishing software - Source: [LP0S9PZTb4w]
- WYSIWYG editing for newsletters, flyers - Source: [LP0S9PZTb4w]
- Required at least 512KB RAM - Source: [LP0S9PZTb4w]

##### Print Shop (Broderbund)
- Banner and sign printing software - Source: [LP0S9PZTb4w]
- Works with Hercules monochrome graphics - Source: [LP0S9PZTb4w]
- Very popular in schools and home offices - Source: [LP0S9PZTb4w]

### IBM 5170 (PC/AT)

#### Overclocking Type-1 Motherboards
- Type-1 motherboards run at 6MHz stock (12MHz crystal divided by 2) - Source: [81ezGc1Eb1M]
- Crystal oscillator is socketed - can swap for higher frequencies - Source: [81ezGc1Eb1M]
- 16MHz crystal = 8MHz CPU speed (successful) - Source: [81ezGc1Eb1M]
- 20MHz crystal = 10MHz CPU speed (achieved with BIOS patch) - Source: [81ezGc1Eb1M]
- 24MHz crystal = 12MHz (unstable, would not POST reliably) - Source: [81ezGc1Eb1M]
- 17.7MHz PAL crystal = 8.8MHz (good compromise speed) - Source: [81ezGc1Eb1M]

#### Type-3 BIOS Speed Check
- IBM added anti-overclocking code in Type-3 BIOS - Source: [81ezGc1Eb1M]
- Checks for >5% overclock and halts at POST code 11 - Source: [81ezGc1Eb1M]
- Also checks for >10% underclock - Source: [81ezGc1Eb1M]
- Stuart's patched BIOS removes speed check entirely - Source: [81ezGc1Eb1M]
- Download: archive.org/details/ibm-5170-type-3-bios-cover - Source: [81ezGc1Eb1M]

#### CPU Upgrade for Overclocking
- Original ceramic CPU rated for 6MHz only - Source: [81ezGc1Eb1M]
- Can push PLCC socket into existing DIP socket (no soldering) - Source: [81ezGc1Eb1M]
- Harris 286 rated 20MHz runs cool even at 10MHz - Source: [81ezGc1Eb1M]
- AMD 286-12 gets very hot at 10MHz, needs heatsink - Source: [81ezGc1Eb1M]
- Performance scaling is linear - no clock dividers on 5170 - Source: [81ezGc1Eb1M]

#### ISA Bus Overclocking
- ISA bus runs at CPU speed on 5170 (not divided) - Source: [81ezGc1Eb1M]
- At 10MHz CPU, ISA also runs 10MHz (25% over 8MHz spec) - Source: [81ezGc1Eb1M]
- Most cards tolerate this overclocking - Source: [81ezGc1Eb1M]
- Later AT clones divided clock to keep ISA at 8MHz - Source: [81ezGc1Eb1M]

#### EPROM Speed for Overclocking
- Original ROMs likely 200ns - adequate for 6-8MHz - Source: [81ezGc1Eb1M]
- Use 120ns EPROMs for 10MHz operation - Source: [81ezGc1Eb1M]

#### RAM Thermal Considerations
- Bank 0 (lower 256K) runs hottest - most memory access there - Source: [81ezGc1Eb1M]
- Original 200ns RAM works at 10MHz but outside spec - Source: [81ezGc1Eb1M]
- Heatsinks on warm chips only useful with case airflow - Source: [81ezGc1Eb1M]

#### Known Instability Signs
- POST error 108 with code 29 hex = timer B check failure - Source: [81ezGc1Eb1M]
- May appear only after machine runs warm for a while - Source: [81ezGc1Eb1M]
- Power cycling often clears error - Source: [81ezGc1Eb1M]
- Random lockups indicate ragged edge of stability - Source: [81ezGc1Eb1M]

#### NecroWare Clock Chip Replacement

##### Overview
- Replaces original MC146818 (Motorola) RTC/NVRAM chip - Source: [xJYnbZY8t1E]
- Open source replacement module with own battery and crystal - Source: [xJYnbZY8t1E]
- Dallas DS1287 compatible replacement - Source: [xJYnbZY8t1E]
- Does not rely on motherboard battery circuit - Source: [xJYnbZY8t1E]
- Battery life expected 10+ years vs 1 year with CR2032 on original - Source: [xJYnbZY8t1E]

##### Original Clock Chip Problems
- Type-1 motherboards have clock chip soldered (not socketed) - Source: [xJYnbZY8t1E]
- Original design used 4x AA batteries - prone to leaking - Source: [xJYnbZY8t1E]
- CR2032 replacement only lasts about 1 year - Source: [xJYnbZY8t1E]
- Original circuit powers both NVRAM and crystal oscillator buffer chip - Source: [xJYnbZY8t1E]
- High standby current drain depletes CR2032 quickly - Source: [xJYnbZY8t1E]

##### Intel vs Motorola Mode
- MC146818 and Dallas DS1287 support both Intel and Motorola modes - Source: [xJYnbZY8t1E]
- IBM 5170 uses Motorola mode - Source: [xJYnbZY8t1E]
- NecroWare module defaults to Intel mode (wrong for 5170) - Source: [xJYnbZY8t1E]
- Pin 1 must be pulled up to 5V (via 10K resistor) for Motorola mode - Source: [xJYnbZY8t1E]
- Pin 1 not connected on original Motorola chip (NC) - Source: [xJYnbZY8t1E]
- Wrong mode causes "system board error" at POST - Source: [xJYnbZY8t1E]
- Same issue encountered on BBC Master (also uses Motorola mode) - Source: [xJYnbZY8t1E]

##### Installation
- Desolder original chip and install DIP socket - Source: [xJYnbZY8t1E]
- Note any bodge wires connected to original chip before removal - Source: [xJYnbZY8t1E]
- Restore bodge wires to socket after installation - Source: [xJYnbZY8t1E]
- Insert NecroWare module into socket - Source: [xJYnbZY8t1E]
- System will not POST at all without clock chip installed - Source: [xJYnbZY8t1E]

#### Extended Memory Configuration (G Setup)

##### Common Mistake
- Extended memory size must match actual hardware configuration - Source: [xJYnbZY8t1E]
- RAM expansion cards may add base memory (128K) plus extended - Source: [xJYnbZY8t1E]
- Must calculate: (Total RAM) - 640K = Extended memory value - Source: [xJYnbZY8t1E]
- Wrong setting causes "memory size error" and possible system freeze - Source: [xJYnbZY8t1E]

##### Example Calculation
- 512K motherboard + 3072K expansion card = 3584K total - Source: [xJYnbZY8t1E]
- If card adds 128K to base memory: base = 640K - Source: [xJYnbZY8t1E]
- Extended memory = 3584K - 640K = 2944K - Source: [xJYnbZY8t1E]
- Enter 640 in base memory field, 2944 in expansion memory field - Source: [xJYnbZY8t1E]

#### BIOS Patching for IDE Support

##### The Problem
- Original IBM BIOS expects MFM controller timing - Source: [xJYnbZY8t1E]
- IDE controllers respond too quickly - Source: [xJYnbZY8t1E]
- System hangs on IDE hard drive access with stock BIOS - Source: [xJYnbZY8t1E]

##### Solutions
- Replace with AMI BIOS (loses IBM authenticity) - Source: [xJYnbZY8t1E]
- Use patched IBM BIOS from GitHub - Source: [xJYnbZY8t1E]
- Patched BIOS fixes timing and adds Type 47 (504MB support) - Source: [xJYnbZY8t1E]
- Original BIOS only has fixed hard drive types (limited sizes) - Source: [xJYnbZY8t1E]

### IBM PC Convertible (5140)

#### Overview
- First IBM laptop computer - Source: [gNbM0UzWrnQ]
- Proprietary expansion system (not standard ISA) - Source: [gNbM0UzWrnQ]
- External sidecar expansion modules available - Source: [gNbM0UzWrnQ]
- Runs DOS applications on battery power - Source: [gNbM0UzWrnQ]
- Historical significance as IBM's entry into portable computing - Source: [gNbM0UzWrnQ]

#### Expansion Options
- CGA adapter modules available - Source: [gNbM0UzWrnQ]
- Printer adapter expansion - Source: [gNbM0UzWrnQ]
- Parallel port expansion available - Source: [gNbM0UzWrnQ]
- Modules connect via sidecar connector on side of unit - Source: [gNbM0UzWrnQ]

### IBM PCjr

#### Keyboard (Later Model)
- Non-chiclet keyboard version feels better than original chiclet - Source: [TaHKjittUNI]
- Still not a great feeling keyboard (all PCjr keyboards feel crappy) - Source: [TaHKjittUNI]
- Uses infrared wireless communication - Source: [TaHKjittUNI]
- Batteries in keyboard for wireless operation - Source: [TaHKjittUNI]
- Can find new old stock units that were never used - Source: [TaHKjittUNI]

#### Keyboard Cable
- Keyboard connector looks like phone jack but is NOT standard phone cable - Source: [TaHKjittUNI]
- RJ45 on one end, square DIN on computer end - Source: [TaHKjittUNI]
- Using wrong cable may not damage PCjr (unlike Macintosh) - Source: [TaHKjittUNI]
- Cable was originally for wired PCjr keyboard option - Source: [TaHKjittUNI]

#### Reset Button Modification
- Adding reset button to PCjr requires drilling hole somewhere - Source: [-9Ae-Lbz8AA]
- Cartridge slot is one option but prevents cartridge use - Source: [-9Ae-Lbz8AA]
- 3D printed rear plate with Pico ATX input could accommodate reset button - Source: [-9Ae-Lbz8AA]
- PCjr community has opinions on proper reset button placement - Source: [-9Ae-Lbz8AA]

#### Monitor
- PCjr monitor is OEM'd by Mitsubishi, based on Mitsubishi AT-13332A - Source: [_MljEAIpQ8g]
- Differences from AT-13332A: Top ventilation, built-in speaker, larger bezel, volume control instead of H-center - Source: [_MljEAIpQ8g]
- Proprietary connector carries audio/video (not standard DE-9) - Source: [_MljEAIpQ8g]
- Internal construction likely very similar to Mitsubishi AT-13332A - Source: [_MljEAIpQ8g]

## CGA Standard Notes

### Digital TTL Monitors
- CGA is a digital TTL standard: 5V or 0V signals - Source: [_MljEAIpQ8g]
- Not analog RGB - signals are digital - Source: [_MljEAIpQ8g]
- DE-9 connector typically used for CGA - Source: [_MljEAIpQ8g]

### Brown Color Handling
- Correct CGA monitors display brown (not dark yellow) for the "brown" color - Source: [_MljEAIpQ8g]
- This distinguishes from monitors that incorrectly show dark yellow - Source: [_MljEAIpQ8g]

### Testing
- Jim Leonard's CGA Compatibility Suite useful for testing CGA monitors - Source: [_MljEAIpQ8g]
- Has modern calibration test pattern - Source: [_MljEAIpQ8g]

## Related Hardware

### VTech CGA Card
- Hidden jumper enables Plantronics 16-color mode - Source: [_MljEAIpQ8g]
- Supports 16 colors on regular CGA adapter using Tandy-style graphics - Source: [_MljEAIpQ8g]

### Planet X3
- Game that supports Plantronics 16-color mode on CGA - Source: [_MljEAIpQ8g]

### Modern CGA Card Clone (AliExpress CPLD-based)

#### Overview
- Modern reproduction CGA card using CPLDs to replicate TTL logic - Source: [xWDg10gnuVI]
- Available on AliExpress for approximately $32 - Source: [xWDg10gnuVI]
- Exact functional replica of IBM CGA card including the snow issue - Source: [xWDg10gnuVI]
- Uses 6845 CRT controller like original IBM card - Source: [xWDg10gnuVI]
- SRAM chips (512K) used instead of original DRAM - Source: [xWDg10gnuVI]
- Dual-port SRAM to handle video RAM contention - Source: [xWDg10gnuVI]

#### Key Characteristics
- Deliberately replicates CGA snow (exact IBM behavior) - Source: [xWDg10gnuVI]
- Functions identically to original IBM CGA for compatibility testing - Source: [xWDg10gnuVI]
- Good for testing software that requires exact IBM CGA behavior - Source: [xWDg10gnuVI]
- Much cheaper than finding original IBM CGA cards - Source: [xWDg10gnuVI]

### IBM CGA Card

#### Specifications
- 16KB video RAM - Source: [0WMTYZ60OvE]
- 6845 CRTC controller chip - Source: [0WMTYZ60OvE], [Ll3Zp3kr8l4]
- Digital TTL RGB output (16 colors in text, 4 colors in graphics) - Source: [0WMTYZ60OvE]
- Composite video output with artifact color support (16 colors like Apple II) - Source: [0WMTYZ60OvE]
- Character ROM on card - Source: [0WMTYZ60OvE]
- Control code in motherboard BIOS, not on card ROM - Source: [0WMTYZ60OvE]

#### CGA Snow

##### Cause
- Snow appears in 80-column text mode when CPU reads/writes video RAM during screen refresh - Source: [0WMTYZ60OvE], [Ll3Zp3kr8l4]
- Video RAM is dual-ported but arbitration causes visible artifacts - Source: [Ll3Zp3kr8l4]
- CPU and 6845 CRTC compete for RAM access - Source: [Ll3Zp3kr8l4]
- No snow in 40-column mode (less bandwidth needed) or graphics modes - Source: [0WMTYZ60OvE], [Ll3Zp3kr8l4]
- Later CGA cards eliminated snow, but IBM original has it - Source: [0WMTYZ60OvE]

##### BIOS Snow Mitigation
- BIOS flashing routine hides snow but causes visible blanking - Source: [0WMTYZ60OvE], [Ll3Zp3kr8l4]
- BIOS disables display during scroll operations - Source: [Ll3Zp3kr8l4]
- Screen blanks briefly, then displays new content - Source: [Ll3Zp3kr8l4]
- Visually distracting but eliminates snow artifacts - Source: [Ll3Zp3kr8l4]

##### Software Snow Mitigation
- ZANSI.SYS: ANSI driver that waits for horizontal retrace before writes - Source: [Ll3Zp3kr8l4]
- Quick CRT: TSR that uses same retrace-wait technique - Source: [Ll3Zp3kr8l4]
- Nancy driver: Similar approach to ZANSI.SYS - Source: [Ll3Zp3kr8l4]
- Software mitigation slower than hardware but no screen blanking - Source: [Ll3Zp3kr8l4]

#### Hardware Modifications

##### Key Chips for Mods
- U24: 74LS244 octal buffer - controls display enable signal - Source: [Ll3Zp3kr8l4]
- U40: 74LS174 hex D flip-flop - display timing - Source: [Ll3Zp3kr8l4]
- 6845 CRTC: Pin 18 is display enable output - Source: [Ll3Zp3kr8l4]
- Character ROM at position for font data - Source: [Ll3Zp3kr8l4]

##### Speed-Up Mod (Disable Screen Blanking)

###### Purpose
- Eliminates BIOS-caused screen blanking during scroll - Source: [Ll3Zp3kr8l4]
- Allows snow but no more black flash during scrolling - Source: [Ll3Zp3kr8l4]
- Useful if you prefer snow over blanking - Source: [Ll3Zp3kr8l4]

###### Implementation
- 74LS244 (U24) pin 17 receives display enable from 6845 - Source: [Ll3Zp3kr8l4]
- Cut the trace to pin 17 of U24 - Source: [Ll3Zp3kr8l4]
- Connect pin 17 to ground (always enabled) - Source: [Ll3Zp3kr8l4]
- Display will no longer blank when software requests it - Source: [Ll3Zp3kr8l4]
- Results: Fast scrolling with snow, no blanking - Source: [Ll3Zp3kr8l4]

###### How It Works
- 6845 CRTC pin 18 outputs display enable signal - Source: [Ll3Zp3kr8l4]
- Signal routes through LS244 buffer to display circuitry - Source: [Ll3Zp3kr8l4]
- BIOS sets mode register to disable display during updates - Source: [Ll3Zp3kr8l4]
- Grounding LS244 input overrides this, display always on - Source: [Ll3Zp3kr8l4]

##### Character Font Mod (Thin vs Thick)

###### Purpose
- Toggle between single-width and double-width character font - Source: [Ll3Zp3kr8l4]
- Thin font: Single pixel wide strokes (more readable to some) - Source: [Ll3Zp3kr8l4]
- Thick font: Double pixel wide strokes (default IBM style) - Source: [Ll3Zp3kr8l4]

###### Implementation - Basic Toggle
- P3 jumper position selects font width - Source: [Ll3Zp3kr8l4]
- Wire switch to P3 pins for manual toggle - Source: [Ll3Zp3kr8l4]
- Can use SPDT switch for instant font change - Source: [Ll3Zp3kr8l4]

###### Implementation - Bold-on-Blink Mod
- Connect P3 to blink attribute signal - Source: [Ll3Zp3kr8l4]
- Blink attribute bit becomes "bold" instead - Source: [Ll3Zp3kr8l4]
- Text with blink attribute shows thick font - Source: [Ll3Zp3kr8l4]
- Non-blinking text shows thin font - Source: [Ll3Zp3kr8l4]
- Creative reuse of blink bit for bold effect - Source: [Ll3Zp3kr8l4]

###### Character ROM Note
- Both font styles stored in same character ROM - Source: [Ll3Zp3kr8l4]
- P3 selects which font data to use - Source: [Ll3Zp3kr8l4]
- No ROM replacement needed for this mod - Source: [Ll3Zp3kr8l4]

##### Status Register Mod

###### Purpose
- Trick software into thinking it's always safe to write - Source: [Ll3Zp3kr8l4]
- Forces status register bit to indicate retrace active - Source: [Ll3Zp3kr8l4]
- Combined with speed-up mod eliminates all retrace waiting - Source: [Ll3Zp3kr8l4]

###### Implementation
- Status register at port 3DAh returns vertical/horizontal retrace status - Source: [Ll3Zp3kr8l4]
- Software waits for retrace bit before writing to avoid snow - Source: [Ll3Zp3kr8l4]
- Forcing bit high makes software think retrace is always occurring - Source: [Ll3Zp3kr8l4]
- Software proceeds immediately without waiting - Source: [Ll3Zp3kr8l4]

###### Warning
- Some software may break if status register is not accurate - Source: [Ll3Zp3kr8l4]
- Games using raster effects need accurate status - Source: [Ll3Zp3kr8l4]
- Best used in combination with display enable mod - Source: [Ll3Zp3kr8l4]

#### Testing
- CheckIt: RAM test for 16KB video memory - Source: [0WMTYZ60OvE]
- Jim Leonard's CGA Compatibility Suite: Various compatibility tests - Source: [0WMTYZ60OvE]
- Area 5150 demo: Ultimate stress test for CGA compatibility (cycle-exact timing) - Source: [0WMTYZ60OvE]
- Area 5150 requires 4.77MHz 8088 CPU and genuine IBM CGA card - Source: [0WMTYZ60OvE]

#### 6845 CRTC Details
- MC6845 or compatible (UM6845, HD6845) - Source: [Ll3Zp3kr8l4]
- Pin 18: Display Enable (active high) - Source: [Ll3Zp3kr8l4]
- Directly controls whether video is output to monitor - Source: [Ll3Zp3kr8l4]
- Software can control via mode register writes - Source: [Ll3Zp3kr8l4]
- Generates horizontal and vertical timing signals - Source: [Ll3Zp3kr8l4]

### IBM PC/XT Overclocking

#### PC Sprint Board
- Open source project for overclocking 5150/5160/clones - Source: [0u6I_VAO22A]
- Replaces clock generator chip with switchable dual-crystal design - Source: [0u6I_VAO22A]
- Stock crystal: 22.11MHz = 7.37MHz CPU (64% faster) - Source: [0u6I_VAO22A]
- Can use higher crystals: 36MHz achieved 11MHz CPU speed on clone board - Source: [0u6I_VAO22A]
- Original IBM chips rated for ~5MHz, clones often handle higher - Source: [0u6I_VAO22A]
- Provides jumper for turbo/normal speed switching - Source: [0u6I_VAO22A]
- Extra pins for reset button (original PC had no reset) - Source: [0u6I_VAO22A]
- GitHub: github.com/reeshub/pc-sprint - Source: [0u6I_VAO22A]

#### PC Sprint Assembly Notes
- Reasonably straightforward kit assembly - Source: [GUvasXbxUPg]
- Requires soldering skills for through-hole components - Source: [GUvasXbxUPg]
- Crystals and jumper headers included in kit - Source: [GUvasXbxUPg]
- Installation requires removing original clock chip - Source: [GUvasXbxUPg]
- Socket original chip location, plug PC Sprint into socket - Source: [GUvasXbxUPg]
- Turbo switch wires can route to front panel - Source: [GUvasXbxUPg]

### 386DX Motherboards (Clones)

#### MTI 386 (Made in USA)
- Texas Instruments chipset (unusual - TI made 386 chipsets) - Source: [5Gfr6lW49aI]
- Built-in multi-I/O (IDE, floppy, 2x serial, parallel) - Source: [5Gfr6lW49aI]
- 64KB cache memory (8K chips x 8) - Source: [5Gfr6lW49aI]
- Max 32MB RAM via 30-pin SIMMs - Source: [5Gfr6lW49aI]
- Uses external battery pack (not leaky onboard NiCad) - Source: [5Gfr6lW49aI]
- MYX Corporation BIOS with animated POST display - Source: [5Gfr6lW49aI]

#### 386DX Survival
- Many 386DX boards destroyed by leaky NiCad batteries - Source: [5Gfr6lW49aI]
- Boards with external battery packs survived better - Source: [5Gfr6lW49aI]
- Original IBM AT used external battery pack - Source: [5Gfr6lW49aI]

#### BIOS Dumping (DOS)
- ROM Dumper utility by Jim Leonard - Source: [5Gfr6lW49aI]
- Works on old systems where BIOS is directly memory-mapped - Source: [5Gfr6lW49aI]
- Dumps F0000-FFFFF range (64KB) - Source: [5Gfr6lW49aI]
- Concatenate halves: `copy /b f0000+f8000 bios.bin` (put /b first) - Source: [5Gfr6lW49aI]

### XT Clone Motherboards

#### Open Source XT BIOS (GLaBIOS/Socketed ROM)
- Open sock 86 is an open source reverse-engineered XT BIOS - Source: [BJAUW2jq2wI]
- Distribution with 2764 EPROMs for clones with 8K ROM sockets - Source: [BJAUW2jq2wI]
- Five chips total: one BIOS chip + four for BASIC - Source: [BJAUW2jq2wI]
- Alternative to proprietary clone BIOSes that may be buggy - Source: [BJAUW2jq2wI]

#### Supersoft Diagnostic ROM on XT Clones
- IBM 5160 diagnostic ROM (from 8 degrees) works on XT clones - Source: [BJAUW2jq2wI]
- Fits in 2764 (8K) ROM socket directly on some clones - Source: [BJAUW2jq2wI]
- Tests system RAM to A0000h and slow refresh test - Source: [BJAUW2jq2wI]
- Rising/falling tones indicate pass/fail status - Source: [BJAUW2jq2wI]
- Useful for troubleshooting clones with unknown BIOS issues - Source: [BJAUW2jq2wI]

#### XT Clone Floppy/DMA Troubleshooting
- Floppy drive requires both IRQ6 and DMA2 to function - Source: [BJAUW2jq2wI]
- XT-IDE does NOT require interrupt or DMA (bypasses them) - Source: [BJAUW2jq2wI]
- If floppy fails but XT-IDE boots, suspect DMA or interrupt controller - Source: [BJAUW2jq2wI]
- CGA card also doesn't use interrupt or DMA - Source: [BJAUW2jq2wI]
- Keyboard uses IRQ2 - if keyboard works, interrupt controller is partially functional - Source: [BJAUW2jq2wI]
- IMD (ImageDisk) bypasses BIOS and talks directly to floppy controller - useful test - Source: [BJAUW2jq2wI]

#### XT Clone DIP Switch Settings
- Usually copy of IBM XT settings exactly - Source: [BJAUW2jq2wI]
- SW1: Math coprocessor, RAM size, display type (color 80 columns = on-off) - Source: [BJAUW2jq2wI]
- SW7-8: Floppy drive count (both on = 1 drive) - Source: [BJAUW2jq2wI]
- Incorrect floppy drive count may cause boot failure - Source: [BJAUW2jq2wI]

#### XT Clone Key Chips (NEC Equivalents)
- 8237 DMA controller = NEC D71037 - Source: [BJAUW2jq2wI]
- 8259 Interrupt controller = NEC D71059C - Source: [BJAUW2jq2wI]
- 8254 Timer = NEC 71054 - Source: [BJAUW2jq2wI]
- 8255 PPI = NEC D8255 - Source: [BJAUW2jq2wI]
- NEC versions rated for higher clock speeds (turbo boards) - Source: [BJAUW2jq2wI]
- Intel originals work as drop-in replacements - Source: [BJAUW2jq2wI]

#### Diagnosing with Kickstart IRQ Card
- POST card that shows IRQ and DMA activity via LEDs - Source: [BJAUW2jq2wI]
- Lights stay on when IRQ/DMA triggered - Source: [BJAUW2jq2wI]
- Floppy access should trigger IRQ6 and DMA2 - Source: [BJAUW2jq2wI]
- If only IRQ6 triggers but no DMA2, suspect DMA controller or termination - Source: [BJAUW2jq2wI]

#### V20 CPU in XT Clones
- NEC V20 is drop-in replacement for 8088 - Source: [BJAUW2jq2wI]
- Provides ~10-15% performance improvement at same clock speed - Source: [BJAUW2jq2wI]
- "System has V20 no FPU" message from some BIOSes - Source: [BJAUW2jq2wI]
- TopBench shows V20 performance similar to PCjr with V20 - Source: [BJAUW2jq2wI]

#### XT Clone Battery Leakage Issues
- Battery leakage can corrode ISA slot contacts and traces - Source: [BJAUW2jq2wI]
- May cause intermittent IRQ/DMA line failures - Source: [BJAUW2jq2wI]
- Check for broken traces between ISA slots and controller chips - Source: [BJAUW2jq2wI]
- Hard drive controllers and floppy controllers equally affected - Source: [BJAUW2jq2wI]

#### XT Clone RAM Troubleshooting (Advanced)

##### Using Schematics
- IBM 5160 schematics work for most XT clones - Source: [GMh5YUbLqLs]
- Chip designators (U1, U2) differ between IBM and clone boards - Source: [GMh5YUbLqLs]
- Use continuity tester with brush probe to find equivalent chips - Source: [GMh5YUbLqLs]
- Trace signals from known-good reference points to identify components - Source: [GMh5YUbLqLs]

##### DMA Refresh Circuit
- DMA channel 0 handles DRAM refresh on PC/XT - Source: [GMh5YUbLqLs]
- DACK0 (DMA acknowledge 0) signal triggers refresh cycles - Source: [GMh5YUbLqLs]
- Should see constant pulsing on DACK0 during operation - Source: [GMh5YUbLqLs]
- Pin 25 on 8237 DMA controller is the key signal - Source: [GMh5YUbLqLs]
- Three 74LS373 latches + 74LS670 register file handle DMA address generation - Source: [GMh5YUbLqLs]
- 74LS138 decoder generates RAS (row address strobe) for each RAM bank - Source: [GMh5YUbLqLs]
- Corrosion damage near these chips can cause random RAM errors - Source: [GMh5YUbLqLs]

##### Parity Error Circuit
- 9th RAM chip per bank stores parity bit - Source: [GMh5YUbLqLs]
- Parity error triggers Non-Maskable Interrupt (NMI) - Source: [GMh5YUbLqLs]
- NMI handler prints "Parity Error" with address and halts system - Source: [GMh5YUbLqLs]
- Diagnostic ROMs may enable/disable parity checking differently - Source: [GMh5YUbLqLs]
- If parity disabled and system works, suspect parity circuit itself - Source: [GMh5YUbLqLs]

##### BIOS Parity Modification
- PC Turbo BIOS source available on GitHub - Source: [GMh5YUbLqLs]
- Can modify NMI handler to do nothing (disable parity check) - Source: [GMh5YUbLqLs]
- Can also disable RAM test routine entirely - Source: [GMh5YUbLqLs]
- System may boot with parity disabled even with faulty RAM - Source: [GMh5YUbLqLs]
- Useful for isolating parity circuit vs actual RAM issues - Source: [GMh5YUbLqLs]

##### Multi-Bank RAM Problems
- Single bank (256K) may work while multiple banks fail - Source: [GMh5YUbLqLs]
- Adding second bank causes random errors = address decoding issue - Source: [GMh5YUbLqLs]
- Check PAL chip settings for 64K vs 256K DRAM configuration - Source: [GMh5YUbLqLs]
- Some boards have trace jumpers that configure bank selection - Source: [GMh5YUbLqLs]
- Cut traces and add pin headers to make configurations switchable - Source: [GMh5YUbLqLs]

##### Bus Transceiver (74LS245)
- Buffer between CPU data bus and RAM data bus - Source: [GMh5YUbLqLs]
- Pin 1: Direction control (XMW signal - memory write) - Source: [GMh5YUbLqLs]
- Pin 19: Enable control (RAM address select) - Source: [GMh5YUbLqLs]
- Check with scope: Both pins should show clean digital signals - Source: [GMh5YUbLqLs]
- RAM-side pins may show floating/tri-state when disabled (normal) - Source: [GMh5YUbLqLs]
- Swapping 74LS245 is common troubleshooting step but often not the issue - Source: [GMh5YUbLqLs]

##### Address Multiplexers (74LS158)
- Generate row/column addresses for DRAM - Source: [GMh5YUbLqLs]
- DRAM uses multiplexed addressing to reduce pin count - Source: [GMh5YUbLqLs]
- Row address latched first, then column address - Source: [GMh5YUbLqLs]
- Difficult to diagnose with scope alone (signals shared with CPU) - Source: [GMh5YUbLqLs]

##### 8288 Bus Controller
- Generates memory read/write and I/O read/write signals - Source: [GMh5YUbLqLs]
- Critical chip - system won't POST without it - Source: [GMh5YUbLqLs]
- Outputs go through 74LS243/245 buffer before reaching peripherals - Source: [GMh5YUbLqLs]
- DMA enable signal can disable these outputs during DMA transfers - Source: [GMh5YUbLqLs]
- Replacement chips from eBay often work (test multiple) - Source: [GMh5YUbLqLs]
- OKI-branded 82C88 chips tested functional in clone boards - Source: [GMh5YUbLqLs]

##### "System Already" BIOS Behavior
- Some clone BIOSes have extremely minimal RAM tests - Source: [GMh5YUbLqLs]
- May print RAM count without actually testing anything - Source: [GMh5YUbLqLs]
- System boots to DOS even with bad RAM if parity disabled - Source: [GMh5YUbLqLs]
- Memory-intensive programs will crash or corrupt data - Source: [GMh5YUbLqLs]
- Use CheckIt or other memory diagnostics to confirm RAM health - Source: [GMh5YUbLqLs]

##### Random RAM Errors (Advanced Troubleshooting)

###### Symptoms
- Random bit errors at various memory addresses - Source: [IPryUBnbM_I]
- Errors not consistent to specific RAM chip - Source: [IPryUBnbM_I]
- Different bits fail on different tests - Source: [IPryUBnbM_I]
- May pass some RAM tests, fail others - Source: [IPryUBnbM_I]

###### Common Cause: 74LS245 Bus Transceiver Failure
- 74LS245 buffers data between CPU bus and RAM - Source: [IPryUBnbM_I]
- Corrosion on pins causes intermittent contact - Source: [IPryUBnbM_I]
- One bad transceiver can cause multiple bit errors - Source: [IPryUBnbM_I]
- Symptoms mimic multiple RAM chip failures - Source: [IPryUBnbM_I]

###### Diagnosis
- Check for corrosion around 74LS245 chips near battery area - Source: [IPryUBnbM_I]
- Inspect pins with magnification for oxidation - Source: [IPryUBnbM_I]
- Test by piggybacking known-good 74LS245 on suspect - Source: [IPryUBnbM_I]
- If errors change or clear, transceiver confirmed bad - Source: [IPryUBnbM_I]

###### Repair
- Clean corroded pins with fiberglass pen or fine abrasive - Source: [IPryUBnbM_I]
- If cleaning doesn't help, replace 74LS245 chip - Source: [IPryUBnbM_I]
- Apply protective coating after repair (nail polish, conformal) - Source: [IPryUBnbM_I]
- Check all transceivers in RAM path, not just one - Source: [IPryUBnbM_I]

##### SuperSoft/Landmark Diagnostic ROM

###### Overview
- Third-party diagnostic ROM for PC/XT compatibles - Source: [IPryUBnbM_I]
- Runs without working system RAM - Source: [IPryUBnbM_I]
- Better diagnostics than stock BIOS - Source: [IPryUBnbM_I]
- Available as 2764 EPROM image - Source: [IPryUBnbM_I]

###### Features
- Tests RAM using only CPU registers (no RAM required to start) - Source: [IPryUBnbM_I]
- Audio feedback for systems with no video - Source: [IPryUBnbM_I]
- Detailed RAM test with address/bit error reporting - Source: [IPryUBnbM_I]
- Tests DMA, interrupt controller, timer chips - Source: [IPryUBnbM_I]

###### Installation
- Burns to standard 2764 or 27128 EPROM - Source: [IPryUBnbM_I]
- Replaces BIOS ROM or goes in diagnostic socket - Source: [IPryUBnbM_I]
- Some clones have dedicated diagnostic ROM socket - Source: [IPryUBnbM_I]
- May need adapter for ROM pinout differences - Source: [IPryUBnbM_I]

###### Advantages Over Stock BIOS
- Continues testing after finding first error - Source: [IPryUBnbM_I]
- Shows pattern of failures to identify root cause - Source: [IPryUBnbM_I]
- Works on dead systems where BIOS won't boot - Source: [IPryUBnbM_I]
- Identifies specific failing bits and addresses - Source: [IPryUBnbM_I]

##### 8288 Bus Controller

###### Overview
- Intel 8288 generates bus control signals from CPU status - Source: [IPryUBnbM_I]
- Creates MEMR, MEMW, IOR, IOW signals - Source: [IPryUBnbM_I]
- Critical chip - system won't function without it - Source: [IPryUBnbM_I]

###### Failure Symptoms
- Complete system failure (no POST) - Source: [IPryUBnbM_I]
- Random crashes during memory access - Source: [IPryUBnbM_I]
- Intermittent failures when chip is warm - Source: [IPryUBnbM_I]
- Ceramic package 8288s run hot and may have thermal issues - Source: [IPryUBnbM_I]

###### Intel vs NEC Variants
- Intel 8288 in ceramic package - Source: [IPryUBnbM_I]
- NEC D71088 is equivalent replacement - Source: [IPryUBnbM_I]
- NEC versions may run cooler - Source: [IPryUBnbM_I]
- OKI 82C88 also compatible - Source: [IPryUBnbM_I]

###### Testing
- Scope bus control signals during operation - Source: [IPryUBnbM_I]
- Compare signal timing to known-good system - Source: [IPryUBnbM_I]
- Swap with known-good 8288 to confirm - Source: [IPryUBnbM_I]

##### PC XT RAM Refresh Architecture
- DMA controller channel 0 handles RAM refresh - Source: [IPryUBnbM_I]
- Timer chip triggers refresh requests periodically - Source: [IPryUBnbM_I]
- If DMA not working, RAM data decays within milliseconds - Source: [IPryUBnbM_I]
- Symptom: Random errors throughout memory, not specific chips - Source: [IPryUBnbM_I]

##### Parity RAM Circuit
- 9 chips per RAM bank (8 data + 1 parity) - Source: [IPryUBnbM_I]
- Parity bit calculated and stored on write - Source: [IPryUBnbM_I]
- Checked on read, NMI triggered if mismatch - Source: [IPryUBnbM_I]
- Parity circuit failure can cause spurious errors - Source: [IPryUBnbM_I]
- Disable parity to test if real RAM error or parity circuit - Source: [IPryUBnbM_I]

##### Warm Start Detection
- PC stores flag in RAM to indicate warm vs cold boot - Source: [GMh5YUbLqLs]
- RAM decay takes time - quick power cycle may retain flag - Source: [GMh5YUbLqLs]
- System may skip memory test thinking it's warm starting - Source: [GMh5YUbLqLs]
- Wait several minutes for full RAM decay before cold boot test - Source: [GMh5YUbLqLs]

##### Oscilloscope Troubleshooting
- Battery-powered scope recommended near high voltage sections - Source: [GMh5YUbLqLs]
- Look for signals that don't go fully high or fully low - Source: [GMh5YUbLqLs]
- DMA refresh pulses visible on multiple address/control lines - Source: [GMh5YUbLqLs]
- Compare suspect board to known-working board with same BIOS - Source: [GMh5YUbLqLs]
- Signals may look identical even with faulty board (frustrating) - Source: [GMh5YUbLqLs]

### Zeos 386SX-16 Motherboard

#### Overview
- Zeos International (St. Paul, Minnesota) - Source: [h9fFt7t12j4]
- 1990 motherboard, VLSI 82C200/201/202/203/205 chipset - Source: [h9fFt7t12j4]
- PC Magazine "Editor's Choice" January 30, 1990 - Source: [h9fFt7t12j4]
- 16MHz 386SX processor (surface mount) - Source: [h9fFt7t12j4]
- Company operated 1981-1995, based in Minneapolis/St. Paul area - Source: [h9fFt7t12j4]

#### Chipset Details
- VLSI 82C2011: Replaces 82C284, 82C288, 84A clock generator, PAL devices - Source: [h9fFt7t12j4]
- VLSI 82C100: Peripheral controller (interrupt, DMA, timer, memory mapper) - Source: [h9fFt7t12j4]
- VLSI 82C202: Memory controller with RAM size jumpers - Source: [h9fFt7t12j4]
- VLSI 82C203: Address buffer chip - Source: [h9fFt7t12j4]
- Available in 16MHz or 12MHz versions (check chip suffix) - Source: [h9fFt7t12j4]

#### RAM Configuration
- 2MB max with 1Mbit DIP chips (18 chips: 16 data + 2 parity) - Source: [h9fFt7t12j4]
- 4MB max by fully populating with 1Mbit chips - Source: [h9fFt7t12j4]
- Uses larger footprint DIP sockets for 1Mbit chips - Source: [h9fFt7t12j4]
- No SIMMs despite being 1990 - cost reduction design - Source: [h9fFt7t12j4]
- 386SX external address bus limited to 16MB (same as 286) - Source: [h9fFt7t12j4]

#### RAM Size Jumpers (82C202)
- Three jumpers: RAM select 0, 1, 2 - Source: [h9fFt7t12j4]
- Jumper ON = logic 0, Jumper OFF = logic 1 (inverted) - Source: [h9fFt7t12j4]
- Consult 82C202 datasheet for RAM size table - Source: [h9fFt7t12j4]

#### Shadow RAM
- Jumper controls shadow RAM enable/disable - Source: [h9fFt7t12j4]
- Shadow copies slow ROM code into fast RAM - Source: [h9fFt7t12j4]
- Significant speed boost for BIOS/VGA ROM calls - Source: [h9fFt7t12j4]
- Disabling shadow RAM frees 384K of upper memory - Source: [h9fFt7t12j4]
- Shadowing introduced with 386-era chipsets, works on 286 too - Source: [h9fFt7t12j4]

#### Turbo Switch
- Hardware jumper or keyboard control selectable - Source: [h9fFt7t12j4]
- Halves CPU speed when disabled (7.9MHz) - Source: [h9fFt7t12j4]
- Some games require non-turbo mode - Source: [h9fFt7t12j4]

#### Common Failures: Shorted Tantalum Capacitors
- 16V tantalums on 12V rail commonly short - Source: [h9fFt7t12j4]
- Insufficient voltage headroom causes failure over time - Source: [h9fFt7t12j4]
- Symptoms: Power supply won't start, or starts then fails - Source: [h9fFt7t12j4]
- Diagnosis: Check continuity from 12V rail to ground - Source: [h9fFt7t12j4]
- Use thermal camera to find shorted cap while feeding current - Source: [h9fFt7t12j4]
- Topdon TC 004 thermal camera useful for this - Source: [h9fFt7t12j4]
- Replace with 25V or 50V electrolytics for margin - Source: [h9fFt7t12j4]
- Multiple tantalums may fail sequentially (replace all) - Source: [h9fFt7t12j4]

#### BIOS
- AMI BIOS from 1986 (licensed for 386SX) - Source: [h9fFt7t12j4]
- Two BIOS chips (16-bit data bus) - Source: [h9fFt7t12j4]
- Basic CMOS setup - limited options - Source: [h9fFt7t12j4]
- Built-in diagnostics (keyboard, video, printer, COM port tests) - Source: [h9fFt7t12j4]

#### Performance
- Comparable to IBM PS/2 Model 35 (20MHz 386SX) in benchmarks - Source: [h9fFt7t12j4]
- Highly competitive for its price point in 1990 - Source: [h9fFt7t12j4]
- Zero wait state video card compatibility issues - Source: [h9fFt7t12j4]
- Some VGA cards incompatible in zero wait state mode - Source: [h9fFt7t12j4]

#### Historical Context
- 386SX: 32-bit internal, 16-bit external data bus - Source: [h9fFt7t12j4]
- Allowed motherboard makers to upgrade 286 designs easily - Source: [h9fFt7t12j4]
- Fewer PCB traces than full 32-bit 386DX boards - Source: [h9fFt7t12j4]
- Computer Shopper magazine was primary sales channel for clones - Source: [h9fFt7t12j4]

### 386DX Motherboard with ALi Chipset and AMD Processor

#### Overview
- 386DX-40 motherboard with AMD processor - Source: [Yew71A7IaIQ]
- ALi chipset (multiple VLSI chips) - Source: [Yew71A7IaIQ]
- 128KB external cache memory (expandable to 256KB) - Source: [Yew71A7IaIQ]
- Date code 1993 on board - Source: [Yew71A7IaIQ]
- Footprint for both DIP and surface mount math coprocessor - Source: [Yew71A7IaIQ]

#### Cache Memory Configuration
- Base: 128KB cache (four 8-bit wide SRAM chips = 64KB x 2 for 32-bit) - Source: [Yew71A7IaIQ]
- Expandable to 256KB with additional SRAM chips - Source: [Yew71A7IaIQ]
- Tag memory chip also required for cache - Source: [Yew71A7IaIQ]
- 386 CPU has no internal cache (L1 is external SRAM) - Source: [Yew71A7IaIQ]

#### SIMM Slot Issues (Damaged Clips)
- 30-pin SIMM slots can survive damaged metal retention clips - Source: [Yew71A7IaIQ]
- Memory modules may still seat and work with bent/broken clips - Source: [Yew71A7IaIQ]
- Requires four modules minimum for 32-bit data bus - Source: [Yew71A7IaIQ]
- SIMMs often "yanked" from boards, damaging clips - Source: [Yew71A7IaIQ]

#### Battery Damage Assessment
- 386 boards commonly destroyed by NiCad battery leakage - Source: [Yew71A7IaIQ]
- Minimal corrosion around battery area = board may survive - Source: [Yew71A7IaIQ]
- Remove leaking battery immediately to prevent further damage - Source: [Yew71A7IaIQ]
- Clean any visible corrosion with IPA - Source: [Yew71A7IaIQ]

#### ISA Bus Speed Configuration
- Some boards have no ISA bus speed configuration in BIOS - Source: [Yew71A7IaIQ]
- Fixed at ~8MHz regardless of CPU speed - Source: [Yew71A7IaIQ]
- Other boards allow clock divider adjustment - Source: [Yew71A7IaIQ]

#### Turbo Mode
- Turbo jumper controls CPU speed (full speed vs reduced) - Source: [Yew71A7IaIQ]
- Missing jumper may cause system to run at reduced speed - Source: [Yew71A7IaIQ]
- Verify speed with Speed600 benchmark after POST - Source: [Yew71A7IaIQ]

#### Crystal Oscillator
- 80MHz crystal / 2 = 40MHz CPU speed - Source: [Yew71A7IaIQ]
- Can swap crystal for different speeds (66MHz for 33MHz CPU) - Source: [Yew71A7IaIQ]
- Useful for running slower math coprocessors - Source: [Yew71A7IaIQ]

### 286 Motherboard with Chips & Technology SCAT Chipset

#### Overview
- 286-12 motherboard with SIP (Single Inline Package) memory - Source: [Yew71A7IaIQ]
- Chips and Technology SCAT chipset - Source: [Yew71A7IaIQ]
- Four banks of SIP memory sockets - Source: [Yew71A7IaIQ]
- Supports up to 8MB RAM with 1Mbit SIPs - Source: [Yew71A7IaIQ]
- External battery connector (not onboard NiCad) - Source: [Yew71A7IaIQ]

#### SCAT Chipset Details
- Single chip integrates: CPU control, clock generation, RTC, CMOS RAM - Source: [Yew71A7IaIQ]
- Also integrates: DMA controllers, interrupt controllers, timer, PPI - Source: [Yew71A7IaIQ]
- Replaces entire AT-class motherboard chipset in one IC - Source: [Yew71A7IaIQ]
- Real-time clock with battery backup built into chipset - Source: [Yew71A7IaIQ]

#### SIP Memory
- Single Inline Package: SIMM with pins instead of edge connector - Source: [Yew71A7IaIQ]
- Electrically equivalent to 30-pin SIMMs - Source: [Yew71A7IaIQ]
- Install in pairs (16-bit data bus on 286) - Source: [Yew71A7IaIQ]
- Four banks = potential for 8 SIP modules - Source: [Yew71A7IaIQ]
- 256Kbit SIPs: 512KB base configuration - Source: [Yew71A7IaIQ]
- 1Mbit SIPs: Up to 8MB maximum - Source: [Yew71A7IaIQ]

#### BIOS Features
- SCAT BIOS includes CPU speed configuration - Source: [Yew71A7IaIQ]
- CPU clock source: proc clock x1/4 or external - Source: [Yew71A7IaIQ]
- RAM wait states configurable (0 to 1) - Source: [Yew71A7IaIQ]
- Dynamic memory sizing auto-detect - Source: [Yew71A7IaIQ]
- Shadow RAM requires 1MB+ installed - Source: [Yew71A7IaIQ]
- EMS page registers built into chipset - Source: [Yew71A7IaIQ]

#### Clock Configuration
- 14.318MHz crystal is standard PC bus clock - Source: [Yew71A7IaIQ]
- SCAT chipset derives CPU clock from internal divider - Source: [Yew71A7IaIQ]
- No separate CPU crystal oscillator needed - Source: [Yew71A7IaIQ]
- CPU speed configurable via BIOS registers - Source: [Yew71A7IaIQ]

#### Performance
- Zero wait state mode gives ~18MHz equivalent speed - Source: [Yew71A7IaIQ]
- One wait state mode reduces performance significantly - Source: [Yew71A7IaIQ]
- Turbo jumper may change actual clock speed (not just wait states) - Source: [Yew71A7IaIQ]

#### Power Management (Early)
- SCAT chipset includes power management features - Source: [Yew71A7IaIQ]
- Sleep mode, proc clock halt options - Source: [Yew71A7IaIQ]
- Unusual for 1989-era chipset - Source: [Yew71A7IaIQ]

#### Compact Form Factor
- Small motherboard due to high integration - Source: [Yew71A7IaIQ]
- Fits in smaller cases than discrete-logic 286 boards - Source: [Yew71A7IaIQ]
- No battery damage due to external battery connector - Source: [Yew71A7IaIQ]

### Generic 386DX Motherboards

#### C&T Chipset Boards (Multi-VLSI Design)
- Chips and Technology chipset: Multiple large VLSI chips make up chipset - Source: [noRZC9y9Uz0]
- More complex than PAL-based designs - Source: [noRZC9y9Uz0]
- Extended BIOS setup with chipset register control - Source: [noRZC9y9Uz0]
- Can configure processor clock source: oscillator direct or system clock multiplied - Source: [noRZC9y9Uz0]
- ISA bus clock divider configurable (processor clock / 3, or T clock) - Source: [noRZC9y9Uz0]
- DMA clock configurable between S clock and S clock-2 - Source: [noRZC9y9Uz0]
- Shadow RAM enable/disable in chipset setup - Source: [noRZC9y9Uz0]
- 40MHz or 50MHz crystal oscillator options: 50MHz / 2 = 25MHz CPU speed - Source: [noRZC9y9Uz0]
- Multi-layer 4-layer PCB construction with hidden trace layers - Source: [noRZC9y9Uz0]

#### Parity RAM on 386DX
- 386DX has 32-bit data bus, needs 32 bits + 4 parity bits per word - Source: [noRZC9y9Uz0]
- 1Mx1 DRAM chips: 8 chips per megabyte of data, 1 extra for parity per byte - Source: [noRZC9y9Uz0]
- 8MB configuration: 9 chips per MB = 72 chips total (8 banks of 9) - Source: [noRZC9y9Uz0]
- Parity calculates checksum on write, verifies on read - Source: [noRZC9y9Uz0]
- Parity error halts system rather than allowing bad data processing - Source: [noRZC9y9Uz0]
- High-end system feature: ensures data integrity, worth extra memory cost - Source: [noRZC9y9Uz0]

#### PAL-Based 386DX Boards
- Uses programmable array logic (PAL) chips instead of large VLSI chipset - Source: [noRZC9y9Uz0]
- Single Chips and Technology IC plus many PAL chips - Source: [noRZC9y9Uz0]
- Earlier/simpler design approach - less integrated than multi-VLSI - Source: [noRZC9y9Uz0]
- No extended BIOS setup options - just basic CMOS setup - Source: [noRZC9y9Uz0]
- Diagnostics built into ROM instead of chipset setup - Source: [noRZC9y9Uz0]
- May have SRAM cache chips (55417 series) for 64KB L1 cache - Source: [noRZC9y9Uz0]

#### 386DX Clock Configuration
- 66MHz crystal oscillator / 2 = 33MHz actual CPU speed - Source: [noRZC9y9Uz0]
- Turbo jumper may change crystal divider ratio - Source: [noRZC9y9Uz0]
- Some boards: Turbo = full speed, Non-turbo = 20MHz - Source: [noRZC9y9Uz0]
- Jumper position not always intuitive - test with benchmark - Source: [noRZC9y9Uz0]

#### 386DX vs 386SX
- 386DX: Full 32-bit external data bus - Source: [noRZC9y9Uz0]
- 386SX: 16-bit external data bus (came out later despite "lower" designation) - Source: [noRZC9y9Uz0]
- 386DX requires 4 SIMMs at a time due to 32-bit bus - Source: [noRZC9y9Uz0]
- Performance scaling 1981-1989: XT to 386DX = 25x faster in 8 years - Source: [noRZC9y9Uz0]

#### Battery Survival
- 386DX boards with external battery connectors survive better than onboard NiCad - Source: [noRZC9y9Uz0]
- 4-pin header for external battery pack = no leakage damage risk - Source: [noRZC9y9Uz0]
- Minor battery leakage on some boards causes minimal damage if caught early - Source: [noRZC9y9Uz0]
- Multi-layer PCB construction makes trace repair difficult if corrosion spreads - Source: [noRZC9y9Uz0]

### IBM EGA Card

#### RAM Upgrade Experiment (4416 to 4464)
- IBM EGA uses 4416 DRAM (16K x 4-bit) chips - Source: [GR7ng-7PBJo]
- Experiment: Replace 4416 chips with 4464 (64K x 4-bit) to add more RAM - Source: [GR7ng-7PBJo]
- Result: Does NOT work - refresh rate incompatibility - Source: [GR7ng-7PBJo]
- 4416 uses different refresh timing than 4464 - Source: [GR7ng-7PBJo]
- 4416 requires 128 refresh cycles per 2ms vs 4464's 256 cycles per 4ms - Source: [GR7ng-7PBJo]
- Card was designed for 4416 refresh timing specifically - Source: [GR7ng-7PBJo]
- Visual symptoms: corrupted display, garbage characters - Source: [GR7ng-7PBJo]
- Some rows work while others corrupt = refresh hitting wrong addresses - Source: [GR7ng-7PBJo]
- Confirmed via datasheet comparison that refresh cycles are incompatible - Source: [GR7ng-7PBJo]
- Conclusion: Cannot simply swap larger DRAM into EGA card for more memory - Source: [GR7ng-7PBJo]

#### Stock Configuration
- 64KB base RAM configuration (original IBM EGA) - Source: [GR7ng-7PBJo]
- Expandable to 256KB via additional RAM chips - Source: [GR7ng-7PBJo]
- Full 256KB required for 640x350 16-color mode - Source: [GR7ng-7PBJo]

### IBM 5154 EGA Monitor

#### Overview
- First commercial multiscan monitor (1984) - Source: [7EezG5OzSQo]
- Supports 15.7kHz (CGA) and ~22kHz (EGA) - Source: [7EezG5OzSQo]
- Actually manufactured by Samsung (OEM) - Source: [7EezG5OzSQo]
- SAMS service documentation available: archive.org/details/Sams_IBM_5154_VDU - Source: [7EezG5OzSQo]

#### Color Decoding
- Uses TBP28L22 PROM chip for color decoding - Source: [7EezG5OzSQo]
- 64-color palette in 640x350 mode - Source: [7EezG5OzSQo]
- Pin 4 on 28L22 controls 16-color vs 64-color mode - Source: [7EezG5OzSQo]
- Mode selected by vertical sync polarity - Source: [7EezG5OzSQo]

#### 64-Color Low-Res Mode Mod
- Can force 64-color mode in 320x200 for games like Iron Man - Source: [7EezG5OzSQo]
- Remove jumper link from 4077 pin 10 to 28L22 pin 4 - Source: [7EezG5OzSQo]
- Add 10K pull-down resistor from pin 4 to ground - Source: [7EezG5OzSQo]
- Wire switch to select automatic vs forced 64-color mode - Source: [7EezG5OzSQo]

### Battery-Damaged Motherboard Assessment

#### Testing Strategy
- Test boards in order of increasing value/complexity - Source: [HtrAvQGuXTw]
- Start with simpler 286 boards, progress to 386/486 - Source: [HtrAvQGuXTw]
- Visual inspection first - look for obvious corrosion damage - Source: [HtrAvQGuXTw]
- Check traces near battery location for breaks - Source: [HtrAvQGuXTw]

#### Dallas RTC Chips
- Dallas DS1287/DS1287A are integrated RTC with internal battery - Source: [HtrAvQGuXTw]
- Battery inside Dallas chip is non-replaceable in standard chips - Source: [HtrAvQGuXTw]
- DS1287A variant has external battery backup pin - Source: [HtrAvQGuXTw]
- Dead Dallas = no time keeping, but board still works - Source: [HtrAvQGuXTw]
- Dead Dallas does NOT leak and corrode like NiCad barrel batteries - Source: [HtrAvQGuXTw]
- Dallas chip failure is benign - just loses settings when powered off - Source: [HtrAvQGuXTw]
- Necroware Dallas replacement module available (modern drop-in) - Source: [HtrAvQGuXTw]

#### Dallas vs Barrel Battery
- Dallas chip with dead battery: No corrosion, board still usable - Source: [HtrAvQGuXTw]
- NiCad barrel battery: Leaks, corrodes traces, can destroy board - Source: [HtrAvQGuXTw]
- Dallas failure mode is much better than barrel battery failure - Source: [HtrAvQGuXTw]
- Boards with Dallas only (no barrel) often survive decades - Source: [HtrAvQGuXTw]

### Cache Memory Testing

#### CachCheck Utility
- Tests cache memory functionality and size - Source: [HtrAvQGuXTw]
- Written by Ray Van Tassel (1995-1998) - Source: [HtrAvQGuXTw]
- Shows cache size detected by testing access times - Source: [HtrAvQGuXTw]
- Measures microseconds per KB at different block sizes - Source: [HtrAvQGuXTw]

#### Interpreting CachCheck Results
- Small blocks (fit in cache): Fast access time - Source: [HtrAvQGuXTw]
- Large blocks (exceed cache): Slower access time - Source: [HtrAvQGuXTw]
- Sharp speed drop indicates cache size limit - Source: [HtrAvQGuXTw]
- 64KB cache typical for 386DX boards - Source: [HtrAvQGuXTw]
- 256KB cache common on 486 boards - Source: [HtrAvQGuXTw]

#### Cache Speed Testing
- Speed600 utility: General performance benchmark - Source: [HtrAvQGuXTw]
- SpeedSys utility: Detailed system speed analysis - Source: [HtrAvQGuXTw]
- Compare cached vs uncached performance to verify cache working - Source: [HtrAvQGuXTw]
- 386 with cache should be noticeably faster than without - Source: [HtrAvQGuXTw]

### Intel 82385 Cache Controller

#### Overview
- External cache controller chip for 386DX systems - Source: [HtrAvQGuXTw]
- Located between CPU and main memory - Source: [HtrAvQGuXTw]
- Manages L1 cache (CPU has no internal cache on 386) - Source: [HtrAvQGuXTw]
- Common on higher-end 386DX motherboards - Source: [HtrAvQGuXTw]

#### Function
- Monitors memory bus for cacheable addresses - Source: [HtrAvQGuXTw]
- Stores frequently accessed data in fast SRAM cache - Source: [HtrAvQGuXTw]
- Significant performance improvement over non-cached 386 - Source: [HtrAvQGuXTw]
- 64KB cache typical with 82385 - Source: [HtrAvQGuXTw]

### 486 DX4 Overdrive Processors

#### Overview
- Intel upgrade processor for 486 systems - Source: [HtrAvQGuXTw]
- Clock-triples internal frequency (33MHz bus = 100MHz internal) - Source: [HtrAvQGuXTw]
- Built-in voltage regulator (runs on 5V but uses 3.3V internally) - Source: [HtrAvQGuXTw]
- Heatsink with fan attached - Source: [HtrAvQGuXTw]

#### Installation
- Socket 1/2/3 486 motherboards supported - Source: [HtrAvQGuXTw]
- Must remove original 486 CPU - Source: [HtrAvQGuXTw]
- May need jumper changes for clock multiplier settings - Source: [HtrAvQGuXTw]
- Some boards need BIOS update for Overdrive support - Source: [HtrAvQGuXTw]

#### Performance
- 100MHz Overdrive significantly faster than 33MHz 486DX - Source: [HtrAvQGuXTw]
- L1 cache tripled effective speed helps performance - Source: [HtrAvQGuXTw]
- Memory bus still limited to 33MHz (bottleneck on some tasks) - Source: [HtrAvQGuXTw]
- Good upgrade path for existing 486 systems - Source: [HtrAvQGuXTw]

#### Identification
- "Overdrive" marking on chip - Source: [HtrAvQGuXTw]
- Larger package than standard 486 (includes voltage regulator) - Source: [HtrAvQGuXTw]
- Integrated heatsink/fan assembly - Source: [HtrAvQGuXTw]
- Various speed grades available (DX2/50, DX2/66, DX4/100) - Source: [HtrAvQGuXTw]
