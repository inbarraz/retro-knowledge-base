# Magnavox / Philips

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| 13MT143S Smart Series | 13" Color CRT TV | [t9bs3i2-5Kc] |
| Color Monitor 40 (CM8502/8564) | Composite CRT Monitor | [xCnqkvF10to] |
| RGB Display 80 | RGB CRT Monitor | [xCnqkvF10to] |

## Platform-Specific Knowledge

### Magnavox 13MT143S Smart Series

#### Overview
- 13" color television, Philips Consumer Electronics North America - Source: [t9bs3i2-5Kc]
- Made in China, manufactured May 2003 - Source: [t9bs3i2-5Kc]
- Uses Chunwa CRT (not Philips CRT) - Source: [t9bs3i2-5Kc]
- Tinted glass phosphor (darker than older sets but very long-lived) - Source: [t9bs3i2-5Kc]
- Excellent CRT donor for Commodore 1702 transplants - Source: [t9bs3i2-5Kc]
- High dot pitch (low resolution but very bright) - Source: [t9bs3i2-5Kc]

#### Board Design
- Isolated switch mode power supply in dedicated section - Source: [t9bs3i2-5Kc]
- Two-chip solution on main board (jungle IC + microcontroller) - Source: [t9bs3i2-5Kc]
- On-screen display generated in microcontroller via RGB to jungle - Source: [t9bs3i2-5Kc]
- RGB mod possible by tapping OSD RGB lines - Source: [t9bs3i2-5Kc]
- Neck board has two footprints (13" and 19"/20" CRT compatibility) - Source: [t9bs3i2-5Kc]
- Control board supports multiple screen sizes with same design - Source: [t9bs3i2-5Kc]

#### Power Supply Section
- Isolated SMPS design (secondary side not referenced to mains) - Source: [t9bs3i2-5Kc]
- B+ around 96-102 volts on secondary side - Source: [t9bs3i2-5Kc]
- Switching transistor has integrated controller (5 pins total) - Source: [t9bs3i2-5Kc]
- Part number BUT11APX for horizontal output transistor - Source: [t9bs3i2-5Kc]
- Optocoupler provides feedback from secondary to primary side - Source: [t9bs3i2-5Kc]
- Bootstrap cap (47µF 25V) common failure point near hot resistor - Source: [t9bs3i2-5Kc]
- Power supply runs constantly (pre-Energy Star design) - Source: [t9bs3i2-5Kc]

#### Known Issues

##### Circuit Bending Damage
- Deflection yoke disconnection kills high voltage generation - Source: [t9bs3i2-5Kc]
- Cannot run TV with horizontal deflection disconnected - Source: [t9bs3i2-5Kc]
- Yoke is critical component of horizontal flyback circuit - Source: [t9bs3i2-5Kc]
- Attempt to use as oscilloscope by connecting audio to yoke fails completely - Source: [t9bs3i2-5Kc]

##### Horizontal Output Transistor Failure
- BUT11APX transistor breaks down under voltage but tests OK with multimeter - Source: [t9bs3i2-5Kc]
- Diode check shows normal 0.4V readings even when faulty - Source: [t9bs3i2-5Kc]
- Fails short when B+ voltage applied, causing excessive current draw - Source: [t9bs3i2-5Kc]
- Returns to "normal" readings when voltage removed - Source: [t9bs3i2-5Kc]
- Thermal camera shows transistor heating rapidly when powered - Source: [t9bs3i2-5Kc]
- Parts board transistor: ST BUL312FR (similar footprint) - Source: [t9bs3i2-5Kc]

##### Bootstrap Cap Failure
- TL brand 47µF 25V caps common failure - Source: [t9bs3i2-5Kc]
- Located near hot resistor, gets baked over time - Source: [t9bs3i2-5Kc]
- Measures in picofarads when dead (should be 47µF) - Source: [t9bs3i2-5Kc]
- ESR meter shows megaohms on dead cap (should be ~1 ohm) - Source: [t9bs3i2-5Kc]
- Replacement: 47µF 50V works fine in this circuit - Source: [t9bs3i2-5Kc]

#### Capacitor Quality
- TL brand caps are poor quality - Source: [t9bs3i2-5Kc]
- Rubicon caps (good quality) - Source: [t9bs3i2-5Kc]
- Gcon/Jon caps (mixed quality) - Source: [t9bs3i2-5Kc]
- B+ caps (160V rated) typically have higher ESR (normal for high voltage) - Source: [t9bs3i2-5Kc]

#### Board Revisions
- Different board designs exist for same model - Source: [t9bs3i2-5Kc]
- Older board (2003): Two-chip solution, surface mount on bottom - Source: [t9bs3i2-5Kc]
- Newer board (2005): Large Philips IC on top, through-hole - Source: [t9bs3i2-5Kc]
- Parts may not be interchangeable between revisions - Source: [t9bs3i2-5Kc]
- Flyback part numbers similar but pinout may differ - Source: [t9bs3i2-5Kc]

#### Degaussing Coil Circuit
- PTC thermistor controls degaussing coil - Source: [t9bs3i2-5Kc]
- Starts low resistance, heats up to high resistance - Source: [t9bs3i2-5Kc]
- Coil gets 120V briefly on power-up, then effectively disconnected - Source: [t9bs3i2-5Kc]
- Thermistor stays hot all the time (inefficient design) - Source: [t9bs3i2-5Kc]
- Failure mode: Opens, degaussing stops working - Source: [t9bs3i2-5Kc]

#### Service Position
- Tilt board up while still connected to CRT - Source: [t9bs3i2-5Kc]
- Cut zip ties for additional wire length - Source: [t9bs3i2-5Kc]
- Use plastic bottle to prop up board - Source: [t9bs3i2-5Kc]
- Allows voltage measurements while running - Source: [t9bs3i2-5Kc]
- High side can have ~160V stored on reservoir cap even when off - Source: [t9bs3i2-5Kc]

### Philips/Magnavox Color Monitor 40 (CM8502/8564)

#### Overview
- Internally identical to Commodore 1084 with features disabled - Source: [xCnqkvF10to]
- Made by Philips, sold under Philips, Magnavox, and Commodore brands - Source: [xCnqkvF10to]
- Has composite video and TTL RGB inputs - Source: [xCnqkvF10to]
- Missing luma/chroma and analog RGB from full 1084 - Source: [xCnqkvF10to]
- Front "green" switch makes screen green (disables R/B) - Source: [xCnqkvF10to]

#### Variants
- CM8502: Standard version - Source: [xCnqkvF10to]
- CM8505: Has comb filter for improved color decoding - Source: [xCnqkvF10to]
- CM8564: TTL RGB board, no analog RGB - Source: [xCnqkvF10to]
- RGB Display 80: Higher resolution CRT version - Source: [xCnqkvF10to]
- Color Monitor 40: Lower resolution TV-grade CRT - Source: [xCnqkvF10to]

#### Internal Architecture
- Same PCB as 1084 with components removed - Source: [xCnqkvF10to]
- IC502: RGB matrix chip (converts component to RGB) - Source: [xCnqkvF10to]
- IC501: NTSC color decoder (outputs component-like signal) - Source: [xCnqkvF10to]
- S533: Inductor filter controls luma bandwidth - Source: [xCnqkvF10to]
- Jumper link 9252 controls S533 grounding - Source: [xCnqkvF10to]

#### Green Switch (SK4) Circuit
- Two-section switch (half for green mode, half for color disable) - Source: [xCnqkvF10to]
- One side feeds 12V via D604/D605 to disable R/B drive - Source: [xCnqkvF10to]
- Other side grounds color control on IC502 - Source: [xCnqkvF10to]
- Green wire jumper from triangle 48 to 27 enables green mode - Source: [xCnqkvF10to]

### High-Resolution Monochrome Luma Mod (SK4 Conversion)

#### Purpose
- Converts useless green mode switch to high-res monochrome mode - Source: [xCnqkvF10to]
- Disables luma filter that causes fuzzy text - Source: [xCnqkvF10to]
- Perfect for Apple II 80-column text display - Source: [xCnqkvF10to]
- Replicates 1084/1702 luma-only mode functionality - Source: [xCnqkvF10to]

#### Background: NTSC Bandwidth Limitation
- Original B&W TV broadcast limited to ~300 lines horizontal resolution - Source: [xCnqkvF10to]
- Bandwidth allocation: 6MHz per TV channel (NTSC) - Source: [xCnqkvF10to]
- Color added via 3.58MHz carrier signal overlaid on luminance - Source: [xCnqkvF10to]
- PAL color carrier at 4.43MHz (slightly higher resolution than NTSC) - Source: [xCnqkvF10to]
- Low-pass filter removes color carrier info but also removes sharpness - Source: [xCnqkvF10to]
- Monochrome monitors can display 600-800 pixels horizontally - Source: [xCnqkvF10to]

#### S533 Filter Operation
- Inductor with capacitor (variable filter) - Source: [xCnqkvF10to]
- When grounded: Filter ENABLED (low-res color-safe mode) - Source: [xCnqkvF10to]
- When floating: Filter DISABLED (high-res monochrome mode) - Source: [xCnqkvF10to]
- On unmodified monitor, jumper link 9252 grounds S533 permanently - Source: [xCnqkvF10to]
- Schematics incorrectly show S533 floating (error in documentation) - Source: [xCnqkvF10to]

#### Mod Instructions
1. Remove wire jumper from triangle 48 to 27 (green wire near SK4) - Source: [xCnqkvF10to]
   - This disables "green only mode" entirely
2. Cut 12V trace from PCB edge side of SK4 - Source: [xCnqkvF10to]
   - Trace goes to two pins: front edge pin and middle pin
3. Ground the front edge pin of SK4 (formerly had 12V) - Source: [xCnqkvF10to]
4. Cut trace between SK4 pins that had 12V (edge pin to middle pin) - Source: [xCnqkvF10to]
5. Remove jumper link 9252 near S533 - Source: [xCnqkvF10to]
   - This normally grounds S533 (enables filter permanently)
6. Run jumper from middle SK4 pin (PCB edge) to 9252 pad (PCB edge) - Source: [xCnqkvF10to]
   - This allows switch to control S533 grounding

#### Mod Result
- Switch OUT: Filter enabled, normal color operation - Source: [xCnqkvF10to]
- Switch IN: Filter disabled + color decoder disabled = high-res monochrome - Source: [xCnqkvF10to]
- No additional parts required - just wire and trace cuts - Source: [xCnqkvF10to]
- Fully reversible by reinstalling jumper links - Source: [xCnqkvF10to]

#### Benefits for Apple II
- 80-column text becomes much sharper - Source: [xCnqkvF10to]
- Removes color fringing from monochrome text modes - Source: [xCnqkvF10to]
- Switch on front is more accessible than 1084 rear switch - Source: [xCnqkvF10to]
- Can toggle between color graphics and sharp monochrome text - Source: [xCnqkvF10to]
- Double hi-res graphics display without artifact colors - Source: [xCnqkvF10to]

### Commodore 1084 Relationship

#### Architecture Differences
- 1084 has full complement: composite, luma/chroma, TTL RGB, analog RGB - Source: [xCnqkvF10to]
- Philips variants have features disabled by omitting components - Source: [xCnqkvF10to]
- Same base PCB design with different population options - Source: [xCnqkvF10to]
- Jumper links bypass unpopulated circuits - Source: [xCnqkvF10to]

#### 1084 Luma/Chroma Switch Operation
- LCA/CVBS switch selects between composite and separate chroma - Source: [xCnqkvF10to]
- In composite mode: S533 grounded (filter enabled) - Source: [xCnqkvF10to]
- In luma/chroma mode: S533 floating (filter disabled) - Source: [xCnqkvF10to]
- Additional transistors (TS514 etc.) handle chroma input switching - Source: [xCnqkvF10to]

#### Comb Filter Variant
- Some monitors have comb filter (delay line circuit) - Source: [xCnqkvF10to]
- Improves NTSC color decoding significantly - Source: [xCnqkvF10to]
- Uses R533 resistor for partial filter instead of full bypass - Source: [xCnqkvF10to]
- Comb defeat switch partially grounds vs fully grounds S533 - Source: [xCnqkvF10to]
