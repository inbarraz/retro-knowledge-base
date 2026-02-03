# NEC

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| D5126 | MFM Hard Drive (20MB) | [CpQ2j2J6wL0] |

## Platform-Specific Knowledge

### D5126 (MFM Hard Drive)

#### Specifications
- Same specs as Seagate ST-225: 650 cylinders, 4 heads, 17 sectors per track - Source: [CpQ2j2J6wL0]
- Type 2 drive in BIOS configuration - Source: [CpQ2j2J6wL0]
- Stepper motor actuator - Source: [CpQ2j2J6wL0]
- Warning sticker: "Do not rotate stepper or disc damage may occur" - Source: [CpQ2j2J6wL0]

#### Common Faults
- "Drive error" at boot - drive not asserting ready signal - Source: [CpQ2j2J6wL0]
- May appear dead with original XT controller but work with different controller - Source: [CpQ2j2J6wL0]

#### Diagnostic Approaches
- Try different MFM controller before declaring drive dead - Source: [CpQ2j2J6wL0]
- Use Speed Store utility for diagnostics: seek test, read test, write test - Source: [CpQ2j2J6wL0]

#### Repair Techniques
- Low-level format can restore drives that appear non-functional - Source: [CpQ2j2J6wL0]
- Magnetic signal may fade over long storage - low-level format refreshes - Source: [CpQ2j2J6wL0]
- XT controllers require debug command to access low-level format menu in BIOS - Source: [CpQ2j2J6wL0]
- 80286+ controllers can use Speed Store or similar utilities - Source: [CpQ2j2J6wL0]
- Mr BIOS has built-in low-level format utility - Source: [CpQ2j2J6wL0]

#### Recovery Success
- Drive appeared dead in original XT, worked perfectly after low-level format with different controller - Source: [CpQ2j2J6wL0]
- ~300 KB/sec transfer speed after recovery - Source: [CpQ2j2J6wL0]
- Seek time: 78ms max, 17.5ms track-to-track - Source: [CpQ2j2J6wL0]

#### Labeling Recommendation
- Write "Type 2" on drive top for future reference - Source: [CpQ2j2J6wL0]
- Saves time looking up specs later - Source: [CpQ2j2J6wL0]
