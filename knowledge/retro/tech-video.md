# Video Capture and Conversion Techniques

> Part of the retro knowledge base. See also: tech-*.md files for other categories.

## Contents
- [Video Chip Breakout Boards](#video-chip-breakout-boards)
- [Lumacode Video Digitizer](#lumacode-video-digitizer)
- [Video Capture and Digitization](#video-capture-and-digitization)
- [SCART RGB Modification (Commodore 1084)](#scart-rgb-modification-commodore-1084)
- [VGA Scan Converters](#vga-scan-converters)

## Video Chip Breakout Boards

### 6847 Video Chip RGB Breakout
- Small breakout board designed by Coconut Bob - Source: [eFatlDatjZM]
- Installs under motherboard over 6847 chip pins - Source: [eFatlDatjZM]
- Provides easy access to video signals for RGB-to-HDMI mods - Source: [eFatlDatjZM]
- Uses pin header or direct wire connections - Source: [eFatlDatjZM]
- Ground, PB, 5V, and other signals broken out - Source: [eFatlDatjZM]
- Compatible systems: TRS-80 CoCo, Dragon 32, Laser 200, MC-10, others - Source: [eFatlDatjZM]
- Much easier than soldering directly to chip pins - Source: [eFatlDatjZM]

## Lumacode Video Digitizer

### Overview
- Lumacode is a digital video signal method for VIC-20 and C64 - Source: [Ga8mk2ErS7w]
- Developed by c0pperdragon as alternative to analog luma conversion - Source: [Ga8mk2ErS7w]
- Encodes pixel data digitally via VIC chip timing - Source: [Ga8mk2ErS7w]
- Requires firmware on RGB2HDMI (or similar) to decode - Source: [Ga8mk2ErS7w]
- Provides perfect pixel-accurate capture with no analog noise - Source: [Ga8mk2ErS7w]

### Installation Requirements
- Lumacode board connects to VIC chip (VIC-II on C64, VIC on VIC-20) - Source: [Ga8mk2ErS7w]
- Different board versions for different machines - Source: [Ga8mk2ErS7w]
- Signal connects to RGB2HDMI analog comparator board - Source: [Ga8mk2ErS7w]

### RGB2HDMI Analog Comparator Wiring (Critical)
- MUST use both pin 2 AND pin 4 for Lumacode signal - Source: [Ga8mk2ErS7w]
- Using only one pin causes missing color data - Source: [Ga8mk2ErS7w]
- Both pins should have Lumacode signal connected - Source: [Ga8mk2ErS7w]
- Common mistake to only wire one pin and get incomplete colors - Source: [Ga8mk2ErS7w]
- Refer to c0pperdragon documentation for exact wiring - Source: [Ga8mk2ErS7w]

### Firmware Configuration
- RGB2HDMI needs specific profile for Lumacode - Source: [Ga8mk2ErS7w]
- Select "Lumacode" as input type in menu - Source: [Ga8mk2ErS7w]
- Different profiles for VIC-20 vs C64 - Source: [Ga8mk2ErS7w]

## Video Capture and Digitization

### Extron RGB-HDMI 300A as Capture Device
- Professional broadcast-grade VGA to HDMI converter - Source: [Ga8mk2ErS7w]
- Handles non-standard resolutions that consumer scalers reject - Source: [Ga8mk2ErS7w]
- Auto-learns timing from input signals - Source: [Ga8mk2ErS7w]
- Useful for capturing from retro computers with odd video timings - Source: [Ga8mk2ErS7w]
- Output goes to standard HDMI capture card - Source: [Ga8mk2ErS7w]
- Available used from broadcast equipment surplus - Source: [Ga8mk2ErS7w]

### Capture vs Display Considerations
- Monitors often more forgiving than capture cards for odd timings - Source: [Ga8mk2ErS7w]
- Capture cards expect standard timings (1080p, 720p, etc.) - Source: [Ga8mk2ErS7w]
- Extron boxes bridge the gap between retro output and capture card input - Source: [Ga8mk2ErS7w]

### Video Capture Tools for Retro Setup

#### Elgato HD60S
- HDMI capture device for streaming/recording - Source: [uaVuXCqab2U]
- Requires USB 3.0 for full bandwidth - Source: [uaVuXCqab2U]
- Works well with OBS for capture - Source: [uaVuXCqab2U]
- Need scan converter/scaler before Elgato for retro sources - Source: [uaVuXCqab2U]

#### Open Source Scan Converter (OSSC)
- Line doubler/scaler for retro video - Source: [uaVuXCqab2U]
- Handles 15kHz RGB, component, composite signals - Source: [uaVuXCqab2U]
- Low latency design for gaming - Source: [uaVuXCqab2U]
- Outputs to HDMI for modern displays/capture - Source: [uaVuXCqab2U]
- Open source firmware, regularly updated - Source: [uaVuXCqab2U]

#### RetroTink 2X Pro
- Simple plug-and-play retro video converter - Source: [uaVuXCqab2U]
- Handles composite, S-Video, component to HDMI - Source: [uaVuXCqab2U]
- Good for quick setup without complex configuration - Source: [uaVuXCqab2U]
- Less flexible than OSSC but easier to use - Source: [uaVuXCqab2U]

#### USB 3.0 Bandwidth Considerations
- Video capture requires sustained USB 3.0 bandwidth - Source: [uaVuXCqab2U]
- Sharing USB controller with other devices can cause drops - Source: [uaVuXCqab2U]
- Dedicated USB 3.0 port recommended for capture devices - Source: [uaVuXCqab2U]

## SCART RGB Modification (Commodore 1084)

### Overview
- Ultimate mod co-developed by Adrian (ADB) and Mark (The Retro Channel) - Source: [gISS9JsnRX8]
- Phillips/boxy 1084 already has SCART footprint on PCB - Source: [gISS9JsnRX8]
- Instructions: imgur.com/gallery/1084s-scart-mod-component-locations-xMcx2ZE - Source: [gISS9JsnRX8]
- Companion video by Mark at Retro Channel has detailed walkthrough - Source: [gISS9JsnRX8]

### SCART Pin Functions
- Pin 16: Fast blanking (switches monitor to RGB mode when high) - Source: [gISS9JsnRX8]
- Pin 20: Composite video input (provides sync for RGB) - Source: [gISS9JsnRX8]
- Pins 7,11,15: RGB video inputs - Source: [gISS9JsnRX8]
- Game consoles send 12V to pin 16 to enable RGB mode - Source: [gISS9JsnRX8]

### The PlayStation Problem
- PS1/PS2 output RGB with sync embedded in composite video - Source: [gISS9JsnRX8]
- Monitor's D-connector expects TTL sync, not composite video - Source: [gISS9JsnRX8]
- Without mod: Picture rolls when complex graphics appear - Source: [gISS9JsnRX8]
- Sync separator IC gets confused by video content in composite signal - Source: [gISS9JsnRX8]
- Simple sync mod doesn't fully solve problem (still has sync issues) - Source: [gISS9JsnRX8]

### Ultimate Mod Solution (VCR Switch Repurpose)
- Uses VCR switch on back to force RGB mode - Source: [gISS9JsnRX8]
- VCR switch normally enables "freewheel sync" for PAL VCRs - Source: [gISS9JsnRX8]
- Repurpose: Wire 10K resistor + 1N4148 diode from switch to switching IC - Source: [gISS9JsnRX8]
- Diode band faces front of monitor - Source: [gISS9JsnRX8]
- Effect: Push switch = force RGB mode with sync from composite jack - Source: [gISS9JsnRX8]

### Wiring for PlayStation (with VCR mod)
- RGB cables to D-jack (analog RGB input) - Source: [gISS9JsnRX8]
- Composite video cable to yellow composite jack - Source: [gISS9JsnRX8]
- Push VCR switch in = RGB mode with proper sync - Source: [gISS9JsnRX8]
- Push VCR switch out = composite video mode - Source: [gISS9JsnRX8]

### Audio Mod (Mono Monitors)
- Install 22k resistor at R303 - Source: [gISS9JsnRX8]
- Install 5.6k resistors at R305 and R306 - Source: [gISS9JsnRX8]
- These combine stereo SCART audio to mono - Source: [gISS9JsnRX8]
- Properly combines via voltage divider (won't overload input) - Source: [gISS9JsnRX8]
- Add jumper link J9275 to connect to audio circuitry - Source: [gISS9JsnRX8]

### Jumper Links to Check/Add
- Some jumper links vary between monitors - Source: [gISS9JsnRX8]
- J9289: May or may not be installed, check your board - Source: [gISS9JsnRX8]
- J9281: May already be installed on some boards - Source: [gISS9JsnRX8]
- Connect SCART composite pin 20 to yellow composite jack - Source: [gISS9JsnRX8]

### SCART Connector Installation
- PCB footprint already exists - just desolder holes - Source: [gISS9JsnRX8]
- Case has cutout with blanking plate (often missing/broken) - Source: [gISS9JsnRX8]
- SCART jack mounts directly to PCB footprint - Source: [gISS9JsnRX8]

### Compatibility After Mod
- SCART composite video + audio: Works normally - Source: [gISS9JsnRX8]
- SCART RGB with fast blanking (game consoles): Works automatically - Source: [gISS9JsnRX8]
- D-jack TTL RGB (CGA): Still works exactly as before - Source: [gISS9JsnRX8]
- D-jack analog RGB (Amiga): Still works exactly as before - Source: [gISS9JsnRX8]
- Luma/Chroma, composite: All still work as before - Source: [gISS9JsnRX8]

## VGA Card Testing and Benchmarking

### vidp speed Utility
- DOS utility for benchmarking ISA video card performance - Source: [Yew71A7IaIQ]
- Tests different video modes: 40x25 text, 80x25 text, 320x200x256 graphics - Source: [Yew71A7IaIQ]
- Run with "0" and "1" for standard modes, "L" for 320x200x256 - Source: [Yew71A7IaIQ]
- Use "+" to enumerate all SVGA extended modes - Source: [Yew71A7IaIQ]
- Results in bytes/kilobytes per millisecond - Source: [Yew71A7IaIQ]
- Good ISA VGA card achieves ~7KB/ms; slower cards ~2-3KB/ms - Source: [Yew71A7IaIQ]
- 8-bit slot operation approximately halves throughput - Source: [Yew71A7IaIQ]

### VGA Card ISA Bus Speed
- ISA bus speed significantly affects video performance - Source: [Yew71A7IaIQ]
- Standard ISA bus: 8MHz; some motherboards allow 10MHz+ - Source: [Yew71A7IaIQ]
- Configure in BIOS: Auto-config or manual clock divider setting - Source: [Yew71A7IaIQ]
- 40MHz CPU / 4 = 10MHz ISA bus (example divider calculation) - Source: [Yew71A7IaIQ]
- Most cards tolerate higher bus speeds; test stability - Source: [Yew71A7IaIQ]
- All ISA cards must tolerate same speed (ROM card, IDE controller) - Source: [Yew71A7IaIQ]

### VGA Capture Device Issues
- Some VGA cards don't play well with capture devices - Source: [Yew71A7IaIQ]
- Symptoms: Shimmering lines, offset image despite working on monitor - Source: [Yew71A7IaIQ]
- VGA DOS modes: 720x400 (text) and 640x400 (graphics) both at 70Hz - Source: [Yew71A7IaIQ]
- Capture devices may confuse these two modes - Source: [Yew71A7IaIQ]
- Extron RGB-HDMI 300A requires serial port profiles for each mode - Source: [Yew71A7IaIQ]
- Create separate profiles for 720x400 and 640x400 with Elgato Stream Deck - Source: [Yew71A7IaIQ]
- Phase adjustment critical for eliminating shimmer - Source: [Yew71A7IaIQ]

### Multi-Mode VGA Cards (VGA/EGA/CGA)
- Dual output: Analog HD15 (VGA) and digital DE-9 (TTL) - Source: [Yew71A7IaIQ]
- DIP switches select monitor type (CGA, MDA, EGA, VGA, multisync) - Source: [Yew71A7IaIQ]
- Some modes require specific switch settings or system hangs - Source: [Yew71A7IaIQ]
- VGA Color mode limits max resolution to 640x480 - Source: [Yew71A7IaIQ]
- TTL digital output can run VGA timings on multisync TTL monitors - Source: [Yew71A7IaIQ]
- Performance in EGA mode often faster than actual EGA cards - Source: [Yew71A7IaIQ]
- Jack-of-all-trades cards useful for systems with various monitors - Source: [Yew71A7IaIQ]

### RGB2HDMI with VGA Timing TTL
- RGB2HDMI can capture VGA-timed TTL output from multi-mode cards - Source: [Yew71A7IaIQ]
- Select OTI VGA profile or create custom profile - Source: [Yew71A7IaIQ]
- 320x200 mode outputs as 640x400 (scan doubled) - Source: [Yew71A7IaIQ]
- May need separate profiles for text (720x400) vs graphics (640x400) - Source: [Yew71A7IaIQ]
- Auto-config may help with geometry and shimmer issues - Source: [Yew71A7IaIQ]
- Color palette limited to 16 TTL colors (no VGA palette support) - Source: [Yew71A7IaIQ]

## VGA Scan Converters

### GBS-8200 with GBS Control Mod

#### Overview
- GBS-8200: Cheap Chinese VGA signal converter (~$20-30) - Source: [ND0BH5ePRIE]
- Converts various input signals to VGA output - Source: [ND0BH5ePRIE]
- Stock firmware has limitations and poor quality - Source: [ND0BH5ePRIE]
- GBS Control mod dramatically improves quality and features - Source: [ND0BH5ePRIE]

#### GBS Control Hardware
- ESP8266 module replaces stock microcontroller - Source: [ND0BH5ePRIE]
- Si5351A clock generator provides custom output frequencies - Source: [ND0BH5ePRIE]
- WiFi interface for configuration and updates - Source: [ND0BH5ePRIE]
- Much better deinterlacing than stock firmware - Source: [ND0BH5ePRIE]

#### Si5351A Clock Generator
- Replaces fixed oscillator with programmable clock - Source: [ND0BH5ePRIE]
- Allows custom output resolutions and refresh rates - Source: [ND0BH5ePRIE]
- Can generate frequencies from 8kHz to 160MHz - Source: [ND0BH5ePRIE]
- Key component for improved sync handling - Source: [ND0BH5ePRIE]

#### Resources
- GitHub: github.com/ramapcsx2/gbs-control - Source: [ND0BH5ePRIE]
- Makes $25 converter comparable to much more expensive scalers - Source: [ND0BH5ePRIE]

## Security Monitors for Retro Computing

### Overview
- Security monitors continued production long after consumer CRT TVs discontinued - Source: [O4eidkDuegQ]
- Square cubicle form factor designed for stacking/mounting - Source: [O4eidkDuegQ]
- Often multi-format (NTSC/PAL) unlike consumer North American TVs - Source: [O4eidkDuegQ]
- Metal cases with handles, built for durability - Source: [O4eidkDuegQ]
- Companies kept buying them to match existing security furniture - Source: [O4eidkDuegQ]

### Speco ProVideo VM-1401C

#### Overview
- 14" (13" US designation) security monitor - Source: [O4eidkDuegQ]
- Supports both NTSC and PAL (rare in North America) - Source: [O4eidkDuegQ]
- Has S-Video input - Source: [O4eidkDuegQ]
- Built-in speaker (tinny audio but functional) - Source: [O4eidkDuegQ]
- Metal case with handles, stackable design - Source: [O4eidkDuegQ]
- Made in Taiwan - Source: [O4eidkDuegQ]

#### Main IC: Philips TDA8361
- Single "jungle IC" handles video decoding - Source: [O4eidkDuegQ]
- Same family as chips in Philips/Magnavox consumer TVs - Source: [O4eidkDuegQ]
- Supports tuner input (unused on this monitor) - Source: [O4eidkDuegQ]
- Has RGB input pins for on-screen display (can be used for RGB mod) - Source: [O4eidkDuegQ]
- Automatic PAL height compensation - Source: [O4eidkDuegQ]

#### Connectors
- Video In and Video Out (BNC) for daisy chaining - Source: [O4eidkDuegQ]
- 75 ohm termination switch (High/Low) - Source: [O4eidkDuegQ]
- S-Video/Composite switch - Source: [O4eidkDuegQ]
- RCA audio jacks - Source: [O4eidkDuegQ]

#### RGB Mod Potential

##### TDA8361 RGB Input (Pin 21)
- RGB input exists for on-screen display function - Source: [O4eidkDuegQ]
- Expects 0-0.7V signal (same as Amiga and other RGB sources) - Source: [O4eidkDuegQ]
- Fast blanking input switches monitor to RGB mode - Source: [O4eidkDuegQ]

##### Mod Components Needed
- 75 ohm termination resistors to ground - Source: [O4eidkDuegQ]
- Coupling capacitors - Source: [O4eidkDuegQ]
- Protection diodes (recommended) - Source: [O4eidkDuegQ]
- Fast blanking signal needs to be >1V (up to 5V is fine) - Source: [O4eidkDuegQ]

##### Sync Handling
- Composite video input provides sync for RGB mode - Source: [O4eidkDuegQ]
- No separate sync input needed - Source: [O4eidkDuegQ]

#### Multi-Format Support
- NTSC and PAL auto-detection - Source: [O4eidkDuegQ]
- Tint control only works in NTSC (PAL doesn't need it) - Source: [O4eidkDuegQ]
- Automatic vertical size adjustment for PAL's extra lines - Source: [O4eidkDuegQ]
- No external geometry controls, all automatic - Source: [O4eidkDuegQ]

#### S-Video Mode
- Enables external chrominance input - Source: [O4eidkDuegQ]
- Disables internal chroma trap filter - Source: [O4eidkDuegQ]
- Much sharper image than composite - Source: [O4eidkDuegQ]
- Can also be used for sharp monochrome input (Apple II text mode) - Source: [O4eidkDuegQ]

#### Build Quality
- High quality capacitors (Jamicon, Fuji) - Source: [O4eidkDuegQ]
- Hot glue securing components (not corrosive RTV) - Source: [O4eidkDuegQ]
- Multi-CRT size support (10" to 21" boards exist) - Source: [O4eidkDuegQ]
- Very clean inside due to vents only on sides/back, not top - Source: [O4eidkDuegQ]

#### Known Issues

##### Worn CRT Symptoms
- Burn-in visible from security camera text overlays - Source: [O4eidkDuegQ]
- Phosphor modeling from thousands of hours of use - Source: [O4eidkDuegQ]
- Dim image requiring max contrast setting - Source: [O4eidkDuegQ]
- Blooming when contrast turned up (overdriving CRT) - Source: [O4eidkDuegQ]
- Loss of sharpness at high contrast settings - Source: [O4eidkDuegQ]

##### Flyback Arcing
- Can occur as flyback transformer ages - Source: [O4eidkDuegQ]
- May be caused by soot/dust near high voltage anode cap - Source: [O4eidkDuegQ]
- Clean CRT around anode cap and high voltage lead first - Source: [O4eidkDuegQ]
- If arcing internal to flyback, windings are breaking down - Source: [O4eidkDuegQ]
- Loud snaps = severe arcing, quiet snaps = early stage - Source: [O4eidkDuegQ]

#### CRT Replacement
- CRT swappable from donor 13" TV - Source: [O4eidkDuegQ]
- Philips/Magnavox CRTs from era are compatible - Source: [O4eidkDuegQ]
- Philips CRTs generally high quality and long-lived - Source: [O4eidkDuegQ]

### Finding Security Monitors
- Check thrift stores, estate sales, office equipment auctions - Source: [O4eidkDuegQ]
- Often found in trash when companies upgrade to flat panels - Source: [O4eidkDuegQ]
- Multi-format capability makes them valuable for retro use - Source: [O4eidkDuegQ]
