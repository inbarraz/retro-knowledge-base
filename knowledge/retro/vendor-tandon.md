# Tandon

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| TM-100 | 5.25" Floppy Drive | [M64hCqBpSDE] |
| TM-252 | MFM Hard Drive | [Rm7JubQdHIE] |

## Platform-Specific Knowledge

### Tandon TM-100 (5.25" Floppy Drive)

#### Overview
- 5.25" floppy disk drive - Source: [M64hCqBpSDE]
- Double-sided 48 TPI (tracks per inch) - Source: [M64hCqBpSDE]
- Shugart-compatible interface - Source: [M64hCqBpSDE]
- New old stock (NOS) units may still be available - Source: [M64hCqBpSDE]

#### Jumper Configuration
- Requires jumper configuration for drive select - Source: [M64hCqBpSDE]
- Drive select jumpers determine drive number (DS0-DS3) - Source: [M64hCqBpSDE]
- Most PC applications use DS1 (after cable twist) - Source: [M64hCqBpSDE]
- Check target system requirements before configuring - Source: [M64hCqBpSDE]

#### Testing NOS Drives
- NOS drives may work perfectly after decades in storage - Source: [M64hCqBpSDE]
- Clean heads with IPA before first use - Source: [M64hCqBpSDE]
- Check belt condition if drive uses belt drive - Source: [M64hCqBpSDE]
- Test with known-good floppy disk - Source: [M64hCqBpSDE]

#### Double-Sided Operation
- Can read/write both sides of floppy disk - Source: [M64hCqBpSDE]
- 48 TPI = 40 tracks per side - Source: [M64hCqBpSDE]
- Compatible with standard PC 360K format - Source: [M64hCqBpSDE]
- Also works with single-sided disks - Source: [M64hCqBpSDE]

### Tandon TM-252 (10MB MFM Hard Drive)

#### Overview
- 10 megabyte ST-506/MFM interface hard drive - Source: [Rm7JubQdHIE]
- Full height 5.25" form factor - Source: [Rm7JubQdHIE]
- Stepper motor actuator (not voice coil) - Source: [Rm7JubQdHIE]
- 4 heads (2 platters) - Source: [Rm7JubQdHIE]
- 306 cylinders, 17 sectors per track - Source: [Rm7JubQdHIE]
- Original retail price approximately $520 in 1985 - Source: [Rm7JubQdHIE]
- Low-level formatting required for use - Source: [Rm7JubQdHIE]

#### Controller Compatibility
- REQUIRES 8-bit XT-class MFM controller - Source: [Rm7JubQdHIE]
- Will NOT work with 16-bit AT-class MFM controllers - Source: [Rm7JubQdHIE]
- 8-bit controllers: Western Digital WD1002-WA2, similar - Source: [Rm7JubQdHIE]
- 16-bit controllers for AT-class machines incompatible - Source: [Rm7JubQdHIE]
- Controller type mismatch causes drive to appear dead - Source: [Rm7JubQdHIE]

#### 8-Bit vs 16-Bit MFM Controller Differences
- 8-bit controllers designed for XT-class PCs (4.77-8MHz) - Source: [Rm7JubQdHIE]
- 16-bit controllers designed for AT-class PCs (286+) - Source: [Rm7JubQdHIE]
- Both use same ST-506 interface to drive - Source: [Rm7JubQdHIE]
- Differences are in ISA bus interface and firmware - Source: [Rm7JubQdHIE]
- 8-bit controllers expect different timing than 16-bit - Source: [Rm7JubQdHIE]
- TM-252 specifically requires 8-bit controller timing - Source: [Rm7JubQdHIE]

#### Testing Notes
- Drive may spin up and appear healthy - Source: [Rm7JubQdHIE]
- "Drive not ready" error with wrong controller type - Source: [Rm7JubQdHIE]
- SpinRite II useful for drive surface testing - Source: [Rm7JubQdHIE]
- Interleave setting affects performance significantly - Source: [Rm7JubQdHIE]
- 80KB/sec with wrong interleave, 411KB/sec with correct - Source: [Rm7JubQdHIE]

#### Physical Condition Challenges
- Screws can become extremely stuck after 40 years - Source: [Rm7JubQdHIE]
- Impact driver (Ryobi or similar) essential for stuck screws - Source: [Rm7JubQdHIE]
- Standard screwdriver may strip screw heads - Source: [Rm7JubQdHIE]
- Stepper motor bearings may need lubrication - Source: [Rm7JubQdHIE]

#### Interleave Optimization
- Optimal interleave determined by SpinRite II testing - Source: [Rm7JubQdHIE]
- Wrong interleave causes severe performance loss - Source: [Rm7JubQdHIE]
- Speed Store utility can set interleave during low-level format - Source: [Rm7JubQdHIE]
- XT-class machines typically need 3:1 or 4:1 interleave - Source: [Rm7JubQdHIE]
