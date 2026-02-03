# Sony

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| KLV-S19A10 | LCD Monitor/TV | [A6kfCOJHs2U] |
| KV-9400 | 9" Trinitron TV | [KwrXDv9wYZ4] |
| CPD-15F23 (Gateway Vivitron 15) | CRT Monitor | [Lt1NtRH4BOg] |
| Sony Computer Monitors (DAS) | CRT Monitor | [Lt1NtRH4BOg] |
| Sony Trinitron (various) | CRT TV | [m3ETdhOuZ2w] |
| KV-1221R | 12" Trinitron TV | [M5AYtjEk-nQ] |
| KV-1222R | 12" Trinitron TV | [YuTTLdqhN3o] |
| KV-1222RS | 12" Trinitron TV (Remote) | [TQVnlb3auVE] |
| KV-9PT50 | 9" Trinitron TV | [ZaFgRhXsFSs] |
| WatchCam FDM-030 | Miniature CRT Monitor | [Mf8zdOXndwY] |
| Watchman FD-10 | Portable B&W CRT TV | [nn76UCUIo3Q] |
| Watchman FD-10A | Portable B&W CRT TV | [TDV9ima4dbA] |
| Mega Watchman FD-500 | Portable B&W CRT TV/Radio | [nY38YvAMEFg] |
| Mega Watchman FD-510 | Portable B&W CRT TV/Radio | [nY38YvAMEFg] |
| CPD-1304 | 13" Trinitron Multiscan Monitor | [S6qUhbXqgUw] |

## Platform-Specific Knowledge

### Sony CPD-1304 Multiscan Monitor

#### Overview
- 13" Trinitron computer monitor from 1991 - Source: [S6qUhbXqgUw]
- Multiscan capability up to 1024x768 at 48kHz - Source: [S6qUhbXqgUw]
- VGA compatible at 31.5kHz - Source: [S6qUhbXqgUw]
- Uses 9-pin connector (not standard VGA) - Source: [S6qUhbXqgUw]
- Adapter cable with 9-pin to VGA included - Source: [S6qUhbXqgUw]

#### CRT Part Numbers
- M34JNQ15X (with anti-glare etched coating) - Source: [S6qUhbXqgUw]
- M34JNQ10X (shiny glass, otherwise compatible) - Source: [S6qUhbXqgUw]
- Last digit difference may only be coating type - Source: [S6qUhbXqgUw]

#### Internal Design
- RGB signals use coax cables from input to neck board - Source: [S6qUhbXqgUw]
- Provides clearest possible signal path - Source: [S6qUhbXqgUw]
- Neck board clamped to CRT (cannot simply unplug) - Source: [S6qUhbXqgUw]
- Heavy monitor construction with integrated clamp - Source: [S6qUhbXqgUw]

#### Common Capacitor Failures

##### High Heat Area Caps
- Section of board near CRT gets extremely hot - Source: [S6qUhbXqgUw]
- 47µF 100V caps commonly fail in this area - Source: [S6qUhbXqgUw]
- Four caps in this area, three found dead in example - Source: [S6qUhbXqgUw]
- Caps connected to R/B drive pots affect those colors - Source: [S6qUhbXqgUw]

##### Bias Circuit Caps
- 47µF 25V caps in bias circuit area - Source: [S6qUhbXqgUw]
- Multiple caps for R/G/B bias commonly fail - Source: [S6qUhbXqgUw]
- Green bias cap was only one that tested OK in example - Source: [S6qUhbXqgUw]
- Blue and red bias caps dead - Source: [S6qUhbXqgUw]

##### 180V Rail Bypass Cap
- 1µF 250V cap between 180V rail and ground - Source: [S6qUhbXqgUw]
- Critical failure mode: tests OK on LCR meter but leaks at voltage - Source: [S6qUhbXqgUw]
- Low voltage cap tester cannot detect this fault - Source: [S6qUhbXqgUw]
- Leakage pulls bias voltage toward ground - Source: [S6qUhbXqgUw]
- Symptom: One color (green) way too bright, others not visible - Source: [S6qUhbXqgUw]
- Replace with 450V rated cap for safety margin - Source: [S6qUhbXqgUw]

#### Diagnostic Techniques

##### Oscilloscope Signal Tracing
- RGB signals should be present at video processing IC input - Source: [S6qUhbXqgUw]
- Driver IC amplifies for cathode drive - Source: [S6qUhbXqgUw]
- Check cathode signals directly - should see all three colors - Source: [S6qUhbXqgUw]
- Compare DC levels between working and non-working cathodes - Source: [S6qUhbXqgUw]

##### Cathode Bias Understanding
- Cathode at ground = full brightness for that color - Source: [S6qUhbXqgUw]
- Cathode at high voltage = off for that color - Source: [S6qUhbXqgUw]
- Bias pot adjusts baseline level - Source: [S6qUhbXqgUw]
- Drive pot adjusts signal amplitude - Source: [S6qUhbXqgUw]
- 180V rail provides bias headroom - Source: [S6qUhbXqgUw]

##### Leaky Cap Test Method
- Disconnect color channel and adjust screen control - Source: [S6qUhbXqgUw]
- If other colors appear when problem color disconnected, signal is getting through - Source: [S6qUhbXqgUw]
- Problem is DC bias offset, not signal path - Source: [S6qUhbXqgUw]

#### CRT Swap Procedure
- Deflection yokes between monitors likely incompatible - Source: [S6qUhbXqgUw]
- Transfer deflection yoke from original CRT to new CRT - Source: [S6qUhbXqgUw]
- Transfer magnetic adjustment pieces and strips - Source: [S6qUhbXqgUw]
- Convergence will need extensive adjustment after swap - Source: [S6qUhbXqgUw]
- Static convergence easier than dynamic - Source: [S6qUhbXqgUw]
- May not achieve perfect results but can be acceptable - Source: [S6qUhbXqgUw]

#### Visual Symptoms of High Usage
- Black soot/dust buildup inside - Source: [S6qUhbXqgUw]
- Baked tape on CRT (brown, brittle) - Source: [S6qUhbXqgUw]
- Discoloration on PCBs - Source: [S6qUhbXqgUw]
- Worn/dim CRT with blurry text - Source: [S6qUhbXqgUw]

#### Geometry Controls
- V Size and other adjustments on side/rear - Source: [S6qUhbXqgUw]
- Screen control (G2) adjusts overall brightness - Source: [S6qUhbXqgUw]
- Focus control on flyback - Source: [S6qUhbXqgUw]
- Switch on side for size presets - Source: [S6qUhbXqgUw]


### Sony KLV-S19A10 LCD Monitor/TV

#### Overview
- 19" 16:9 LCD monitor/TV - Source: [A6kfCOJHs2U]
- Multi-input "jack of all trades" retro display - Source: [A6kfCOJHs2U]
- CCFL (cold cathode) backlight - Source: [A6kfCOJHs2U]
- Standard VESA mount compatible - Source: [A6kfCOJHs2U]
- Heavy due to built-in speakers - Source: [A6kfCOJHs2U]
- Separate large external power supply - Source: [A6kfCOJHs2U]

#### Inputs
- Composite video (2 inputs) - Source: [A6kfCOJHs2U]
- S-Video (shared with composite) - Source: [A6kfCOJHs2U]
- Component video (up to 1080i) - Source: [A6kfCOJHs2U]
- VGA (PC RGB) - Source: [A6kfCOJHs2U]
- HDMI - Source: [A6kfCOJHs2U]
- RF (analog tuner only) - Source: [A6kfCOJHs2U]

#### Picture Modes
- Vivid: Too bright, max backlight, excessive sharpening - Source: [A6kfCOJHs2U]
- Pro: Recommended mode, backlight manageable - Source: [A6kfCOJHs2U]
- Standard/Natural: Middle ground options - Source: [A6kfCOJHs2U]

#### Aspect Ratio Modes
- Normal: True 4:3 pillarboxed - Source: [A6kfCOJHs2U]
- Full: Stretches 4:3 to 16:9 evenly - Source: [A6kfCOJHs2U]
- Wide Zoom: Non-linear stretch (center less stretched than edges) - Source: [A6kfCOJHs2U]
- Zoom: Crops top/bottom, fills width - Source: [A6kfCOJHs2U]

#### Service Menu Access
- Display + 5 + Volume Up + Power On - Source: [A6kfCOJHs2U]
- Shows operating hours, version numbers - Source: [A6kfCOJHs2U]
- WB (White Balance) section has RGB Drive and RGB Black level controls - Source: [A6kfCOJHs2U]
- Default values typically 512 - Source: [A6kfCOJHs2U]
- Power cycle to exit service mode - Source: [A6kfCOJHs2U]

#### Known Issues/Limitations

##### Black Crush
- Loses detail in dark scenes - Source: [A6kfCOJHs2U]
- PLUGE bars not fully visible even at max brightness - Source: [A6kfCOJHs2U]
- Component input has less black crush than composite - Source: [A6kfCOJHs2U]
- Cannot be fully corrected via service menu - Source: [A6kfCOJHs2U]

##### Overscan
- Always crops edges on HDMI input - Source: [A6kfCOJHs2U]
- Always crops edges on composite/S-video - Source: [A6kfCOJHs2U]
- VGA input does NOT overscan (pixel-perfect possible) - Source: [A6kfCOJHs2U]

##### Input Limitations
- No PAL support (NTSC only) - Source: [A6kfCOJHs2U]
- VGA does NOT support 15kHz (no Amiga/ST/CoCo3 direct) - Source: [A6kfCOJHs2U]
- HDMI has forced overscan and appears to use DAC conversion - Source: [A6kfCOJHs2U]
- HDMI showed interference pattern (possible cap issue) - Source: [A6kfCOJHs2U]
- Very slow input switching (several seconds black screen) - Source: [A6kfCOJHs2U]
- VGA text mode (720x400) cannot be set to 4:3 - forced 16:9 small - Source: [A6kfCOJHs2U]

##### Composite Video Filter
- Color killer does not disable chroma filter - Source: [A6kfCOJHs2U]
- 80-column text always soft (unlike Apple monitors) - Source: [A6kfCOJHs2U]
- Workaround: Use S-video with Luma-only for sharp B&W text - Source: [A6kfCOJHs2U]

#### Compatibility Testing Results

##### Apple IIc
- Composite: 40-col readable, 80-col soft/blurry - Source: [A6kfCOJHs2U]
- S-video (Luma only): Sharp text but no color - Source: [A6kfCOJHs2U]
- Color graphics work with expected artifact coloring - Source: [A6kfCOJHs2U]
- H-Center adjustment available for Apple II horizontal shift - Source: [A6kfCOJHs2U]

##### Commodore 64
- Composite: Very good, sharp text, vibrant colors - Source: [A6kfCOJHs2U]
- S-video: Fantastic quality, super sharp - Source: [A6kfCOJHs2U]
- Handles 240p progressive scan perfectly (no interlace artifacts) - Source: [A6kfCOJHs2U]

##### Amiga 600
- Composite: Works, 80-col text readable-ish - Source: [A6kfCOJHs2U]
- VGA (15kHz): "Unsupported Video Format" - does not work - Source: [A6kfCOJHs2U]
- Rock-solid image on composite (no interference) - Source: [A6kfCOJHs2U]

##### DOS PC (VGA)
- 640x480: Works well in 4:3 mode, pixel-perfect available - Source: [A6kfCOJHs2U]
- 720x400 (text): Forced to small centered image, no 4:3 stretch - Source: [A6kfCOJHs2U]
- EGA (640x350): Bars on top/bottom, no proper scaling - Source: [A6kfCOJHs2U]
- Custom VGA modes (320x240): Works, recognized as 640x480 - Source: [A6kfCOJHs2U]
- Hardware scrolling games run perfectly smooth - Source: [A6kfCOJHs2U]

##### HDMI (720p from PC)
- Works but has overscan even at 800x600 - Source: [A6kfCOJHs2U]
- Text blurry (not pixel-perfect) - Source: [A6kfCOJHs2U]
- Suspected DAC conversion to component internally - Source: [A6kfCOJHs2U]

##### Component (Blu-ray player)
- 480i: Works perfectly - Source: [A6kfCOJHs2U]
- 480p: Works perfectly - Source: [A6kfCOJHs2U]
- 720p: Works - Source: [A6kfCOJHs2U]
- 1080i: Works - Source: [A6kfCOJHs2U]
- Rock-solid image quality - Source: [A6kfCOJHs2U]
- Better black level reproduction than composite - Source: [A6kfCOJHs2U]

#### Backlight Longevity
- CCFL backlights wear out over time - Source: [A6kfCOJHs2U]
- Reduce backlight setting via PWM to extend life - Source: [A6kfCOJHs2U]
- Pro mode uses lower backlight than Vivid - Source: [A6kfCOJHs2U]

#### Remote Control
- RM-Y8001 remote - Source: [A6kfCOJHs2U]
- "Wega Gate" button for menu access - Source: [A6kfCOJHs2U]
- Wide button cycles aspect ratio modes - Source: [A6kfCOJHs2U]
- TV Video button cycles inputs - Source: [A6kfCOJHs2U]
- Freeze button (pause frame) requires remote - Source: [A6kfCOJHs2U]

#### Physical Controls (no remote)
- TV Video, Wega Gate, Channel up/down, Volume up/down - Source: [A6kfCOJHs2U]
- Power, Enter buttons on top edge - Source: [A6kfCOJHs2U]
- Most functions accessible without remote - Source: [A6kfCOJHs2U]

### Sony KV-9400 (9" Trinitron TV)

#### Overview
- 9" Trinitron television from 1982 - Source: [KwrXDv9wYZ4]
- Small "kitchen TV" form factor - Source: [KwrXDv9wYZ4]
- Trinitron aperture grille technology (single-gun design) - Source: [KwrXDv9wYZ4]
- High quality picture for size - Source: [KwrXDv9wYZ4]

#### Tuner System

##### Channel Selection Mechanism
- Uses voltage-controlled tuner (varactor tuning) - Source: [KwrXDv9wYZ4]
- Channel preset buttons set specific tuning voltages - Source: [KwrXDv9wYZ4]
- Each button has corresponding trim pot for fine adjustment - Source: [KwrXDv9wYZ4]
- 12 preset channel buttons on front panel - Source: [KwrXDv9wYZ4]

##### AFT (Automatic Fine Tuning)
- AFT switch on back panel - Source: [KwrXDv9wYZ4]
- When enabled: TV automatically adjusts tuning for best picture - Source: [KwrXDv9wYZ4]
- When disabled: Manual tuning only (may be needed for edge channels) - Source: [KwrXDv9wYZ4]

#### Common Failure: Channel Selector Buttons

##### Symptoms
- Pressing channel button produces no response or wrong channel - Source: [KwrXDv9wYZ4]
- Some buttons work, others don't - Source: [KwrXDv9wYZ4]
- Buttons feel mushy or don't click properly - Source: [KwrXDv9wYZ4]

##### Cause
- Rubber membrane keyboard matrix switches deteriorate with age - Source: [KwrXDv9wYZ4]
- Conductive rubber pads lose conductivity over 40+ years - Source: [KwrXDv9wYZ4]
- Similar failure mode to VCR and remote control buttons - Source: [KwrXDv9wYZ4]

##### Repair Options
- Replace conductive rubber pads (if available) - Source: [KwrXDv9wYZ4]
- Apply conductive paint to existing pads (temporary fix) - Source: [KwrXDv9wYZ4]
- Remove failed switches entirely and hardwire to single channel - Source: [KwrXDv9wYZ4]
- In video: 12 bad switches removed, TV set to channel 3 only - Source: [KwrXDv9wYZ4]

#### External Video Input
- Rear panel has external video/audio input jacks - Source: [KwrXDv9wYZ4]
- Allows use as composite video monitor - Source: [KwrXDv9wYZ4]
- Bypasses tuner entirely when using external input - Source: [KwrXDv9wYZ4]
- Good for retro gaming and computer use - Source: [KwrXDv9wYZ4]

#### Maintenance

##### Scratchy Pots/Controls
- Volume and other controls may become scratchy with age - Source: [KwrXDv9wYZ4]
- Apply DeoxIT D5 to potentiometer shafts - Source: [KwrXDv9wYZ4]
- Work control back and forth to distribute cleaner - Source: [KwrXDv9wYZ4]
- May need to access pots internally for severe cases - Source: [KwrXDv9wYZ4]

##### General Reliability
- Trinitron TVs are generally reliable - Source: [KwrXDv9wYZ4]
- Main failures: Channel buttons, capacitors, solder joints - Source: [KwrXDv9wYZ4]
- CRT typically outlasts other components - Source: [KwrXDv9wYZ4]

### Sony DAS (Digital Alignment System) CRT Calibration

#### Overview
- Software-based calibration system for Sony CRT monitors from mid-1990s onward - Source: [Lt1NtRH4BOg]
- Replaces need for internal potentiometer adjustments - Source: [Lt1NtRH4BOg]
- Monitors store calibration data in internal EEPROM - Source: [Lt1NtRH4BOg]
- Without DAS software, many adjustments are inaccessible - Source: [Lt1NtRH4BOg]
- Applies to computer monitors, not consumer TVs - Source: [Lt1NtRH4BOg]

#### Gateway Vivitron 15 = Sony CPD-15F23
- Gateway sold OEM'd Sony monitors under "Vivitron" brand - Source: [Lt1NtRH4BOg]
- Vivitron 15 is Sony CPD-15F23 internally - Source: [Lt1NtRH4BOg]
- Uses same DAS calibration system - Source: [Lt1NtRH4BOg]
- Service menu and DAS compatible with Sony documentation - Source: [Lt1NtRH4BOg]

#### Serial Port Connection

##### Pinout (Service Port on Monitor)
- Pin 1: GND - Source: [Lt1NtRH4BOg]
- Pin 2: 5V power - Source: [Lt1NtRH4BOg]
- Pin 3: RXD (receive data) - Source: [Lt1NtRH4BOg]
- Pin 4: TXD (transmit data) - Source: [Lt1NtRH4BOg]

##### Signal Levels
- 5V TTL serial, NOT RS-232 - Source: [Lt1NtRH4BOg]
- RS-232 uses +/- 12V, will damage monitor - Source: [Lt1NtRH4BOg]
- Need USB-to-TTL adapter, NOT USB-to-serial - Source: [Lt1NtRH4BOg]

##### Recommended Adapters
- FTDI-based USB-TTL adapters work well - Source: [Lt1NtRH4BOg]
- CH340 adapters cause blue screens with DOS DAS software - Source: [Lt1NtRH4BOg]
- Clone FTDI chips may fail with newer Windows drivers - Source: [Lt1NtRH4BOg]
- Genuine FTDI adapters recommended for reliability - Source: [Lt1NtRH4BOg]

#### DAS Software Versions

##### DOS Versions
- DAS 3.5: Early DOS version - Source: [Lt1NtRH4BOg]
- DAS 5.7: Later DOS version with more monitor support - Source: [Lt1NtRH4BOg]
- DAS 1.45: Specific monitor family support - Source: [Lt1NtRH4BOg]
- DAS H1: Different monitor series - Source: [Lt1NtRH4BOg]
- DAS 1.07: Earlier revision - Source: [Lt1NtRH4BOg]
- Different versions support different monitor models - Source: [Lt1NtRH4BOg]
- Must use correct version for specific monitor - Source: [Lt1NtRH4BOg]

##### Windows Versions (WinDAS)
- WinDAS 1: Early Windows version - Source: [Lt1NtRH4BOg]
- WinDAS 3: More monitor support - Source: [Lt1NtRH4BOg]
- WinDAS 4: Later version with professional monitors - Source: [Lt1NtRH4BOg]
- WinDAS requires valid COM port - Source: [Lt1NtRH4BOg]
- May need to specify COM port in settings - Source: [Lt1NtRH4BOg]

##### Software Availability
- Archive.org has DAS software with dongle patches - Source: [Lt1NtRH4BOg]
- Original software required hardware dongle for access - Source: [Lt1NtRH4BOg]
- Patched versions remove dongle requirement - Source: [Lt1NtRH4BOg]
- Search "Sony DAS" on archive.org - Source: [Lt1NtRH4BOg]

#### Calibration Features

##### Geometry Adjustments
- Horizontal size and position - Source: [Lt1NtRH4BOg]
- Vertical size and position - Source: [Lt1NtRH4BOg]
- Pincushion and barrel correction - Source: [Lt1NtRH4BOg]
- Trapezoid (keystone) correction - Source: [Lt1NtRH4BOg]
- Rotation - Source: [Lt1NtRH4BOg]

##### Color Calibration
- RGB gain (drive) controls - Source: [Lt1NtRH4BOg]
- RGB bias (cutoff) controls - Source: [Lt1NtRH4BOg]
- White balance adjustment - Source: [Lt1NtRH4BOg]
- Grayscale tracking - Source: [Lt1NtRH4BOg]

##### Convergence
- Digital convergence adjustment - Source: [Lt1NtRH4BOg]
- Sub-pixel level precision on some models - Source: [Lt1NtRH4BOg]
- Grid pattern calibration screens - Source: [Lt1NtRH4BOg]

##### Focus
- Dynamic focus adjustment - Source: [Lt1NtRH4BOg]
- Corner focus optimization - Source: [Lt1NtRH4BOg]

#### Troubleshooting DAS Connection

##### No Communication
- Verify correct COM port in software - Source: [Lt1NtRH4BOg]
- Check TX/RX not swapped - Source: [Lt1NtRH4BOg]
- Verify 5V TTL levels (not RS-232) - Source: [Lt1NtRH4BOg]
- Try different USB-TTL adapter - Source: [Lt1NtRH4BOg]

##### Software Crashes
- CH340 adapters cause issues with DOS DAS - Source: [Lt1NtRH4BOg]
- Use FTDI-based adapter instead - Source: [Lt1NtRH4BOg]
- Run DOS versions in actual DOS, not DOSBox - Source: [Lt1NtRH4BOg]
- WinDAS may need compatibility mode on modern Windows - Source: [Lt1NtRH4BOg]

##### Wrong Monitor Detected
- Use DAS version specific to monitor model - Source: [Lt1NtRH4BOg]
- Monitor reports model ID over serial - Source: [Lt1NtRH4BOg]
- If ID not in database, software won't calibrate - Source: [Lt1NtRH4BOg]

#### Historical Context
- Sony moved to digital calibration in mid-1990s - Source: [Lt1NtRH4BOg]
- Eliminated internal potentiometers that drifted over time - Source: [Lt1NtRH4BOg]
- Service centers had DAS hardware and dongles - Source: [Lt1NtRH4BOg]
- Hobbyists now use patched software versions - Source: [Lt1NtRH4BOg]
- Monitors became difficult to service without DAS software - Source: [Lt1NtRH4BOg]

## General Notes on Consumer LCD TVs for Retro Use

### Composite Input Quality
- Most consumer LCDs keep chroma filter active even with no color signal - Source: [A6kfCOJHs2U]
- Results in soft 80-column text - Source: [A6kfCOJHs2U]
- Apple IIe/IIc color monitors are unique exception (auto-disable filter) - Source: [A6kfCOJHs2U]

### 240p Handling
- Important for retro gaming (consoles, computers) - Source: [A6kfCOJHs2U]
- Some LCDs show interlace artifacts on 240p - Source: [A6kfCOJHs2U]
- This Sony handles 240p correctly (smooth 60fps) - Source: [A6kfCOJHs2U]

### PAL Support
- Sony, Samsung, LG consumer sets (North American) typically don't support PAL - Source: [A6kfCOJHs2U]
- Chinese/Taiwan import brands often do support PAL - Source: [A6kfCOJHs2U]
- Sony PVMs support all standards (NTSC, PAL, SECAM variants) - Source: [A6kfCOJHs2U]

### Sony KV-1222RS (12" Trinitron TV with Remote)

#### Overview
- 12" Trinitron television from May 1984 - Source: [TQVnlb3auVE]
- RS = Remote Commander (remote control model) - Source: [TQVnlb3auVE]
- CRT part number: 330ADB22 - Source: [TQVnlb3auVE]
- Cool early 80s Sony aesthetic - silver bezel, boxy design - Source: [TQVnlb3auVE]
- Simulated wood grain on sides - Source: [TQVnlb3auVE]
- Handles on sides (like larger Sony TVs) - Source: [TQVnlb3auVE]
- Brushed metal door covers front controls - Source: [TQVnlb3auVE]

#### Controls
- Front panel: V-Hold, Hue, Color, Brightness, Auto Color - Source: [TQVnlb3auVE]
- Top panel: Picture (digital up/down), Normal/Cable TV switch - Source: [TQVnlb3auVE]
- Top panel: Add/Erase buttons for channel memory - Source: [TQVnlb3auVE]
- Master On/Off switch (disables power/remote) - Source: [TQVnlb3auVE]
- Soft power button (allows remote on/off) - Source: [TQVnlb3auVE]
- Headphone jack on side - Source: [TQVnlb3auVE]

#### Remote Control (RM-707)
- IR remote control (relatively new technology in 1984) - Source: [TQVnlb3auVE]
- Metal top construction - Source: [TQVnlb3auVE]
- Controls power, channel, volume, picture level - Source: [TQVnlb3auVE]
- Battery leakage common problem with age - Source: [TQVnlb3auVE]

#### Tuner Programming
- Digital channel memory system - Source: [TQVnlb3auVE]
- Type channel on remote, press Add to store - Source: [TQVnlb3auVE]
- Press Erase to remove channel from scan - Source: [TQVnlb3auVE]
- Channel up/down cycles through stored channels only - Source: [TQVnlb3auVE]
- LED display shows current channel number - Source: [TQVnlb3auVE]

#### RF Connections
- VHF: 75 ohm F connector (unusual - most had screw terminals) - Source: [TQVnlb3auVE]
- UHF: Still has screw terminals - Source: [TQVnlb3auVE]
- External antenna with slot-in mount system - Source: [TQVnlb3auVE]
- Coax-only RF path provides sharper picture than twin lead - Source: [TQVnlb3auVE]

#### Internal Design
- More integrated than KV-9400 (1982) despite only 2 years newer - Source: [TQVnlb3auVE]
- Multiple 40-pin DIP ICs handling tuner/control functions - Source: [TQVnlb3auVE]
- Remote amplifier board and channel display board on top - Source: [TQVnlb3auVE]
- Main A-board handles: VIF, Chroma, Audio, V deflection, power supply - Source: [TQVnlb3auVE]
- C-board (neck board) handles RGB output and drive/bias - Source: [TQVnlb3auVE]
- 23kV high voltage, not adjustable - Source: [TQVnlb3auVE]
- Dynamic convergence not adjustable (per label inside) - Source: [TQVnlb3auVE]

#### Accessible Adjustments (Back Panel)
- H-Stat (convergence for Trinitron) - Source: [TQVnlb3auVE]
- Focus - Source: [TQVnlb3auVE]
- Screen (G2/brightness) - Source: [TQVnlb3auVE]
- V-Size (through hole in case) - Source: [TQVnlb3auVE]

#### Neck Board Adjustments (C-Board)
- Blue Drive, Green Drive (Red not adjustable) - Source: [TQVnlb3auVE]
- Red Bias, Green Bias, Blue Bias - Source: [TQVnlb3auVE]
- Clear plastic cap covers high voltage connector for safety - Source: [TQVnlb3auVE]
- Use ceramic/plastic adjustment tool (non-conductive) - Source: [TQVnlb3auVE]

#### CRT Grayscale Calibration Procedure
- Turn color all the way down first - Source: [TQVnlb3auVE]
- Adjust brightness to just show gray bars - Source: [TQVnlb3auVE]
- Set Drive controls first for white balance - Source: [TQVnlb3auVE]
- Set Bias controls second for black level balance - Source: [TQVnlb3auVE]
- Go back and forth between drive and bias adjustments - Source: [TQVnlb3auVE]
- Best done in dark room - Source: [TQVnlb3auVE]
- Worn CRT will need blue/green drives turned up to compensate for weak guns - Source: [TQVnlb3auVE]

#### Worn CRT Symptoms
- Image too red/warm (red gun still strong, blue/green worn) - Source: [TQVnlb3auVE]
- Can be compensated by adjusting drive/bias - Source: [TQVnlb3auVE]
- If drives maxed out with no improvement, CRT is too far gone - Source: [TQVnlb3auVE]
- Blooming may occur if drives pushed too high - Source: [TQVnlb3auVE]

#### Purity Problems
- Color distortion in corners (green/blue missing) - Source: [TQVnlb3auVE]
- Visible on solid color screens (red/green/blue bars) - Source: [TQVnlb3auVE]
- May worsen when TV orientation changed - Source: [TQVnlb3auVE]
- Turn off, let cool, turn back on to degauss - Source: [TQVnlb3auVE]
- Persistent purity problems may indicate shadow mask damage - Source: [TQVnlb3auVE]
- Could be from being dropped or internal component shift - Source: [TQVnlb3auVE]

### Sony KV-9PT50 (9" Trinitron TV - CRT Anatomy Teardown)

#### Overview
- 9" Trinitron television from November 1997 - Source: [ZaFgRhXsFSs]
- Example unit was drop-damaged with cracked CRT neck - Source: [ZaFgRhXsFSs]
- Isolated power supply design - Source: [ZaFgRhXsFSs]
- Highly integrated (jungle IC handles most functions) - Source: [ZaFgRhXsFSs]

#### Drop Damage Assessment
- CRT glass cracked at neck = unfixable (lost vacuum) - Source: [ZaFgRhXsFSs]
- High voltage arcing occurs when vacuum lost - Source: [ZaFgRhXsFSs]
- Plastic case took brunt of impact, broke into pieces - Source: [ZaFgRhXsFSs]
- Sony's metal CRT mounting structure survived impact better than plastic - Source: [ZaFgRhXsFSs]
- Shadow mask on Trinitrons can warp from impact, causing unfixable purity issues - Source: [ZaFgRhXsFSs]
- Smaller 9" CRTs may be more resilient to impact than large TVs - Source: [ZaFgRhXsFSs]

#### CRT Part Number
- Sony A23LDU10X (23cm = 9 inch) - Source: [ZaFgRhXsFSs]
- Made in US - older TVs have inch measurements, 80s+ have metric - Source: [ZaFgRhXsFSs]

#### CRT Anatomy (Detailed Teardown)

##### Degaussing Coil
- Wire wrapped in black loops around front perimeter of CRT - Source: [ZaFgRhXsFSs]
- Sony routes along top edge only (not sides) on this model - Source: [ZaFgRhXsFSs]
- Thermistor cuts off degaussing current when warm (no relay) - Source: [ZaFgRhXsFSs]
- 60Hz/50Hz AC mains passes through briefly at power-on - Source: [ZaFgRhXsFSs]

##### Convergence Assembly
- Contains small magnets in sliding adjusters - Source: [ZaFgRhXsFSs]
- Affects alignment of RGB beams - Source: [ZaFgRhXsFSs]
- Glued in place at factory after adjustment - Source: [ZaFgRhXsFSs]
- B&W CRTs only need centering rings (no convergence assembly) - Source: [ZaFgRhXsFSs]

##### Deflection Yoke
- Coils that deflect electron beam horizontally and vertically - Source: [ZaFgRhXsFSs]
- Small magnets/strips inside for corner alignment - Source: [ZaFgRhXsFSs]
- Rubber bumpers position yoke precisely on CRT neck - Source: [ZaFgRhXsFSs]
- Factory tech adjusts position, then sticks bumpers to lock it - Source: [ZaFgRhXsFSs]
- Moving yoke forward/backward affects convergence - Source: [ZaFgRhXsFSs]
- Rotating yoke affects picture alignment - Source: [ZaFgRhXsFSs]

##### DAG (Aquadag) Coating
- Gray coating on outside of CRT glass - Source: [ZaFgRhXsFSs]
- Connected to ground via copper fingers or wire - Source: [ZaFgRhXsFSs]
- CRT is large capacitor: inside=high voltage, outside=ground - Source: [ZaFgRhXsFSs]

##### Implosion Band
- Metal band welded around front of CRT - Source: [ZaFgRhXsFSs]
- Provides strength to curved front glass under vacuum - Source: [ZaFgRhXsFSs]
- When curved glass compresses, band prevents expansion/implosion - Source: [ZaFgRhXsFSs]
- Never remove or modify implosion band - Source: [ZaFgRhXsFSs]

##### Electron Gun Assembly
- Three holes for RGB electron emission - Source: [ZaFgRhXsFSs]
- Trinitrons have guns in horizontal line (not triangle like shadow mask) - Source: [ZaFgRhXsFSs]
- Cathodes are heated by filament (like vacuum tube) - Source: [ZaFgRhXsFSs]
- G1, G2, G4 grids control brightness and focus - Source: [ZaFgRhXsFSs]
- Pins hermetically sealed into glass (vacuum tight) - Source: [ZaFgRhXsFSs]

##### Trinitron Shadow Mask (Aperture Grille)
- Thin wires (not dots like conventional shadow mask) - Source: [ZaFgRhXsFSs]
- RGB beams converge and wires create shadows - Source: [ZaFgRhXsFSs]
- Makes characteristic "ting" sound when tapped - Source: [ZaFgRhXsFSs]
- Very fragile to impact - can warp causing purity issues - Source: [ZaFgRhXsFSs]

#### PCB Architecture (1997 Era)

##### Neck Board
- Connects to CRT socket - Source: [ZaFgRhXsFSs]
- Three transistors for RGB cathode drive - Source: [ZaFgRhXsFSs]
- High voltage wires for focus/grid from flyback - Source: [ZaFgRhXsFSs]

##### Flyback Transformer
- Takes ~40V B+ and generates 18-20kV for CRT - Source: [ZaFgRhXsFSs]
- Switched at 15.6kHz (NTSC horizontal rate) - Source: [ZaFgRhXsFSs]
- Internal diode converts AC to DC - Source: [ZaFgRhXsFSs]
- Also generates G2, focus, and other auxiliary voltages - Source: [ZaFgRhXsFSs]
- Common failure: internal arcing when insulation breaks down - Source: [ZaFgRhXsFSs]
- Visual sign of failure: cracks in case, visible damage - Source: [ZaFgRhXsFSs]

##### Jungle IC
- Converts composite/S-video/component to RGB for cathodes - Source: [ZaFgRhXsFSs]
- On this set: also generates horizontal drive signal - Source: [ZaFgRhXsFSs]
- Handles vertical drive, dynamic convergence - Source: [ZaFgRhXsFSs]
- Has analog and digital RGB inputs - Source: [ZaFgRhXsFSs]
- Analog RGB input takes 0-0.7V signal (standard RGB level) - Source: [ZaFgRhXsFSs]
- I2C controllable - can switch between inputs - Source: [ZaFgRhXsFSs]

##### Microcontroller
- Under metal shield can - Source: [ZaFgRhXsFSs]
- Handles remote control, buttons, on-screen display - Source: [ZaFgRhXsFSs]
- Sends digital RGB OSD graphics to jungle IC - Source: [ZaFgRhXsFSs]
- Constantly sends commands to jungle IC over I2C - Source: [ZaFgRhXsFSs]
- May override user I2C commands (making mods difficult) - Source: [ZaFgRhXsFSs]

##### Tuner
- Large silver box, highly integrated - Source: [ZaFgRhXsFSs]
- Controlled via I2C from microcontroller - Source: [ZaFgRhXsFSs]
- Outputs video/audio to switcher chip - Source: [ZaFgRhXsFSs]

##### Power Supply
- Isolated switching design - Source: [ZaFgRhXsFSs]
- Generates 5V for logic and ~40V B+ for flyback - Source: [ZaFgRhXsFSs]
- Degaussing thermistor in this section - Source: [ZaFgRhXsFSs]

#### RGB Mod Potential
- Analog RGB input on jungle IC not connected (grounded through cap) - Source: [ZaFgRhXsFSs]
- Could inject 0-0.7V RGB to analog input pins - Source: [ZaFgRhXsFSs]
- Feed sync to composite video input - Source: [ZaFgRhXsFSs]
- Pin control or I2C to switch to RGB mode - Source: [ZaFgRhXsFSs]
- Challenge: microcontroller may constantly override I2C commands - Source: [ZaFgRhXsFSs]
- Some jungle ICs have undocumented datasheets making mods impossible - Source: [ZaFgRhXsFSs]

#### CRT Swap Considerations
- Trinitron CRTs may not be interchangeable between models - Source: [ZaFgRhXsFSs]
- High-res computer monitor CRTs incompatible with TV CRTs - Source: [ZaFgRhXsFSs]
- Deflection yoke setup must be redone for each CRT - Source: [ZaFgRhXsFSs]
- Convergence magnets need readjustment - Source: [ZaFgRhXsFSs]
- Service manual has alignment procedures - Source: [ZaFgRhXsFSs]

### Sony KV-1222R (12" Trinitron TV - Degaussing Case Study)

#### Overview
- 12" Trinitron television - Source: [YuTTLdqhN3o]
- Example unit had severe purity/color contamination issues - Source: [YuTTLdqhN3o]
- Used to demonstrate degaussing techniques - Source: [YuTTLdqhN3o]

#### Purity Problem Description
- Green/purple color contamination in corners and edges - Source: [YuTTLdqhN3o]
- Electron beam hitting wrong phosphor stripes - Source: [YuTTLdqhN3o]
- Built-in degauss coil unable to clear magnetization - Source: [YuTTLdqhN3o]
- External degaussing wand also ineffective - Source: [YuTTLdqhN3o]

#### Repair Attempt: External Degaussing
- Used bulk tape eraser as degaussing wand - Source: [YuTTLdqhN3o]
- Multiple passes across screen face with TV powered on - Source: [YuTTLdqhN3o]
- Pulled away slowly to 3+ feet before turning off degausser - Source: [YuTTLdqhN3o]
- Purity improved but not fully resolved - Source: [YuTTLdqhN3o]

#### Repair Workaround: Neodymium Magnets
- Small neodymium magnets placed on external case - Source: [YuTTLdqhN3o]
- Positioned near affected screen areas - Source: [YuTTLdqhN3o]
- Experimented with magnet orientation (flip, rotate) - Source: [YuTTLdqhN3o]
- Tiny position adjustments have large visual effect - Source: [YuTTLdqhN3o]
- Multiple magnets used for different problem areas - Source: [YuTTLdqhN3o]
- Taped in place once optimal position found - Source: [YuTTLdqhN3o]
- Result: Usable picture despite unresolved underlying issue - Source: [YuTTLdqhN3o]

#### Lessons Learned
- Some magnetization is too deep for degaussing to fix - Source: [YuTTLdqhN3o]
- Aperture grille or internal metal can hold permanent magnetism - Source: [YuTTLdqhN3o]
- Neodymium magnet trick is workaround, not proper repair - Source: [YuTTLdqhN3o]
- Start with weakest/smallest magnet available - Source: [YuTTLdqhN3o]
- Moving TV after magnet placement may shift compensation - Source: [YuTTLdqhN3o]

### Sony KV-1221R (12" Trinitron TV)

#### Overview
- 12" Trinitron television from 1982 - Source: [M5AYtjEk-nQ]
- Futuristic, unusual aesthetic design for the era - Source: [M5AYtjEk-nQ]
- Remote control included and functional - Source: [M5AYtjEk-nQ]
- Aperture grille Trinitron technology (single-gun design) - Source: [M5AYtjEk-nQ]

#### Tuning System
- Uses varactor tuning (voltage-controlled oscillator) - Source: [M5AYtjEk-nQ]
- No click-stop mechanical tuner - electronic tuning - Source: [M5AYtjEk-nQ]
- Tuner adjustment may be needed for proper channel reception - Source: [M5AYtjEk-nQ]

#### CRT Drive and Bias Adjustment

##### When to Adjust
- Weak or absent colors indicate drive/bias issues - Source: [M5AYtjEk-nQ]
- One gun weaker than others causes color shift - Source: [M5AYtjEk-nQ]
- Blue gun was weak on example unit - Source: [M5AYtjEk-nQ]

##### Adjustment Procedure
- Drive controls adjust brightness of each color gun - Source: [M5AYtjEk-nQ]
- Bias controls adjust black level of each color gun - Source: [M5AYtjEk-nQ]
- Adjust with gray ramp test pattern if available - Source: [M5AYtjEk-nQ]
- May need to increase weak gun drive to restore color balance - Source: [M5AYtjEk-nQ]

#### Power Supply Fault

##### Symptom
- TV turns off immediately after powering on - Source: [M5AYtjEk-nQ]
- Can be kept running by holding power button - Source: [M5AYtjEk-nQ]
- Automatic shutoff protection circuit triggering - Source: [M5AYtjEk-nQ]

##### Cause
- Likely capacitor failure in power supply - Source: [M5AYtjEk-nQ]
- Over-voltage or under-voltage protection may be tripping - Source: [M5AYtjEk-nQ]
- Requires capacitor testing/replacement to fix properly - Source: [M5AYtjEk-nQ]

##### Workaround
- Holding power button bypasses automatic shutoff - Source: [M5AYtjEk-nQ]
- Not recommended for long-term use - Source: [M5AYtjEk-nQ]
- Protection circuit exists for safety reasons - Source: [M5AYtjEk-nQ]

### Sony WatchCam FDM-030 (Miniature CRT Monitor)

#### Overview
- Flat CRT professional miniature monitor - Source: [Mf8zdOXndwY]
- Very small form factor with professional build quality - Source: [Mf8zdOXndwY]
- Uses BNC video input (75 ohm) - Source: [Mf8zdOXndwY]
- Designed for professional video monitoring applications - Source: [Mf8zdOXndwY]

#### Display Characteristics
- Darker phosphor coating for higher contrast ratio - Source: [Mf8zdOXndwY]
- Professional-grade CRT technology in miniature package - Source: [Mf8zdOXndwY]
- No external brightness control accessible - Source: [Mf8zdOXndwY]
- Fixed brightness level set for professional use - Source: [Mf8zdOXndwY]

#### Applications
- Portable video field monitoring - Source: [Mf8zdOXndwY]
- Compact monitoring station - Source: [Mf8zdOXndwY]
- Professional broadcast/production use - Source: [Mf8zdOXndwY]

### Sony Trinitron Flyback Replacement

#### Sourcing Parts
- Original Sony flyback transformers no longer available - Source: [m3ETdhOuZ2w]
- Donor boards from dead Sony TVs are best parts source - Source: [m3ETdhOuZ2w]
- Flyback must match specific model/series - Source: [m3ETdhOuZ2w]
- Different screen sizes use different flybacks - Source: [m3ETdhOuZ2w]

#### Flyback Compatibility
- Not all Sony flybacks are interchangeable - Source: [m3ETdhOuZ2w]
- Same screen size may use different flybacks in different years - Source: [m3ETdhOuZ2w]
- Check part numbers before attempting swap - Source: [m3ETdhOuZ2w]
- Some flybacks have different pin configurations - Source: [m3ETdhOuZ2w]

#### Repair vs Replace
- Flyback failure often means TV is economically dead - Source: [m3ETdhOuZ2w]
- If matching donor available, replacement worthwhile - Source: [m3ETdhOuZ2w]
- Consider keeping parts TVs for future repairs - Source: [m3ETdhOuZ2w]

### Sony Watchman FD-10A (Portable B&W CRT)

#### Overview
- Flat CRT black and white portable TV - Source: [TDV9ima4dbA]
- December 1991 manufacture date - Source: [TDV9ima4dbA]
- Later Watchman model (not first generation) - Source: [TDV9ima4dbA]
- 2" screen with slanted phosphor display - Source: [TDV9ima4dbA]

#### Display Technology
- Electron gun and deflection yoke on side of tube - Source: [TDV9ima4dbA]
- Electron beam shoots sideways, hits angled phosphor screen - Source: [TDV9ima4dbA]
- You look through electron beam path at phosphor - Source: [TDV9ima4dbA]
- Special circuitry handles geometric distortion from angled phosphor - Source: [TDV9ima4dbA]
- No tinted front glass - washed out in ambient light - Source: [TDV9ima4dbA]
- Later CRTs used tinted glass to improve contrast - Source: [TDV9ima4dbA]

#### Controls
- UHF/VHF band switch on side - Source: [TDV9ima4dbA]
- Power switch: Off, Sound Only, TV - Source: [TDV9ima4dbA]
- Volume control - Source: [TDV9ima4dbA]
- Tuning control (damped wheel mechanism) - Source: [TDV9ima4dbA]
- Earphone jack for private listening - Source: [TDV9ima4dbA]
- Telescoping antenna - Source: [TDV9ima4dbA]

#### Power
- Takes 4 AA batteries - Source: [TDV9ima4dbA]
- Battery cover may not fit with NiMH rechargeable batteries (slightly larger) - Source: [TDV9ima4dbA]
- DC 6V average power consumption 1.6W (~266mA) - Source: [TDV9ima4dbA]
- No external DC jack (cheap model) - Source: [TDV9ima4dbA]
- Must supply power directly to board for bench testing - Source: [TDV9ima4dbA]

#### Internal Design
- High voltage section with voltage tripler/quadrupler - Source: [TDV9ima4dbA]
- Two wires for horizontal deflection, two for vertical - Source: [TDV9ima4dbA]
- Red and blue wires go to high voltage section - Source: [TDV9ima4dbA]
- Small PCB with brightness pot (actually screen control, ~300V) - Source: [TDV9ima4dbA]
- Focus pot accessible through hole in side of case - Source: [TDV9ima4dbA]
- Ground clip on CRT must be connected when testing out of case - Source: [TDV9ima4dbA]

#### Common Issues

##### Vertical Deflection Fold-Over
- Image wraps around at bottom of screen - Source: [TDV9ima4dbA]
- Brighter strip visible at bottom where image folds - Source: [TDV9ima4dbA]
- Worse when set has been off for long time - Source: [TDV9ima4dbA]
- Improves after running for a while - Source: [TDV9ima4dbA]
- Cause: Bad capacitor in vertical deflection circuit - Source: [TDV9ima4dbA]

##### Diagnosing Bad Cap with Soldering Iron
- Heat each cap in deflection section while watching image - Source: [TDV9ima4dbA]
- Cap that affects deflection when heated is in deflection circuit - Source: [TDV9ima4dbA]
- Cap that makes problem WORSE when heated is bad cap - Source: [TDV9ima4dbA]
- In this case: 22µF 6.3V YEC brand cap - Source: [TDV9ima4dbA]
- Cap tested OK on LCR meter but had high ESR (~7 ohms) - Source: [TDV9ima4dbA]

##### Cap Replacement Fix
- Replace 22µF 6.3V with ceramic cap (non-polarized) - Source: [TDV9ima4dbA]
- Ceramic caps can be put in backwards - no polarity concern - Source: [TDV9ima4dbA]
- If cap too large for original location, solder on back of board - Source: [TDV9ima4dbA]
- Can use through-hole cap by soldering legs to SMD cap - Source: [TDV9ima4dbA]
- Fix completely eliminated fold-over problem - Source: [TDV9ima4dbA]

##### Band Switch Failure
- Switch becomes scratchy and unreliable - Source: [TDV9ima4dbA]
- Difficult to tune channels with dirty switch - Source: [TDV9ima4dbA]
- Switch may break when cleaning (extremely fragile) - Source: [TDV9ima4dbA]
- Fix: Remove switch entirely, jumper for UHF-only operation - Source: [TDV9ima4dbA]
- Identify which positions to bridge by measuring continuity - Source: [TDV9ima4dbA]

##### Dim Picture on Cold Start
- Picture very dim when first turned on - Source: [TDV9ima4dbA]
- Brightness comes up after warmup period - Source: [TDV9ima4dbA]
- Likely more caps failing in cathode drive circuit - Source: [TDV9ima4dbA]
- May also be worn CRT - Source: [TDV9ima4dbA]
- Service manual needed for further diagnosis - Source: [TDV9ima4dbA]
- FD-20 schematic available online, similar but not identical - Source: [TDV9ima4dbA]

#### Cap Brands
- YEC caps: Problematic brand, prone to failure - Source: [TDV9ima4dbA]
- Nichicon caps: Also present in set, mixed quality for era - Source: [TDV9ima4dbA]

#### Testing Notes
- Set to "Sound Only" draws 55mA vs 200mA with picture on - Source: [TDV9ima4dbA]
- Ground CRT DAG coating to board when testing outside case - Source: [TDV9ima4dbA]
- Small board near neck has ~300V - be careful - Source: [TDV9ima4dbA]
- Low current high voltage won't kill but will shock - Source: [TDV9ima4dbA]
- Use ceramic screwdriver to adjust pots safely - Source: [TDV9ima4dbA]

### Sony Watchman FD-10 (Portable B&W CRT)

#### Overview
- Flat CRT black and white portable TV - Source: [nn76UCUIo3Q]
- "Watchman" branding - iconic Sony portable line - Source: [nn76UCUIo3Q]
- Extremely compact form factor - Source: [nn76UCUIo3Q]
- Uses flat CRT technology (not standard round tube) - Source: [nn76UCUIo3Q]

#### Display Technology
- Flat tension mask CRT - Source: [nn76UCUIo3Q]
- Black and white only - Source: [nn76UCUIo3Q]
- Higher contrast than early LCD portables - Source: [nn76UCUIo3Q]
- Superior image quality to LCD TVs of same era - Source: [nn76UCUIo3Q]

#### Battery Operation
- Uses AA batteries - Source: [nn76UCUIo3Q]
- Battery life depends on CRT power consumption - Source: [nn76UCUIo3Q]
- More power-hungry than modern devices but reasonable for CRT - Source: [nn76UCUIo3Q]

#### Comparison to LCD Portables
- Much better picture quality than Casio LCD TVs - Source: [nn76UCUIo3Q]
- Better contrast and viewing angles - Source: [nn76UCUIo3Q]
- B&W only vs color LCD, but image clearer - Source: [nn76UCUIo3Q]
- Demonstrated technology advantage of CRT for the era - Source: [nn76UCUIo3Q]

### Sony Mega Watchman FD-500/FD-510

#### Overview
- Portable B&W CRT TV with AM/FM radio - Source: [nY38YvAMEFg]
- Approximately 3.5" CRT (not flat like smaller Watchmen) - Source: [nY38YvAMEFg]
- Large speaker on top with good sound quality - Source: [nY38YvAMEFg]
- "It's a Sony" sticker often left on by original owners - Source: [nY38YvAMEFg]
- FD-500 and FD-510 are similar with slight styling differences - Source: [nY38YvAMEFg]
- FD-510 has pull-out carrying handle, FD-500 has fold-out handle - Source: [nY38YvAMEFg]

#### Power
- Takes 8 D-cell batteries (impractical for modern use) - Source: [nY38YvAMEFg]
- DC barrel input (center negative, typical Sony) - Source: [nY38YvAMEFg]
- Also has AC mains transformer input - Source: [nY38YvAMEFg]
- Can be modified to use center positive by rewiring - Source: [nY38YvAMEFg]
- 12V operation - Source: [nY38YvAMEFg]

#### Controls
- TV band selector (VHF/UHF) - Source: [nY38YvAMEFg]
- Picture on/off (disable CRT to save battery while listening) - Source: [nY38YvAMEFg]
- Function selector: FM, AM, TV - Source: [nY38YvAMEFg]
- Tuning knob with dial cord mechanism - Source: [nY38YvAMEFg]
- Volume and tone controls - Source: [nY38YvAMEFg]
- Headphone jack on side - Source: [nY38YvAMEFg]

#### CRT Adjustments (side panel)
- Contrast control - Source: [nY38YvAMEFg]
- Brightness control - Source: [nY38YvAMEFg]
- Vertical hold control - Source: [nY38YvAMEFg]

#### Connectors
- External antenna input - Source: [nY38YvAMEFg]
- No composite video input on these models - Source: [nY38YvAMEFg]
- Composite mod possible by tapping into video circuit - Source: [nY38YvAMEFg]

#### Common Issues

##### Battery Corrosion
- D-cell batteries leak and corrode battery compartment - Source: [nY38YvAMEFg]
- Corrosion can spread to other components - Source: [nY38YvAMEFg]
- Clean with brush and neutralize with baking soda - Source: [nY38YvAMEFg]
- May need to remove battery terminals entirely - Source: [nY38YvAMEFg]

##### Dial Cord Failure
- Tuning dial cord breaks over time - Source: [nY38YvAMEFg]
- Results in tuner that doesn't respond to knob - Source: [nY38YvAMEFg]
- Repair requires disassembly and restringing - Source: [nY38YvAMEFg]
- Special dial cord string needed - Source: [nY38YvAMEFg]

#### Composite Mod Considerations
- B&W TV composite mods produce sharp image - Source: [nY38YvAMEFg]
- BUT: Contrast ratio varies with screen content (dark areas turn gray when little white on screen) - Source: [nY38YvAMEFg]
- This is characteristic of B&W TV cathode drive design - Source: [nY38YvAMEFg]
- No easy fix without redesigning cathode drive circuit - Source: [nY38YvAMEFg]
- Image sharper than RF but contrast behavior makes it less than ideal for computer display - Source: [nY38YvAMEFg]

#### FM Radio Quality
- Large speaker produces full sound - Source: [nY38YvAMEFg]
- Tone control allows good audio adjustment - Source: [nY38YvAMEFg]
- Sounds shockingly good compared to small Casio portables - Source: [nY38YvAMEFg]
- Worth keeping functional just for radio listening - Source: [nY38YvAMEFg]
