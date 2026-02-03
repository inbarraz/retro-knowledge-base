# VTech / Laser

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| Laser XT Turbo | XT Clone | [36NPrsEcNww] |
| Laser 200 | Home Computer | [DXOP0uP5P60] |
| CGA/MDA Clone Card | ISA Video Card | [JljZ4OEZ5nI] |

## Platform-Specific Knowledge

### Laser 200 (Color Computer 200)

#### Overview
- Low-cost home computer, similar market to ZX Spectrum - Source: [DXOP0uP5P60]
- Made in Hong Kong by Video Technologies - Source: [DXOP0uP5P60]
- Z80 CPU - Source: [DXOP0uP5P60]
- Uses Motorola video chip (same as TI-99, MSX, Dragon 32) - Source: [DXOP0uP5P60]
- Green text color and scheme identical to Dragon 32 - Source: [DXOP0uP5P60]
- Has 8 colors: green, yellow, blue, red, buff, cyan, magenta, orange - Source: [DXOP0uP5P60]
- Buff color confirms Motorola video chip usage - Source: [DXOP0uP5P60]

#### Keyboard
- Chiclet keyboard similar to ZX Spectrum - Source: [DXOP0uP5P60]
- Keys may trigger BASIC commands like ZX Spectrum (unconfirmed) - Source: [DXOP0uP5P60]
- Keyboard is soldered to main PCB (not membrane connector) - Source: [DXOP0uP5P60]

#### Construction
- Built down to extremely low cost - Source: [DXOP0uP5P60]
- All metal keyboard - Source: [DXOP0uP5P60]
- RF shield adhered to bottom of case - Source: [DXOP0uP5P60]
- Piezoelectric speaker (cheapest possible) - Source: [DXOP0uP5P60]
- Warranty void seals on screws - Source: [DXOP0uP5P60]

#### Power Supply
- Needs standard 9V DC, center positive barrel jack - Source: [DXOP0uP5P60]
- Has internal 5V regulator with large heatsink - Source: [DXOP0uP5P60]
- 5V regulator dissipates significant heat - Source: [DXOP0uP5P60]
- Like ZX Spectrum in this regard - Source: [DXOP0uP5P60]

#### Potential Mods
- Remove 5V regulator and heatsink, supply 5V directly - Source: [DXOP0uP5P60]
- Would run cooler without regulator heat dissipation - Source: [DXOP0uP5P60]

#### Video Output
- Has RF modulator with Channel 3/4 switch (NTSC channels) - Source: [DXOP0uP5P60]
- PAL/NTSC compatibility unknown from single unit - Source: [DXOP0uP5P60]

#### Internal Components
- Z80 processor (SIS brand) - Source: [DXOP0uP5P60]
- ~2K static RAM chip - Source: [DXOP0uP5P60]
- 40-pin DIP video chip (Motorola) - Source: [DXOP0uP5P60]
- Limited internal visibility due to shielding - Source: [DXOP0uP5P60]

#### Comparison Notes
- Similar architecture to Tandy MC-10 - Source: [DXOP0uP5P60]
- Both use Motorola chipset with similar graphics capability - Source: [DXOP0uP5P60]

### Laser XT Turbo

#### Overview
- VTech (Video Technology Corporation) branded XT clone - Source: [36NPrsEcNww]
- Uses custom surface-mount VTech ICs (similar package style to Laser 128) - Source: [36NPrsEcNww]
- Siemens 8088 CPU - Source: [36NPrsEcNww]
- Runs at 4.77MHz and 10MHz (turbo mode) - Source: [36NPrsEcNww]
- Date codes indicate 1989 manufacture (very late for XT) - Source: [36NPrsEcNww]
- Manual: minuszerodegrees.net/manuals/VTech/VTech%20-%20Laser%20Turbo%20XT%20-%20Operations%20Manual.pdf - Source: [36NPrsEcNww]

#### Memory Configuration
- 512K base memory with 256K chips - Source: [36NPrsEcNww]
- Upgrade to 640K: Install four 4464 chips in empty sockets - Source: [36NPrsEcNww]
- Supports up to 1MB EMS memory on motherboard - Source: [36NPrsEcNww]
- EMS uses 41256 chips (256K x 1 bit) - Source: [36NPrsEcNww]
- EMS memory bank-switched into high address space - Source: [36NPrsEcNww]

#### Keyboard Compatibility Issue
- May NOT work with standard XT keyboards - Source: [36NPrsEcNww]
- Standard XT keyboard produces continuous beeping - Source: [36NPrsEcNww]
- Original Laser keyboard has different layout (plus-shaped arrow keys instead of inverted T) - Source: [36NPrsEcNww]
- UPDATE: Requires jumper to disable keyboard lock (reverse of other systems) - Source: [36NPrsEcNww]
- Works with normal XT keyboard after jumper installed - Source: [36NPrsEcNww]

#### Power Supply
- VTech PS150 (150W) - Source: [36NPrsEcNww]
- Multi-voltage capable - Source: [36NPrsEcNww]
- Uses non-standard motherboard power connector (not IBM-style) - Source: [36NPrsEcNww]

#### Motherboard Features
- Reset button on rear (afterthought design, button plugs into motherboard) - Source: [36NPrsEcNww]
- AMI BIOS ROM - Source: [36NPrsEcNww]
- Separate keyboard BIOS chip - Source: [36NPrsEcNww]
- Math coprocessor socket - Source: [36NPrsEcNww]
- Version A marking on PCB - Source: [36NPrsEcNww]
- Bodge components soldered on bottom (resistor array, bypass caps) - Source: [36NPrsEcNww]

#### Original Video Card
- Laser-branded dual-mode CGA/MDA card - Source: [36NPrsEcNww]
- Toggle switch to force composite output to monochrome or color - Source: [36NPrsEcNww]
- Has onboard BIOS (unlike IBM original where BIOS is on motherboard) - Source: [36NPrsEcNww]
- Jumper to disable card BIOS when used in other computers - Source: [36NPrsEcNww]
- Two video output jacks: one mono, one color (labeled on card) - Source: [36NPrsEcNww]

#### Multi-Function I/O Card
- Laser branded - Source: [36NPrsEcNww]
- Floppy controller - Source: [36NPrsEcNww]
- Two serial ports - Source: [36NPrsEcNww]
- Parallel port - Source: [36NPrsEcNww]
- Game port - Source: [36NPrsEcNww]
- Real-time clock (with VARTA battery that leaks) - Source: [36NPrsEcNww]
- Foam spacer prevents card wobble against slot covers - Source: [36NPrsEcNww]

### VARTA Battery Damage

#### Symptoms
- Corrosion spreads to nearby slots and components - Source: [36NPrsEcNww]
- Green crusty deposits on slot connectors - Source: [36NPrsEcNww]
- Corrosion can travel via capillary action in multiple directions - Source: [36NPrsEcNww]
- Ground plane eaten away on affected cards - Source: [36NPrsEcNww]
- Solder mask bubbles and peels off - Source: [36NPrsEcNww]

#### Repair Approach
- Cut battery off first before cleaning - Source: [36NPrsEcNww]
- Naval jelly: Paint on with brush, let sit ~20 minutes - Source: [36NPrsEcNww]
- Naval jelly bubbles as it works (acid-base reaction) - Source: [36NPrsEcNww]
- NiCad leakage is basic, naval jelly (phosphoric acid) neutralizes it - Source: [36NPrsEcNww]
- Vinegar is milder alternative but takes longer - Source: [36NPrsEcNww]
- Vinegar soak: Wrap card in plastic, pour vinegar over it - Source: [36NPrsEcNww]
- CRITICAL: Scrub thoroughly with soap and water after treatment - Source: [36NPrsEcNww]
- Multiple passes may be needed for stubborn corrosion - Source: [36NPrsEcNww]
- Apply DeoxIT to cleaned slot connectors - Source: [36NPrsEcNww]

#### Long-Term Prognosis
- Unknown if corrosion continues eating copper under solder mask over time - Source: [36NPrsEcNww]
- Boards may work after cleaning but fail years later - Source: [36NPrsEcNww]
- Traces can be open underneath despite surface looking OK - Source: [36NPrsEcNww]
- May need to trace out every via and run bodge wires - Source: [36NPrsEcNww]

## Peripherals

### Seagate ST-225R (RLL)
- RLL-certified version of ST-225 - Source: [36NPrsEcNww]
- Holds ~32MB instead of 20MB (MFM) - Source: [36NPrsEcNww]
- Can survive long storage and still work - Source: [36NPrsEcNww]
- May need SpinRite low-level format to refresh after long storage - Source: [36NPrsEcNww]
- Alternative: Low-level format via controller card BIOS (g=c800:5 in DEBUG) - Source: [36NPrsEcNww]

### Seagate MFM Controller (XT)
- Surface-mount design (later generation, more compact) - Source: [36NPrsEcNww]
- Has mounting holes for hard card bracket configuration - Source: [36NPrsEcNww]
- Hard card variant: Drive mounts directly on card bracket - Source: [36NPrsEcNww]
- This controller allows typing in heads/cylinders (more flexible than fixed 20/32MB) - Source: [36NPrsEcNww]
- PIN 1 identification: Square solder pad = pin 1, round pads for rest - Source: [36NPrsEcNww]

### Chinon 360K Floppy Drive
- Induction motor (permanent magnets + coils on PCB) - Source: [36NPrsEcNww]
- Metal fragments can get inside and cause crunchy noises - Source: [36NPrsEcNww]
- Fix: Blow compressed air into motor area - Source: [36NPrsEcNww]
- Can disassemble (3 Phillips screws) to clean coils - Source: [36NPrsEcNww]
- AC induction motor allows precise speed control - Source: [36NPrsEcNww]

### VTech CGA/MDA Clone Card

#### Overview
- Clone CGA/MDA graphics card for XT/AT systems - Source: [JljZ4OEZ5nI]
- Dual-mode card supporting both CGA and MDA - Source: [JljZ4OEZ5nI]
- Has hidden features not documented in manual - Source: [JljZ4OEZ5nI]

#### Specifications
- 64KB video RAM (double the standard CGA's 16KB) - Source: [JljZ4OEZ5nI]
- Extra RAM enables Hercules-compatible graphics mode - Source: [JljZ4OEZ5nI]
- Uses 6845 CRTC compatible chip - Source: [JljZ4OEZ5nI]

#### Hidden Plantronics 16-Color Mode
- Supports undocumented Plantronics ColorPlus 16-color mode - Source: [JljZ4OEZ5nI]
- Requires specific jumper configuration to enable - Source: [JljZ4OEZ5nI]
- Plantronics mode uses 64KB RAM to double color depth - Source: [JljZ4OEZ5nI]
- Standard CGA: 4 colors in 320x200, Plantronics: 16 colors - Source: [JljZ4OEZ5nI]
- Not many programs support Plantronics mode - Source: [JljZ4OEZ5nI]
- Some Sierra games (King's Quest era) support Plantronics - Source: [JljZ4OEZ5nI]

#### Jumper Configuration for Plantronics
- Default jumpers configured for standard CGA mode - Source: [JljZ4OEZ5nI]
- Specific jumper positions enable Plantronics mode - Source: [JljZ4OEZ5nI]
- Documentation for jumper settings typically not included - Source: [JljZ4OEZ5nI]
- May need experimentation to find correct settings - Source: [JljZ4OEZ5nI]

#### Color MDA Mode (Undocumented)
- Can run MDA in color mode (unusual feature) - Source: [JljZ4OEZ5nI]
- Not standard MDA behavior (MDA is normally monochrome only) - Source: [JljZ4OEZ5nI]
- Achieved through 6845 programming tricks - Source: [JljZ4OEZ5nI]
- Color MDA shows colored text on CGA monitor - Source: [JljZ4OEZ5nI]

#### Video Output
- Has composite video output with mono jack - Source: [JljZ4OEZ5nI]
- Mono jack provides cleaner composite than RCA - Source: [JljZ4OEZ5nI]
- RGB output via standard CGA connector - Source: [JljZ4OEZ5nI]
- MDA output via separate connector - Source: [JljZ4OEZ5nI]

#### Comparison to IBM CGA
- More features than original IBM CGA - Source: [JljZ4OEZ5nI]
- 64KB RAM vs IBM's 16KB - Source: [JljZ4OEZ5nI]
- Plantronics compatibility IBM CGA lacks - Source: [JljZ4OEZ5nI]
- Clone cards often had more features than originals - Source: [JljZ4OEZ5nI]

## Testing Notes

### XT Motherboard Testing
- XT BIOS has no setup menu - use DIP switches for configuration - Source: [36NPrsEcNww]
- POST card shows dash-dash (normal for XT, no POST codes) - Source: [36NPrsEcNww]
- Speaker connection: Two pins, usually on left side of header - Source: [36NPrsEcNww]
- VGA/EGA cards work because they have onboard BIOS (unlike CGA/MDA on IBM) - Source: [36NPrsEcNww]
- Use mouse pads under motherboard to raise it off desk (prevents card brackets hitting) - Source: [36NPrsEcNww]
