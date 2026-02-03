# CRT and Display Techniques

> Part of the retro knowledge base. See also: tech-*.md files for other categories.

## Contents
- [CRT Degaussing and Purity Problems](#crt-degaussing-and-purity-problems)
- [CRT Glass Scratch Removal](#crt-glass-scratch-removal)
- [CRT Rejuvenation](#crt-rejuvenation)
- [CRT Horizontal Oscillator Troubleshooting](#crt-horizontal-oscillator-troubleshooting)
- [CRT/Display](#crtdisplay)
- [CRT Phosphor Identification](#crt-phosphor-identification)
- [CRT Monitor Transplant](#crt-monitor-transplant)
- [CRT Grid-to-Cathode Short Diagnosis](#crt-grid-to-cathode-short-diagnosis)
- [Monitor Voltage Conversion (240V to 120V)](#monitor-voltage-conversion-240v-to-120v)
- [Flyback Transformer Issues](#flyback-transformer-issues)
- [CRT Wear and Aging](#crt-wear-and-aging)
- [Vertical Deflection IC Troubleshooting](#vertical-deflection-ic-troubleshooting)
- [Cathode Bias Circuit Troubleshooting](#cathode-bias-circuit-troubleshooting)

## CRT Degaussing and Purity Problems

### How Purity Problems Manifest
- Color contamination in corners or edges of screen - Source: [YuTTLdqhN3o]
- Electron beam doesn't hit correct phosphor dots/stripes - Source: [YuTTLdqhN3o]
- Green or purple tint in areas that should be neutral/white - Source: [YuTTLdqhN3o]
- Problem can appear after moving TV or exposure to magnets - Source: [YuTTLdqhN3o]

### How CRT Color Works (Shadow Mask vs Aperture Grille)
- Three electron guns (R, G, B) aim at phosphor screen - Source: [YuTTLdqhN3o]
- Shadow mask: Metal plate with holes that guide electrons to correct phosphor dots - Source: [YuTTLdqhN3o]
- Aperture grille (Trinitron): Vertical wires/slots instead of dots - Source: [YuTTLdqhN3o]
- External magnetic fields deflect electron beam before it reaches mask/grille - Source: [YuTTLdqhN3o]
- Deflected beam hits wrong phosphor = color impurity - Source: [YuTTLdqhN3o]

### Built-in Degaussing Circuit
- Automatic degauss coil runs briefly at power-on - Source: [YuTTLdqhN3o]
- Produces decaying AC field that neutralizes residual magnetism - Source: [YuTTLdqhN3o]
- Takes about 2-3 seconds, then coil goes cold - Source: [YuTTLdqhN3o]
- Power off for 15-30 minutes, then turn on again to re-degauss - Source: [YuTTLdqhN3o]
- May need multiple cycles to fully clear minor magnetization - Source: [YuTTLdqhN3o]

### External Degaussing Coil (Bulk Eraser)
- Bulk tape eraser or dedicated CRT degaussing wand - Source: [YuTTLdqhN3o]
- Hold at edge of screen, turn on, move slowly across face in circular motion - Source: [YuTTLdqhN3o]
- Pull away from screen while still on (minimum 3 feet away) - Source: [YuTTLdqhN3o]
- Then turn off - turning off near screen re-magnetizes it - Source: [YuTTLdqhN3o]
- Watch screen wobble as magnetic field affects electron beam - Source: [YuTTLdqhN3o]
- Multiple passes may be needed for stubborn magnetization - Source: [YuTTLdqhN3o]

### External Degaussing Procedure Details
- TV must be ON during degaussing so you can see the effect - Source: [YuTTLdqhN3o]
- Start degaussing wand at edge of screen, not center - Source: [YuTTLdqhN3o]
- Move wand in slow circular motions across entire face - Source: [YuTTLdqhN3o]
- Gradually increase distance from screen while still moving - Source: [YuTTLdqhN3o]
- Get at least 3-4 feet away before turning off degausser - Source: [YuTTLdqhN3o]
- Sudden field collapse (turning off) near screen creates new magnetization - Source: [YuTTLdqhN3o]

### When Degaussing Doesn't Work
- Some magnetization is too strong for degaussing to fix - Source: [YuTTLdqhN3o]
- Internal components (shadow mask, aperture grille) can become permanently magnetized - Source: [YuTTLdqhN3o]
- Degaussing only works on external surfaces and degauss coil path - Source: [YuTTLdqhN3o]
- Deeply seated magnetization in metal structures won't respond - Source: [YuTTLdqhN3o]

### Neodymium Magnet Workaround
- Small neodymium magnets can compensate for residual magnetization - Source: [YuTTLdqhN3o]
- Place magnet on external case near affected area - Source: [YuTTLdqhN3o]
- Experiment with position and orientation (flip magnet, move around) - Source: [YuTTLdqhN3o]
- Magnet creates opposing field that cancels contamination - Source: [YuTTLdqhN3o]
- Very small adjustments have big effects - move in tiny increments - Source: [YuTTLdqhN3o]
- May need multiple magnets for different areas - Source: [YuTTLdqhN3o]
- Tape magnet in place once optimal position found - Source: [YuTTLdqhN3o]
- Not a "proper" fix but can restore usable picture - Source: [YuTTLdqhN3o]

### Neodymium Magnet Warnings
- Too strong a magnet can make things worse - Source: [YuTTLdqhN3o]
- Start with smallest/weakest magnet available - Source: [YuTTLdqhN3o]
- Distance from CRT affects field strength - use spacers if needed - Source: [YuTTLdqhN3o]
- Moving magnet while TV is on shows real-time effect - Source: [YuTTLdqhN3o]
- Once taped in place, don't move TV or magnet may shift - Source: [YuTTLdqhN3o]

### Causes of Magnetization
- Speakers near TV (especially unshielded speakers) - Source: [YuTTLdqhN3o]
- Magnetic toys, tools, or equipment stored near TV - Source: [YuTTLdqhN3o]
- Moving TV while it contains magnetized metal - Source: [YuTTLdqhN3o]
- Lightning strikes or power surges - Source: [YuTTLdqhN3o]
- Age-related degradation of internal degauss coil - Source: [YuTTLdqhN3o]
- TV orientation change (Earth's magnetic field affects CRT differently) - Source: [YuTTLdqhN3o]

### Purity Ring Adjustment (Advanced)
- Deflection yoke has purity rings that can be adjusted - Source: [YuTTLdqhN3o]
- Should only be adjusted with proper service manual procedure - Source: [YuTTLdqhN3o]
- Requires removing back cover and accessing yoke assembly - Source: [YuTTLdqhN3o]
- Professional alignment tools preferred - Source: [YuTTLdqhN3o]
- Incorrect adjustment can make purity worse than before - Source: [YuTTLdqhN3o]

## CRT Glass Scratch Removal

### Polishing Method
- Use automotive orbital polisher with rubbing compound - Source: [8lUA2bOAnDI]
- Mix pumice hand cleaner (Fast Orange) with rubbing compound (Turtle Wax) - Source: [8lUA2bOAnDI]
- Apply to foam pad and polish affected area - Source: [8lUA2bOAnDI]
- Takes significant elbow grease and time - Source: [8lUA2bOAnDI]
- Glass will warm up locally during polishing - Source: [8lUA2bOAnDI]

### Safety Considerations
- CRTs use leaded glass - polish outdoors or in detached space - Source: [8lUA2bOAnDI]
- Don't breathe the dust created - Source: [8lUA2bOAnDI]
- Wear gloves and clothes you don't mind getting dirty - Source: [8lUA2bOAnDI]
- Cover TV with painters plastic, exposing only scratch area - Source: [8lUA2bOAnDI]
- Slurry sprays everywhere - protect surroundings - Source: [8lUA2bOAnDI]

### Results
- Softens sharp edges of scratches (makes them less visible) - Source: [8lUA2bOAnDI]
- Deep scratches may show slight rainbow refraction after polishing - Source: [8lUA2bOAnDI]
- Complete removal possible with more time and effort - Source: [8lUA2bOAnDI]
- Scratches that catch fingernail = deep, require polishing - Source: [8lUA2bOAnDI]
- Toothpaste or nail polish won't fix deep scratches - Source: [8lUA2bOAnDI]

### Note on Glass Hardness
- Sand/rocks scratch glass (silica harder than glass) - Source: [8lUA2bOAnDI]
- Metal keys generally won't scratch CRT glass - Source: [8lUA2bOAnDI]
- Middle of curved CRT face most vulnerable when laid facedown - Source: [8lUA2bOAnDI]

## CRT Rejuvenation

### Warning
- Rejuvenation often makes CRTs worse, not better - Source: [7blLes8Vgbs]
- Some testers/rejuvenators work better than others - Source: [7blLes8Vgbs]
- Already-dim CRTs may be completely destroyed by rejuvenation - Source: [7blLes8Vgbs]
- Test emissions before and after - if worse, stop immediately - Source: [7blLes8Vgbs]

### Alternatives
- Swap CRT from donor monitor if same tube type - Source: [7blLes8Vgbs]
- Keep working monitors for CRT harvesting - Source: [7blLes8Vgbs]

## CRT Horizontal Oscillator Troubleshooting

### Frequency Measurement with Phone App
- Spectroid app (Android, free) shows horizontal oscillator frequency - Source: [9QiSXeCf9tw], [Ve5gsO4u7pc]
- Can detect frequencies up to ~25kHz with phone microphone - Source: [9QiSXeCf9tw]
- NTSC monitors should run at 15.7kHz - Source: [9QiSXeCf9tw], [Ve5gsO4u7pc]
- Free-running oscillator (no video input) may be off frequency (e.g., 16.5kHz) - Source: [Ve5gsO4u7pc]
- If frequency doesn't change when video connected, video signal not reaching sync separator - Source: [Ve5gsO4u7pc]
- Commodore PET runs at 22kHz (inaudible to most people) - Source: [9QiSXeCf9tw]
- Great for verifying monitor is running without oscilloscope - Source: [9QiSXeCf9tw]

### Low High Voltage Symptoms
- Oscillator running too slowly = low high voltage output - Source: [9QiSXeCf9tw]
- At 14kHz: only ~2000V instead of ~11000V expected - Source: [9QiSXeCf9tw]
- Symptoms: Very dim picture, severe geometry issues (bowing) - Source: [9QiSXeCf9tw]
- Flyback generates multiple voltage rails - all affected when HV low - Source: [9QiSXeCf9tw]

### Variable Inductor Adjustment
- Horizontal oscillator coil (slug-tuned inductor) affects frequency - Source: [9QiSXeCf9tw]
- Use plastic alignment tool to adjust - Source: [9QiSXeCf9tw]
- Watch frequency on phone app while adjusting - Source: [9QiSXeCf9tw]
- Picture brightens as high voltage increases toward correct frequency - Source: [9QiSXeCf9tw]

### IC Orientation Issues
- Samsung/rebadged ICs may lack pin 1 marking - Source: [9QiSXeCf9tw]
- Look for beveled edge on package (pin 1 indicator) - Source: [9QiSXeCf9tw]
- Check PCB silkscreen for pin 1 marking before installing - Source: [9QiSXeCf9tw]
- IC installed backwards may not immediately fail but won't work - Source: [9QiSXeCf9tw]

### Deflection Yoke as Tuned Component
- Yoke + flyback form tuned circuit for high voltage - Source: [9QiSXeCf9tw]
- Without proper yoke: only 500-1000V instead of 10000V+ - Source: [9QiSXeCf9tw]
- Broken trace to yoke connector causes no/low high voltage - Source: [9QiSXeCf9tw]
- Monitor won't work properly without correct deflection yoke - Source: [9QiSXeCf9tw]
- Disconnecting horizontal deflection yoke kills entire high voltage section - Source: [t9bs3i2-5Kc]
- Circuit bending attempt (audio to yoke) results in completely non-functional TV - Source: [t9bs3i2-5Kc]
- Two-pin horizontal, three-pin vertical connectors have polarity clips - Source: [t9bs3i2-5Kc]
- Reversed yoke polarity = flipped picture orientation - Source: [t9bs3i2-5Kc]

### Ground Leads Safety
- Always connect CRT ground lead to chassis before powering on - Source: [9QiSXeCf9tw]
- Dag coating on CRT can float to dangerous voltage without ground - Source: [9QiSXeCf9tw]
- Can cause arcing and component damage if not grounded - Source: [9QiSXeCf9tw]

## CRT/Display

### Initial Power-On Testing
- First test: Apply AC power with no input signal, verify high voltage and no sparks - Source: [_MljEAIpQ8g]
- Listen for unusual sounds, watch for smoke or arcing - Source: [_MljEAIpQ8g]
- Watch for collapse pattern when turning off (indicates working deflection) - Source: [_MljEAIpQ8g]

### CRT Adjustment Controls
- Focus control: Usually on flyback transformer - Source: [_MljEAIpQ8g]
- Screen control: On flyback, adjusts raster brightness baseline - Source: [_MljEAIpQ8g]
- Drive controls: Adjust individual color gun intensity (on neck board) - Source: [_MljEAIpQ8g]
- Bias/cut controls: Used with service mode for calibration - Source: [_MljEAIpQ8g]
- Service mode switch: Draws single horizontal line for proper drive/cut adjustment - Source: [_MljEAIpQ8g]
- Width/horizontal size: Often requires plastic adjustment tool, not metal - Source: [_MljEAIpQ8g]

### Worn CRT Diagnosis
- Very dim picture requiring high brightness setting - Source: [_MljEAIpQ8g]
- Blooming when brightness increased (text becomes blown out) - Source: [_MljEAIpQ8g]
- Weak color guns (typically red and blue weaker than green) - Source: [_MljEAIpQ8g]
- Drive control maxed out indicates weak gun - Source: [_MljEAIpQ8g]
- Camera auto-gain makes dim CRTs look better in photos than in person - always test in person - Source: [_MljEAIpQ8g]

### CRT Quality Notes
- Mitsubishi tubes have characteristic greenish-blue phosphor color - Source: [_MljEAIpQ8g]
- Corner correction magnets on deflection yoke indicate quality manufacturing - Source: [_MljEAIpQ8g]
- JVC 1702 monitors (North American) are ultra-reliable - Source: [_MljEAIpQ8g]
- Japanese-made monitors from 1980s were generally top quality - Source: [_MljEAIpQ8g]
- P4 phosphor = white phosphor, common in 12" TV-style CRTs - Source: [_uq86UDmbsU]

### CRT Swapping/Replacement
- Use CRT tester to determine G2/screen voltage requirements before swapping - Source: [_uq86UDmbsU]
- G2 voltage ranges: Lower (200-300V) for older TV-style P4 CRTs, Higher (500-600V) for computer green/amber CRTs - Source: [_uq86UDmbsU]
- When G2 voltage is too low for a CRT, you get NO image at all (not even faint) - Source: [_uq86UDmbsU]
- Measure deflection yoke inductance with multimeter to check compatibility - Source: [_uq86UDmbsU]
- If yoke inductance doesn't match, keep original yoke and just swap the tube - Source: [_uq86UDmbsU]
- Check physical compatibility: mounting tabs, anode cap position, rear connector keying - Source: [_uq86UDmbsU]
- G2 voltage can be measured on back of CRT connector (carefully - up to 600V!) - Source: [_uq86UDmbsU]
- Loosen deflection yoke before testing, position it while powered, then tighten - Source: [_uq86UDmbsU]
- Centering rings on deflection yoke adjust overall image position (B&W CRTs only) - Source: [_uq86UDmbsU]

### CRT "Cataracts" (PVA Glue Clouding)
- PVA glue between CRT face and safety glass clouds over time creating hazy appearance - Source: [_uq86UDmbsU]
- PVA glue may be water-soluble - submerging front in water may dissolve it - Source: [_uq86UDmbsU]
- Alternative: Heat front of CRT to loosen glue, pry off safety glass - Source: [_uq86UDmbsU]
- SAFETY: Heated PVA releases toxic fumes - work outside only - Source: [_uq86UDmbsU]
- SAFETY: Risk of implosion - wear face shield, gloves, full body coverage - Source: [_uq86UDmbsU]

### CRT Storage
- Wrap CRT in bubble wrap with appropriate size box - Source: [_uq86UDmbsU]
- Use toilet paper roll over neck to protect fragile neck area - Source: [_uq86UDmbsU]
- Keep spare CRTs for future repairs - Source: [_uq86UDmbsU]

### UV Flashlight Phosphor Identification
- Use 365nm UV flashlight to identify CRT phosphor type - Source: [kVEmURyF87M]
- Green phosphor CRTs glow bright green under UV light - Source: [kVEmURyF87M]
- Amber phosphor CRTs glow purple/violet under UV light - Source: [kVEmURyF87M]
- White (P4) phosphor CRTs glow white/gray under UV light - Source: [kVEmURyF87M]
- Useful for identifying unmarked or faded phosphor labels - Source: [kVEmURyF87M]
- Can verify CRT hasn't been swapped with different phosphor type - Source: [kVEmURyF87M]
- 365nm wavelength most effective (standard "black light" wavelength) - Source: [kVEmURyF87M]

### DC Restoration (Black Level Clamping)
- Maintains consistent black level regardless of scene brightness - Source: [KrX3s_Dp7kc]
- Without DC restoration: Bright scenes raise baseline, dark scenes drop it - Source: [KrX3s_Dp7kc]
- With DC restoration ON: Black level stays constant - Source: [KrX3s_Dp7kc]
- Found on professional and some consumer monitors as switch - Source: [KrX3s_Dp7kc]
- Also called "black level clamping" in some documentation - Source: [KrX3s_Dp7kc]
- Generally preferred ON for computer/text display - Source: [KrX3s_Dp7kc]
- May be left OFF for video/film content depending on preference - Source: [KrX3s_Dp7kc]

### CRT Tester Usage (Sencore/B&K TR-850)

#### Setup
- Match tester socket to CRT base configuration - Source: [IW_R8-Xmiic]
- Connect ground lead to CRT DAG (graphite) coating - Source: [IW_R8-Xmiic]
- Note CRT temperature before testing (cold vs warm affects readings) - Source: [IW_R8-Xmiic]

#### Emissions Test
- Measures cathode electron emission capability - Source: [IW_R8-Xmiic]
- Green zone: Good emissions, CRT healthy - Source: [IW_R8-Xmiic]
- Yellow zone: Weak emissions, CRT questionable - Source: [IW_R8-Xmiic]
- Red zone: Dead or dying CRT - Source: [IW_R8-Xmiic]
- Warm CRT may read better than cold - let tube heat up and retest - Source: [IW_R8-Xmiic]

#### Life Test
- Predicts remaining useful life under stress - Source: [IW_R8-Xmiic]
- Good life test = years of service expected - Source: [IW_R8-Xmiic]
- Poor life test = may fail soon despite working now - Source: [IW_R8-Xmiic]
- Useful for deciding whether to invest in restoration - Source: [IW_R8-Xmiic]

#### CRT Rejuvenation/Baking
- Heats cathode to burn off contamination - Source: [IW_R8-Xmiic]
- May temporarily restore weak tubes - Source: [IW_R8-Xmiic]
- Not a permanent fix - tube may degrade again - Source: [IW_R8-Xmiic]
- Risk of making tube worse if already marginal - Source: [IW_R8-Xmiic]
- Use only as last resort on otherwise worthless tubes - Source: [IW_R8-Xmiic]

### Deflection Yoke Transfer

#### When to Transfer Yoke
- Required when replacement CRT has incompatible yoke - Source: [IW_R8-Xmiic]
- Measure inductance with multimeter to compare - Source: [IW_R8-Xmiic]
- Significantly different inductance = keep original yoke - Source: [IW_R8-Xmiic]
- Similar inductance = can use yoke from new tube - Source: [IW_R8-Xmiic]

#### Procedure
- Loosen yoke clamp (usually plastic screw or spring clip) - Source: [IW_R8-Xmiic]
- Slide yoke off old CRT neck - Source: [IW_R8-Xmiic]
- Clean yoke interior of old adhesive if present - Source: [IW_R8-Xmiic]
- Slide onto new CRT neck - Source: [IW_R8-Xmiic]
- Position while powered for correct geometry - Source: [IW_R8-Xmiic]
- Tighten clamp only after image properly aligned - Source: [IW_R8-Xmiic]

#### Yoke Position Effects
- Too far back: Overscan, corners cut off - Source: [IW_R8-Xmiic]
- Too far forward: Underscan, black borders - Source: [IW_R8-Xmiic]
- Rotation affects image tilt - Source: [IW_R8-Xmiic]
- Use centering rings for fine position adjustment - Source: [IW_R8-Xmiic]

### 9-inch VGA to Mac CRT Swap

#### Compatibility
- 9-inch Mac CRTs fit in some 9-inch VGA monitors - Source: [Haqmom9xIZU]
- Mounting tabs must match between CRT and chassis - Source: [Haqmom9xIZU]
- Mac CRT mounting tabs compatible with EMC EM-916A monitor - Source: [Haqmom9xIZU]
- Mac CRT may need to be rotated 180° for neck board clearance - Source: [Haqmom9xIZU]

#### Ground Wire Adaptation
- Mac CRT has DAG ground via metal wire to rear of tube - Source: [Haqmom9xIZU]
- VGA monitor may not have this wire - add one if missing - Source: [Haqmom9xIZU]
- Harvest ground wire from scrap Mac analog boards - Source: [Haqmom9xIZU]
- Attach ground wire to chassis screw near CRT corner - Source: [Haqmom9xIZU]

#### Geometry Adjustment
- Use yoke centering rings for overall image position - Source: [Haqmom9xIZU]
- Magnetic tabs on yoke adjust corner geometry - Source: [Haqmom9xIZU]
- Separate V-size pots may exist for text mode vs graphics mode - Source: [Haqmom9xIZU]
- 640x480 and text mode may need different height settings - Source: [Haqmom9xIZU]

#### High Voltage Test
- Check for stored charge before removing CRT - Source: [Haqmom9xIZU]
- High voltage probe with discharge indicator recommended - Source: [Haqmom9xIZU]
- Old monitors often have bleeder resistor (no stored charge) - Source: [Haqmom9xIZU]

#### Phosphor Color Options
- White phosphor: standard for VGA monochrome - Source: [Haqmom9xIZU]
- Green phosphor: common from Mac CRTs - Source: [Haqmom9xIZU]
- Amber phosphor: possible but unusual for VGA - Source: [Haqmom9xIZU]
- Any 9-inch CRT with compatible tabs can be used - Source: [Haqmom9xIZU]

### Sony DAS (Digital Alignment System) Calibration

#### Overview
- Sony CRT monitors from mid-1990s onward use software-based calibration - Source: [Lt1NtRH4BOg]
- Replaces internal potentiometers with EEPROM-stored settings - Source: [Lt1NtRH4BOg]
- Requires special DAS software and serial connection - Source: [Lt1NtRH4BOg]
- Without DAS, many adjustments are inaccessible - Source: [Lt1NtRH4BOg]

#### Connection Requirements
- 5V TTL serial (NOT RS-232) - Source: [Lt1NtRH4BOg]
- Pinout: Pin 1=GND, Pin 2=5V, Pin 3=RXD, Pin 4=TXD - Source: [Lt1NtRH4BOg]
- Use USB-to-TTL adapter (NOT USB-to-serial) - Source: [Lt1NtRH4BOg]
- FTDI adapters recommended, CH340 causes issues with DOS DAS - Source: [Lt1NtRH4BOg]

#### Software Availability
- Multiple versions: DOS (DAS 3.5, 5.7, etc.) and Windows (WinDAS 1-4) - Source: [Lt1NtRH4BOg]
- Different versions support different monitor models - Source: [Lt1NtRH4BOg]
- Archive.org has patched versions (dongle requirement removed) - Source: [Lt1NtRH4BOg]
- Search "Sony DAS" on archive.org - Source: [Lt1NtRH4BOg]

#### OEM Monitors
- Gateway Vivitron monitors are OEM Sony internally - Source: [Lt1NtRH4BOg]
- Gateway Vivitron 15 = Sony CPD-15F23 - Source: [Lt1NtRH4BOg]
- Use DAS version matching Sony model number - Source: [Lt1NtRH4BOg]

## CRT Phosphor Identification

### UV Flashlight Test
- Use 365nm UV flashlight to identify phosphor type - Source: [3DbmGtHJ-Wc]
- Green phosphor: Glows bright green under UV - Source: [3DbmGtHJ-Wc]
- White phosphor: Glows grayish-white under UV - Source: [3DbmGtHJ-Wc]
- Dark blue response indicates unusual/unknown phosphor type - Source: [3DbmGtHJ-Wc]
- UV flashlight casts little visible light, good for dark inspection - Source: [3DbmGtHJ-Wc]

## CRT Monitor Transplant

### Cross-Chassis Transplant
- Check deflection yoke inductance matches between donor and target - Source: [0ZKsQsZhDvw]
- May need to keep original yoke and just swap the tube - Source: [0ZKsQsZhDvw]
- Check mounting tab position on implosion band for physical compatibility - Source: [0ZKsQsZhDvw]
- Width coil adjustment: Use plastic tool only (never metal in coil) - Source: [0ZKsQsZhDvw]
- Centering rings on deflection yoke adjust overall image position - Source: [0ZKsQsZhDvw]

### Phosphor Color Notes
- Green phosphor: Eyes very sensitive, appears brighter than amber - Source: [0ZKsQsZhDvw]
- Amber phosphor: Wears out faster, often dim on old monitors - Source: [0ZKsQsZhDvw]
- Converting amber monitor to green via CRT swap is viable - Source: [0ZKsQsZhDvw]
- Some amber CRTs use amber-tinted glass over white phosphor (Zenith) - Source: [ALwFZ-77k0Y]
- Phosphor color often doesn't match visible phosphor coating color - Source: [ALwFZ-77k0Y]

### CRT Mounting Tab Compatibility
- Tabs on implosion band determine chassis compatibility - Source: [ALwFZ-77k0Y]
- Front tabs: IBM 5155, Macintosh - compatible with each other - Source: [ALwFZ-77k0Y]
- Back tabs: Commodore PET, Apple IIc monitors - Source: [ALwFZ-77k0Y]
- NEVER cut/weld tabs on implosion band (structural safety) - Source: [ALwFZ-77k0Y]
- Can use spacers for different tab positions if gap acceptable - Source: [ALwFZ-77k0Y]

### Deflection Yoke Compatibility
- Measure inductance with LCR meter before swapping yokes - Source: [ALwFZ-77k0Y]
- Yoke inductance affects high voltage generation - Source: [ALwFZ-77k0Y]
- Mismatched yoke = improper high voltage (too low or unstable) - Source: [ALwFZ-77k0Y]
- When swapping CRT only, keep original yoke if inductance differs - Source: [ALwFZ-77k0Y]

### CRT Discharge Safety
- Always discharge before touching any HV components - Source: [ALwFZ-77k0Y]
- Clip ground lead to CRT DAG coating, not chassis - Source: [ALwFZ-77k0Y]
- Discharging through chassis can destroy components - Source: [ALwFZ-77k0Y]
- Residual charge can rebuild after initial discharge - check again - Source: [ALwFZ-77k0Y]
- Static-like shock possible even after discharge - Source: [ALwFZ-77k0Y]

## CRT Grid-to-Cathode Short Diagnosis

### Symptoms
- Blooming (bright spots expand) - Source: [MnRD1khu4Qk]
- Retrace lines visible - Source: [MnRD1khu4Qk]
- Image flickers/cuts in and out - Source: [MnRD1khu4Qk]
- Tapping CRT neck causes image changes - Source: [MnRD1khu4Qk]
- Image very dark initially, slowly brightens - Source: [MnRD1khu4Qk]
- Weird noises from drive electronics - Source: [MnRD1khu4Qk]
- Short pulls cathode to ground = maximum brightness - Source: [MnRD1khu4Qk]

### Diagnosis
- CRT tester shows G1 (grid) to cathode short - Source: [MnRD1khu4Qk]
- Short may be intermittent - comes and goes with tapping - Source: [MnRD1khu4Qk]
- B&W CRT only uses one gun (red connection on tester) - Source: [MnRD1khu4Qk]
- Check emissions after confirming shorts - CRT may still have life - Source: [MnRD1khu4Qk]

### Attempted Repair
- CRT tester "Remove Shorts" function rarely works - Source: [MnRD1khu4Qk]
- If short won't clear with tester, CRT is junk - Source: [MnRD1khu4Qk]
- CRT swap is only option for shorted tubes - Source: [MnRD1khu4Qk]

### Assessment Criteria
- Is the set worth saving? Common TVs may not justify CRT hunt - Source: [MnRD1khu4Qk]
- Keep PCB for spare parts even if CRT is bad - Source: [MnRD1khu4Qk]
- Keep deflection yoke - may fit other projects - Source: [MnRD1khu4Qk]
- "Can't save them all" - CRTs are consumable items - Source: [MnRD1khu4Qk]

## Monitor Voltage Conversion (240V to 120V)

### Bypass Transformer Method
- Find B+ voltage (often 12V on small monitors) - Source: [6YU9IUAsIrE]
- Remove transformer and bridge rectifier diodes - Source: [6YU9IUAsIrE]
- Use Meanwell 12V switching power supply (size depends on wattage) - Source: [6YU9IUAsIrE]
- Connect PSU output directly to bulk capacitor (observe polarity!) - Source: [6YU9IUAsIrE]
- Linear regulator on board smooths any PSU noise - Source: [6YU9IUAsIrE]
- Result: Multi-voltage input (100-240V) - Source: [6YU9IUAsIrE]

### Testing B+ Requirements
- Measure voltage on large bulk capacitor while running on original voltage - Source: [6YU9IUAsIrE]
- Use bench supply to find minimum operating voltage - Source: [6YU9IUAsIrE]
- Monitor at 18V bulk cap voltage may run fine at 12V - Source: [6YU9IUAsIrE]
- Excessive voltage creates heat in regulator - Source: [6YU9IUAsIrE]

### Philips Monitor Characteristics
- Often run on ~12V B+ - Source: [6YU9IUAsIrE]
- Work at 50Hz or 60Hz without adjustment - Source: [6YU9IUAsIrE]
- Single IC handles horizontal and vertical - Source: [6YU9IUAsIrE]
- PCBs often have unpopulated footprints for audio, SCART, MDA input - Source: [6YU9IUAsIrE]
- Olivetti/European monitors often Philips-based - Source: [6YU9IUAsIrE]

## Vertical Deflection IC Troubleshooting

### NEC uPC1031H2 Vertical Deflection IC
- Integrated vertical deflection IC for monochrome/small color CRT - Source: [QqzmxYsK5xc]
- Contains oscillator, size control, and power amp in single package - Source: [QqzmxYsK5xc]
- Input: V-sync pulse from motherboard - Source: [QqzmxYsK5xc]
- Output: Direct drive to deflection yoke - Source: [QqzmxYsK5xc]
- External components: V-hold pot, V-size pot, linearity pot - Source: [QqzmxYsK5xc]
- Common in terminal CRT boards, generic monitor boards - Source: [QqzmxYsK5xc]

### Vertical Deflection vs Horizontal Deflection
- Vertical runs at 60Hz (50Hz PAL) - within audio frequency range - Source: [QqzmxYsK5xc]
- Simple push-pull transistor pair or integrated IC sufficient for vertical - Source: [QqzmxYsK5xc]
- Horizontal generates high voltage through flyback - failure = no display - Source: [QqzmxYsK5xc]
- Vertical failure = squished/collapsed image but screen still illuminates - Source: [QqzmxYsK5xc]

### Symptoms of Vertical Deflection Problems
- Image severely squished at top and/or bottom - Source: [QqzmxYsK5xc]
- Text lines appearing upside down (wraparound) - Source: [QqzmxYsK5xc]
- V-size control has delayed or erratic effect - Source: [QqzmxYsK5xc]
- Image height varies randomly - Source: [QqzmxYsK5xc]
- Jittery vertical position - Source: [QqzmxYsK5xc]

### Intermittent Vertical Problems
- Old electrolytic caps may need to "reform" after long storage - Source: [QqzmxYsK5xc]
- Problem may fix itself after 30+ minutes of operation - Source: [QqzmxYsK5xc]
- If self-heals, likely capacitor issue not IC failure - Source: [QqzmxYsK5xc]
- Still advisable to replace old caps preemptively - Source: [QqzmxYsK5xc]

### Deflection Yoke Testing
- Measure inductance: typical vertical coil 2.7-4.15mH - Source: [QqzmxYsK5xc]
- Measure resistance: typical 2-7 ohms - Source: [QqzmxYsK5xc]
- Use LCR meter or inductance function on multimeter - Source: [QqzmxYsK5xc]
- Out-of-spec readings indicate possible yoke damage - Source: [QqzmxYsK5xc]

## CRT Wear and Aging

### Cold Cathode Backlight Aging (Laptops)
- CCFL backlights in 1990s laptops dim significantly over 25+ years - Source: [U17OCGDJwkg]
- NOS (new old stock) laptops still show dim screens despite never being used - Source: [U17OCGDJwkg]
- Backlight dimming happens even in storage (tube aging) - Source: [U17OCGDJwkg]
- Inverter board typically fine, problem is the actual CCFL tube - Source: [U17OCGDJwkg]
- Modern LED backlight conversion possible but requires skill - Source: [U17OCGDJwkg]

### Phosphor Degradation
- Phosphor dims over time with use (like fluorescent lights) - Source: [rB_Sayi600o]
- Finite lifespan based on hours of use - Source: [rB_Sayi600o]
- UV excites phosphor, which dims over lifetime - Source: [rB_Sayi600o]

### Cathode Wear
- Cathodes in neck generate electrons - Source: [rB_Sayi600o]
- Wear out over time, generate fewer emissions - Source: [rB_Sayi600o]
- Three separate cathodes for RGB age at different rates - Source: [rB_Sayi600o]
- Different content affects wear (more blue usage = faster blue cathode wear) - Source: [rB_Sayi600o]
- Weak cathode = color imbalance on white (e.g., green tint = weak blue) - Source: [rB_Sayi600o]

### Flyback Transformer Failure Signs
- Loud whine on power-up = possible shorted flyback - Source: [rB_Sayi600o]
- Snapping/arcing sounds = flyback breaking down - Source: [rB_Sayi600o]
- Arcing causes momentary picture shrink and dim - Source: [rB_Sayi600o]
- High voltage (~20-23kV) breaks down insulation over time - Source: [rB_Sayi600o]
- Flyback generates ALL voltages in monitor - must work for anything to work - Source: [rB_Sayi600o]

### Visual Inspection Indicators
- Black soot around anode cap = high hours of use - Source: [rB_Sayi600o]
- Static electricity attracts dust to high voltage areas - Source: [rB_Sayi600o]
- Soot darker than normal house dust - Source: [rB_Sayi600o]
- Bulging or cracked flyback = imminent failure - Source: [rB_Sayi600o]

### CRT Cataracts (Safety Glass Degradation)
- Some monitors/terminals have laminated safety glass bonded to CRT face - Source: [RneTw_LThzQ]
- Common on DEC terminals (VT-100, VT-220, etc.) - Source: [RneTw_LThzQ]
- Adhesive/glue layer between glass and CRT degrades over decades - Source: [RneTw_LThzQ]
- Degradation appears as milky, cloudy, or yellowish patches - Source: [RneTw_LThzQ]
- Nicknamed "cataracts" due to appearance similarity - Source: [RneTw_LThzQ]
- Does not affect CRT function, only visibility - Source: [RneTw_LThzQ]
- Repair requires carefully separating safety glass from CRT face - Source: [RneTw_LThzQ]
- High risk of CRT damage during removal - many collectors leave as-is - Source: [RneTw_LThzQ]

## Flyback Transformer Issues

### Hygroscopic Glue on Flyback Clamps
- Silicone glue used to hold flyback clamps absorbs water over time - Source: [nkbNcoueY2c]
- Moisture causes rust on metal clamp underneath - Source: [nkbNcoueY2c]
- Common on Philips flybacks and many CRT monitors - Source: [nkbNcoueY2c]
- Rust can weaken mechanical connection to PCB - Source: [nkbNcoueY2c]

### Cold Solder Joints on Flyback
- High current through flyback legs causes thermal cycling - Source: [nkbNcoueY2c]
- Solder joints can crack over years of heating/cooling - Source: [nkbNcoueY2c]
- Symptoms: Intermittent no-video, high voltage dropout - Source: [nkbNcoueY2c]
- Reflow all flyback connections as preventative measure - Source: [nkbNcoueY2c]
- Use fresh solder with flux when reflowing - Source: [nkbNcoueY2c]

## Cathode Bias Circuit Troubleshooting

### How Cathode Bias Works
- Cathode at ground potential = maximum brightness for that color - Source: [S6qUhbXqgUw]
- Cathode at high voltage potential = off (no electron emission) - Source: [S6qUhbXqgUw]
- Bias pot sets DC offset (baseline level) for each color - Source: [S6qUhbXqgUw]
- Drive pot sets AC signal amplitude for each color - Source: [S6qUhbXqgUw]
- 180V B+ rail typically provides bias headroom - Source: [S6qUhbXqgUw]

### Symptoms of Bias Circuit Problems
- One color extremely bright, others absent - Source: [S6qUhbXqgUw]
- Bias/drive pots have no effect on problem color - Source: [S6qUhbXqgUw]
- Screen collapses to single-color line when powered off - Source: [S6qUhbXqgUw]
- Other colors appear normal when problem color disconnected - Source: [S6qUhbXqgUw]

### Diagnosis with Oscilloscope
- Check signal at video processing IC input - all colors should be present - Source: [S6qUhbXqgUw]
- Check signal at driver IC output - all colors should be amplified - Source: [S6qUhbXqgUw]
- Check cathode signals directly - compare DC levels - Source: [S6qUhbXqgUw]
- Problem color cathode DC level much lower than others = bias fault - Source: [S6qUhbXqgUw]

### Leaky High Voltage Cap Failure Mode
- Bypass caps on B+ rail may test OK on LCR meter - Source: [S6qUhbXqgUw]
- Low voltage testers cannot detect leakage at operating voltage - Source: [S6qUhbXqgUw]
- Leaky cap pulls bias rail toward ground - Source: [S6qUhbXqgUw]
- Result: One color way too bright regardless of adjustment - Source: [S6qUhbXqgUw]
- Solution: Replace suspect high voltage caps with higher rated values - Source: [S6qUhbXqgUw]

### Isolation Test Method
- Disconnect problem color signal at coax connector - Source: [S6qUhbXqgUw]
- Turn up screen control - Source: [S6qUhbXqgUw]
- If other colors now visible with bias/drive controls working - Source: [S6qUhbXqgUw]
- Then signal path is fine, problem is DC bias offset - Source: [S6qUhbXqgUw]

### Common Cap Values in Bias Circuits
- 47µF 25V for bias circuits - Source: [S6qUhbXqgUw]
- 47µF 100V near drive transistors - Source: [S6qUhbXqgUw]
- 1µF 250V+ on high voltage rails - Source: [S6qUhbXqgUw]
- Replace with same or higher voltage rating - Source: [S6qUhbXqgUw]
