# Mountain Technologies

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| Mountain 20MB Drivecard | Hard Card (8-bit ISA, 20MB) | [cXbDSudlSTQ] |

## Platform-Specific Knowledge

### Mountain Drivecard 20MB

#### Overview
- ISA 8-bit hard card with integrated MFM hard drive - Source: [cXbDSudlSTQ]
- Unlike Plus hard cards, uses standard ST-506/MFM interface drive - Source: [cXbDSudlSTQ]
- Mountain also manufactured tape drives - Source: [cXbDSudlSTQ]
- Made in Japan - Source: [cXbDSudlSTQ]

#### Hardware
- Standard MFM hard drive connectors on the drive itself - Source: [cXbDSudlSTQ]
- Drive can be removed and used with standard MFM controller - Source: [cXbDSudlSTQ]
- Uses Opti controller chip with Z8/Z80 microcontroller - Source: [cXbDSudlSTQ]
- Has 6116 SRAM chips (two) for controller buffer - Source: [cXbDSudlSTQ]
- Has decorative plastic trim cover for aesthetics - Source: [cXbDSudlSTQ]
- Stepper motor visible externally (not sealed in drive) - Source: [cXbDSudlSTQ]
- Has parking solenoid to lock head when powered off - Source: [cXbDSudlSTQ]

#### Controller Specifics
- Opti BIOS at C800 address - Source: [cXbDSudlSTQ]
- Controller handles low-level format directly - Source: [cXbDSudlSTQ]
- Speed Store utility can low-level format through Opti BIOS - Source: [cXbDSudlSTQ]

#### Common Issues
- Stiction: drive fails to spin up after long storage - Source: [cXbDSudlSTQ]
- Percussive maintenance can free stuck spindle - Source: [cXbDSudlSTQ]
- Drives with stiction will never be fully reliable again - Source: [cXbDSudlSTQ]

#### Controller Compatibility Warning
- Low-level format written by Opti controller NOT compatible with standard WD controllers - Source: [cXbDSudlSTQ]
- Moving drive to different controller brand requires complete re-low-level format - Source: [cXbDSudlSTQ]
- Hard drive error (1701) when using drive formatted by different controller = need low-level format - Source: [cXbDSudlSTQ]

#### Using Drive Outside Hard Card
- Can remove drive and connect to standard 16-bit MFM controller - Source: [cXbDSudlSTQ]
- Must low-level format when changing controllers - Source: [cXbDSudlSTQ]
- Standard MFM cables and power connector work - Source: [cXbDSudlSTQ]

#### Maintenance
- Must use PARK utility before powering off - Source: [cXbDSudlSTQ]
- Old drives require head parking to prevent media damage - Source: [cXbDSudlSTQ]
