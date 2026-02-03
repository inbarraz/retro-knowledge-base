# ATI Technologies

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| Graphics Solution Rev 3 | Video Card (CGA/MDA) | [I-im7v0QVdw] |

## Platform-Specific Knowledge

### ATI Graphics Solution Rev 3

#### Overview
- Dual-mode CGA and MDA compatible video card - Source: [I-im7v0QVdw]
- Can display CGA color graphics OR MDA monochrome text - Source: [I-im7v0QVdw]
- Switchable between modes via DIP switch or jumper - Source: [I-im7v0QVdw]
- Popular card from early PC clone era - Source: [I-im7v0QVdw]

#### Character Generator ROM
- Contains font bitmaps for text mode display - Source: [I-im7v0QVdw]
- 8x8 or 8x14 pixel character cells depending on mode - Source: [I-im7v0QVdw]
- ROM failure causes garbled or missing characters - Source: [I-im7v0QVdw]
- Can be verified by reading character ROM data and comparing to known-good - Source: [I-im7v0QVdw]

#### Troubleshooting: Stuck Bit Analysis

##### Using ASCII Character Patterns
- Stuck bits cause predictable character substitutions - Source: [I-im7v0QVdw]
- Compare displayed character to expected character - Source: [I-im7v0QVdw]
- Convert both to binary, XOR to find stuck bit - Source: [I-im7v0QVdw]
- ASCII tables essential for this diagnosis - Source: [I-im7v0QVdw]

##### Example: Space Displayed as Zero
- Space character = ASCII 32 = 00100000 binary - Source: [I-im7v0QVdw]
- Zero character = ASCII 48 = 00110000 binary - Source: [I-im7v0QVdw]
- XOR result = 00010000 = bit 4 stuck at 1 - Source: [I-im7v0QVdw]
- Data bit 4 has problem in video RAM or data path - Source: [I-im7v0QVdw]

##### Confirming with Multiple Characters
- Check several character pairs to confirm pattern - Source: [I-im7v0QVdw]
- All substitutions should show same bit stuck - Source: [I-im7v0QVdw]
- Inconsistent results may indicate intermittent or multiple failures - Source: [I-im7v0QVdw]

#### Data Path Components

##### 74LS273 Octal D-Type Flip-Flop
- Latches character data between video RAM and character generator - Source: [I-im7v0QVdw]
- 8-bit latch, one bit per data line - Source: [I-im7v0QVdw]
- Failure of one flip-flop causes stuck bit on that data line - Source: [I-im7v0QVdw]
- Common failure point on Graphics Solution cards - Source: [I-im7v0QVdw]

##### Diagnosis Method
- Use oscilloscope to check data lines at 74LS273 - Source: [I-im7v0QVdw]
- Compare input pin activity to output pin activity - Source: [I-im7v0QVdw]
- Stuck output with active input = bad flip-flop - Source: [I-im7v0QVdw]
- All 8 bits should show similar activity patterns - Source: [I-im7v0QVdw]

##### Replacement
- 74LS273 is common part, widely available - Source: [I-im7v0QVdw]
- Replace with same family (LS) for proper timing - Source: [I-im7v0QVdw]
- Socket the replacement for easy future service - Source: [I-im7v0QVdw]
- Verify all data bits working after replacement - Source: [I-im7v0QVdw]

#### Video RAM Testing
- Video RAM can also cause stuck bit symptoms - Source: [I-im7v0QVdw]
- Test by writing test patterns to video memory - Source: [I-im7v0QVdw]
- Read back and compare - stuck bits show consistent errors - Source: [I-im7v0QVdw]
- Replace suspect RAM chips if testing confirms failure - Source: [I-im7v0QVdw]

#### Mode Selection
- DIP switches or jumpers select CGA vs MDA mode - Source: [I-im7v0QVdw]
- Must match monitor type connected - Source: [I-im7v0QVdw]
- CGA mode: Uses CGA-compatible monitor (color or mono) - Source: [I-im7v0QVdw]
- MDA mode: Uses MDA-compatible monochrome monitor - Source: [I-im7v0QVdw]

#### Connector Pinouts
- DE-9 connector for CGA mode output - Source: [I-im7v0QVdw]
- Different connector may be used for MDA mode - Source: [I-im7v0QVdw]
- Check card documentation for specific pinout - Source: [I-im7v0QVdw]

## Related Techniques

### Stuck Bit Diagnosis (General Video Cards)
- Applicable to any character-mode video card - Source: [I-im7v0QVdw]
- Works for CGA, MDA, Hercules, EGA text modes - Source: [I-im7v0QVdw]
- Does not apply to graphics mode issues - Source: [I-im7v0QVdw]
- ASCII table reference essential for diagnosis - Source: [I-im7v0QVdw]
