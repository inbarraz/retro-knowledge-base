# Samsung

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| CD-1452M | EGA Monitor | [7EezG5OzSQo] |

## Platform-Specific Knowledge

### Samsung CD-1452M EGA Monitor

#### Key Discovery: Identical to IBM 5154
- Samsung OEM'd the IBM 5154 EGA monitor - Source: [7EezG5OzSQo]
- FCC ID starts with same digits as IBM 5154 - Source: [7EezG5OzSQo]
- Internal layout, controls, schematics nearly identical - Source: [7EezG5OzSQo]
- Can use IBM 5154 SAMS service documentation for repairs - Source: [7EezG5OzSQo]
- SAMS available at: archive.org/details/Sams_IBM_5154_VDU - Source: [7EezG5OzSQo]

#### Differences from IBM 5154
- Decoder board not shielded (IBM has metal shield) - Source: [7EezG5OzSQo]
- Has green-only mode switch on front (IBM doesn't) - Source: [7EezG5OzSQo]
- Uses TTL logic instead of 28L22 PROM for color decoding - Source: [7EezG5OzSQo]

#### Specifications
- Dual-scan: 15.7kHz (CGA) and ~22kHz (EGA) - Source: [7EezG5OzSQo]
- 640x350 at 60Hz (EGA mode) - Source: [7EezG5OzSQo]
- 640x200/320x200 at 60Hz (CGA mode) - Source: [7EezG5OzSQo]
- Supports 64 colors in 640x350 mode - Source: [7EezG5OzSQo]
- Does NOT support VGA (31.5kHz minimum) - Source: [7EezG5OzSQo]
- 25kV high voltage via tripler - Source: [7EezG5OzSQo]
- Toshiba CRT inside - Source: [7EezG5OzSQo]

#### Controls
- Back panel: H Size 1, H Size 2, two recessed pots - Source: [7EezG5OzSQo]
- Side PCB: H Freq 1, H Freq 2, H Phase 1, H Phase 2 - Source: [7EezG5OzSQo]
- Contrast knob: Push in = fixed, Pull out = adjustable - Source: [7EezG5OzSQo]
- Front switch: Green-only mode (can repurpose for 64-color mod) - Source: [7EezG5OzSQo]

#### Power Supply Service
- Contains X2 REFAs that must be replaced - Source: [7EezG5OzSQo]
- Brown glue near power resistor damages nearby caps - Source: [7EezG5OzSQo]
- 1µF 50V cap near power resistor prone to failure - Source: [7EezG5OzSQo]
- B+ adjustment pot - don't touch without service manual - Source: [7EezG5OzSQo]

#### 64-Color EGA Mode Modification
- Most EGA monitors only decode 64 colors in 350-line mode - Source: [7EezG5OzSQo]
- Games like Iron Man support 64 colors in 320x200 mode - Source: [7EezG5OzSQo]
- Without mod: 320x200 mode stuck at 16 colors - Source: [7EezG5OzSQo]
- Vertical sync polarity signals mode to monitor - Source: [7EezG5OzSQo]

#### Mod Procedure (Samsung CD-1452M)
1. Locate 4077 chip output (pin 10) going to 74LS157 (pin 1) - Source: [7EezG5OzSQo]
2. Remove jumper link between the two chips - Source: [7EezG5OzSQo]
3. Add 1K pull-down resistor from 74LS157 pin 1 to ground - Source: [7EezG5OzSQo]
4. Wire front green switch between the two jumper link pads - Source: [7EezG5OzSQo]
5. Switch out = automatic mode, Switch in = forced 64-color mode - Source: [7EezG5OzSQo]

#### Mod Notes
- IBM 5154 uses 28L22 PROM instead of 74LS157 - same principle - Source: [7EezG5OzSQo]
- IBM: Pin 4 on 28L22 is the mode select input - Source: [7EezG5OzSQo]
- 10K pull-down may work on IBM; Samsung needed 1K - Source: [7EezG5OzSQo]

### Historical Context

#### EGA Monitor Era
- EGA released 1984 with IBM 5154 - first commercial multiscan monitor - Source: [7EezG5OzSQo]
- VGA arrived 1987 - EGA monitors quickly obsolete - Source: [7EezG5OzSQo]
- Most EGA monitors had short useful life (3-4 years) - Source: [7EezG5OzSQo]
- VGA monitors dropped support for 15kHz scan rates - Source: [7EezG5OzSQo]
- True multisync monitors (CGA+EGA+VGA) were expensive and short-lived - Source: [7EezG5OzSQo]
