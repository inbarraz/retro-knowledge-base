# Power Supply and Electrical Techniques

> Part of the retro knowledge base. See also: tech-*.md files for other categories.

## Contents
- [Power Supply Replacement](#power-supply-replacement)
- [IEC Mains Input Modification](#iec-mains-input-modification)
- [Power Supply Tools](#power-supply-tools)
- [RIFA Safety Capacitor Replacement](#rifa-safety-capacitor-replacement)
- [Brown Glue / Component Stabilizer Damage](#brown-glue--component-stabilizer-damage)

## Power Supply Replacement

### PicoRC / ATX4VC Open Source PSU Replacement
- GitHub: github.com/dekuNukem/PicoRC and github.com/dekuNukem/ATX4VC - Source: [5Gfr6lW49aI]
- Tindie: ~$35 for kits - Source: [5Gfr6lW49aI]
- Replaces dead power supplies without opening original PSU - Source: [5Gfr6lW49aI]
- Uses PicoATX power supply with 12V DC barrel jack - Source: [5Gfr6lW49aI]
- Available for: IBM PC/XT/AT, Apple II, Apple IIgs, Mac Plus, Mac SE, BBC Micro, Osborne 1 - Source: [5Gfr6lW49aI]

### ISA Bus Power Card (PicoRC for IBM PC)
- Plugs into ISA slot, powers entire system through bus - Source: [5Gfr6lW49aI]
- Has spade connectors for direct connection to motherboard power pins - Source: [5Gfr6lW49aI]
- Includes onboard 7905 regulator for -5V (needed by some sound cards) - Source: [5Gfr6lW49aI]
- Modern ATX supplies don't have -5V rail, this generates it from -12V - Source: [5Gfr6lW49aI]
- Works with any machine, not just standard AT connector - Source: [5Gfr6lW49aI]

### ATX4VC Breakout Board
- Breakout board from ATX connector with fuses per rail - Source: [5Gfr6lW49aI]
- Lever-style connectors (not screw terminals) - Source: [5Gfr6lW49aI]
- Cut original PSU wires and connect to appropriate rails - Source: [5Gfr6lW49aI]
- Fuses protect vintage hardware from ATX power supply overcurrent - Source: [5Gfr6lW49aI]

### USB-C Power Delivery for Vintage PCs
- USB-C PD power bank can power vintage PC at 12V - Source: [5Gfr6lW49aI]
- Need USB-C to barrel jack cable with PD chip in jack - Source: [5Gfr6lW49aI]
- 486 DX2/66 with VGA card, IDE, etc. draws only ~20 watts - Source: [5Gfr6lW49aI]
- Old processors have constant power draw (no power saving states) - Source: [5Gfr6lW49aI]
- Portable battery-powered retro PC is possible - Source: [5Gfr6lW49aI]

### ATX for AT Adapters
- Available on eBay - converts ATX to AT power connector - Source: [5Gfr6lW49aI]
- Issue: Modern ATX supplies lack -5V rail - Source: [5Gfr6lW49aI]
- Older ATX supplies (like 350W models) have both -5V and -12V - Source: [5Gfr6lW49aI]
- Older ATX supplies have better 5V current capacity (35A vs modern focus on 12V) - Source: [5Gfr6lW49aI]

### ATX4VC Breakout Board (General Purpose)
- GitHub: github.com/dekuNukem/ATX4VC - Source: [ANbiQW-Ppt4]
- Breaks out +12V, +5V, +3.3V, -5V, -12V from ATX supplies - Source: [ANbiQW-Ppt4]
- Works with Pico ATX supplies (12V barrel jack input) - Source: [ANbiQW-Ppt4]
- Individual fuses per rail for protection - Source: [ANbiQW-Ppt4]
- Fan headers with PWM speed control and temperature sensor input - Source: [ANbiQW-Ppt4]
- USB-C outputs (standby and switched) - Source: [ANbiQW-Ppt4]
- Addressable RGB LED headers for case lighting - Source: [ANbiQW-Ppt4]
- Use 4-6 amp 12V supply for machines like TRS-80 Model 3 - Source: [ANbiQW-Ppt4]
- Compatible with: BBC Micro, Osborne 1, Macintosh Plus, many others - Source: [ANbiQW-Ppt4]
- Generates -5V onboard (doesn't require ATX supply to have it) - Source: [ANbiQW-Ppt4]

## IEC Mains Input Modification

### Adding IEC Inlet to Monitors with Captive Cords

#### Overview
- Many vintage monitors have hardwired power cords - Source: [pavO4CKse0Y]
- Adding IEC inlet allows use of standard detachable power cord - Source: [pavO4CKse0Y]
- Easier for transport, storage, and regional power compatibility - Source: [pavO4CKse0Y]
- Panel mount IEC inlets available from electronics suppliers - Source: [pavO4CKse0Y]

#### Safety Precautions
- Discharge all capacitors before working inside - Source: [pavO4CKse0Y]
- Monitor mains voltage is lethal - always disconnect power - Source: [pavO4CKse0Y]
- Use proper strain relief for internal wiring - Source: [pavO4CKse0Y]
- Ensure secure ground connection to chassis - Source: [pavO4CKse0Y]

#### Commodore 1084 Specific
- Original cord enters through strain relief bushing - Source: [pavO4CKse0Y]
- Replace with panel-mount IEC C14 inlet - Source: [pavO4CKse0Y]
- Drill or punch hole for IEC inlet near original cord entry - Source: [pavO4CKse0Y]
- Wire: brown=live, blue=neutral, green/yellow=ground - Source: [pavO4CKse0Y]

#### Apple RGB Monitor Specific
- Similar process to 1084 - Source: [pavO4CKse0Y]
- Original power cable often in poor condition after decades - Source: [pavO4CKse0Y]
- IEC mod improves safety with modern cable - Source: [pavO4CKse0Y]

## Power Supply Tools

### Strain Relief Bushing Tool (Pro's Kit CP-311)
- Specialized tool for installing/removing strain relief bushings - Source: [NHz1e1Wu1iI]
- Also known as cable gland or cord grip - Source: [NHz1e1Wu1iI]
- Allows easy removal of power cables from chassis - Source: [NHz1e1Wu1iI]
- Also works on audio equipment, amplifiers, test equipment - Source: [NHz1e1Wu1iI]
- Available from Mouser, DigiKey, and tool suppliers - Source: [NHz1e1Wu1iI]
- Pro's Kit brand offers quality version - Source: [NHz1e1Wu1iI]

## RIFA Safety Capacitor Replacement

### Mac Plus/512 Analog Board RIFA Caps
- X-cap (across mains): 0.1µF - Source: [nkbNcoueY2c]
- Y-caps (line to chassis): 4700pF (0.0047µF) - Source: [nkbNcoueY2c]
- Replace with equivalent X-rated or Y-rated safety capacitors - Source: [nkbNcoueY2c]
- Cracked RIFA will eventually explode with smoke - Source: [nkbNcoueY2c]
- Replace preemptively - don't wait for failure - Source: [nkbNcoueY2c]

### Identifying RIFA Caps
- Usually yellow or light brown color - Source: [nkbNcoueY2c]
- "RIFA" brand name visible on larger examples - Source: [nkbNcoueY2c]
- Look for surface cracking (indicates moisture ingress) - Source: [nkbNcoueY2c]
- Located near mains input, IEC connector area - Source: [nkbNcoueY2c]
- Can be inside IEC connector housing on some PSUs - Source: [nkbNcoueY2c]

### X-Cap vs Y-Cap Explanation
- X-caps: Connected across mains (line to neutral) - Source: [y8xNVP6yEXs]
- Y-caps: Connected from line/neutral to chassis ground - Source: [y8xNVP6yEXs]
- Both are safety-rated capacitors for EMI/RFI filtering - Source: [y8xNVP6yEXs]
- X-cap failure: Can short and blow fuse, no safety hazard - Source: [y8xNVP6yEXs]
- Y-cap failure: Could energize chassis - must be very reliable - Source: [y8xNVP6yEXs]
- Replace X-caps with X-rated, Y-caps with Y-rated only - Source: [y8xNVP6yEXs]
- Typical X-cap values: 0.1µF, 0.01µF across mains - Source: [y8xNVP6yEXs]
- Typical Y-cap values: 2200pF, 4700pF line to ground - Source: [y8xNVP6yEXs]

### Apple IIe Power Supply (Dynacomp 606-5001) RIFA Replacement

#### Overview
- Dynacomp 606-5001 third-party PSU commonly found in Apple IIe - Source: [y8xNVP6yEXs]
- Contains RIFA X-caps across mains input - Source: [y8xNVP6yEXs]
- Standard 0.1µF RIFA cap prone to cracking and smoking - Source: [y8xNVP6yEXs]

#### Safety Warning
- DC filter caps inside PSU can hold high voltage even when unplugged - Source: [y8xNVP6yEXs]
- Wait several minutes after unplugging before servicing - Source: [y8xNVP6yEXs]
- Or discharge caps through resistor (1K-10K ohm) - Source: [y8xNVP6yEXs]
- Never short DC caps directly - can damage capacitors - Source: [y8xNVP6yEXs]

#### Replacement Procedure
- Remove PSU from Apple IIe case - Source: [y8xNVP6yEXs]
- Open PSU case (note safety interlock switch if present) - Source: [y8xNVP6yEXs]
- Locate RIFA caps near mains input (yellow/brown, often cracked) - Source: [y8xNVP6yEXs]
- Note capacitor values (typically 0.1µF X-rated) - Source: [y8xNVP6yEXs]
- Desolder old caps and install new X-rated safety caps - Source: [y8xNVP6yEXs]
- Match or exceed original voltage rating (typically 250VAC X2) - Source: [y8xNVP6yEXs]

#### Testing After Replacement
- Visual inspection for proper soldering - Source: [y8xNVP6yEXs]
- Measure DC rails with multimeter before connecting to computer - Source: [y8xNVP6yEXs]
- Check +5V, +12V, -5V, -12V rails against spec - Source: [y8xNVP6yEXs]

### Apple IIe Unenhanced Motherboard Testing

#### Joystick Port Diagnostics
- Joystick port pins should float high when no joystick connected - Source: [y8xNVP6yEXs]
- Pins pulled low indicate possible short or stuck button logic - Source: [y8xNVP6yEXs]
- Test with multimeter: measure voltage on joystick connector pins - Source: [y8xNVP6yEXs]
- Normal: approximately +5V on button/paddle lines - Source: [y8xNVP6yEXs]
- Low/grounded: indicates problem with motherboard or external short - Source: [y8xNVP6yEXs]
- Keyboard keys may map to joystick buttons - check for stuck keys - Source: [y8xNVP6yEXs]

## Switch Mode Power Supply Troubleshooting

### Protection Mode Symptoms
- Clicking/ticking sound indicates SMPS attempting to start - Source: [t9bs3i2-5Kc]
- Starts briefly, then shuts down into protection - Source: [t9bs3i2-5Kc]
- Repeats continuously as controller retries - Source: [t9bs3i2-5Kc]
- Common causes: Short on secondary side or bootstrap cap failure - Source: [t9bs3i2-5Kc]

### Bootstrap Cap Testing
- Small cap near switching transistor (often 47µF 25V) - Source: [t9bs3i2-5Kc]
- Gets baked by nearby hot resistors - Source: [t9bs3i2-5Kc]
- Dead cap reads picofarads instead of microfarads - Source: [t9bs3i2-5Kc]
- ESR meter shows megaohms instead of ~1 ohm - Source: [t9bs3i2-5Kc]
- DE5000 LCR meter good for in-circuit testing - Source: [t9bs3i2-5Kc]
- Replace with same or higher voltage rating - Source: [t9bs3i2-5Kc]

### Isolating Primary vs Secondary Faults
- Lift inductor feeding B+ to horizontal/flyback section - Source: [t9bs3i2-5Kc]
- If SMPS now starts and B+ appears, short is on load side - Source: [t9bs3i2-5Kc]
- Check secondary side caps for shorts with multimeter - Source: [t9bs3i2-5Kc]
- Use oscilloscope on B+ cap to see startup pulse pattern - Source: [t9bs3i2-5Kc]

### Service Position Testing
- Tilt PCB up while still connected to CRT - Source: [t9bs3i2-5Kc]
- Cut zip ties for extra wire length if needed - Source: [t9bs3i2-5Kc]
- Prop up with non-conductive object (plastic bottle) - Source: [t9bs3i2-5Kc]
- Allows probing while system running - Source: [t9bs3i2-5Kc]

### High Voltage Safety
- Primary side reservoir cap holds ~160-300V DC even when off - Source: [t9bs3i2-5Kc]
- Use 100x scope probe to view voltages safely - Source: [t9bs3i2-5Kc]
- Use resistor (1K-10K) to discharge caps before probing - Source: [t9bs3i2-5Kc]
- Secondary side only dangerous with SMPS running - Source: [t9bs3i2-5Kc]
- With SMPS running, drain resistor keeps primary cap from accumulating - Source: [t9bs3i2-5Kc]

### Using Bench Supply for Fault Finding
- Disconnect SMPS from load section - Source: [t9bs3i2-5Kc]
- Feed voltage directly to B+ rail via test clips - Source: [t9bs3i2-5Kc]
- Start with 12V 1A limit (12W into circuit) - Source: [t9bs3i2-5Kc]
- No current draw = no short at that voltage - Source: [t9bs3i2-5Kc]
- Ramp up voltage watching for current spike (breakdown) - Source: [t9bs3i2-5Kc]
- Compare working board vs faulty board at same voltage - Source: [t9bs3i2-5Kc]
- Dead short with voltage-dependent onset = transistor breakdown - Source: [t9bs3i2-5Kc]

### Thermal Camera Fault Location
- Feed limited current into shorted rail - Source: [t9bs3i2-5Kc]
- 12V @ 1-3A generates visible heat on shorted component - Source: [t9bs3i2-5Kc]
- Topdon TC004 thermal camera works well for this - Source: [t9bs3i2-5Kc]
- Metal heatsinks reflect IR - may show false readings - Source: [t9bs3i2-5Kc]
- Look at PCB traces too - trace heating reveals current path - Source: [t9bs3i2-5Kc]
- Large components (flyback) absorb heat without visible hotspot - Source: [t9bs3i2-5Kc]

## Brown Glue / Component Stabilizer Damage

### Identification
- Brown glue/gunk used to secure components during shipping - Source: [7blLes8Vgbs]
- Found on inductors, diodes, capacitors near flyback area - Source: [7blLes8Vgbs]
- Becomes corrosive and conductive over decades - Source: [7blLes8Vgbs]
- Same problem on IBM monitors - Source: [7blLes8Vgbs]

### Symptoms
- Shorted semiconductors (diodes, transistors) - Source: [7blLes8Vgbs]
- Cracked/degraded capacitors - Source: [7blLes8Vgbs]
- Corroded inductors - Source: [7blLes8Vgbs]
- No video despite working oscillator - Source: [7blLes8Vgbs]

### Repair
- Clean with IPA and scrape off all brown gunk - Source: [7blLes8Vgbs]
- Check all adjacent components for shorts - Source: [7blLes8Vgbs]
- Replace any damaged diodes, caps, inductors - Source: [7blLes8Vgbs]
- Look for brown glue FIRST when troubleshooting - Source: [7blLes8Vgbs]
