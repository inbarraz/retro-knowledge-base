# Plus Development Corporation

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| Plus Hardcard 20 | Hard Card (8-bit ISA, 20MB) | [cXbDSudlSTQ], [ehwtjy6skw4], [lzMoEwTTFJs] |
| Plus Hardcard 40 | Hard Card (8-bit ISA, 40MB) | [cXbDSudlSTQ], [ehwtjy6skw4] |

## Platform-Specific Knowledge

### Plus Hardcard Series

#### Overview
- Hard cards plug directly into ISA slot, no cables or external power needed - Source: [cXbDSudlSTQ]
- Designed for easy consumer upgrade of IBM PC 5150 and XT clones - Source: [cXbDSudlSTQ]
- Powered directly from ISA bus (no Molex power connector) - Source: [cXbDSudlSTQ]
- Contains custom 3.5" hard drives (not standard interface) - Source: [cXbDSudlSTQ]
- Has onboard BIOS ROM for hard drive initialization - Source: [cXbDSudlSTQ]
- Originally very expensive ($700 for 20MB, equivalent to $1500-2000 adjusted) - Source: [cXbDSudlSTQ]

#### Hardware Configuration
- PC/XT jumper for system compatibility - Source: [cXbDSudlSTQ]
- First/Second drive selection jumper - Source: [cXbDSudlSTQ]
- Hardcard 20: Uses 27C64 ROM chips (two) - Source: [cXbDSudlSTQ]
- Hardcard 40: Uses 27C256 ROM chips, different board layout - Source: [cXbDSudlSTQ]
- ROMs are not interchangeable between 20MB and 40MB versions - Source: [cXbDSudlSTQ]
- ROMs are one-time programmable (not reusable) - Source: [cXbDSudlSTQ]

#### Common Failure Modes
- Rubber bump stops inside drives turn to goo over time - Source: [cXbDSudlSTQ]
- Sticky goo prevents head assembly from moving - Source: [cXbDSudlSTQ]
- Stiction: heads stick to disc platters during storage - Source: [cXbDSudlSTQ]
- Controller failures cause inability to write (drive appears to degrade) - Source: [cXbDSudlSTQ]
- Very unreliable - most Plus hard cards found today don't work - Source: [cXbDSudlSTQ]

#### Troubleshooting
- No schematics available for repair - Source: [cXbDSudlSTQ]
- Cannot swap drives between cards (custom drives) - Source: [cXbDSudlSTQ]
- If doesn't work, usually not repairable - "they either work or they don't" - Source: [cXbDSudlSTQ]
- BIOS ROM at C800 conflicts with many other cards (XT-IDE, etc.) - Source: [cXbDSudlSTQ]
- Percussive maintenance can free stuck spindle but doesn't fix controller issues - Source: [cXbDSudlSTQ]

#### Stiction Recovery
- Hold drive and pivot around spindle axis - Source: [cXbDSudlSTQ]
- Hit sharply to break free stuck platters - Source: [cXbDSudlSTQ]
- May need to power on while hitting to spin up - Source: [cXbDSudlSTQ]

#### Hardcard 40 Specific
- Shows as two 20MB drives to DOS (limitation of DOS 3.3 max 32MB partition) - Source: [cXbDSudlSTQ]
- Divide utility exists to reconfigure as single large volume - Source: [cXbDSudlSTQ]
- Drive labeled E-RLL encoding with sector translation - Source: [cXbDSudlSTQ]
- Sector translation prevents standard low-level format tools from working - Source: [cXbDSudlSTQ]
- Drives run at 3000 RPM (unusual, most drives are 3600 RPM) - Source: [cXbDSudlSTQ]

#### Useful Utilities
- Divide: Utility to reconfigure volume sizes (available on Plus driver disks) - Source: [cXbDSudlSTQ]
- Plus Drive.sys: Driver needed in CONFIG.SYS for proper operation - Source: [cXbDSudlSTQ]

### Plus Acquisition by Quantum
- Quantum acquired Plus Corporation - Source: [cXbDSudlSTQ]
- Quantum Hardcard EZ series evolved from Plus designs - Source: [cXbDSudlSTQ]

### Plus Hardcard Follow-Up Testing

#### Hardcard 20 Update
- Works only on XT-class machines (8088/8086) - Source: [ehwtjy6skw4]
- Does NOT work on 286 machines (bus speed issues) - Source: [ehwtjy6skw4]
- PC/XT jumper: PC = first/only drive, XT = second drive - Source: [ehwtjy6skw4]
- Must set to "PC" if only hard drive in system - Source: [ehwtjy6skw4]
- Utility disc available at ibm-pc.org/firmware/other/plus%20hardcard/ - Source: [ehwtjy6skw4]
- Light.com: TSR shows Plus icon in corner when drive active - Source: [ehwtjy6skw4]
- Sound.com: Makes clicking noise through PC speaker for activity - Source: [ehwtjy6skw4]
- HCD menu system included for organizing large drive - Source: [ehwtjy6skw4]
- ATplus utility for AT machines (not for XT) - Source: [ehwtjy6skw4]

#### Hardcard 40 Status
- Confirmed dead - controller error 1701 on all tests - Source: [ehwtjy6skw4]
- May have worked on 286 due to different firmware - Source: [ehwtjy6skw4]
- Stiction still present - requires percussive maintenance - Source: [ehwtjy6skw4]
- 40MB version uses different board design than 20MB - Source: [ehwtjy6skw4]

#### Reddit Fix for Rubber Goo Problem
- Clean rubber goo from stop post inside drive - Source: [ehwtjy6skw4]
- Apply heat shrink tubing over cleaned post - Source: [ehwtjy6skw4]
- Prevents head assembly from getting stuck again - Source: [ehwtjy6skw4]
- Requires opening drive enclosure (risk of contamination) - Source: [ehwtjy6skw4]
- Reddit post: r/vintagecomputing/comments/16wqa83/ - Source: [ehwtjy6skw4]

### Plus Hardcard 20 Teardown Analysis

#### Internal Construction
- Contains custom 3.5" drive mechanism built by Quantum - Source: [lzMoEwTTFJs]
- Plus Development Corporation was actually Quantum internally - Source: [lzMoEwTTFJs]
- Drive mechanism is NOT a standard Quantum drive, custom design - Source: [lzMoEwTTFJs]
- Single-platter design with heads on both sides - Source: [lzMoEwTTFJs]
- All ISA bus powered (no external Molex connector) - Source: [lzMoEwTTFJs]

#### Head Positioning System
- Uses optical sensor for head positioning (unusual for hard drives) - Source: [lzMoEwTTFJs]
- Optical encoder wheel with slits, light shines through to sensor - Source: [lzMoEwTTFJs]
- Voice coil actuator moves head assembly - Source: [lzMoEwTTFJs]
- Voice coil magnets are weaker than modern neodymium drives - Source: [lzMoEwTTFJs]
- No modern-style servo patterns on platter surface - Source: [lzMoEwTTFJs]

#### Rubber Bump Stop Deterioration (Fatal Failure Mode)
- Rubber bump stops at each end of head travel prevent crash - Source: [lzMoEwTTFJs]
- Rubber deteriorates into sticky goo over 30-40 years - Source: [lzMoEwTTFJs]
- Same failure mode as cassette deck rubber belts - Source: [lzMoEwTTFJs]
- Goo prevents head assembly from moving freely - Source: [lzMoEwTTFJs]
- Head gets stuck at one end of travel, can't seek - Source: [lzMoEwTTFJs]
- Rubber deterioration is essentially a death sentence for these drives - Source: [lzMoEwTTFJs]
- Even cleaning the goo may not help if bearing is damaged - Source: [lzMoEwTTFJs]

#### Head Assembly Details
- Heads mounted on spring steel flexures (same as modern drives) - Source: [lzMoEwTTFJs]
- Springs keep heads floating on air cushion above platter - Source: [lzMoEwTTFJs]
- Contact start/stop design (heads land on platter when stopped) - Source: [lzMoEwTTFJs]
- Landing zone on platter where heads park - Source: [lzMoEwTTFJs]

#### Controller Board
- Contains ST-506/412 compatible interface logic - Source: [lzMoEwTTFJs]
- Handles all encoding/decoding on the card - Source: [lzMoEwTTFJs]
- MFM encoding like standard ST-506 drives - Source: [lzMoEwTTFJs]
- Has BIOS ROM for initialization - Source: [lzMoEwTTFJs]

#### Why These Drives Fail
- Not designed for multi-decade storage - Source: [lzMoEwTTFJs]
- Expected service life was 5-7 years - Source: [lzMoEwTTFJs]
- Rubber components degrade regardless of storage conditions - Source: [lzMoEwTTFJs]
- No replacement parts available - Source: [lzMoEwTTFJs]
- Custom drive mechanism means no donor swaps possible - Source: [lzMoEwTTFJs]
